"""
Stripe Webhook Handler — Barb App
Deploy this to Render.com (free tier)
Listens for Stripe payment events → updates student tier in Supabase
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json, os, hmac, hashlib, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

STRIPE_SECRET     = os.environ.get("STRIPE_SECRET_KEY", "")
WEBHOOK_SECRET    = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
SUPABASE_URL      = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY      = os.environ.get("SUPABASE_KEY", "")   # service_role key

PIONEER_PRICE_IDS = os.environ.get("STRIPE_PIONEER_PRICE_IDS", "").split(",")
ORG_PRICE_IDS     = os.environ.get("STRIPE_ORG_PRICE_IDS", "").split(",")


def supabase_patch(email: str, data: dict):
    if not SUPABASE_URL or not SUPABASE_KEY:
        return
    try:
        url = f"{SUPABASE_URL}/rest/v1/students?email=eq.{urllib.parse.quote(email)}"
        payload = json.dumps(data).encode()
        req = urllib.request.Request(url, data=payload, method="PATCH", headers={
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
        })
        urllib.request.urlopen(req, timeout=5)
    except Exception as e:
        print(f"Supabase error: {e}")


def get_customer_email(customer_id: str) -> str:
    """Fetch email from Stripe customer record."""
    try:
        req = urllib.request.Request(
            f"https://api.stripe.com/v1/customers/{customer_id}",
            headers={"Authorization": f"Bearer {STRIPE_SECRET}"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read())
            return data.get("email", "")
    except Exception:
        return ""


def resolve_tier(price_id: str) -> str:
    if price_id in PIONEER_PRICE_IDS:
        return "pioneer"
    if price_id in ORG_PRICE_IDS:
        return "organization"
    return "free"


def verify_signature(body: bytes, sig_header: str) -> bool:
    try:
        parts = {k: v for k, v in (p.split("=", 1) for p in sig_header.split(","))}
        ts    = parts.get("t", "")
        sig   = parts.get("v1", "")
        expected = hmac.new(
            WEBHOOK_SECRET.encode(), f"{ts}.".encode() + body, hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected, sig)
    except Exception:
        return False


class WebhookHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Barb webhook active")

    def do_POST(self):
        if self.path != "/stripe-webhook":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body   = self.rfile.read(length)
        sig    = self.headers.get("Stripe-Signature", "")

        if not verify_signature(body, sig):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid signature")
            return

        event = json.loads(body)
        etype = event.get("type", "")
        obj   = event.get("data", {}).get("object", {})

        print(f"Event: {etype}")

        # ── Subscription created or updated ──────────────────────────────────
        if etype in ("customer.subscription.created", "customer.subscription.updated"):
            customer_id = obj.get("customer", "")
            status      = obj.get("status", "")   # active, past_due, canceled
            items       = obj.get("items", {}).get("data", [])
            price_id    = items[0].get("price", {}).get("id", "") if items else ""
            tier        = resolve_tier(price_id) if status == "active" else "free"
            email       = get_customer_email(customer_id)

            if email:
                expires = None
                if status == "active":
                    period_end = obj.get("current_period_end", 0)
                    expires = datetime.fromtimestamp(period_end, tz=timezone.utc).isoformat()
                supabase_patch(email, {
                    "tier": tier,
                    "subscription_status": status,
                    "stripe_customer_id": customer_id,
                    "tier_expires_at": expires,
                })
                print(f"Updated {email} → {tier} ({status})")

        # ── Subscription canceled ─────────────────────────────────────────────
        elif etype == "customer.subscription.deleted":
            customer_id = obj.get("customer", "")
            email       = get_customer_email(customer_id)
            if email:
                supabase_patch(email, {"tier": "free", "subscription_status": "canceled", "tier_expires_at": None})
                print(f"Downgraded {email} → free (canceled)")

        # ── One-time checkout completed ───────────────────────────────────────
        elif etype == "checkout.session.completed":
            email       = obj.get("customer_details", {}).get("email", "")
            customer_id = obj.get("customer", "")
            mode        = obj.get("mode", "")
            if mode == "subscription" and email:
                supabase_patch(email, {"stripe_customer_id": customer_id})
                print(f"Checkout complete for {email}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"Webhook server running on port {port}")
    HTTPServer(("0.0.0.0", port), WebhookHandler).serve_forever()
