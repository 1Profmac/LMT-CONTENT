# SOP-05 — Content Development
## Article → WordPress → SEO → Weekly Distribution

**Purpose:** Produce one article per week that ranks on Google and drives bookings.
**Trigger:** Content idea or topic selected for the week.
**Owner:** Brian McKinney
**Time required:** 2-3 hours (writing + publish + distribution)
**Frequency:** Weekly

---

## QUICK REFERENCE
1. Write plain text draft — pick ONE keyphrase
2. Add SEO layer (internal links, Yoast fields, CTA)
3. Paste into WordPress (standard blocks only) → fill Yoast → View Source test
4. Request indexing in Google Search Console
5. Run content engine Mon–Fri

---

## PREREQUISITES
- [ ] Topic and focus keyphrase decided
- [ ] WordPress admin access
- [ ] Google Search Console access
- [ ] Canva Pro (for carousel — Day 2)

---

## STEP-BY-STEP

### STEP 1 — Plain Text Draft
- Write as plain text first — no formatting, no links
- ONE focus keyphrase (what someone would Google)
- Keyphrase in first 100 words
- H2/H3 subheadings every 200-300 words
- Minimum 800 words (pillar) or 500+ (shorter)
- End with CTA

### STEP 2 — SEO Layer (before WordPress)

**Internal links (3-5 per article):**
Use descriptive anchor text — never "click here"
Cross-link: Problem ↔ Opportunity ↔ Solution ↔ Guide articles

**External links (1-2):**
AARP, RAND, HBR, DOL/WIOA, EEOC — opens in new tab

**Yoast fields to prepare before pasting into WP:**
```
Focus keyphrase: [exact search term]
SEO title: [under 60 chars, keyphrase near front]
Meta description: [under 155 chars, keyphrase + hook]
Slug: [short-keyword-rich — NEVER change after publishing]
Alt text for featured image: [describes image + keyphrase]
```

**CTA at bottom of every article:**
- Booking: https://cal.com/brian-mckinney-mrtu8q
- Course: https://learnmoretechnologies.com/join-now
- Email: hello@learnmoretechnologies.com

### STEP 3 — WordPress Copy
- Paste using **STANDARD BLOCKS ONLY**: Heading, Paragraph, List, Image
- NO BuddyBoss shortcodes | NO LearnDash shortcodes in blog posts
- Fill Yoast box: keyphrase + SEO title + meta description
- Confirm green light for SEO + Readability

**Verification test (do not skip):**
Right-click → View Page Source → Ctrl+F for a sentence from your article.
If it's not in the source HTML → Google can't see it → do not publish yet.

### STEP 4 — Review Before Publishing
- [ ] Preview in incognito — does it render?
- [ ] View Page Source → Ctrl+F test passes
- [ ] Yoast SEO light: GREEN
- [ ] Readability light: GREEN
- [ ] Featured image has alt text
- [ ] All internal links work
- [ ] CTA with booking link at bottom
- [ ] Numbers are current and verified (no inflated stats)

### STEP 5 — Request Indexing
1. Google Search Console → URL Inspection
2. Paste the article URL
3. Click **REQUEST INDEXING** — once only, never repeat
4. Do NOT change the slug after this point

### STEP 6 — Content Engine (One Article = One Week)

| Day | Action |
|---|---|
| Monday | Publish WP article → post excerpt on LinkedIn + FB with link |
| Tuesday | Build Canva carousel from article |
| Wednesday | Post carousel on LinkedIn + FB → send Agentic50 newsletter |
| Thursday | Repost carousel to FB Groups |
| Friday | Text engagement post on LinkedIn + FB |

Every post includes: booking link + #agentic50 + CTA + article link

### STEP 7 — Weekly Monitoring (Every Monday)
- Search Console → Pages (how many indexed?)
- Search Console → Performance (impressions, clicks, position)
- LinkedIn Analytics → post performance
- HubSpot → new contacts from content

---

## DECISION POINTS
- **Yoast stays orange/red?** → Rewrite intro to include keyphrase earlier. Add more subheadings. Shorten sentences.
- **View Source test fails?** → Do NOT publish. Content is loaded by JavaScript — Google can't crawl it. Check for BuddyBoss shortcodes interfering.
- **Article under 500 words?** → Either expand or combine with a related piece. Thin content hurts rankings.

## COMMON MISTAKES
- Changing the slug after publishing (breaks Google's index for that URL)
- Skipping the View Source test (you won't know content is invisible until rankings tank)
- Using inflated numbers (always use verified stats from feedback_verified_numbers.md)
- Publishing without a CTA booking link

## DO NOT
- Change slugs after publishing
- Use BuddyBoss or LearnDash shortcodes in articles
- Resubmit the same URL to Google multiple times
- Publish without Yoast fields filled
