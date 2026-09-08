# SOP-11 — Build and Maintain the SOP System
## Capture command + SOP folder — never repeat a complex process

**Purpose:** Document any repeatable process so it never has to be figured out again. Prevents duplicated work, lost knowledge, and wasted time.
**Trigger:** Any time you finish a complex task you might need to do again.
**Owner:** Brian McKinney
**Time required:** 5-10 minutes per SOP
**Frequency:** Any time a new repeatable process is completed

---

## QUICK REFERENCE
1. Finish the task
2. Type `/capture` in Claude Code
3. Describe what you just did (rough is fine)
4. Claude writes and saves the SOP automatically
5. Next time — follow the SOP instead of figuring it out again

---

## STEP-BY-STEP

### STEP 1 — Finish the Task First
- Complete the task before capturing it
- Don't try to document while doing — finish first, then capture

### STEP 2 — Run `/capture`
- Open Claude Code
- Type `/capture` and press Enter
- Claude will ask one question: "What did you just do?"

### STEP 3 — Describe the Task (rough is fine)
- Say what you did in plain language — messy is OK
- Claude structures it, you don't have to
- Example: "I built a PowerPoint using Python and exported the slides as PNGs for HeyGen"

### STEP 4 — Claude Writes and Saves the SOP
- Claude automatically:
  - Reads the SOP index to get the next number
  - Writes the SOP in Craig Hewitt's format
  - Saves it to the SOPs folder
  - Updates SOP-INDEX.md

### STEP 5 — Confirm and Move On
- Claude confirms: "Saved as SOP-[number]"
- Next time you do this task — open the SOP and follow it

---

## WHERE EVERYTHING LIVES

| Item | Location |
|---|---|
| All SOP files | `05-OPS/05-BUSINESS-OPS/06-REFERENCE/SOPs/` |
| SOP index | `SOPs/SOP-INDEX.md` |
| `/capture` skill | `C:\Users\Jordyn\.claude\commands\capture.md` |

---

## DECISION POINTS

**If the process is only partially done:**
- Still run `/capture` — describe what's done and what's left
- Claude saves the done part as a SOP and drops the in-progress part into TODO.md

**If the SOP already exists and you improved the process:**
- Run `/capture` and say "this is an update to an existing SOP"
- Claude will update the existing file instead of creating a new one

**If you're not sure it's worth documenting:**
- If you spent more than 30 minutes figuring it out → document it
- If you'll do it again → document it
- If someone (or an agent) might do it for you → document it

---

## COMMON MISTAKES
- Waiting too long after finishing — details fade fast, capture immediately
- Describing the task too vaguely ("I did some stuff in Claude") — give enough detail for Claude to structure it
- Skipping `/capture` because "I'll remember" — you won't

## TOOLS & ACCESS NEEDED
- Claude Code (with `/capture` command installed)
- SOPs folder: `05-OPS/05-BUSINESS-OPS/06-REFERENCE/SOPs/`
