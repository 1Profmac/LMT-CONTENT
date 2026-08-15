# Video Production System — HP Gaming Computer
## 5-Minute YouTube Videos: HeyGen + ElevenLabs + Canva + Claude Code Render

---

## Two Machines, Two Jobs

| Machine | Role | What It Does |
|---------|------|-------------|
| **Road laptop (Jordyn)** | Content management | Write, post, Canva carousels, HubSpot, LinkedIn, email |
| **HP Gaming PC (home)** | Video production | HeyGen capture, ElevenLabs voiceover, Canva b-roll, Claude Code render pipeline |

**Rule:** Never try to render video on the road laptop. It can't handle it. Build carousels and text content on the road. Build video at home.

---

## The 5-Minute Video Pipeline

### Step 1: SCRIPT (Claude Code — either machine)
- Write the script using `/yt-short` or `/content-day` or manually
- Script lives in git: `50techbridge-content/youtube-shorts/scripts/` or `content/articles/`
- Plain text only. No stage directions. No annotations.
- 5-minute video = ~750 words spoken

### Step 2: HEYGEN (browser — HP gaming PC)
- Paste script into HeyGen
- Use your avatar
- Settings:
  - Background: GREEN SCREEN (chroma key, not solid color)
  - Resolution: 1920x1080
  - Export as MP4
- Save to: `layers/brian/[video-name]-brian-nobg.mp4`
- This gives you the talking head layer with transparent/green background

### Step 3: ELEVENLABS (browser — HP gaming PC)
- If you want higher quality audio than HeyGen produces:
  - Paste same script into ElevenLabs
  - Use your cloned voice
  - Download MP3/WAV
  - Save to: `layers/audio/[video-name]-voiceover.mp3`
- Then in HeyGen: mute the avatar audio, sync to ElevenLabs track in render
- OR: Use HeyGen audio if quality is good enough (skip this step)

### Step 4: CANVA B-ROLL (browser — HP gaming PC)
- Create 5 b-roll clips in Canva using Magic Media or stock video
- Each clip: 20 seconds, 1920x1080
- Download as MP4
- Save to: `layers/clips/[video-name]/clip-01.mp4` through `clip-05.mp4`
- Also create gap slides (bullet point slides for between clips):
  - Navy background, gold text, 3 bullets per slide
  - Export as PNG: `layers/slides/[video-name]/gap-01.png` through `gap-05.png`

### Step 5: CHROME OVERLAY (one-time, already built)
- Branded header/footer overlay: `layers/chrome/header-footer-1920x1080.png`
- Transparent PNG with 50+TechBridge branding
- This is the same across all videos — build once, reuse forever

### Step 6: CLAUDE CODE RENDER (HP gaming PC terminal)
- Claude Code runs the Python render script
- Command: `python lmt-video-overlay.py config.json`
- The script composites all layers:

```
Layer 1 (bottom): Navy background (1920x1080)
Layer 2: B-roll clips (timed to script sections)
Layer 3: Gap slides (between clips, key bullet points)
Layer 4: Brian talking head with green screen keyed out
Layer 5 (top): Chrome overlay (branded header/footer)
Audio: HeyGen audio or ElevenLabs voiceover
```

- Output: finished MP4 in all formats

### Step 7: EXPORT (Claude Code)
The render script produces:
- `[video-name]-LANDSCAPE.mp4` (16:9, YouTube)
- `[video-name]-VERTICAL.mp4` (9:16, LinkedIn/Shorts/Reels)
- `[video-name]-SQUARE.mp4` (1:1, Facebook/Instagram)
- YouTube metadata package (title, description, tags, thumbnail text)

---

## Config File Template

Create one config per video. Save to `video-builder/configs/`

```json
{
  "video_name": "sizzle-reel-50techbridge",
  "duration": 300,
  "resolution": {"width": 1920, "height": 1080},
  "background": "layers/base/navy-1920x1080.png",
  "brian": {
    "file": "layers/brian/sizzle-brian-nobg.mp4",
    "position": {"x": 0, "y": 0},
    "size": {"width": 1920, "height": 1080},
    "show_start": 8,
    "show_end": 290,
    "chromakey": "green"
  },
  "audio": {
    "source": "heygen",
    "file": "layers/brian/sizzle-brian-nobg.mp4",
    "voiceover_override": null
  },
  "clips": [
    {"file": "layers/clips/sizzle/clip-01.mp4", "start": 10, "end": 33},
    {"file": "layers/clips/sizzle/clip-02.mp4", "start": 45, "end": 68},
    {"file": "layers/clips/sizzle/clip-03.mp4", "start": 80, "end": 103},
    {"file": "layers/clips/sizzle/clip-04.mp4", "start": 115, "end": 138},
    {"file": "layers/clips/sizzle/clip-05.mp4", "start": 150, "end": 173}
  ],
  "gap_slides": [
    {
      "file": "layers/slides/sizzle/gap-01.png",
      "start": 33, "end": 45,
      "bullets": ["13 Locations", "Targeted 3X Completion Rate", "Increased Confidence"]
    },
    {
      "file": "layers/slides/sizzle/gap-02.png",
      "start": 68, "end": 80,
      "bullets": ["Competitive Cost Per Participant", "6 Modules", "WIOA Eligible"]
    },
    {
      "file": "layers/slides/sizzle/gap-03.png",
      "start": 103, "end": 115,
      "bullets": ["Peer Instructors", "Real Projects", "AI Tutors 24/7"]
    },
    {
      "file": "layers/slides/sizzle/gap-04.png",
      "start": 138, "end": 150,
      "bullets": ["MBE Certified", "Self-Paced", "Customized to Your Org"]
    },
    {
      "file": "layers/slides/sizzle/gap-05.png",
      "start": 173, "end": 189,
      "bullets": ["One 30-Min Call", "Pilot Program", "Results You Can Report"]
    }
  ],
  "chrome": "layers/chrome/header-footer-1920x1080.png",
  "output_dir": "output/sizzle-reel/",
  "formats": ["landscape", "vertical", "square"]
}
```

