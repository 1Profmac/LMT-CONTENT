# BETA #2 — Website Consolidation & Automation

**Created:** May 3, 2026
**Status:** Parked — come back when ready

---

## 1. WEBSITE CONSOLIDATION

### Current Nav (5 items — too many)
Train · Workforce · Speak · Work With Brian · Start Free Today

### New Nav (2 items)
**Start Free Today** · **Work With Brian**

### Pages to Retire
- /train/ → redirect to /work-with-brian/
- /workforce/ → redirect to /work-with-brian/
- /speak/ → redirect to /work-with-brian/ (or /lmt-speak-page/)

### Steps
1. Review Train page HTML — save to BETA2 folder
2. Review Workforce page HTML — save to BETA2 folder
3. Review Speak page HTML — save to BETA2 folder
4. Pull any unique content worth keeping into Work With Brian page
5. Set up 301 redirects (Yoast will do this automatically when slugs change)
6. Update nav menu: Appearance → Menus → remove Train, Workforce, Speak
7. Test all links

---

## 2. MAKE.COM AUTOMATION

### Scenario 1: Application Form → HubSpot + Mailchimp
- Trigger: Google Sheet "Work With Brian Applications" → new row
- Route by Q5 ("What do you need?"):
  - Partner training OR Speaker → HubSpot contact + deal + email Brian "HOT LEAD"
  - Private coaching → HubSpot contact + email Brian "HOT LEAD"
  - Not sure yet → Mailchimp only (tag: lead-nurture)
- All applicants → Mailchimp tag: applied-workwithbrian

### Scenario 2: Course Registration → Google Sheet + Notification
- Trigger: LearnDash enrollment (or new Google Form for course signups)
- Action: Add to Google Sheet "Course Registrations"
- Action: Email Brian with who signed up, what course, when

---

## 3. COURSE SIGNUP GOOGLE SHEET

### Same system as Work With Brian form:
- Google Form for course registration
- Responses → Google Sheet "Course Registrations"
- Make.com watches sheet → adds to Mailchimp + notifies Brian

### Questions:
1. Your Name
2. Your Email
3. Which course are you interested in?
4. How did you hear about us?

---

## 4. ONE VOICE NOTIFICATION SYSTEM

### Problem
Mailchimp notifications aren't informative enough. Brian needs ONE source of truth for all leads/signups.

### Solution: Unified email alert from Make.com

Every notification Brian gets follows the same format:

```
Subject: [TYPE] New [lead/signup] from [Name]

WHO: [Name] — [Email]
WHAT: [Partner training / Speaking / Coaching / Course signup]
WHERE: [Organization name] — [City]
WHEN: [Timestamp]
HOW BIG: [Org size if applicable]
TIMELINE: [Ready now / 30 days / 90 days / Exploring]

ACTION REQUIRED:
- Hot lead → Send Calendly link within 24 hours
- Warm lead → Reply within 48 hours
- Course signup → Auto-enrolled, no action needed
```

### Types:
- `[HOT LEAD]` — Partner training or coaching, ready now/30 days
- `[WARM LEAD]` — Any need, 90 days or exploring
- `[COURSE SIGNUP]` — Free course enrollment
- `[NEWSLETTER]` — Agentic50 subscriber

All notifications come from Make.com → Brian's email. One format. One voice.

---

## 5. LINKEDIN BANNER UPDATE

Swap: use "13 Locations" framing
Keep: Targeted 3x Completion Rate · MBE Certified

---

## FILE LOCATIONS

- This file: `00-STAGING/BETA2/BETA2-TODO.md`
- Work With Brian page (current): `04-ASSETS/templates/work-with-brian-page.html`
- Git: `lmt-claude-brain/pages/LMT-WorkWithBrian-Page.html`
- Train page HTML: save to `00-STAGING/BETA2/train-page-backup.html`
- Workforce page HTML: save to `00-STAGING/BETA2/workforce-page-backup.html`
- Speak page HTML: save to `00-STAGING/BETA2/speak-page-backup.html`
