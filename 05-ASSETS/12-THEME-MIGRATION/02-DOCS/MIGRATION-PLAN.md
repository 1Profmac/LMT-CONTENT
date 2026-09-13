# Theme Migration Plan — Remove BuddyBoss from Public Site
## Status: PREPARATION — Not started
## Created: May 15, 2026

---

## Why
BuddyBoss Platform plugin loads article content via JavaScript, not HTML.
Google cannot read our 38 published articles. 4 months of content work is invisible.
BuddyBoss and LearnDash support have been contacted. No fix available yet.

## The Split — Two WordPress Sites, Each Doing One Job

| | learnmoretechnologies.com | learn.learnmoretechnologies.com |
|---|---|---|
| **Platform** | WordPress | WordPress |
| **Theme** | GeneratePress (clean, fast, SEO) | BuddyBoss Theme |
| **Plugins** | Yoast SEO, Jetpack | BuddyBoss Platform, BuddyBoss Pro, LearnDash |
| **Purpose** | Content, SEO, lead gen, Google ranking | Courses, community, student portal |
| **Google** | Indexes everything — 38 articles visible | Doesn't need indexing (behind login) |
| **Audience** | Public — anyone searching | Private — enrolled students |
| **Content** | Articles, blog, branded pages | Courses, lessons, quizzes, certificates |
| **CTA** | "Start Free Lesson" → links to subdomain | Student dashboard, progress tracking |
| **Mailchimp** | Signup forms, newsletter | Not needed |
| **Cal.com** | Booking links | Not needed |

## What Stays on learnmoretechnologies.com
- 38 published articles (standard WP posts — no changes needed)
- All internal links (unchanged)
- All Yoast SEO fields (unchanged)
- All redirects (unchanged)
- All URLs and slugs (unchanged)
- Branded pages (self-contained HTML — work on any theme)

## Branded Pages Ready (self-contained HTML, theme-independent)

| Page | File | Slug |
|---|---|---|
| Homepage | homepage-advocacy-education-speaking.html | / |
| Partner With Us | partner-with-us-page.html | /partner-with-us/ |
| Become a Sponsor | sponsor-page.html | /sponsor/ |
| Start Free Lesson | start-free-lesson-FINAL.html | /start-free-lesson/ |

## What Moves to Subdomain (learn.learnmoretechnologies.com)
- LearnDash courses, lessons, quizzes, certificates
- BuddyBoss community (profiles, groups, forums)
- Student registration/login
- BuddyBoss Theme + BuddyBoss Platform + BuddyBoss Pro
- All course-related pages

## What Stays on learnmoretechnologies.com
- WordPress + GeneratePress theme
- 38 published articles (standard WP posts)
- Yoast SEO Premium
- Jetpack Social
- All branded pages (Homepage, Partner With Us, Sponsor, Start Free Lesson)
- Mailchimp signup forms
- Cal.com booking links
- Google Business Profile
- All redirects
- Additional CSS (accessibility + branding)

## How They Connect
- "Start Free Lesson" button on main site → links to learn.learnmoretechnologies.com
- Articles on main site mention courses → link to subdomain
- Subdomain login page → branded to match main site colors
- Students find you on Google (main site) → enroll on subdomain
- Two separate WordPress installs, one Bluehost account

## Recommended Clean Themes (free, SEO-optimized)
1. **GeneratePress** — fastest, lightest, best SEO
2. **Astra** — most popular, huge customization
3. **Kadence** — modern, good free version

## Migration Steps (when ready)

### Step 1: Backup
- [ ] Full site backup on Bluehost (already done May 15)

### Step 2: Switch Theme
- [ ] Install GeneratePress (or Astra/Kadence)
- [ ] Activate it
- [ ] Test: View Source on article → Ctrl+F for article text
- [ ] If text appears → Google indexing problem is FIXED

### Step 3: Restore Branded Pages
- [ ] Go to each page in WordPress editor
- [ ] Switch to Code Editor
- [ ] Paste the HTML from this folder (each file has <!-- wp:html --> wrapper)
- [ ] Publish

### Step 4: Customize Theme
- [ ] Set brand colors: navy #0E1C2F, gold #C8942E
- [ ] Set fonts: DM Sans (body), Playfair Display (headings)
- [ ] Add Additional CSS from site-css-backup-may15.txt
- [ ] Update nav menu if needed

### Step 5: Test Everything
- [ ] Homepage renders correctly
- [ ] All 38 articles load
- [ ] Partner With Us page renders
- [ ] Start Free Lesson page works
- [ ] Mailchimp signup form works
- [ ] View Source shows article content in HTML
- [ ] Mobile responsive check

### Step 6: Request Indexing
- [ ] Go to Search Console → URL Inspection
- [ ] Request indexing for all 38 articles
- [ ] Submit sitemap: sitemap_index.xml

### Step 7: Set Up Student Portal (later)
- [ ] Create subdomain: learn.learnmoretechnologies.com
- [ ] Install WordPress + BuddyBoss + LearnDash
- [ ] Migrate courses
- [ ] Update course links on main site

---

## DO NOT
- Switch themes without a backup
- Delete BuddyBoss before courses are migrated
- Change any article URLs or slugs
- Do this on a Friday night

## Files in This Folder
- homepage-advocacy-education-speaking.html
- partner-with-us-page.html
- sponsor-page.html
- start-free-lesson-FINAL.html
- site-css-backup-may15.txt
- MIGRATION-PLAN.md (this file)

## Pages NOT Needed (replaced)
- contact-us-page.html → replaced by Partner With Us
- join-now-page.html → replaced by Start Free Lesson
