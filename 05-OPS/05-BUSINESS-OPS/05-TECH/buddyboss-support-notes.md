# BuddyBoss Support — Technical Notes
## Updated: May 15, 2026

---

## Issue: Article content not in HTML source code — Google cannot index

### What We've Done
- Updated BuddyBoss Platform Pro to 3.0.1 — DID NOT FIX the issue
- Updated BuddyBoss Platform to 3.0.1 — TESTING NOW
- Full site backup taken before updates
- Sent initial support ticket May 14, 2026

### The Problem (unchanged after Pro update)
- View Page Source on any blog post → Ctrl+F for article text → 0/0 results
- HTML source shows only BuddyBoss template code: `tmpl-bb-link-preview`, `bb-url-scrapper`, `bb-ajax-loader`
- Article renders visually for visitors (JavaScript loads the content)
- Google Search Console: "Discovered - currently not indexed" on all posts
- Google URL Inspection → HTML tab shows template code, not article content
- Google URL Inspection → Screenshot tab shows page renders visually
- Google URL Inspection → MORE INFO tab shows JavaScript error: "Uncaught SyntaxError: Unexpected token '<'" from sfwd-lms/includes/course-grid/templates/skins/grid/script.js
- Only 6-8 pages indexed out of 38 published

### What We Need From BuddyBoss
1. How do we configure BuddyBoss Theme/Platform so blog post content is rendered in the initial HTML (server-side), not loaded via JavaScript?
2. Is there a setting to enable server-side rendering for posts?
3. Is this a known issue with BuddyBoss Theme and SEO/Google indexing?
4. Does the 3.0.1 update address this?

### Environment
- WordPress 6.9.4
- BuddyBoss Platform: 3.0.1 (just updated from 2.21.1)
- BuddyBoss Platform Pro: 3.0.1 (just updated from 2.13.2)
- BuddyBoss Theme: check version
- LearnDash LMS: active
- Yoast SEO Premium: 27.6
- Hosting: Bluehost
- Site: https://learnmoretechnologies.com
- Example post: https://learnmoretechnologies.com/what-is-agetech-complete-guide/

### Timeline
- May 13: Discovered issue (View Source test)
- May 13: Confirmed via Google Search Console URL Inspection
- May 14: Sent initial support ticket
- May 15: Updated Platform Pro to 3.0.1 — no change
- May 15: Updating Platform to 3.0.1 — testing
