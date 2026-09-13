# Universal Nav — WordPress Setup
**Date:** 2026-08-18
Apply to: learnmoretechnologies.com AND 50plustechbridge.com

---

## STEP 1 — WP Menu Items

Go to: **WP Admin → Appearance → Menus**

Set the Primary Menu to these items in this order:

| Label | URL | Notes |
|---|---|---|
| About | /about/ | Internal |
| Train | /train/ | Internal |
| Speaking | /speak/ | Internal |
| 50+TechBridge | https://50plustechbridge.com | External — check "Open in new tab" |
| Digital Pioneer Gallery | https://digitalpioneer.ai | External — add CSS class: `menu-btn-gallery` |
| Book a Call | https://cal.com/brian-mckinney-mrtu8q/speaking-inquiry | External — add CSS class: `menu-btn-call` |
| Start Free Lesson | https://50plustechbridge.com/start-free-lesson/ | External — add CSS class: `menu-btn-lesson` |

> To add CSS classes to menu items:
> In Menu editor → click item → check "CSS Classes" option
> (Enable via Screen Options → top right of Menus page)

---

## STEP 2 — Additional CSS

Go to: **WP Admin → Appearance → Customize → Additional CSS**

Paste this:

```css
/* ── UNIVERSAL NAV STYLE ── */
.site-header,
#masthead,
#site-header {
  background: #0A1520 !important;
  border-bottom: 1px solid rgba(200,148,46,.2) !important;
  position: sticky !important;
  top: 0 !important;
  z-index: 9999 !important;
}

/* Nav links */
.navigation-primary a,
#site-navigation a,
.main-navigation a {
  color: #A8B8CC !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 15px !important;
  font-weight: 500 !important;
}
.navigation-primary a:hover,
#site-navigation a:hover {
  color: #fff !important;
}

/* Logo */
.site-title a,
.custom-logo-link {
  color: #fff !important;
}

/* Digital Pioneer Gallery button (purple) */
li.menu-btn-gallery > a,
.menu-item.menu-btn-gallery > a {
  background: rgba(123,47,190,.15) !important;
  border: 1px solid rgba(123,47,190,.4) !important;
  border-radius: 6px !important;
  color: #9B6DFF !important;
  font-weight: 600 !important;
  font-size: 13px !important;
  padding: 5px 14px !important;
}
li.menu-btn-gallery > a:hover,
.menu-item.menu-btn-gallery > a:hover {
  background: rgba(123,47,190,.3) !important;
  color: #b89dff !important;
}

/* Book a Call button (gold outline) */
li.menu-btn-call > a,
.menu-item.menu-btn-call > a {
  color: #C8942E !important;
  border: 1px solid rgba(200,148,46,.35) !important;
  border-radius: 8px !important;
  padding: 8px 18px !important;
  font-weight: 600 !important;
  font-size: 14px !important;
}
li.menu-btn-call > a:hover,
.menu-item.menu-btn-call > a:hover {
  background: rgba(200,148,46,.1) !important;
  color: #E8B84B !important;
}

/* Start Free Lesson button (gold solid) */
li.menu-btn-lesson > a,
.menu-item.menu-btn-lesson > a {
  background: #C8942E !important;
  color: #0E1C2F !important;
  border-radius: 8px !important;
  padding: 9px 20px !important;
  font-weight: 700 !important;
  font-size: 14px !important;
}
li.menu-btn-lesson > a:hover,
.menu-item.menu-btn-lesson > a:hover {
  background: #E8B84B !important;
}
```

---

## STEP 3 — Hide Page Titles

Already handled by the BuddyBoss reset in each HTML file.

---

## RESULT

Every page on every site will show:

```
LearnMore Technologies  |  About  Train  Speaking  50+TechBridge  [Digital Pioneer Gallery]  [Book a Call]  [Start Free Lesson →]
```

- Same dark navy background
- Same gold CTAs
- Same purple Digital Pioneer badge
- Sticky on scroll
- Hamburger on mobile
