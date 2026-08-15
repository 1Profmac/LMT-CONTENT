# LMT Content Development Process
## Craig Hewitt Method + SEO Rules + Brian's Content Engine
## Updated: May 14, 2026

---

## STEP 1: Plain Text Draft (Craig's Step 1)
Write the article as plain text first. No formatting, no links, no images. Just the argument.

**While drafting, nail these:**
- Pick ONE focus keyphrase (what someone would Google to find this)
- Put the keyphrase in the first 100 words
- Use H2/H3 subheadings every 200-300 words with keyword variations
- Cover the topic completely — Google ranks topical authority, not keyword stuffing
- Minimum 800 words for pillar articles, 500+ for shorter posts
- End with a CTA

---

## STEP 2: SEO Layer (New — Before WordPress)
Before touching WordPress, add these to the plain text:

### Internal Links (3-5 per article)
Link to other articles in the hub using descriptive anchor text:
- "the $850 billion cost of ageism in the workforce" — not "click here"
- Use the 4-category system to cross-link:
  - Problem articles link to → Opportunity + Solution articles
  - Opportunity articles link to → Problem + Solution articles
  - Solution articles link to → Problem + Practical Guide articles
  - Practical Guides link to → Solution + Problem articles

### External Authority Links (1-2 per article)
- AARP, RAND Corporation, HBR, DOL/WIOA, EEOC
- Opens in new tab
- Bolsters credibility with Google

### CTA at Bottom
- Booking link: https://cal.com/brian-mckinney-mrtu8q
- Course link: https://learnmoretechnologies.com/join-now
- Email: hello@learnmoretechnologies.com

### Yoast SEO Fields (prepare before pasting into WP)
- Focus keyphrase — exact search term
- SEO title — under 60 characters, keyphrase near front
- Meta description — under 155 characters, includes keyphrase, ends with hook
- Slug — short, keyword-rich, NEVER change after publishing
- SEO keywords — 5-8 related terms for tags and content planning

### Yoast SEO Output Template (Claude generates this for every article)
```
Focus keyphrase: [exact search term]
SEO title: [under 60 chars, keyphrase near front]
Meta description: [under 155 chars, keyphrase included, ends with hook]
Slug: [short-keyword-rich-slug]
SEO keywords: [keyword1, keyword2, keyword3, keyword4, keyword5]
Alt text for featured image: [describes image + includes keyphrase]
```

### Featured Image Prompt (for AI image generation or Canva)
Claude generates a featured image prompt for every article:
```
FEATURED IMAGE PROMPT:
Style: Professional, modern, warm tones (gold #c8942f, navy #0e1c2f)
Subject: [specific to article topic]
Text overlay: [article title or key stat]
Dimensions: 1200x628px (WordPress/social share optimized)
Brand: Include 50+TechBridge or Learn More Technologies logo
Mood: [empowering / urgent / educational — matches article tone]
Alt text: [descriptive text including focus keyphrase]
```

### Images
- Featured image with alt text containing keyphrase
- At least 1 image in body with descriptive alt text

---

## STEP 3: WordPress Copy (Craig's Step 2)
Paste into WordPress using STANDARD BLOCKS ONLY:
- Heading block (H1, H2, H3)
- Paragraph block
- List block
- Image block

### CRITICAL RULES
- NO BuddyBoss shortcodes or dynamic widgets inside article body
- NO LearnDash shortcodes in blog posts
- Content MUST be in the raw HTML — not loaded by JavaScript
- **Verification test:** Right-click → View Page Source → Ctrl+F for a sentence from your article. If it's not in the source, Google can't see it.

### Fill Yoast Box
- Paste focus keyphrase
- Paste SEO title
- Paste meta description
- Confirm green light for SEO + Readability

---

## STEP 4: Review & Publish (Craig's Step 3 — "Read the Doc")
Before hitting Publish:

1. Preview in incognito window — does it render?
2. View Page Source → Ctrl+F test — is content in HTML?
3. Yoast light is GREEN (not orange/red)
4. Readability score is GREEN
5. Featured image has alt text
6. All internal links work
7. CTA with booking link is at bottom
8. Proof points are current: 200+ adults, 12 locations, 9 libraries, 3 senior centers

---

## STEP 5: Request Indexing
After publishing:
1. Go to Google Search Console → URL Inspection
2. Paste the new article URL
3. Click REQUEST INDEXING (once — never repeat)
4. Do NOT change the slug after this point

---

