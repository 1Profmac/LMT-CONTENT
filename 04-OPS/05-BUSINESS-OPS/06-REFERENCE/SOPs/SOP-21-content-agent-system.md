# SOP-21 — Content Agent System (Craig Hewitt Method)
## One idea → LinkedIn + Newsletter + Twitter + Podcast, automatically

**Purpose:** Use Craig Hewitt's `claudecode-writer` repo to turn raw notes into multi-platform content without manually reformatting for each channel.
**Trigger:** You have a content idea, raw notes, or a lesson/topic to publish
**Owner:** Brian McKinney
**Time required:** 20–30 min per content cycle
**Frequency:** Weekly (or per content piece)

---

## QUICK REFERENCE
1. Drop raw idea/notes into `/rawnotes`
2. Run `/extract-themes` to find angles
3. Run `/research [topic]` to pull data and trends
4. Run `/write` to create full article in your voice
5. Review auto-generated LinkedIn, newsletter, Twitter, and podcast versions
6. Post or schedule each piece

---

## STEP-BY-STEP

### STEP 1 — Open the Repo in Claude Code
- Navigate to: `G:/My Drive/LMT-CONTENT/04-OPS/05-BUSINESS-OPS/craig-hewitt-repos/claudecode-writer/`
- Open Claude Code in that folder (or run `claude` from that directory in terminal)

### STEP 2 — Set Up Your Voice (one-time)
- Edit `context/writing-examples.md` — paste 3–5 examples of your best LinkedIn posts or articles
- Edit `context/research-sources.md` — add your trusted sources (Pew Research, AARP, MIT, etc.)
- This only needs to be done once; the system learns your voice from these files

### STEP 3 — Drop Your Idea
- Open the `/rawnotes` folder
- Create a new `.md` file — name doesn't matter
- Dump your idea, voice note transcript, or bullet points — rough is fine

### STEP 4 — Extract Themes
- Run: `/extract-themes`
- Claude reads your rawnotes and surfaces 3–5 content angles
- Pick the one that fits your audience best

### STEP 5 — Research
- Run: `/research [your chosen topic]`
- Claude checks your trusted sources first, then pulls trends and data
- Output goes into `/research` folder

### STEP 6 — Write the Article
- Run: `/write`
- Claude creates a full long-form article in your voice
- Saved to `/drafts` folder
- Review and edit — this is your master piece

### STEP 7 — Get All Platform Versions
- After `/write`, Claude auto-generates:
  - **LinkedIn post** — professional hook, engagement drivers
  - **Newsletter section** — subject line + personal tone
  - **Twitter/X thread** — shareable, punchy
  - **Podcast Q&A script** — conversational, sounds natural
- Review each version — they're optimized for each platform already

### STEP 8 — Publish or Schedule
- LinkedIn → post directly or paste into Buffer
- Newsletter → paste into MailerLite
- Twitter/X → post or schedule
- Podcast → use as episode outline or script

---

## ALTERNATIVE AI TOOLS (Craig Hewitt Method)
Craig also uses other AI tools alongside Claude Code for this workflow:
- **Cursor** — alternative to Claude Code for writing and editing (same idea, different UI)
- Use Cursor if you prefer a VS Code-style editor feel
- Both work with the same repo and slash commands
- Claude Code is recommended for Brian since it's already set up

---

## DECISION POINTS

**If you have a lesson that just launched:**
- Use `/rawnotes` to paste the lesson topic → run full cycle → gets you SOP-17 content automatically

**If you're short on time:**
- Skip `/extract-themes` — just drop notes and run `/research` + `/write` directly

**If the voice sounds off:**
- Add more examples to `context/writing-examples.md` — the system needs 5+ good samples

---

## COMMON MISTAKES
- Skipping the voice setup (context files) — output will sound generic without them
- Writing polished notes in `/rawnotes` — rough is fine, it's meant for brain dumps
- Editing each platform version from scratch — edit the master article first, then regenerate
- Forgetting to add your trusted sources to `context/research-sources.md`

## TOOLS & ACCESS NEEDED
- Claude Code (already installed)
- `G:/My Drive/LMT-CONTENT/04-OPS/05-BUSINESS-OPS/craig-hewitt-repos/claudecode-writer/`
- MailerLite (for newsletter publishing)
- Buffer free (for scheduling)
- Cursor (optional alternative to Claude Code)

---

## STATUS: EVALUATING (as of 2026-09-11)
- Repo is cloned and reviewed — structure confirmed
- Next step: populate `context/writing-examples.md` with Brian's voice samples and test one full cycle
