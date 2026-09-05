# TODO: Build AI Operations Agent — Chief of Staff System

**Created:** June 20, 2026
**Status:** Pending (complete after Houston trip)
**Priority:** HIGH — this is the backbone for the AI Ops Assistant role

---

## Goal

Build one agent system that handles: email triage, calendar management, CRM/contact tracking, grant deadline alerts, follow-ups, and weekly reports. Replace manual HubSpot work with an AI agent that reads/writes to HubSpot automatically.

---

## Craig Hewitt's Hermes Chief of Staff (Use as Blueprint)

**Repo:** `05-BUSINESS-OPS/craig-hewitt-repos/hermes-chief-of-staff/`
**GitHub:** https://github.com/TheCraigHewitt/hermes-chief-of-staff

### What it does (and we need):
| Skill | Function | Brian's Equivalent |
|-------|----------|-------------------|
| `executive-assistant` | Inbox triage, email drafting, calendar mgmt | `/email-triage` + `/calendar-manage` |
| `daily-task-manager` | Task file — add, complete, prioritize | `/daily` + `/deadline-tracker` |
| `daily-task-prep` | Nightly automation — prep tomorrow's tasks | Not built yet |
| `relationship-manager` | Follow-up tracking, outreach cadence | `/crm` |
| `chief-of-staff` | Orchestrator — morning briefings, EOD reviews | `/weekly-report` + `/monday` |

### Daily rhythm to replicate:
1. **2 AM** — Auto-prep tomorrow's task list
2. **8 AM** — Morning briefing delivered (no command needed)
3. **All day** — Inbox sweep every 15 minutes
4. **Twice daily** — Check for due follow-ups
5. **End of day** — Review what got done, capture what's next

### Key files to study:
- `templates/CHIEF_OF_STAFF_CONTEXT.example.md` — Config template (adapt for Brian)
- `docs/operating-model.md` — Full system architecture
- `docs/recommended-founder-setup.md` — Fastest path to working setup
- `docs/adaptation-guide.md` — How to customize
- `skills/executive-assistant/references/calendar-rules.md` — Calendar logic
- `skills/executive-assistant/references/email-templates.md` — Email templates
- `skills/relationship-manager/references/follow-up-cadence.md` — Follow-up rules

### What Craig's repo DOESN'T have (we need to add):
- HubSpot CRM integration
- Grant/contract deadline tracking
- Google Calendar MCP connection
- Gmail MCP connection
- Capability statement generation

---

## Other Craig Repos to Reference

| Repo | Use For |
|------|---------|
| `skills/cowork/inbox-triage/` | Email triage pattern (already adapted) |
| `skills/cowork/personal-crm/` | Contact management pattern (already adapted) |
| `skills/cowork/morning-briefing/` | Daily briefing pattern |
| `skills/sales/linkedin-outreach/` | LinkedIn outreach automation |
| `skills/sales/pipeline-review/` | Deal pipeline tracking |
| `skills/sales/lead-research/` | Prospect research |
| `polyboard/` | Agent orchestration dashboard |

---

## Step-by-Step Build Plan

### Phase 1: Connect HubSpot (Day 1)
- [ ] Create HubSpot Private App (Settings → Integrations → Private Apps)
- [ ] Enable scopes: contacts, deals, companies, engagements
- [ ] Copy access token
- [ ] Install HubSpot MCP server: `npm install @hubspot/mcp-server`
- [ ] Add to Claude Code settings.json
- [ ] Test: "list my HubSpot contacts"

### Phase 2: Adapt Chief of Staff Config (Day 1)
- [ ] Copy `CHIEF_OF_STAFF_CONTEXT.example.md` → customize for Brian
- [ ] Set: email accounts (brian@learnmo.com, hello@learnmoretechnologies.com)
- [ ] Set: calendar (Google Calendar via MCP)
- [ ] Set: authority levels (what agent can do without asking)
- [ ] Set: work hours (8am-6pm CT)
- [ ] Set: VIP contacts and escalation rules (from inbox-config.md)

### Phase 3: Wire Up Skills (Day 2)
- [ ] Update `/email-triage` to push flagged items to HubSpot
- [ ] Update `/crm` to read/write HubSpot contacts instead of local files
- [ ] Update `/calendar-manage` to create prep blocks automatically
- [ ] Update `/deadline-tracker` to send email warnings via Gmail MCP
- [ ] Build `/morning-briefing` skill (from Craig's pattern)
- [ ] Build `/eod-review` skill

### Phase 4: Automation Layer (Day 3)
- [ ] Set up cron jobs or Make.com scenarios for:
  - 7 AM: `/morning-briefing` auto-run
  - 9 AM, 1 PM, 5 PM: `/email-triage` auto-run
  - 10 AM, 4 PM: Follow-up check
  - 6 PM: EOD review
- [ ] Test full day cycle end-to-end

### Phase 5: Grant Pipeline in HubSpot (Day 3)
- [ ] Create custom deal pipeline in HubSpot: "Grants"
- [ ] Stages: Researching → Go/No-Go → Drafting → Review → Submitted → Awarded → Reporting
- [ ] Add Elevate, Nexus, NEA, SXSW as deals
- [ ] Connect `/deadline-tracker` to pull from HubSpot pipeline

---

## What This Replaces

| Current Process | New Process |
|----------------|-------------|
| Open HubSpot, manually update contacts | "Add contact" → agent writes to HubSpot |
| Check Gmail, mentally prioritize | Agent triages automatically 3x/day |
| Remember to follow up | Agent alerts when follow-ups are due |
| Check calendar for conflicts | Agent flags conflicts and blocks prep time |
| Manually track grant deadlines | Agent warns at 7 days and 48 hours |
| Run 6 slash commands every morning | One morning briefing, auto-delivered |
| Open 4 tabs to check status | One weekly report pulls from all systems |

---

## Resources

- HubSpot MCP setup: https://composio.dev/toolkits/hubspot/framework/claude-code
- Craig's Chief of Staff: https://github.com/TheCraigHewitt/hermes-chief-of-staff
- Craig's 47 skills: https://github.com/TheCraigHewitt/skills
- AI Hero agent framework: https://www.aihero.dev/5-agent-skills-i-use-every-day
- HubSpot Private Apps: HubSpot → Settings → Integrations → Private Apps
