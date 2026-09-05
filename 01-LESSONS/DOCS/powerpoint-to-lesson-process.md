# PowerPoint → Lesson Page Process
Last updated: 2026-08-26

Use this every time you have a new PowerPoint + voiceover ready to publish as a lesson.

---

## Step 1 — Export PowerPoint as Video
- PowerPoint → **File → Export → Create a Video**
- Quality: **Full HD (1080p)**
- Check **"Use recorded timings and narrations"** (includes your voiceover)
- Save as **MP4**

---

## Step 2 — Upload to YouTube
- Go to **YouTube Studio → Create → Upload**
- Set visibility to **Unlisted** (only people with the link can see it)
- Add title, description, thumbnail
- Once uploaded, copy the **video ID** from the URL
  - Example: `youtube.com/watch?v=abc123XYZ` → ID is `abc123XYZ`

---

## Step 3 — Update the Lesson Page HTML
- Open `LESSON-PAGE-TEMPLATE.html` from `Desktop/LMT-CONTENT/01-LESSONS/`
- Find the YouTube embed line — looks like this:
  ```
  src="https://www.youtube.com/embed/VIDEO_ID_HERE
  ```
- Replace `VIDEO_ID_HERE` with your new video ID
- Update the lesson title, activity steps, and "Next Day" preview text
- Save the file

---

## Step 4 — Paste into LearnDash
- WordPress → **LearnDash LMS → Lessons → [Lesson Name] → Edit**
- Switch to **Code Editor**
- Select all existing code → Delete
- Paste updated HTML
- Click **Update**

---

## File Locations
| File | Location |
|---|---|
| Lesson page template | `01-LESSONS/LESSON-PAGE-TEMPLATE.html` |
| Lesson 1 page | `01-LESSONS/LESSON-01/` |
| Lesson 2 page | `01-LESSONS/LESSON-02/` |
| Lesson 3 page | `01-LESSONS/LESSON-03/` |
| Exported MP4s | `01-LESSONS/LESSON-X/YOUTUBE/` |

---

## Notes
- Always set YouTube to **Unlisted** for lesson videos — not Public
- Two video styles per lesson: **Coffee Talk** and **The Classroom** — you need two separate YouTube IDs per lesson
- Test the embed in Chrome before publishing to LearnDash
