# SOP-13 — HeyGen: Create Avatar + Generate Talking Head
## Photo Avatar setup (one-time) + per-video generation

**Purpose:** Create a HeyGen Photo Avatar from a still image and generate a talking head video synced to an ElevenLabs voiceover.
**Trigger:** New lesson video needs a talking head, or a new avatar needs to be set up.
**Owner:** Brian McKinney
**Time required:** 15-30 min (first-time avatar setup) | 10-15 min (per video after setup)
**Frequency:** Avatar setup = once per character | Video generation = every lesson

---

## QUICK REFERENCE
1. PART A (one-time): Upload photo → create Photo Avatar → wait for processing
2. PART B (per video): New video → upload ElevenLabs MP3 → select avatar → set to transparent → generate → download

---

## AVATAR ROSTER

| Avatar | Used For |
|---|---|
| Brian McKinney | Default — general lessons |
| Dr. Maya | Lesson 3 (Don't Get Scammed) and future security/expert topics |

---

## PART A — CREATE DR. MAYA PHOTO AVATAR (one-time setup)

### STEP 1 — Open HeyGen Avatars
1. Go to **app.heygen.com** → log in
2. Top navigation → click **Avatars**
3. Click **+ Create Avatar** → select **Photo Avatar**

### STEP 2 — Upload the Photo
1. Click **Upload Photo**
2. Select: `C:\Users\Jordyn\Desktop\DR. Maya.png`
3. Make sure the photo meets these requirements:
   - Face clearly visible, front-facing
   - Good lighting, no harsh shadows
   - Plain or blurred background preferred
4. Click **Next**

### STEP 3 — Name and Configure
1. Name: `Dr. Maya`
2. Select voice: choose from HeyGen voices OR leave blank (you'll upload your own audio)
3. Click **Create Avatar**
4. HeyGen will process — this takes **5-15 minutes**
5. You'll get a notification when it's ready — do not close the tab

### STEP 4 — Verify
1. Go to **Avatars** → find Dr. Maya in your avatar list
2. Click **Preview** — she should animate correctly
3. If the preview looks off (mouth not syncing, face distorted) → delete and re-upload with a higher resolution photo

---

## PART B — BUILD SCENE-BY-SCENE VIDEO (every lesson)

> WARNING: Use **app.heygen.com** directly — NOT the Canva HeyGen plugin (it only generates 2.5 seconds)

### STEP 1 — Start a New Video
1. app.heygen.com → click **Create Video**
2. Select **Scene by scene** → **Build it yourself**

### STEP 2 — Build Each Scene (repeat for all 15)
For each scene, in order:

**Background:**
- Click **Background** → **Upload** → select matching slide PNG
- Scene 1 = `slide_01.png`, Scene 2 = `slide_02.png`, etc.

**Audio:**
- Click the **audio/script panel** → **Upload Audio**
- Select matching scene MP3 from `Voice3/scenes/`
- Scene 1 = `SCENE 1 — slide01-opening.mp3`, etc.

**Avatar:**
- Click **Avatar** → search `Dr. Maya` → select her
- Layout: **Circle**
- Background: **Remove** (transparent — NOT white)
- Position: **bottom corner**

**Add next scene:**
- Click **+ Add Scene** → repeat for Scene 2 through Scene 15

### STEP 3 — Review All 15 Scenes
- Scroll through all scenes in the left panel
- Confirm each scene has: correct background + correct audio + Dr. Maya avatar
- Do NOT generate until all 15 scenes are set up

### STEP 4 — Generate and Download
1. Click **Generate** (top right)
2. Wait — generation takes 10-20 minutes for 15 scenes
3. When complete: click **Download** → save as MP4
4. Filename: `Lesson3-DrMaya-FINAL.mp4`
5. Save to: `01-LESSONS/20260818 LMTnew lessons script/Lesson3/Voice3/`

---

## DECISION POINTS

**Photo Avatar looks distorted or mouth doesn't sync:**
- Delete the avatar → re-upload with a higher resolution photo
- Make sure the photo has no text overlays or cropping near the face

**HeyGen generates wrong length (too short or cuts off):**
- Delete and re-upload the MP3 — confirm the file is not corrupted
- Check the MP3 plays fully in Windows Media Player before uploading

**White halo appears around avatar in Canva:**
- You selected white background instead of transparent
- Re-generate in HeyGen with **Avatar Background → Remove**

**Avatar V not available:**
- Try **Avatar V2** or the next available motion engine
- Do not use the default — Avatar V gives the most natural movement

---

## COMMON MISTAKES
- Using the Canva HeyGen plugin (only 2.5 seconds — useless for lessons)
- White background instead of transparent (causes halo around avatar in Canva)
- Not waiting for Photo Avatar to process before trying to use it
- Saving the MP4 to Downloads instead of the correct lesson folder

## LESSON 3 FILE LOCATIONS
| File | Path |
|---|---|
| Voiceover MP3 | `01-LESSONS/20260818 LMTnew lessons script/Lesson3/Lesson3 Script.mp3` |
| Slide PNGs | `01-LESSONS/20260818 LMTnew lessons script/Lesson3/slides-png/slide_01.png` through `slide_15.png` |
| Dr. Maya photo | `C:\Users\Jordyn\Desktop\DR. Maya.png` |

## TOOLS & ACCESS NEEDED
- app.heygen.com (NOT the Canva plugin)
- Dr. Maya photo: `C:\Users\Jordyn\Desktop\DR. Maya.png`
- ElevenLabs MP3 voiceover (from SOP-01 Step 1)
