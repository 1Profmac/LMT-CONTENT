# SOP-16 — WPCode Nav Injection
## Override BuddyBoss nav styling with JavaScript — no CSS fight

**Purpose:** BuddyBoss overrides Additional CSS for nav elements. This process uses WPCode to inject JavaScript that applies inline styles directly to nav links — inline styles always win.
**Trigger:** Any nav styling change needed (pill shapes, button colors, highlights)
**Owner:** Brian McKinney
**Time required:** 5 minutes
**Frequency:** One-time setup per site; edit the snippet to change styles

---

## QUICK REFERENCE
1. Write JS that targets `#primary-navbar li a` and applies inline styles
2. WPCode → + Add Snippet → JavaScript Snippet
3. Paste JS (no script tags), set title, set Location = Site Wide Footer
4. Toggle Active → Save Snippet
5. Hard refresh site to verify

---

## STEP-BY-STEP

### STEP 1 — Write the JavaScript
- Target selector: `#primary-navbar li a` (confirmed from DevTools)
- Apply inline styles via `element.style.cssText` — these beat ALL BuddyBoss CSS
- To target a specific nav item (e.g. Start Free Lessons): `a.href.indexOf('start-free')`
- File saved at: `Desktop/nav-wpcode-inject.html` — copy JS between the `<script>` tags

### STEP 2 — Open WPCode
- WordPress admin → **WPCode** → **+ Add Snippet**
- Click **JavaScript Snippet**

### STEP 3 — Paste and Configure
- Add title: `Nav Pill Fix` (or descriptive name)
- Paste the JS code — do NOT include `<script>` tags
- Scroll to **Insertion** section
- Insert Method: **Auto Insert**
- Location: **Site Wide Footer** (must be footer — nav must exist in DOM first)

### STEP 4 — Activate and Save
- Toggle **Active** (blue)
- Click **Update** (top right)

### STEP 5 — Verify
- Go to the live site — hard refresh (Ctrl+Shift+R)
- Check nav pills are equal and Start Free Lessons is gold
- If not: check the href slug matches what's in the JS (`start-free`)

---

## DECISION POINTS

**If styles don't apply:**
- Open DevTools → Console tab — look for JS errors
- Confirm `#primary-navbar` exists: type `document.querySelector('#primary-navbar')` in console
- If null: the selector changed — inspect the nav and update the selector in the snippet

**If only some items are styled:**
- The JS uses `querySelectorAll` — all matching links get styled
- Check for nested `<ul>` dropdowns — may need `#primary-navbar a` (all descendants) instead of `li > a`

**If the gold button isn't applying:**
- Check the actual href: right-click Start Free Lessons → Inspect → copy the `href` value
- Update `indexOf('start-free')` to match the actual slug

---

## COMMON MISTAKES
- Pasting the `<script>` tags into WPCode — only paste the JS inside them
- Setting location to Header instead of Footer — the nav doesn't exist yet when header runs
- Forgetting to toggle Active before saving — snippet won't fire

## CURRENT NAV CONFIGURATION (as of 2026-09-08)
| Item | Style |
|---|---|
| About | Pill, transparent |
| Programs | Pill, transparent |
| Digital Pioneer Gallery | Pill, transparent (gold removed) |
| Work With Us | Pill, transparent |
| Start-Free-Lessons | Pill, gold (#C8942E), bold |

## TOOLS & ACCESS NEEDED
- WordPress admin access → WPCode plugin (already installed)
- Nav JS file: `Desktop/nav-wpcode-inject.html`
- DevTools (F12) to inspect nav HTML if selector needs updating
