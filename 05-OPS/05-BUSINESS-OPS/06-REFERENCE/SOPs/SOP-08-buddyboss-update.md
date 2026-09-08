# SOP-08 — BuddyBoss Plugin Update
## Backup → Update → Test → Recover if needed

**Purpose:** Update BuddyBoss safely without breaking the site or Google indexing.
**Trigger:** BuddyBoss plugin or theme update is available in WordPress dashboard.
**Owner:** Brian McKinney
**Time required:** 30-45 minutes
**Frequency:** When updates are available (do not auto-update)

---

## QUICK REFERENCE
1. Full backup via Bluehost FIRST
2. Record "before" state (View Source test on key article)
3. Update BuddyBoss Platform only (NOT LearnDash at the same time)
4. Test within 5 minutes of update
5. If broken → restore backup immediately

---

## PREREQUISITES
- [ ] Bluehost backup tool access
- [ ] WordPress admin access
- [ ] Note current BuddyBoss version before starting

---

## STEP-BY-STEP

### STEP 1 — PRE-UPDATE (do not skip)

**Backup:**
- [ ] Log into Bluehost → run **Full Site Backup**
- [ ] Wait for backup to complete before touching anything
- [ ] Record current BuddyBoss version: ___________

**Record "Before" state:**
- [ ] View Source on `/what-is-agetech-complete-guide/` → Ctrl+F "AgeTech is the technology sector" → RESULT: ___
- [ ] View Source on `/850-billion-cost-ageism-workforce/` → Ctrl+F "Age discrimination costs" → RESULT: ___
- [ ] Test MailerLite signup form — does it work? ___
- [ ] Test course page — does LearnDash render? ___
- [ ] Test login page — does it load? ___

### STEP 2 — UPDATE
- [ ] WordPress → Plugins → Update **BuddyBoss Platform**
- [ ] Update **BuddyBoss Theme** (if update available)
- [ ] **DO NOT update LearnDash at the same time — one plugin at a time**

### STEP 3 — POST-UPDATE (test within 5 minutes)
- [ ] Homepage loads?
- [ ] View Source → `/what-is-agetech-complete-guide/` → Ctrl+F → content in HTML?
- [ ] View Source → `/850-billion-cost-ageism-workforce/` → Ctrl+F → content in HTML?
- [ ] Blog page loads with articles?
- [ ] MailerLite signup form works?
- [ ] Course page renders?
- [ ] Login page works?

---

## DECISION POINTS

**If article text NOW appears in View Source (was missing before):**
- CELEBRATE — Google indexing issue is fixed
- Search Console → URL Inspection → test one article
- Request indexing for all articles (one at a time)
- Reply to BuddyBoss support: "3.0 update fixed the issue"
- Monitor Search Console for indexing over next 7 days

**If article text STILL missing from View Source:**
- Do NOT panic
- Screenshot the View Source result
- Reply to BuddyBoss support with screenshot
- Check if anything else broke
- If other things broke → RESTORE BACKUP immediately
- If only rendering issue persists → keep update, wait for support response

**If site is broken after update:**
- RESTORE BACKUP immediately via Bluehost
- Reply to BuddyBoss support: "Update broke the site, restored to previous version"
- Do NOT attempt the update again until support responds

---

## COMMON MISTAKES
- Updating BuddyBoss AND LearnDash at the same time (impossible to isolate what broke)
- Skipping the backup (no recovery option if something breaks)
- Not running the View Source test before updating (can't compare before/after)

## TOOLS & ACCESS NEEDED
- Bluehost control panel (backup tool)
- WordPress admin
- BuddyBoss support ticket (if something breaks)
