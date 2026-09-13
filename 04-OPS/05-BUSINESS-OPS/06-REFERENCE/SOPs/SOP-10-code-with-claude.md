# SOP-10 — Build or Fix Code with Claude
## Web pages, assets, scripts — start to finish

**Purpose:** Build or fix web pages and digital assets using Claude without starting from scratch or repeating yourself.
**Trigger:** Any time you need to build a new web page, fix an existing one, or create a code-based asset (script, tool, form, etc.)
**Owner:** Brian McKinney
**Time required:** 30-60 minutes
**Frequency:** As needed

---

## QUICK REFERENCE
1. Define exactly what you need BEFORE opening Claude
2. Give Claude the full context — URL, existing code, what's broken or missing
3. Copy the code → test it in a browser or run it locally
4. Fix errors by pasting them back to Claude — never guess
5. Save the working file to the correct folder

---

## STEP-BY-STEP

### STEP 1 — Define the Task Before Opening Claude
Write down (even rough notes):
- What are you building? (new page, fix existing, new script, asset)
- What should it do when it's done?
- What tool or platform will it run on? (WordPress, LearnDash, plain HTML, Python, etc.)
- Do you have existing code to share, or starting from scratch?

### STEP 2 — Open Claude and Give Full Context
Tell Claude all of this at once — don't drip-feed:
- "I need to build / fix / update [what]"
- "It lives on [platform/site]"
- "Here is the existing code:" [paste it]
- "Here is what's broken or what I want added:" [describe clearly]
- "Output: give me the full code ready to copy/paste"

### STEP 3 — Copy the Code Claude Gives You
- Copy the entire code block
- Do NOT edit it manually before testing — test it as-is first

### STEP 4 — Test It
**Web page (WordPress):**
- Paste into the correct WordPress editor (page, CSS, or Code block)
- Preview in a private/incognito browser
- Check on mobile too

**Python script:**
- Save as a `.py` file in the correct project folder
- Run it: `python filename.py`
- Watch the terminal for errors

**HTML/standalone file:**
- Save as `.html`
- Open in Chrome — does it look right?

**You'll know it worked when:** the page or script does exactly what you described in Step 1.

### STEP 5 — If Something Is Broken
- Copy the exact error message (all of it)
- Go back to Claude: "This error happened: [paste error]. Fix it."
- Do NOT try to guess the fix yourself — paste the error, let Claude solve it
- Repeat until it works

### STEP 6 — Save the Working File
- Save to the correct project folder immediately
- Naming convention: `LMT-[project]-[description]-[date].[ext]`
  Example: `LMT-Lesson3-PPT-Builder-20260907.py`
- If it's a WordPress CSS fix → note it in `debug_nav_css.md` or the relevant SOP

---

## DECISION POINTS

**Claude's code doesn't work and you've tried twice:**
- Stop trying the same approach
- Tell Claude: "That approach isn't working. Give me a completely different way to do this."

**You need to change something small in the code:**
- Don't edit the code manually — tell Claude what to change and get a clean updated version
- Manual edits cause hard-to-trace bugs

**The fix breaks something else on the page:**
- Take a screenshot of what broke
- Tell Claude: "The fix worked but now [X] is broken. Here's what I see: [describe/screenshot]"

**Web page CSS change isn't showing:**
- Site-wide CSS goes in **Appearance → Customize → Additional CSS** — NOT in individual page code blocks
- See: `feedback_wp_css.md` for the CSS rule

---

## COMMON MISTAKES
- Starting in Claude before knowing what you actually need (wastes 30+ minutes)
- Editing Claude's code manually before testing (creates unfixable mystery bugs)
- Not saving the working version before making changes (lose working code)
- Pasting code in the wrong WordPress location (page block vs. Additional CSS)

## TOOLS & ACCESS NEEDED
- Claude (claude.ai or Claude Code)
- WordPress admin (for web page fixes)
- Python 3 installed (for scripts)
- Chrome / incognito browser (for testing)
- Correct project folder in `LMT-CONTENT/`
