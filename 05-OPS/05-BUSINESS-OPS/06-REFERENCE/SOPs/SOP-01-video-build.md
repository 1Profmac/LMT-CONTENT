# SOP-01 — Video Build Pipeline
## Master overview: Script → Voice → Avatar → Canva → YouTube

**Purpose:** Full lesson video from script to published — order of operations and links to each sub-SOP.
**Trigger:** New lesson script is finalized and ready to produce.
**Owner:** Brian McKinney
**Time required:** 2-4 hours total across all steps
**Frequency:** Every new lesson

---

## PIPELINE ORDER

```
STEP 1 → ElevenLabs    Generate voiceover MP3 from script
STEP 2 → HeyGen        Create talking head MP4 (see SOP-13)
STEP 3 → Canva         Assemble slides + audio + export MP4 (see SOP-14)
STEP 4 → YouTube       Upload Unlisted → get video ID
STEP 5 → LearnDash     Paste video ID into lesson page
```

---

## STEP 1 — Generate Voiceover (ElevenLabs)
1. Go to elevenlabs.io → Text to Speech
2. Paste the finalized lesson script
3. Voice: **Brian McKinney** | Model: **Eleven Multilingual v2** | Speed: **1.0**
4. Generate → Download MP3
5. Save as: `Lesson[X]-Voice-Over-FINAL.mp3` in `Lesson[X]/` folder

---

## STEP 2 — Generate Talking Head (HeyGen)
→ **Follow SOP-13** for full steps including Photo Avatar setup

**Avatar by lesson:**
| Lesson | Avatar |
|---|---|
| Lesson 1, 2 (default) | Brian McKinney |
| Lesson 3 (Don't Get Scammed) | Dr. Maya |

Save HeyGen MP4 to: `Lesson[X]/` folder

---

## STEP 3 — Assemble Video in Canva
→ **Follow SOP-14** for full steps

Summary: Duplicate previous lesson → swap slides → replace audio → set durations → add PIP → preview → export MP4 1080p

Save final MP4 to: `01-LESSONS/LESSON-0[X]/YOUTUBE/`

---

## STEP 4 — Upload to YouTube
1. YouTube Studio → **Create** → **Upload**
2. Visibility: **Unlisted** (set this FIRST — before anything else)
3. Title, description, thumbnail → follow **SOP-04** (YouTube SEO package)
4. Copy the video ID from the URL (the string after `v=`)

---

## STEP 5 — Publish to LearnDash
1. WordPress → LearnDash → open the lesson page
2. Find the video embed block
3. Paste the YouTube video ID
4. Update/publish the lesson
5. Mark TODO.md complete

---

## FILE LOCATIONS

| File | Location |
|---|---|
| Script | `01-LESSONS/20260818 LMTnew lessons script/Lesson[X]/` |
| Slide PNGs | `01-LESSONS/20260818 LMTnew lessons script/Lesson[X]/slides-png/` |
| Voiceover MP3 | `01-LESSONS/20260818 LMTnew lessons script/Lesson[X]/` |
| HeyGen MP4 | `01-LESSONS/20260818 LMTnew lessons script/Lesson[X]/` |
| Final video MP4 | `01-LESSONS/LESSON-0[X]/YOUTUBE/` |

---

## RELATED SOPs
- **SOP-13** — HeyGen: create avatar + generate talking head
- **SOP-14** — Canva: assemble and export lesson video
- **SOP-04** — YouTube SEO package
- **SOP-02** — PPT to lesson (slide deck → PNGs)