---

## Video Content Queue (build when home)

### Priority 1: Sizzle Reel (60 seconds)
- Script: Already written in `06-MARKETING/sizzle/SIZZLE-REEL-PACKAGE.md`
- Purpose: DMs, email outreach, LinkedIn Featured, website hero
- Pin to LinkedIn profile immediately after upload

### Priority 2: "How to Keep Your Job Over 50" Series Intro (90 seconds)
- Script: Episode 1 from `06-MARKETING/master-claude-series/mini-series-scripts.md`
- Purpose: YouTube Short + LinkedIn video post to launch the series
- Can also be the trailer for the course

### Priority 3: Workforce Pitch Video (3-5 minutes)
- Script: Based on Article 3 (13 Locations) or Article 5 (Deploy This Quarter)
- Purpose: Send to workforce directors instead of a cold email
- This is the video that replaces the pitch deck

### Priority 4: Course Lesson Videos (3-5 min each, 10 total)
- Scripts: Already written in `master-claude-series/video-scripts.md`
- Purpose: LearnDash course content
- Build all 10 in one batch session

---

## Batch Production Day (when home)

When you're at the HP gaming PC, batch everything. Don't make one video at a time.

### Morning Block (2 hours): Generate Raw Assets
1. Paste all scripts into HeyGen → generate all talking heads (they render in parallel)
2. Paste all scripts into ElevenLabs → generate all voiceovers
3. Open Canva → create all b-roll clips and gap slides for all videos
4. Download everything to the correct `layers/` folders

### Afternoon Block (2 hours): Render
1. Create config.json for each video
2. Run Claude Code render pipeline for each: `python lmt-video-overlay.py config.json`
3. Review outputs
4. Fix any timing or quality issues
5. Final render

### End of Day: Upload
1. Upload to YouTube (scheduled, not all at once)
2. Save landscape versions for website/email
3. Save vertical versions for LinkedIn/Shorts/Reels
4. Save square versions for Facebook/Instagram
5. Update content calendar with publish dates

---

## What You Do On The Road vs At Home

| Task | Road Laptop | HP Gaming PC |
|------|------------|--------------|
| Write scripts | Yes | Yes |
| Build Canva carousels (static) | Yes | Yes |
| Post to LinkedIn/FB | Yes | Yes |
| Send newsletter | Yes | Yes |
| Work HubSpot | Yes | Yes |
| HeyGen talking head (quick, 60 sec) | Yes (browser) | Yes |
| ElevenLabs voiceover | Yes (browser) | Yes |
| Build Canva video (with b-roll) | No — too slow | Yes |
| Claude Code video render | No — can't handle it | Yes |
| Batch produce multiple videos | No | Yes |
| Upload to YouTube | Yes (if already rendered) | Yes |

---

## YouTube SEO (every video, no exceptions)

Every video gets a full SEO package before upload. Reference: `06-MARKETING/YOUTUBE-SEO-GUIDE.md`

**Checklist before hitting Publish in YouTube Studio:**
- [ ] Title: under 60 chars, keyword front-loaded
- [ ] Description: hook in first 2 lines, resource links, about block, hashtags
- [ ] Tags: 15 permanent + 5-8 topic-specific (20+ total)
- [ ] Thumbnail: your face + 3-5 words, high contrast, Canva 1280x720
- [ ] Chapters: timestamps in description starting at 0:00
- [ ] End screen: subscribe + best video + newest video
- [ ] Cards: 1-2 links to related videos
- [ ] Playlist: assigned to correct playlist
- [ ] Scheduled publish time (don't dump them all at once)

**Playlists to create in YouTube Studio (one time):**
1. "How to Keep Your Job Over 50" — the mini-series
2. "AI Training for Adults 50+" — how-to and course content
3. "The Numbers Nobody Told You" — data/stats/research
4. "Workforce Development & WIOA" — for org decision-makers
5. "50+TechBridge Course Preview" — lesson clips and demos

---

## Software Requirements — HP Gaming PC

Confirm these are installed:
- [ ] Python 3.10+
- [ ] FFmpeg (for video processing)
- [ ] Claude Code CLI
- [ ] Git (for pulling scripts from repo)
- [ ] `lmt-video-overlay.py` render script (from `50techbridge-content/video-builder/`)
- [ ] Chrome browser (for HeyGen, ElevenLabs, Canva)

---

## The Goal

One batch day at home produces:
- 1 sizzle reel (60 sec) — use immediately for all outreach
- 1 series intro (90 sec) — launch the mini-series with video
- 1 workforce pitch video (5 min) — replaces cold emails
- 4-10 course lessons (3-5 min each) — fills out LearnDash

Then you go back on the road with a library of video content that posts itself on schedule while you focus on HubSpot, LinkedIn, and closing contracts.
