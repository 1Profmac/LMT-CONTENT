# SOP-02 — PowerPoint → Lesson Page
## PPT export → YouTube → LearnDash

**Purpose:** Turn a finished PowerPoint into a live lesson page on the website.
**Trigger:** PowerPoint slide deck is finalized and approved.
**Owner:** Brian McKinney
**Time required:** 30-45 minutes
**Frequency:** Per lesson

---

## QUICK REFERENCE
1. PPT → File → Export → Create Video → 1080p → MP4
2. YouTube Studio → Upload → Unlisted → copy video ID
3. Open lesson HTML → replace VIDEO_ID_HERE → save
4. WordPress → LearnDash → Lessons → Code Editor → paste → Update

---

## PREREQUISITES
- [ ] PowerPoint finalized (all slides reviewed)
- [ ] Voiceover recorded or timed narrations added to PPT
- [ ] YouTube Studio access
- [ ] WordPress / LearnDash admin access
- [ ] Lesson HTML template open and ready

---

## STEP-BY-STEP

### STEP 1 — Export PPT as Video
1. PowerPoint → **File → Export → Create a Video**
2. Quality: **Full HD (1080p)**
3. Check **"Use recorded timings and narrations"** (includes voiceover)
4. Click **Create Video** → save as MP4
5. Save to: `01-LESSONS/LESSON-03/YOUTUBE/lesson3-LANDSCAPE.mp4`

### STEP 2 — Upload to YouTube
1. YouTube Studio → **Create → Upload video**
2. Select your MP4
3. While uploading, fill in:
   - Title (see SOP-04 for SEO formula)
   - Description (see SOP-04 for template)
   - Thumbnail (upload Canva PNG)
   - Playlist: **50+TechBridge Course**
   - Audience: **Not made for kids**
4. Visibility: **Unlisted** (NOT Public for lesson videos)
5. Once uploaded → copy the **video ID** from the URL
   - URL example: `youtube.com/watch?v=abc123XYZ`
   - Video ID: `abc123XYZ`

### STEP 3 — Update Lesson Page HTML
1. Open: `01-LESSONS/LESSON-PAGE-TEMPLATE.html`
2. Find the YouTube embed line:
   ```
   src="https://www.youtube.com/embed/VIDEO_ID_HERE
   ```
3. Replace `VIDEO_ID_HERE` with your actual video ID
4. Update lesson title, activity steps, and "Next Day" preview text
5. Save the file as `lesson3-page.html`

### STEP 4 — Paste into LearnDash
1. WordPress → **LearnDash LMS → Lessons → Lesson 3 → Edit**
2. Switch to **Code Editor** (top right of editor)
3. Select all existing code → Delete
4. Paste updated HTML
5. Click **Update**
6. Preview in incognito window to verify it loads correctly

---

## DECISION POINTS
- **Two video styles (Coffee Talk + Classroom)?** → Upload each separately, get two video IDs, update both embed spots in the HTML.
- **Video renders but has no audio?** → Check "Use recorded timings and narrations" was checked on export.
- **LearnDash shows blank after paste?** → Switch back to Visual editor, then back to Code. Re-paste.

## COMMON MISTAKES
- Setting YouTube to **Public** instead of **Unlisted** for lesson videos
- Pasting wrong video ID (copy from URL bar AFTER video finishes processing)
- Forgetting to test in incognito before calling it done

## TOOLS & ACCESS NEEDED
- Microsoft PowerPoint
- YouTube Studio (youtube.com/studio)
- WordPress admin (50plustechbridge.com/wp-admin)
- LearnDash plugin

## FILE LOCATIONS
| File | Location |
|---|---|
| Lesson HTML template | `01-LESSONS/LESSON-PAGE-TEMPLATE.html` |
| Lesson 1 | `01-LESSONS/LESSON-01/` |
| Lesson 2 | `01-LESSONS/LESSON-02/` |
| Lesson 3 | `01-LESSONS/LESSON-03/` |
