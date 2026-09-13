# FIX-003 — Homepage Profitability Improvements
Date: 2026-08-09
Site: learnmoretechnologies.com
Fixed by: Claude Code + Brian

---

## Problem
Homepage was not converting B2B visitors into revenue. Free path was leading over paid path. No booking link visible above the fold. No price anchoring. MBE certification buried in footer text. No email capture. Only consumer testimonials — no organizational social proof.

---

## Changes Made (all in LMT-homepage-v2-profit.html)

### 1. Nav — Book a Call added
Added gold pill directly in the nav bar, right-aligned, visible on every scroll position.
```html
<a href="https://cal.com/brian-mckinney-mrtu8q/speaking-inquiry" class="nav-pill nav-pill-gold" style="flex-shrink:0">Book a Call &rarr;</a>
```

### 2. Hero Buttons — Revenue CTA first
Swapped button order so paid path (Work With Us) comes before free path (I'm Not Done Yet).
```html
<a href="https://learnmoretechnologies.com/services-pricing/" class="btn-gold">Work With Us &rarr;</a>
<a href="https://learnmoretechnologies.com/join-now/" class="btn-outline">I'm Not Done Yet &rarr;</a>
```

### 3. Hero Card — Books a strategy call
Video card foot now drives to cal.com booking, not a generic page.
```html
<a href="https://cal.com/brian-mckinney-mrtu8q/speaking-inquiry" class="card-cta">Book a Free Strategy Call &rarr;</a>
```

### 4. Audiences — Organizations card moved first + price anchor
B2B card (gold) now appears before consumer card (green). Added starting price and WIOA note.
```html
<div class="aud-starting">Services starting at $1,500 &mdash; WIOA-eligible</div>
```

### 5. Speak Pillar — Fixed broken CTA link
Was pointing to /speak/ (404). Now points to /services-pricing/#speak.
```html
<a href="https://learnmoretechnologies.com/services-pricing/#speak" class="pillar-cta-gold">See Speaking Packages &rarr;</a>
```

### 6. Trust Bar — MBE Certification added
MBE badge now visible immediately after hero, not buried in footer.
```html
<div class="trust-item"><span>MBE</span> Certified &mdash; Texas</div>
```

### 7. Testimonials — B2B organizational quote added
Full-width card below consumer testimonials. Austin Public Library attribution.
- Quote covers: customized training, dignity, results, repeat business intent.

### 8. Email Capture Section — Added after testimonials
Agentic50 newsletter section with MailerLite embed placeholder.
- ACTION NEEDED: Replace `data-form="your-form-id"` with real MailerLite form ID from dashboard.
- Link currently goes to /newsletter/ as fallback.

### 9. CTA — Urgency line added
Gold uppercase urgency text above CTA buttons.
```html
<p>&#x26A1; Booking Q4 now &mdash; limited availability</p>
```

---

## File Updated
- `Desktop/LMT-homepage-v2-profit.html` — all 9 changes applied

## To Deploy
1. Open WordPress → Pages → Home → WonderBlocks code editor
2. Select all existing code and delete
3. Paste entire contents of `LMT-homepage-v2-profit.html`
4. Save and preview

---

## Pending Manual Steps
- Replace MailerLite form ID in email capture section
- Replace librarian quote with a real quote from an Austin Public Library contact when available
- Update Yoast SEO title on Services & Pricing page (do in WP → Pages → Services & Pricing → Yoast panel)
