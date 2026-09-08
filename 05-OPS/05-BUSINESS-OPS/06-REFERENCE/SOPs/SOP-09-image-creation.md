# SOP-09 — AI Image Creation
## OpenArt.ai → Store → HeyGen or Canva

**Purpose:** Create AI images for lessons, videos, and assets without rewriting prompts from scratch each time.
**Trigger:** Any time a new image is needed — lesson slide, thumbnail, background, avatar scene, or marketing asset.
**Owner:** Brian McKinney
**Time required:** 10-20 minutes
**Frequency:** Multiple times per week

---

## QUICK REFERENCE
1. Write image prompt in Claude first — be specific about style, subject, mood
2. Paste prompt into OpenArt.ai → generate
3. Review → regenerate if needed (max 3 tries before rewriting the prompt)
4. Download → rename → store in correct folder immediately
5. Load into HeyGen (background/scene) OR Canva (layout/design)

---

## STEP-BY-STEP

### STEP 1 — Write the Prompt in Claude
- Open Claude → describe the image you need
- Tell Claude: subject, style, mood, colors, what NOT to include
- Ask Claude to write a clean OpenArt.ai prompt
- Copy the prompt

**Good prompt elements:**
- Subject: "50+ adult woman at a laptop, confident expression"
- Style: "photorealistic" or "illustration" or "flat design"
- Mood: "warm, professional, empowering"
- Brand colors: "navy and gold color palette"
- Avoid: "no text overlay, no clutter, no young people"

### STEP 2 — Generate in OpenArt.ai
- Go to openart.ai → log in
- Paste Claude's prompt into the prompt box
- Select model (use default unless a specific model is known to work better)
- Click **Generate**

### STEP 3 — Review the Result
- Does it match the subject?
- Does it look professional? (no extra fingers, distorted faces, garbled text)
- Does it fit the brand feel (navy/gold/warm/professional)?
- If NO → click **Regenerate** (same prompt, new result) — try up to 3 times
- If still not right → go back to Claude and refine the prompt

### STEP 4 — Download and Rename
- Click the image → **Download**
- Rename immediately before saving:
  `LMT-[topic]-[use]-[date].png`
  Example: `LMT-Lesson3-ScamAlert-20260907.png`

### STEP 5 — Store in Correct Folder
- **Lesson image** → `01-LESSONS/[LessonFolder]/IMAGES/`
- **General asset** → `06-ASSETS/IMAGES/`
- **Thumbnail** → `06-ASSETS/THUMBNAILS/`
- **HeyGen background** → `06-ASSETS/HEYGEN/BACKGROUNDS/`
- If the folder doesn't exist → save to `06-ASSETS/IMAGES/` and note it

### STEP 6 — Load into HeyGen or Canva

**HeyGen (scene/background — no talking head):**
- Open app.heygen.com → New video
- Select background → Upload → choose your image
- Use as scene background behind text or B-roll

**Canva (layout/marketing asset):**
- Open Canva → your design
- Uploads tab → Upload Media → select your image
- Drop into layout → size and position

---

## DECISION POINTS

**Image looks wrong after 3 regenerations:**
- Go back to Claude — describe what's wrong ("the face looks distorted," "not professional enough")
- Ask Claude to rewrite the prompt with those fixes
- Paste the new prompt and try again

**Need a talking head video (not just a scene image):**
- This SOP covers non-talking-head images only
- For HeyGen avatar videos → follow **SOP-01 (Video Build)**

**Image needs higher resolution:**
- OpenArt.ai has an upscale option after generating — use it before downloading
- Or use Upscayl (free desktop app) after downloading

---

## COMMON MISTAKES
- Generating without a Claude prompt first (vague prompts = bad images, wasted time)
- Not renaming the file before saving (impossible to find later)
- Saving to Downloads instead of the correct asset folder
- Skipping upscale for large-display images (thumbnails, lesson slides)

## TOOLS & ACCESS NEEDED
- Claude (prompt writing)
- openart.ai (image generation)
- Canva Pro (layout)
- app.heygen.com (video scenes)
- Upscayl — optional, free desktop upscaler
