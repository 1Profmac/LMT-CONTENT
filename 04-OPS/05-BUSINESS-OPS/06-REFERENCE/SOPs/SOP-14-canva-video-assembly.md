# SOP-14 — Canva Video Assembly
## Duplicate previous lesson → swap slides → add audio → export MP4

**Purpose:** Assemble the final lesson video in Canva using slide PNGs, ElevenLabs voiceover, and HeyGen talking head — without starting from scratch.
**Trigger:** Slide PNGs, voiceover MP3, and HeyGen MP4 are all ready.
**Owner:** Brian McKinney
**Time required:** 45-60 minutes
**Frequency:** Every new lesson video

---

## QUICK REFERENCE
1. Open previous lesson in Canva → File → Make a copy → rename it
2. Upload new PNGs, MP3, HeyGen MP4
3. Swap slide images (delete old → drag in new)
4. Replace voiceover on timeline
5. Set slide durations → add HeyGen PIP → preview → export MP4

---

## PREREQUISITES
- [ ] Slide PNGs ready in `Lesson[X]/slides-png/` (named slide_01 through slide_15)
- [ ] Voiceover MP3 ready (from ElevenLabs — see SOP-01)
- [ ] HeyGen MP4 ready (from app.heygen.com — see SOP-13)
- [ ] Canva Pro logged in

---

## STEP-BY-STEP

### STEP 1 — Duplicate the Previous Lesson
1. Go to canva.com → log in
2. Open the previous lesson design (e.g., "Lesson-02-Talk-to-AI")
   - Find it on the home screen under **Recent designs**, OR
   - Left sidebar → **Projects** → search "Lesson-02"
3. Once inside: click **File** (top left) → **Make a copy**
4. A copy opens in a new tab
5. Click the filename in the top center bar → clear it → type: `Lesson-03-Dont-Get-Scammed`
6. Press **Enter**

### STEP 2 — Upload New Assets
1. Left sidebar → **Uploads** → **Upload files**
2. Upload all new slide PNGs from `slides-png/`
3. Upload the new voiceover MP3
4. Upload the HeyGen MP4 (Dr. Maya talking head)
5. Wait for all uploads to complete before touching the canvas

### STEP 3 — Swap the Slide Images
Work left to right through each slide page — do not skip around:
1. Click the existing slide image on the canvas → **Delete**
2. From Uploads, drag the matching new PNG onto the page
3. Resize to fill the full canvas (drag corners)
4. Right-click → **Set as background** if it sits behind other elements
5. Repeat for all 15 slides

### STEP 4 — Replace the Voiceover
1. Open the timeline (bottom of Canva screen)
2. Click the existing MP3 audio bar → **Delete**
3. From Uploads, drag the new MP3 onto the timeline
4. It auto-spans all slides — this is correct

### STEP 5 — Set Slide Durations
1. Click each slide's bar in the timeline
2. Drag the **right edge** to adjust duration
3. Timing guide:
   - **Content slides:** 20-35 seconds
   - **Opening slide:** 8-10 seconds
   - **Closing slide:** 8-10 seconds
4. Play through and adjust until slides and audio feel in sync

### STEP 6 — Add HeyGen Talking Head (PIP)
1. From Uploads, drag the HeyGen MP4 (Dr. Maya) onto the **first slide** (opening)
2. Resize to a small circle → position in the **bottom right corner**
3. Duplicate onto the **last slide** (closing) only
4. Do NOT put the avatar on every slide — it distracts from the content

### STEP 7 — Preview the Full Video
1. Click **Play** (triangle icon, top toolbar)
2. Watch the entire video — check for:
   - Audio synced with slides?
   - Dr. Maya appears on opening and closing only?
   - No blank slides or jarring cuts?
3. Fix any timing issues before exporting

### STEP 8 — Export
1. Top right → **Share** → **Download**
2. File type: **MP4 Video**
3. Quality: **1080p**
4. Click **Download** — wait for render to complete
5. Save as: `Lesson3-FINAL.mp4`
6. Move to: `01-LESSONS/LESSON-03/YOUTUBE/`

---

## DECISION POINTS

**Slides out of order after swapping:**
- Check PNG filenames — should be `slide_01` through `slide_15`
- Drag pages in the left panel to reorder

**Audio cuts off before last slide ends:**
- Shorten the last slide's duration to match where audio ends
- Or trim silence from the end of the MP3 in ElevenLabs and re-upload

**Dr. Maya has a white box around her:**
- She was exported with white background in HeyGen instead of transparent
- Go back to SOP-13 → re-generate with **Avatar Background → Remove**

**Canva is slow or freezing:**
- Close all other browser tabs
- Export anyway — render engine is separate from editor speed

**Slide durations don't match voiceover pacing:**
- Do NOT try to match exactly — aim for natural feel
- Give each slide enough time for a viewer to read + absorb the content

---

## COMMON MISTAKES
- Starting from scratch instead of duplicating Lesson 2 (wastes 30+ min)
- Uploading new PNGs before deleting old ones (confusion — which is which?)
- Forgetting to replace the audio (exporting with Lesson 2's voiceover)
- Putting Dr. Maya on every slide (opening + closing only)
- Skipping the preview before exporting

## LESSON 3 FILE LOCATIONS
| File | Path |
|---|---|
| Voiceover MP3 | `01-LESSONS/20260818 LMTnew lessons script/Lesson3/Lesson3 Script.mp3` |
| Slide PNGs | `01-LESSONS/20260818 LMTnew lessons script/Lesson3/slides-png/slide_01.png` through `slide_15.png` |
| HeyGen MP4 (save here) | `01-LESSONS/20260818 LMTnew lessons script/Lesson3/Lesson3-DrMaya-TalkingHead.mp4` |
| Final export (save here) | `01-LESSONS/LESSON-03/YOUTUBE/Lesson3-FINAL.mp4` |

## TOOLS & ACCESS NEEDED
- Canva Pro (canva.com)
- Slide PNGs: `01-LESSONS/20260818 LMTnew lessons script/Lesson3/slides-png/`
- Voiceover MP3: from ElevenLabs (SOP-01)
- HeyGen MP4: from app.heygen.com (SOP-13)

## RELATED SOPs
- SOP-01 — Master pipeline overview
- SOP-13 — HeyGen avatar setup + video generation
- SOP-04 — YouTube SEO package (next step after export)
