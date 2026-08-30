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

## STEP 2 — HEYGEN TALKING HEAD (use HeyGen directly — NOT the Canva app)

**WARNING:** The HeyGen Canva app only generates a 2.5-second clip — not the full video. Always use HeyGen directly at app.heygen.com for full-length talking head generation.

1. Go to **app.heygen.com**
2. Click **Create Video** → **Scene by scene** → **Build it yourself**
3. In the Script panel (left side): click the audio icon → upload your ElevenLabs MP3 (`Welcome-Voice-Over-FINAL.mp3`)
4. On the right panel, select **Avatar: Brian McKinney** (Bright Horizon look)
5. Set **Motion Engine: Avatar V** (moves like you, adapts to script)
6. Under **Avatar Background** → click **Remove** (transparent background)
7. Under **Layout** → select **Circle** for circular PIP style
8. Click **Generate** (top right)
9. When done, download the MP4
10. Upload the MP4 to Canva via **Uploads**

### To add talking head to Canva slides:
- Drag the HeyGen MP4 onto slide 1 → position in bottom corner
- Resize to PIP size (small, corner placement)
- Copy (Ctrl+C) → paste (Ctrl+V) onto each slide you want Brian to appear on
- Brian only needs to appear on slide 1 (open) and slide 7 (close) — slides 2–6 are content only

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
- **Do NOT use HeyGen Canva app for talking head** — it only generates 2.5 seconds, not the full video
- Always use HeyGen directly at app.heygen.com for full-length talking head
- To set slide duration: click the dark navy bar at the bottom of the timeline → drag the RIGHT EDGE
- To remove background on a video clip in Canva: click the clip → click BG Remover in toolbar
- HeyGen Avatar Background → Remove = transparent background (no download workaround needed)
- Always preview before downloading to catch sync issues
