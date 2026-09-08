# SOP-15 — ElevenLabs Scene Voiceovers
## Split lesson script into 15 individual scene MP3s for HeyGen

**Purpose:** Generate individual scene voiceover MP3s in ElevenLabs so each HeyGen scene has its own matched audio — same method used for Lesson 2b and 2c.
**Trigger:** Lesson script is finalized and HEYGEN-scenes file has been created. Ready to generate audio.
**Owner:** Brian McKinney
**Time required:** 30-45 minutes (15 scenes)
**Frequency:** Every new lesson video

---

## QUICK REFERENCE
1. Open HEYGEN-scenes-lesson-0X.txt from the lesson folder
2. ElevenLabs → Text to Speech → select correct voice
3. Copy Scene 1 text → generate → download → save with scene name
4. Repeat for all 15 scenes
5. Save all MP3s to `Lesson[X]/Voice[X]/scenes/`

---

## PREREQUISITES
- [ ] HEYGEN-scenes-lesson-0X.txt created and finalized (see SOP-13)
- [ ] ElevenLabs account logged in
- [ ] `Voice[X]/scenes/` folder exists in lesson folder
- [ ] README.txt in scenes folder lists correct voice name

---

## STEP-BY-STEP

### STEP 1 — Open the Scene Script File
- Navigate to lesson folder: `01-LESSONS/20260818 LMTnew lessons script/Lesson[X]/`
- Open `HEYGEN-scenes-lesson-0X.txt`
- Keep this file open — you will copy from it 15 times

### STEP 2 — Open ElevenLabs
- Go to elevenlabs.io → log in
- Click **Text to Speech**
- Select the correct voice for this lesson:

| Lesson | Voice |
|---|---|
| Lesson 1, 2 (default) | Brian McKinney |
| Lesson 3 (Don't Get Scammed) | Dr. Maya |

- Settings: **Eleven Multilingual v2** | Speed: **1.0**

### STEP 3 — Generate Scene 1
- In the HEYGEN-scenes file, find `SCENE 1`
- Copy all text between the dashes (the scene content only — not the header)
- Paste into ElevenLabs text box
- Click **Generate**
- Click **Download**
- Save as: `SCENE 1 — slide01-[name].mp3`
- Move to: `Lesson[X]/Voice[X]/scenes/`

### STEP 4 — Repeat for All 15 Scenes
- Clear the ElevenLabs text box
- Copy next scene text → generate → download → save with scene number and name
- Work in order: Scene 1 through Scene 15
- Do not skip scenes or generate out of order

### STEP 5 — Verify All 15 Files
- Open `Voice[X]/scenes/` folder
- Confirm 15 MP3 files are present, named correctly
- Play each one quickly to check audio is clean (no cutoffs, no errors)

---

## LESSON 3 FILE LOCATIONS
| Item | Path |
|---|---|
| Scene script | `Lesson3/HEYGEN-scenes-lesson-03.txt` |
| Scenes folder | `Lesson3/Voice3/scenes/` |
| Voice | Dr. Maya |

## SCENE-TO-SLIDE MAP (Lesson 3)
| Scene | Starts with | Ends with |
|---|---|---|
| 1 | "You already did the brave part..." | "...wants your fear." |
| 2 | "I am not going to spend..." | "...most of the country." |
| 3 | "You are not the punchline..." | "...hunted by professionals." |
| 4 | "Skill one. Spot a fake..." | "...not the logo." |
| 5 | "The sender. Would Amazon..." | "...That test is dead." |
| 6 | "'Social Security will be suspended...'" | "...costume's sleeve." |
| 7 | "Skill two. Name the pressure..." | "...Hurry. Fear. Secrecy. Authority." |
| 8 | "Hurry. Twenty minutes..." | "...They can fake it." |
| 9 | "There is a fifth lever..." | "...they do not get to drive." |
| 10 | "The new costume — a voice you love..." | "...You are literate." |
| 11 | "Skill three. Passwords..." | "...they can reset everything else." |
| 12 | "What if you cannot remember..." | "...on the internet." |
| 13 | "Now the second lock..." | "...You never speak it to a stranger." |
| 14 | "If it already happened..." | "...guarantee of no chance." |
| 15 | "Your homework. Twenty minutes..." | "...I'll see you in the room." |

---

## DECISION POINTS

**Scene audio cuts off early:**
- The text may have been truncated when copying — go back to the scenes file and re-copy the full scene text

**Voice sounds wrong or inconsistent between scenes:**
- Always use the same voice and same model settings for every scene in one lesson
- Do not switch voices mid-lesson

**Scene generates but sounds robotic:**
- Break long sentences into shorter ones in the script before pasting
- Avoid very long run-on sentences — ElevenLabs handles shorter phrases better

---

## COMMON MISTAKES
- Copying the scene header (SCENE 1 — slide01-title) into ElevenLabs — copy content only
- Saving to Downloads instead of `Voice[X]/scenes/` immediately
- Generating out of order and losing track of which scene is which
- Not naming files with the scene number — impossible to match to slides later

## TOOLS & ACCESS NEEDED
- elevenlabs.io (Text to Speech)
- HEYGEN-scenes-lesson-0X.txt (from lesson folder)
- `Voice[X]/scenes/` folder (must exist before starting)

## NEXT STEP AFTER THIS SOP
→ SOP-13 (HeyGen) — upload scene MP3s + slide PNGs into HeyGen scenes