## STEP 6: Content Engine — One Article = One Week
(Brian's weekly distribution system)

| Day | Action |
|---|---|
| Monday | Publish WP article → post excerpt on LinkedIn + FB with article link |
| Tuesday | Build Canva carousel from article |
| Wednesday | Post carousel on LinkedIn + FB → send Agentic50 newsletter with article link |
| Thursday | Repost carousel to FB Groups |
| Friday | Text engagement post on LinkedIn + FB |

### Every Post Includes
- Booking link: https://cal.com/brian-mckinney-mrtu8q
- #agentic50
- CTA (question or action)
- Link back to the article (backlink for Google)

---

## STEP 7: Weekly Monitoring (Every Monday)
- Google Search Console → Pages → how many indexed?
- Google Search Console → Performance → impressions, clicks, position
- Yoast dashboard → SEO scores
- LinkedIn Analytics → post performance
- HubSpot → new contacts from content

---

## Article Categories (Content Hub)

### The Problem (Ageism & The Gap)
- $76 Trillion Blind Spot
- $850 Billion Cost of Ageism
- Digital Divide for Adults Over 50
- Confidence Gap: AI Training Fails Workers 50+

### The Opportunity (AI & Workforce)
- AI Gap Is Real — 10 Consulting Firms
- Thriving in AI: Career Security After 50+
- 50+ Workforce Is Your Biggest Untapped Asset

### The Solution (50+TechBridge)
- What Is AgeTech? Complete Guide 2026
- From Awareness to Action: Beyond AARP
- What Your Agency Will Discover
- From 13 Locations to 50,000 Pioneers

### Practical Guides
- How WIOA Funds Pay for AI Training
- AI Workshops: 90-Minute Turnkey Solution
- Smartphones for Independent Living

---

## Published Articles — Full Inventory

### The Problem (Ageism & The Gap)
| ID | Title | URL | Status |
|---|---|---|---|
| 2334 | The $76 Trillion Blind Spot: Why Marketers Ignore Adults 50+ | /the-76-trillion-blind-spot-why-marketers-ignore-adults-50/ | Rewrite |
| 2296 | The $850 Billion Cost of Ignoring Your Experienced Workers | /850-billion-cost-ageism-workforce/ | Rewrite |
| 2318 | The Digital Divide for Adults Over 50: Data, Causes, and Solutions | /digital-divide-adults-over-50/ | Rewrite |
| 2328 | The Confidence Gap: Why AI Training Fails Workers Over 50+ | /ai-confidence-gap-older-workers/ | Rewrite |

### The Opportunity (AI & Workforce)
| ID | Title | URL | Status |
|---|---|---|---|
| 2448 | The AI Gap Is Real. 10 Consulting Firms Proved It. | /the-ai-gap-is-real-10-consulting-firms-proved-it-50techbridge-was-already-there/ | Rewrite |
| 2508 | Thriving in the Age of AI: Career Security After 50+ | /thriving-in-the-age-of-ai-career-security-after-50/ | Rewrite |
| 2290 | Why Your 50+ Workforce Is Your Biggest Untapped Asset | /50-plus-workforce-untapped-asset/ | Rewrite |

### The Solution (50+TechBridge)
| ID | Title | URL | Status |
|---|---|---|---|
| 2314 | What Is AgeTech? The Complete Guide for 2026 | /what-is-agetech-complete-guide/ | Rewrite (absorb 468) |
| 2470 | From Awareness to Action: Leading the Solution Beyond AARP | /from-awareness-to-action-leading-the-solution-beyond-aarp/ | Rewrite |
| 2294 | What Your Agency Will Discover by Deploying 50+TechBridge | /what-your-agency-will-discover-by-deploying-50techbridge/ | Rewrite |
| 2336 | From 13 Locations to 50,000 Digital Pioneers | /from-13-locations-to-50000-digital-pioneers/ | Rewrite |

### Practical Guides
| ID | Title | URL | Status |
|---|---|---|---|
| 2209 | How WIOA Funds Pay for AI Training for Adults 50+ | /how-wioa-funds-pay-for-ai-training-for-adults-50/ | Rewrite |
| 2222 | AI Workshops for Experienced Employees: 90-Minute Solution | /ai-workshops-for-experienced-employees-the-90-minute-turnkey-solution/ | Rewrite |
| 818 | How 50+ Adults Can Use Smartphones for Independent Living | /how-50-adults-can-use-smartphones-for-independent-living-2026-complete-guide/ | Rewrite (absorb 588, 536, 756) |

### Redirect (delete/merge)
| ID | Title | URL | Redirect To |
|---|---|---|---|
| 2300 | Why the $850B Series Is a Letter to the 50+ Community | /why-the-850-billion-series-is-really-a-letter-to-the-50-community/ | → 2296 |
| 415 | Life After 50 In A Digital World | /life-after-50-in-a-digital-world/ | → 2318 |
| 468 | The AgeTech Guide: Technology for Aging Well | /the-agetech-guide-technology-for-aging-well/ | → 2314 |
| 588 | Independent Living With Mobile Devices & Tablets | /independent-living-with-mobile-devices-tablets-10-ways-smart-tech-actually-makes-life-easier-after-50/ | → 818 |
| 536 | How 50PlusTechbridge Is Helping Redefine Independent Living | /how-50plustechbridge-is-helping-redefine-independent-living/ | → 818 |
| 756 | 10 Tech Tools That Make Independent Living Easier After 50 | /independent-living-with-agete/ | → 818 |

### Deprioritized
| ID | Title | URL | Status |
|---|---|---|---|
| 2401 | Influence Is Not Who You Know | /influence-is-not-who-you-know/ | Keep — personal essay, low SEO value |

---

## DO NOT
- Change slugs after publishing
- Use BuddyBoss shortcodes in articles
- Publish without Yoast fields filled in
- Publish without the View Source test
- Publish without internal links
- Resubmit the same URL to Google multiple times
- Skip the booking link CTA
- Inflate proof points (real numbers: 200+ adults, 12 locations, 9 libraries, 3 senior centers)

---

## Tools
- **WordPress** — publishing (standard blocks only)
- **Yoast SEO** — on-page SEO fields
- **Google Search Console** — indexing + monitoring
- **Canva** — carousels
- **HeyGen** — 60-sec talking heads (browser-based)
- **LinkedIn** — primary distribution
- **Facebook** — mirror LinkedIn
- **HubSpot** — pipeline
- **Cal.com** — booking
- **Claude Code** — article rewrites via WP REST API
