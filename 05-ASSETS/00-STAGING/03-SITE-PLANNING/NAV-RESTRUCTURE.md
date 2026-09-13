# Navigation Restructure — May 12, 2026

## Current Nav
```
Programs | Work With Us | Contact Us | Start Free Lesson
```

## New Nav
```
Programs | Partner With Us | Start Free Lesson
```

## Partner With Us — Dropdown/Sub-pages

| Nav Item | Slug | Page | Cal.com Link |
|----------|------|------|-------------|
| Deploy 50+TechBridge | /partner/ (main) | partner-with-us-page.html | /discovery-call |
| Become a Sponsor | /sponsor/ | sponsor-page.html | /brian-mckinney-mrtu8q |
| Book Brian to Speak | (links to Cal.com) | — | /speaking-inquiry |
| Let's Connect | (links to Cal.com) | — | /lets-connect |

## WordPress Steps
1. Create new Page: "Partner With Us" — paste partner-with-us-page.html
   - Template: Full Width Content
   - Slug: /partner/
2. Create new Page: "Become a Sponsor" — paste sponsor-page.html
   - Template: Full Width Content
   - Slug: /sponsor/
   - Parent page: Partner With Us
3. Go to Appearance → Menus
4. Remove "Work With Us" and "Contact Us" from nav
5. Add "Partner With Us" to nav
6. "Start Free Lesson" stays as the gold CTA button
7. Update footer links to match

## Pages to Build
- [x] partner-with-us-page.html — BUILT (00-STAGING/)
- [x] sponsor-page.html — BUILT (00-STAGING/)
- [ ] Deploy to WordPress
- [ ] Update nav menu
- [ ] Update footer

## Files in Staging
- 00-STAGING/partner-with-us-page.html
- 00-STAGING/sponsor-page.html
- 00-STAGING/sponsor-form-fields.md
- 00-STAGING/NAV-RESTRUCTURE.md
