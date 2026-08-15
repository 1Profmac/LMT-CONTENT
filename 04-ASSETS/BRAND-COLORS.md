# LMT Brand Colors — Official Hex Reference

> Source of truth: Appearance → Customize → Additional CSS on 50plustechbridge.com
> Do NOT use approximations — always pull from this file.
> Last verified: July 21, 2026

---

## Core Palette

| Name        | Hex       | Usage                                   |
|-------------|-----------|-----------------------------------------|
| Dark Navy   | `#0d1b2a` | Background, footer                      |
| Gold        | `#d4a843` | LMT button, links, accents              |
| Gold Dark   | `#b8922e` | Gold hover state                        |
| Purple      | `#7c3aed` | Digital Pioneer Gallery button          |
| Purple Dark | `#6d28d9` | Purple hover state                      |
| Brand Green | `#27ae60` | Start Free Lesson button                |
| Green Dark  | `#1e8449` | Green hover state                       |
| Light Grey  | `#cccccc` | Footer text                             |
| White       | `#ffffff`  | Headings on dark backgrounds            |

---

## Navigation Buttons

| Button                  | Hex       | Text       | Method                          |
|-------------------------|-----------|------------|---------------------------------|
| Learn More Technologies | `#d4a843` | `#0d1b2a`  | CSS targets `href*="learnmoretechnologies"` |
| Digital Pioneer Gallery | `#7c3aed` | `#ffffff`  | CSS targets `a.nav-cta` class   |
| Start Free Lessons      | `#27ae60` | `#ffffff`  | CSS targets `href*="start-free"` etc. |

---

## Fonts

| Role      | Family                   | Weight  |
|-----------|--------------------------|---------|
| Headlines | Playfair Display (serif) | 700–900 |
| Body / UI | DM Sans (sans-serif)     | 400–700 |

---

## Notes
- CSS file location: `Appearance → Customize → Additional CSS`
- Nav buttons use URL-based attribute selectors — no CSS class assignment needed in Menus editor
- If Start Free Lesson green button doesn't appear: inspect the href → add it to `nav a[href*="..."]` selector

---

_Last updated: 2026-07-21_
