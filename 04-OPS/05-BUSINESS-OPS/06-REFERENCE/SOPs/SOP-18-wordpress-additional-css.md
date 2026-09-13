# SOP-18 — WordPress Additional CSS Management
## One master CSS file — paste to override BuddyBoss and LearnDash site-wide

**Purpose:** BuddyBoss and LearnDash generate CSS that conflicts with brand styling. All site-wide overrides live in one master file. Never fight individual elements — update the master file and republish.
**Trigger:** Any site-wide styling change needed (nav, lesson pages, sidebar, fonts)
**Owner:** Brian McKinney
**Time required:** 5 minutes
**Frequency:** Any time site CSS needs updating

---

## QUICK REFERENCE
1. Open `Desktop/50tb-additional-css.txt` in Notepad
2. Make changes to the relevant section
3. Select all → copy
4. WordPress → Appearance → Customize → Additional CSS → select all → paste → Publish
5. Hard refresh site (Ctrl+Shift+R)

---

## STEP-BY-STEP

### STEP 1 — Find the master CSS file
- File lives at: `C:\Users\Jordyn\Desktop\50tb-additional-css.txt`
- This is the ONLY place site CSS lives — never scatter fixes across individual pages

### STEP 2 — Make the change
- Open in Notepad
- Find the relevant section (each section is labeled with a comment)
- Edit only what needs changing

### STEP 3 — Paste into WordPress
- WordPress → **Appearance → Customize → Additional CSS**
- Select ALL existing code (Ctrl+A) → delete
- Paste the full contents of `50tb-additional-css.txt`
- Click **Publish**

### STEP 4 — Verify
- Hard refresh the site: **Ctrl+Shift+R**
- Check the affected element looks correct
- If broken: re-open the file, fix, repeat

---

## WHAT'S IN THE MASTER CSS FILE (sections)

| Section | What it does |
|---|---|
| FONTS | Imports DM Sans + Playfair Display from Google Fonts |
| NAV | Equal pill shape all items, gold on Start-Free-Lessons only |
| LEARNDASH LESSON PAGES | Removes BuddyBoss white background, resets padding |
| HIDE DEFAULT CHROME | Hides LearnDash headers, breadcrumbs, quiz items |
| SIDEBAR | Dark navy background, gold accent on active lesson |

---

## NAV CONFIGURATION (as of 2026-09-08)

BuddyBoss nav button classes are set in **Appearance → Menus → click item → CSS Classes field**

| Nav Item | CSS Class | Styling |
|---|---|---|
| Digital Pioneer Gallery | *(none — removed)* | Plain link |
| Start-Free-Lessons | `menu-btn-lesson` | Gold pill via CSS |

**To change a nav button:** Appearance → Menus → click item → edit CSS Classes field → Save Menu

---

## DECISION POINTS

**If a style change only affects one lesson page:**
- Put it in the lesson's LearnDash HTML code block — NOT in Additional CSS

**If BuddyBoss overrides your CSS:**
- Use two IDs in the selector: `#site-navigation #primary-navbar` beats any single-ID BuddyBoss rule
- Or target by the exact CSS class from Appearance → Menus

**If the nav button gold isn't applying:**
- Check Appearance → Menus → confirm `menu-btn-lesson` is still in the CSS Classes field
- Confirm the Additional CSS has `#primary-navbar li.menu-btn-lesson > a { background: #C8942E !important; }`

---

## COMMON MISTAKES
- Editing CSS directly in the Customizer without updating `50tb-additional-css.txt` — gets lost next time
- Pasting nav CSS in multiple places — always ONE block in the master file
- Forgetting to Publish in the Customizer (changes don't save until you hit Publish)
- Using Ctrl+F5 instead of Ctrl+Shift+R to clear cache

## TOOLS & ACCESS NEEDED
- `C:\Users\Jordyn\Desktop\50tb-additional-css.txt` — master CSS file
- WordPress → Appearance → Customize → Additional CSS
- Caching plugin: clear cache after any CSS change if changes don't show
