# Grant Tracker — Learn More Technologies / 50+TechBridge

## How to Use This Tracker
1. Add every grant opportunity as a new row
2. Update status weekly (Monday)
3. Flag deadlines: **7-DAY WARNING** and **48-HOUR WARNING**
4. Submit draft to Brian 72 hours before deadline
5. Move completed/declined grants to the Archive section

---

## Active Pipeline

| # | Grant Name | Funder | Amount | Deadline | Status | 7-Day Flag | 48-Hr Flag | Notes |
|---|-----------|--------|--------|----------|--------|-----------|-----------|-------|
| 1 | Nexus Creative Grant | City of Austin | $5,000 | Final report pending | In Progress | - | - | Final report due 30 days after last activity |
| 2 | | | | | Researching | | | |
| 3 | | | | | Researching | | | |

## Status Key
- **Researching** — evaluating fit, gathering info
- **Go** — decided to apply (passed Go/No-Go filter)
- **Drafting** — application in progress
- **Review** — draft sent to Brian for approval
- **Submitted** — application filed
- **Awarded** — funding received
- **Reporting** — grant active, reports due
- **Declined** — did not apply (log reason)
- **Rejected** — applied, not selected

---

## Go/No-Go Checklist (Before Starting Any Application)

- [ ] Does the grant fund digital literacy, workforce development, or community development?
- [ ] Does it serve adults 50+ or underserved populations?
- [ ] Is the amount worth the effort? (minimum $2,500)
- [ ] Can we meet the deadline with 72 hours review time?
- [ ] Do we meet all eligibility requirements?
- [ ] Is there a reporting burden we can handle?

If 4+ boxes checked = **GO**. Otherwise = **DECLINE** and log the reason.

---

## Deadline Alert Schedule

| When | Action |
|------|--------|
| **14 days out** | Confirm Go/No-Go. Begin drafting if Go |
| **7 days out** | **7-DAY WARNING** — draft should be 80% complete |
| **72 hours out** | Submit draft to Brian for review |
| **48 hours out** | **48-HOUR WARNING** — final edits only |
| **24 hours out** | Final submission. No new changes |
| **Day of** | Confirm submission received. Save confirmation |

---

## Monthly Research Targets

Search these sources weekly for new opportunities:

| Source | URL | Focus |
|--------|-----|-------|
| Grants.gov | grants.gov | Federal grants — WIOA, digital equity, aging |
| Texas Workforce Commission | twc.texas.gov | State workforce development |
| City of Austin | austintexas.gov/grants | Local community grants |
| Foundation Directory | candid.org | Private foundations |
| GrantWatch | grantwatch.com | Aggregated grant listings |
| NDIA | digitalinclusion.org | Digital inclusion specific |
| AARP Foundation | aarp.org/foundation | Aging and technology |

---

## Archive (Completed / Declined)

| Grant Name | Funder | Amount | Result | Date | Notes |
|-----------|--------|--------|--------|------|-------|
| | | | | | |

---

## Google Sheet Version

For real-time tracking with auto-alerts, create a Google Sheet with these columns:
1. Grant Name
2. Funder
3. Amount
4. Deadline (date format)
5. Status (dropdown)
6. Days Until Deadline (formula: =deadline-TODAY())
7. 7-Day Flag (conditional formatting: yellow when <=7)
8. 48-Hr Flag (conditional formatting: red when <=2)
9. Assigned To
10. Brian Review Date
11. Notes

Set up conditional formatting:
- **Yellow row** when Days Until Deadline <= 7
- **Red row** when Days Until Deadline <= 2
- **Green row** when Status = "Awarded"
- **Gray row** when Status = "Declined" or "Rejected"
