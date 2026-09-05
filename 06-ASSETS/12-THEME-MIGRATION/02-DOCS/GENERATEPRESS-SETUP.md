# GeneratePress Theme Setup Checklist
## Match BuddyBoss brand on clean theme
## Updated: May 15, 2026

---

## Step 1: Install GeneratePress (5 min)
- [ ] Appearance → Themes → Add New → search "GeneratePress"
- [ ] Install → Activate
- [ ] Optional: Install GeneratePress Premium ($59/year) for more control — free version works fine to start

---

## Step 2: Brand Colors (5 min)
Go to Appearance → Customize → Colors

### Body
- [ ] Background: #0E1C2F
- [ ] Text: #FFFFFF

### Header
- [ ] Background: #0E1C2F

### Primary Navigation
- [ ] Background: #0E1C2F
- [ ] Links: #FFFFFF
- [ ] Links hover: #C8942E

### Buttons
- [ ] Background: #C8942E
- [ ] Text: #0E1C2F
- [ ] Hover background: #E8B84B

### Content
- [ ] Background: #0E1C2F
- [ ] Text: #FFFFFF
- [ ] Links: #C8942E

### Sidebar Widgets
- [ ] Background: #0E1C2F
- [ ] Text: #FFFFFF
- [ ] Links: #C8942E

### Footer Widgets
- [ ] Background: #0E1C2F
- [ ] Text: #FFFFFF

### Footer Bar
- [ ] Background: #0E1C2F
- [ ] Text: #A0AEC0

---

## Step 3: Fonts (5 min)
Go to Appearance → Customize → Typography

| Element | Font | Weight | Size |
|---|---|---|---|
| Body | DM Sans | 400 | 24px |
| H1 | Playfair Display | 900 | 52px |
| H2 | Playfair Display | 700 | 40px |
| H3 | DM Sans | 700 | 30px |
| Navigation | DM Sans | 500 | 20px |

Google Fonts URL (if needed):
```
https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@300;400;500;600;700&display=swap
```

---

## Step 4: Header / Nav Bar (10 min)
Go to Appearance → Customize → Header

- [ ] Upload logo (LEARNMORE TECHNOLOGIES white logo)
- [ ] Background color: #0E1C2F
- [ ] Nav links color: #FFFFFF
- [ ] Nav links hover: #C8942E
- [ ] Add nav items:
  - Programs
  - 50+Blog
  - Partner With Us
  - Start Free Lesson (gold button style)

### Start Free Lesson Button CSS
Add to Additional CSS:
```css
.main-navigation .start-free-lesson a,
.main-navigation .menu-item-has-button a {
    background: #C8942E !important;
    color: #0E1C2F !important;
    padding: 12px 24px !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}
.main-navigation .start-free-lesson a:hover,
.main-navigation .menu-item-has-button a:hover {
    background: #E8B84B !important;
}
```

---

## Step 5: Footer (5 min)
Go to Appearance → Customize → Footer

- [ ] Background: #0E1C2F
- [ ] Text color: #A0AEC0
- [ ] Link color: #C8942E
- [ ] Add footer content:
  - © 2026 Learn More Technologies. MBE Certified.
  - hello@learnmoretechnologies.com
  - Social links: LinkedIn, YouTube, Facebook

---

## Step 6: Blog Layout (5 min)
Go to Appearance → Customize → Blog

- [ ] Post layout: columns or list (your choice)
- [ ] Show featured image: yes
- [ ] Show excerpt: yes
- [ ] Excerpt length: 30-40 words
- [ ] Read more text: "Read Article →"

---

## Step 7: Paste Additional CSS
Go to Appearance → Customize → Additional CSS

Paste the complete CSS from `site-css-backup-may15.txt` in this folder. This includes:
- Blog page styling
- Accessibility text sizes (24px body, 52px H1)
- YouTube iframe fixes
- BuddyBoss activation page overrides (can remove these after migration)
- All custom page overrides

NOTE: Remove the BuddyBoss-specific CSS resets after migration:
```css
/* REMOVE THESE AFTER SWITCHING — they're BuddyBoss overrides */
.bb-grid,.container,#content,#primary,#main,.site-main{...}
```

---

## Step 8: Set Homepage and Blog Page
Go to Settings → Reading

- [ ] Homepage displays: A static page
- [ ] Homepage: Programs (or whatever your homepage is)
- [ ] Posts page: 50+Blog

---

## Step 9: Paste Branded Pages
For each branded page, go to Pages → edit → Code Editor → paste HTML:

- [ ] Homepage → paste homepage-advocacy-education-speaking.html
- [ ] Partner With Us → paste partner-with-us-page.html
- [ ] Sponsor → paste sponsor-page.html
- [ ] Start Free Lesson → paste start-free-lesson-FINAL.html

Each file has `<!-- wp:html -->` wrapper — WordPress renders them as raw HTML.
The inline `<style>` tags in each file override the theme — design stays identical.

---

## Step 10: Test
- [ ] Homepage loads with branded design
- [ ] Partner With Us shows 3 cards (navy/gold)
- [ ] Start Free Lesson works with hCaptcha
- [ ] Blog page lists articles
- [ ] Individual article loads with correct styling
- [ ] Nav bar shows correct menu items with gold button
- [ ] Footer shows correct info
- [ ] Mobile responsive — check on phone
- [ ] View Source on article → Ctrl+F for article text → FOUND
- [ ] Mailchimp signup form works
- [ ] Cal.com booking links work

---

## What Will Look Different
- Blog listing page layout (GeneratePress style vs BuddyBoss style)
- Default article page layout (wider content area, cleaner)
- Profile/community pages GONE (moved to subdomain)
- Simpler, faster page loads

## What Will Look Identical
- Homepage (inline CSS)
- Partner With Us (inline CSS)
- Sponsor page (inline CSS)
- Start Free Lesson (inline CSS)
- Brand colors (set in Customizer)
- Fonts (set in Customizer)
- Text sizes (set in Additional CSS)

---

## Estimated Time: 30-45 minutes
