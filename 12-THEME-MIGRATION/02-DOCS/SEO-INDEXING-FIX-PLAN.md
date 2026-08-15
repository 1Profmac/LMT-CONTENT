# Google Indexing Fix Plan — Learn More Technologies
## Date: May 13, 2026

---

## CONFIRMED ROOT CAUSE — May 13, 2026
BuddyBoss theme loads article content via JavaScript, NOT in the HTML source code.
- View Page Source → Ctrl+F for article text → 0/0 results
- Google's crawler reads HTML → sees no content → skips indexing
- Search Console shows: "Discovered - currently not indexed" on all posts
- Google CAN render the page (screenshot shows it) but the HTML is empty
- Secondary issue: LearnDash Course Grid script throws a JavaScript SyntaxError on every page

## ACTION REQUIRED: Contact BuddyBoss Support
Tell them:
"My blog post content is not in the HTML source code. When I View Page Source
and search for text from my article, it returns 0 results. Google Search Console
shows 'Discovered - currently not indexed' on all my posts. Your theme is loading
article content via JavaScript and Google can't see it. How do I fix this?"

Until this is resolved, Yoast fields, internal links, and keywords won't help —
Google can't read the content at all.

---

## PHASE 1: Fix the JavaScript Error (Do First)
**Goal:** Remove the broken LearnDash script that may be blocking Google's renderer

1. Install "Asset CleanUp" plugin (free, by Developer Developer)
2. Open each blog post in the WordPress editor
3. Scroll to Asset CleanUp section at bottom
4. Find: `sfwd-lms/includes/course-grid/templates/skins/grid/script.js`
5. Disable it on ALL posts (not pages, not courses — just posts)
6. Save

**Test:** Go to Search Console → TEST LIVE URL on one article → check MORE INFO tab → JavaScript error should be gone

---

## PHASE 2: Clean the Sitemap (Same Day)
**Goal:** Stop Google from wasting crawl budget on junk pages

1. Go to Yoast SEO → Settings → Content Types
2. Click "Show more" to reveal all types
3. Turn OFF "Show in search results" for:
   - Submitted Essays
   - Replies
   - Discussions
   - Forums
   - Assignments
   - Certificates
   - Lessons (unless public standalone content)
   - Topics (LearnDash)
   - Quizzes
4. SAVE each page after toggling
5. Go to Yoast SEO → Settings → Categories & Tags
6. Turn OFF:
   - Discussion Tags
   - Group Categories
   - Course Tags
7. SAVE

**Test:** Visit learnmoretechnologies.com/sitemap_index.xml — should only show:
- post-sitemap.xml
- page-sitemap.xml
- category-sitemap.xml
- sfwd-courses-sitemap.xml (keep if courses are public)
- author-sitemap.xml

---

## PHASE 3: Request Indexing for All Articles (Same Day)
**Goal:** Tell Google to crawl your real content NOW

Go to Search Console → URL Inspection → paste each URL → click REQUEST INDEXING:

1. https://learnmoretechnologies.com/what-is-agetech-complete-guide/
2. https://learnmoretechnologies.com/the-76-trillion-blind-spot-why-marketers-ignore-adults-50/
3. https://learnmoretechnologies.com/850-billion-cost-ageism-workforce/
4. https://learnmoretechnologies.com/the-ai-gap-is-real-10-consulting-firms-proved-it-50techbridge-was-already-there/
5. https://learnmoretechnologies.com/digital-divide-adults-over-50/
6. https://learnmoretechnologies.com/ai-confidence-gap-older-workers/
7. https://learnmoretechnologies.com/thriving-in-the-age-of-ai-career-security-after-50/
8. https://learnmoretechnologies.com/50-plus-workforce-untapped-asset/
9. https://learnmoretechnologies.com/from-awareness-to-action-leading-the-solution-beyond-aarp/
10. https://learnmoretechnologies.com/why-the-850-billion-series-is-really-a-letter-to-the-50-community/
11. https://learnmoretechnologies.com/from-13-locations-to-50000-digital-pioneers/
12. https://learnmoretechnologies.com/what-your-agency-will-discover-by-deploying-50techbridge/
13. https://learnmoretechnologies.com/influence-is-not-who-you-know/
14. https://learnmoretechnologies.com/how-50-adults-can-use-smartphones-for-independent-living-2026-complete-guide/
15. https://learnmoretechnologies.com/the-agetech-guide-technology-for-aging-well/
16. https://learnmoretechnologies.com/how-50plustechbridge-is-helping-redefine-independent-living/
17. https://learnmoretechnologies.com/life-after-50-in-a-digital-world/
18. https://learnmoretechnologies.com/independent-living-with-mobile-devices-tablets-10-ways-smart-tech-actually-makes-life-easier-after-50/
19. https://learnmoretechnologies.com/independent-living-with-agete/
20. https://learnmoretechnologies.com/how-wioa-funds-pay-for-ai-training-for-adults-50/
21. https://learnmoretechnologies.com/ai-workshops-for-experienced-employees-the-90-minute-turnkey-solution/
22. https://learnmoretechnologies.com/blog/

Do ONE at a time. Wait for each to confirm before doing the next.
Do NOT resubmit the same URL twice — one request per URL.

---

## PHASE 4: Article Consolidation & Rewrite (This Week)
**Goal:** 21 articles → 14 keepers + 7 redirects. Every keeper gets SEO fields + internal links via API.

