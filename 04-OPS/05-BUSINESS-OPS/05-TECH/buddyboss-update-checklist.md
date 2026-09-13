# BuddyBoss 3.0 Update Checklist
## Date: May 15, 2026
## Status: PENDING

---

## PRE-UPDATE (Do Before Touching Anything)

### Backup
- [ ] Full site backup via Bluehost
- [ ] Note current BuddyBoss version: ___________
- [ ] Note current BuddyBoss Theme version: ___________

### Record "Before" State
- [ ] View Source on /what-is-agetech-complete-guide/ → Ctrl+F "AgeTech is the technology sector" → RESULT: ___
- [ ] View Source on /850-billion-cost-ageism-workforce/ → Ctrl+F "Age discrimination costs" → RESULT: ___
- [ ] Screenshot Search Console URL Inspection for one article
- [ ] Test Mailchimp signup form → does it work? ___
- [ ] Test course page → does LearnDash render? ___
- [ ] Test login page → does it load? ___
- [ ] Run Watchdog manually → does email arrive with content? ___

---

## UPDATE

- [ ] Update BuddyBoss Platform plugin
- [ ] Update BuddyBoss Theme (if update available)
- [ ] DO NOT update LearnDash at the same time — one plugin at a time

---

## POST-UPDATE (Test Immediately)

### Critical Tests (do within 5 minutes)
- [ ] Homepage loads? ___
- [ ] View Source on /what-is-agetech-complete-guide/ → Ctrl+F "AgeTech is the technology sector" → RESULT: ___
- [ ] View Source on /850-billion-cost-ageism-workforce/ → Ctrl+F "Age discrimination costs" → RESULT: ___
- [ ] Blog page loads with articles? ___
- [ ] Mailchimp signup form works? ___
- [ ] Course page renders? ___
- [ ] Login page works? ___
- [ ] BuddyBoss community features work (profiles, groups)? ___

### If Article Text NOW Appears in View Source:
- [ ] CELEBRATE — Google indexing problem is FIXED
- [ ] Go to Search Console → URL Inspection → test one article
- [ ] Request indexing for all 38 articles (one at a time)
- [ ] Reply to BuddyBoss support: "3.0 update fixed the issue"
- [ ] Monitor Search Console for indexing over next 7 days

### If Article Text STILL Missing from View Source:
- [ ] DO NOT PANIC
- [ ] Screenshot the View Source result
- [ ] Reply to BuddyBoss support with screenshot: "Updated to 3.0, issue persists"
- [ ] Check if anything else broke
- [ ] If other things broke → RESTORE BACKUP immediately
- [ ] If only the rendering issue persists → keep 3.0, wait for support response

### If Site Is Broken After Update:
- [ ] RESTORE BACKUP immediately via Bluehost
- [ ] Reply to BuddyBoss support: "3.0 update broke the site, restored to previous version"
- [ ] Do NOT attempt the update again until support responds

---

## WATCHDOG STATUS
Current issue: Watchdog PHP script sending blank emails
Fix needed: Upload v3.1 (wp_mail version) to Bluehost
File location: Desktop/LMT-CONTENT/05-BUSINESS-OPS/lmt-watchdog.php
