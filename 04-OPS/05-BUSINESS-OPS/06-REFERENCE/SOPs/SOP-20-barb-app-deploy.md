# SOP-20 — Barb App Build & Deploy
## Add tiers, Supabase login, and Stripe monetization to the Barb Streamlit app

**Purpose:** Deploy a new version of the Barb app with student login, progress tracking, and paid tiers (Free / Pioneer / Organization)
**Trigger:** Upgrading the Barb app or rebuilding it from scratch
**Owner:** Brian McKinney
**Time required:** 45–60 minutes
**Frequency:** Per major app version release

---

## QUICK REFERENCE
1. Run Supabase SQL — create students table + add tier columns
2. Set up Stripe — two products, two Payment Links
3. Deploy webhook.py to Render.com
4. Add all secrets to Streamlit Cloud
5. Replace app file on GitHub → Streamlit auto-redeploys

---

## STEP-BY-STEP

### STEP 1 — Supabase Setup (~10 min)
- Go to supabase.com → your `barb-app` project → SQL Editor → New Query
- If students table doesn't exist, run the CREATE TABLE block from `SUPABASE-SETUP.md`
- Then run the ALTER TABLE block to add tier columns:
  ```sql
  ALTER TABLE students
    ADD COLUMN IF NOT EXISTS tier TEXT DEFAULT 'free',
    ADD COLUMN IF NOT EXISTS stripe_customer_id TEXT,
    ADD COLUMN IF NOT EXISTS subscription_status TEXT DEFAULT 'inactive',
    ADD COLUMN IF NOT EXISTS tier_expires_at TIMESTAMPTZ;
  ```
- Go to Settings → API → copy Project URL and anon public key

### STEP 2 — Stripe Setup (~20 min)
- Follow `G:\My Drive\LMT-CONTENT\07-THE-APP\STRIPE-SETUP.md` exactly
- Create two products: Pioneer ($9/mo) and Organization ($49/mo)
- Save both Payment Link URLs — needed in Streamlit secrets

### STEP 3 — Deploy Webhook to Render.com (~10 min)
- Go to render.com → New → Web Service → connect GitHub repo
- Upload `webhook.py` (at `G:\My Drive\LMT-CONTENT\07-THE-APP\webhook.py`)
- Set environment variables in Render:
  - `STRIPE_SECRET_KEY`
  - `STRIPE_WEBHOOK_SECRET` (from Stripe → Developers → Webhooks)
  - `SUPABASE_URL`
  - `SUPABASE_KEY` (service_role key — NOT anon)
  - `STRIPE_PIONEER_PRICE_IDS` (comma-separated price IDs)
  - `STRIPE_ORG_PRICE_IDS` (comma-separated price IDs)
- Copy the Render service URL → paste into Stripe webhook endpoint

### STEP 4 — Add Secrets to Streamlit Cloud (~5 min)
- Go to Streamlit Cloud → your app → Settings → Secrets
- Paste all secrets:
  ```toml
  ANTHROPIC_API_KEY = "sk-ant-..."
  MAILERLITE_API_KEY = "..."
  MAILERLITE_GROUP_ID = "..."
  SUPABASE_URL = "https://xxxx.supabase.co"
  SUPABASE_KEY = "eyJ..."
  STRIPE_PIONEER_LINK = "https://buy.stripe.com/..."
  STRIPE_ORG_LINK = "https://buy.stripe.com/..."
  ```

### STEP 5 — Deploy New App Version (~2 min)
- Open GitHub repo → navigate to app folder
- Replace existing app file with contents of `securestep-app-v5.py`
- Commit → Streamlit detects the change and auto-redeploys
- Wait ~60 seconds → open securestep.ai to confirm

---

## DECISION POINTS

**If students table already exists from a prior version:**
- Skip the CREATE TABLE step — just run the ALTER TABLE for tier columns
- Use `ADD COLUMN IF NOT EXISTS` to avoid errors

**If Render.com webhook is not set up yet:**
- Manually upgrade students in Supabase Table Editor (tier, subscription_status) while webhook is pending
- This works immediately — webhook just automates it for new signups

**If Streamlit app shows secrets error on deploy:**
- Check Streamlit Cloud → Settings → Secrets — all 7 keys must be present
- Check for typos in key names (case-sensitive)

---

## COMMON MISTAKES
- Using the Supabase `anon` key for Supabase in Render (must use `service_role` key — has write access)
- Forgetting to add tier columns before deploying v5 (app will crash on login)
- Not copying the Stripe webhook signing secret into Render — webhook will reject all events
- Deploying to the wrong Streamlit app (check the URL matches securestep.ai)

## TOOLS & ACCESS NEEDED
- supabase.com — barb-app project (service_role key in Settings → API)
- stripe.com — Developers → API Keys + Webhooks
- render.com — free tier Web Service
- Streamlit Cloud — app Settings → Secrets
- GitHub — repo with app file

## KEY FILES
- `G:\My Drive\LMT-CONTENT\07-THE-APP\securestep-app-v5.py` — latest app version
- `G:\My Drive\LMT-CONTENT\07-THE-APP\webhook.py` — Stripe → Supabase tier updater
- `G:\My Drive\LMT-CONTENT\07-THE-APP\SUPABASE-SETUP.md` — full Supabase guide
- `G:\My Drive\LMT-CONTENT\07-THE-APP\STRIPE-SETUP.md` — full Stripe guide