### Category 1: The Problem (Ageism & The Gap)
1. ID 2334 — The $76 Trillion Blind Spot
2. ID 2296 — The $850 Billion Cost of Ageism (absorb 2300)
3. ID 2318 — The Digital Divide for Adults Over 50 (absorb 415)
4. ID 2328 — The Confidence Gap: Why AI Training Fails Workers 50+

### Category 2: The Opportunity (AI & Workforce)
5. ID 2448 — The AI Gap Is Real. 10 Consulting Firms Proved It.
6. ID 2508 — Thriving in the Age of AI: Career Security After 50+
7. ID 2290 — Why Your 50+ Workforce Is Your Biggest Untapped Asset

### Category 3: The Solution (50+TechBridge)
8. ID 2314 — What Is AgeTech? Complete Guide for 2026 (absorb 468)
9. ID 2470 — From Awareness to Action: Beyond AARP
10. ID 2294 — What Your Agency Will Discover by Deploying 50+TechBridge
11. ID 2336 — From 13 Locations to 50,000 Digital Pioneers

### Category 4: Practical Guides
12. ID 2209 — How WIOA Funds Pay for AI Training for Adults 50+
13. ID 2222 — AI Workshops for Experienced Employees: 90-Minute Solution
14. ID 818 — How 50+ Adults Can Use Smartphones for Independent Living (absorb 588, 536, 756)

### Redirects Needed
- 468 → 2314 (AgeTech guide)
- 415 → 2318 (Digital Divide)
- 588 → 818 (Smartphones)
- 536 → 818
- 756 → 818
- 2300 → 2296 ($850B)
- 2401 — Influence Is Not Who You Know (keep but deprioritize, personal essay)

### Each Rewrite Includes
- Focus keyphrase, SEO title, meta description (Yoast)
- 3-5 internal links to other articles in the hub
- 1-2 external authority links (AARP, RAND, HBR, DOL, EEOC)
- CTA with booking link: https://cal.com/brian-mckinney-mrtu8q
- Updated proof points (200+ adults, 12 locations)
- Standard WordPress blocks only (no BuddyBoss shortcodes)

---

## PHASE 5: Add Internal Links Between Articles (This Week)
**Goal:** Connect your content so Google sees a hub, not 22 orphan pages

Every article should link to 2-3 other articles on your site.
Every article should have 1-2 external authority links (AARP, HBR, RAND, EEOC).
Every article should end with a CTA linking to cal.com/brianmckinney.

Link map:
- AgeTech Guide → links to $76T, $850B, Confidence Gap
- $76T Blind Spot → links to $850B, AI Gap, AgeTech Guide
- $850B Ageism → links to $76T, Untapped Asset, AI Gap
- AI Gap → links to $850B, Confidence Gap, $76T
- Digital Divide → links to Confidence Gap, AgeTech Guide, $850B
- Confidence Gap → links to AI Gap, Digital Divide, Thriving in AI
- Thriving in AI → links to Confidence Gap, Untapped Asset, AI Gap
- Untapped Asset → links to $850B, $76T, Thriving in AI
- Beyond AARP → links to $850B, AgeTech Guide, Digital Divide
- All others → link to at least 2 of the above pillar articles

(Claude will provide the exact rewritten articles with links embedded)

---

## PHASE 6: Build Backlinks (Ongoing Weekly)
**Goal:** External links pointing to your articles = Google trusts your site faster

Weekly actions:
- Post 1 article link on LinkedIn with a carousel or text post
- Share 1 article in relevant Facebook groups
- Include article links in your Agentic50 newsletter
- When doing outreach emails, include a relevant article link
- Submit your site to relevant directories (AgeTech, workforce dev)

---

## PHASE 7: Fix the 404 Page (Today)
**Goal:** Stop losing the 70 impressions going to a dead URL

Install "Redirection" plugin (free, by John Godley)
Add redirect:
- FROM: /850-billion-cost-age-discrimination-workforce/
- TO: /850-billion-cost-ageism-workforce/

---

## PHASE 8: Monitor Progress (Weekly Check)
**Goal:** Track what's working

Every Monday check:
- Search Console → Pages → how many indexed?
- Search Console → Performance → impressions, clicks, position
- Yoast dashboard → SEO scores

Expected timeline:
- Week 1: JavaScript error fixed, sitemap cleaned, indexing requested
- Week 2-3: Articles start appearing as indexed in Search Console
- Week 4-6: Rankings begin (position 20-50 range)
- Week 6-12: Rankings improve with backlinks and internal links

---

## TOMORROW'S TO-DO LIST

1. Contact BuddyBoss support — tell them article content is not in HTML source code, Google can't index posts
2. Finish Google Business Profile — upload photos, set hours, add services, add social links
3. Delete the duplicate unverified Google Business listing (309 East 11th Street)
4. Send Google review link to 5 past participants/partners: https://g.page/r/CYS5efh1dTMBEAE/review
5. Add review link to email signature and post-workshop follow-up emails
6. Respond to LinkedIn service requests (Sadie Ashmore White — Speaking, Mario A. Vitale — LMT inquiry)

---

## DO NOT DO
- Do not change slugs again (every slug change resets Google's clock)
- Do not resubmit the same URL multiple times
- Do not update LearnDash or BuddyBoss without backing up first
- Do not install unnecessary plugins
- Do not touch the Advanced URL Cleanup section in Yoast
