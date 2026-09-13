# Stripe + Tier Setup — Barb App Monetization

## One-time setup (~20 minutes)

---

### STEP 1 — Create Stripe account
1. Go to stripe.com → sign up (free)
2. Complete business verification (Learn More Technologies LLC)
3. Go to Dashboard → make sure you're in LIVE mode (not Test)

---

### STEP 2 — Create two products

**Product 1 — Pioneer**
1. Stripe Dashboard → Products → + Add Product
2. Name: `Pioneer`
3. Description: `Live AI chat, Spanish, read aloud, save conversations`
4. Pricing: $9.00 / month → recurring
5. Click Save → copy the **Payment Link** URL

**Product 2 — Organization**
1. + Add Product
2. Name: `Organization`
3. Description: `Instructor mode, class roster, CSV export, custom branding`
4. Pricing: $49.00 / month → recurring
5. Click Save → copy the **Payment Link** URL

---

### STEP 3 — Update Supabase table

In Supabase → SQL Editor → New Query → Run this:

```sql
ALTER TABLE students
  ADD COLUMN tier TEXT DEFAULT 'free',
  ADD COLUMN stripe_customer_id TEXT,
  ADD COLUMN subscription_status TEXT DEFAULT 'inactive',
  ADD COLUMN tier_expires_at TIMESTAMPTZ;

-- Index for fast tier lookups
CREATE INDEX idx_students_tier ON students(tier);
```

---

### STEP 4 — Add Stripe webhook (receives payment confirmation)

1. Stripe Dashboard → Developers → Webhooks → + Add Endpoint
2. Endpoint URL: `https://your-webhook-server.onrender.com/stripe-webhook`
   (deploy webhook.py to Render.com — see below)
3. Events to listen to:
   - `customer.subscription.created`
   - `customer.subscription.updated`
   - `customer.subscription.deleted`
   - `checkout.session.completed`
4. Copy the **Webhook Signing Secret** (starts with `whsec_`)

---

### STEP 5 — Deploy webhook handler to Render.com (free)

1. Go to render.com → sign up with GitHub
2. New → Web Service → connect your GitHub repo
3. Or: paste `webhook.py` into a new repo and connect it
4. Environment variables to set in Render:
   - `STRIPE_SECRET_KEY` — from Stripe Dashboard → Developers → API Keys
   - `STRIPE_WEBHOOK_SECRET` — the `whsec_` key from Step 4
   - `SUPABASE_URL` — your Supabase project URL
   - `SUPABASE_KEY` — your Supabase service_role key (NOT anon key — has write access)

---

### STEP 6 — Add all keys to Streamlit secrets

```toml
ANTHROPIC_API_KEY = "sk-ant-..."
MAILERLITE_API_KEY = "..."
MAILERLITE_GROUP_ID = "..."
SUPABASE_URL = "https://xxxx.supabase.co"
SUPABASE_KEY = "eyJ..."
STRIPE_PIONEER_LINK = "https://buy.stripe.com/..."
STRIPE_ORG_LINK = "https://buy.stripe.com/..."
```

---

### STEP 7 — Manually upgrade a student (while webhook is being set up)

In Supabase → Table Editor → students → find the student → edit:
- Set `tier` to `pioneer` or `organization`
- Set `subscription_status` to `active`

This works immediately. The webhook automates this for new signups.

---

## Tier Feature Map

| Feature | free | pioneer | organization |
|---|---|---|---|
| All 3 lessons | ✓ | ✓ | ✓ |
| Barb offline answers | ✓ | ✓ | ✓ |
| Progress tracker | ✓ | ✓ | ✓ |
| Live AI (Claude) | — | ✓ | ✓ |
| Spanish mode | — | ✓ | ✓ |
| Read aloud | — | ✓ | ✓ |
| Save conversations | — | ✓ | ✓ |
| Instructor Mode | — | — | ✓ |
| Class Roster | — | — | ✓ |
| CSV Export | — | — | ✓ |
| Custom branding | — | — | ✓ |

## Pricing
| Tier | Price | Who buys it |
|---|---|---|
| Free | $0 | Individual students, library patrons |
| Pioneer | $9/month | Self-motivated learners, caregivers |
| Organization | $49/month | Libraries, senior centers, workforce programs |
