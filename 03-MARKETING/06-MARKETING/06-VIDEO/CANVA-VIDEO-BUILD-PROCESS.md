# Canva Video Build Process
## Welcome Video — PPT + B-Roll + HeyGen Talking Head
### Last Updated: 2026-08-30

---

## ASSETS YOU NEED BEFORE YOU START

- [ ] ElevenLabs voiceover MP3 (3:00–3:30)
- [ ] PPT slides exported as PDF (7 slides)
- [ ] B-roll images or video clips (from Gemini or stock)
- [ ] HeyGen talking head (generated inside Canva — see Step 2)

---

## STEP 1 — ELEVENLABS VOICEOVER

1. Open ElevenLabs → Text to Speech
2. Paste script from `ELEVENLABS-WELCOME-SCRIPT.txt` (Desktop)
3. Select voice: **Brian McKinney**
4. Select model: **Eleven Multilingual v2**
5. Speed: **1.0** (do not slow down — add more script content if audio is too short)
6. Click **Generate speech**
7. Download the MP3 — save to Desktop as `Welcome-Voice-Over-FINAL.mp3`

---

## STEP 2 — HEYGEN TALKING HEAD (inside Canva)

1. Open your Canva video project
2. Click **Apps** on the left sidebar
3. Search for **HeyGen AI Avatars** → click it
4. Click **Use in existing design**
5. Select your avatar (Brian McKinney)
6. Paste the welcome script
7. Generate — HeyGen renders and drops the video directly into your Canva project
8. Resize and position in the corner (PIP — picture in picture) on slides 1 and 7

---

## STEP 3 — BUILD THE VIDEO IN CANVA

### 3A — Import Your Slides
1. Click **Uploads** on the left sidebar
2. Upload `welcome-video-slides.pdf` (Desktop)
3. When prompted, click **Apply all pages** (imports all 7 slides)

### 3B — Add Audio
1. Click **Uploads** → upload `Welcome-Voice-Over-FINAL.mp3`
2. Drag the MP3 onto the timeline — it spans all slides automatically

### 3C — Set Slide Durations
Click each slide's navy bar at the bottom of the timeline and drag the right edge to set duration.

| Slide | Content | Duration |
|-------|---------|----------|
| 1 | Welcome / Cover | 25s |
| 2 | Fridge Line | 20s |
| 3 | Stats | 35s |
| 4 | Map (3 lessons) | 45s |
| 5 | Safety | 20s |
| 6 | Homework | 25s |
| 7 | Closing | 35s |

**Total: 3:25**

### 3D — Add B-Roll
1. Click **Uploads** → upload your b-roll images or video clips
2. Drag each clip onto the appropriate slide
3. Resize to fill the background or position as a side element

### 3E — Add HeyGen Talking Head
1. Your HeyGen clip is already in the project from Step 2
2. Drag it onto slides 1 and 7 (open and close)
3. Resize to bottom corner — PIP (picture in picture) style

---

## STEP 4 — PREVIEW AND EXPORT

1. Click **Preview** (top right) — watch the full video
2. Check audio sync with slides
3. When satisfied: click **Share** → **Download** → **MP4 Video**
4. Save to Desktop as `welcome-video-FINAL.mp4`

---

## STEP 5 — UPLOAD TO YOUTUBE

1. Go to YouTube Studio → Upload
2. Set visibility: **Unlisted**
3. Copy the video ID from the URL
4. Paste video ID into LearnDash lesson page
5. Mark TODO.md item complete

---

## NOTES

- Canva does NOT auto-sync slide durations to voiceover — set each manually
- Beat Sync only works with music, not voiceover
- HeyGen Canva app drops the talking head directly into your project — no download needed
- Always preview before downloading to catch sync issues
