# LMT Command List
**Say these exact phrases to Claude to get the right result every time.**

---

## VIDEO PRODUCTION

### New Full YouTube Video
> "New full video — here's my HeyGen recording [path] and my 6 Canva clips [paths]. Use TEMPLATE-FULL-VIDEO."

### New YouTube Short
> "New Short — here's my HeyGen recording [path]. Use TEMPLATE-SHORT-VIDEO."

### Re-render existing video
> "Re-render [config name] — nothing has changed."

### Check what was built before
> "Check Git for the last working [lesson/short/full] config and use that as the template."

---

## CONTENT CREATION

### YouTube Short script + package
> "/yt-short [topic] [tone]"
> Example: `/yt-short ageism indictment`

### YouTube Opportunity tone short
> "/yt-short-opportunity [topic]"

---

## FOLDER CLEANUP

### Clean and organize LMT folder
> "/lmt-cleanup"

---

## SEO & PUBLISHING

### Yoast SEO fields for any content
> "Give me Yoast fields for this page/post."

---

## MEMORY & CONTEXT

### If Claude seems to forget how we work
> "Check your memory and the Git history before doing anything."

### If something is broken
> "Check Git for the last working version of [file/script]."

### Save something for future sessions
> "Remember this for next time: [what to remember]"

---

## VIDEO ASSET REQUIREMENTS

| Asset | Spec | Filename | Where |
|---|---|---|---|
| HeyGen Full Video | Landscape 1920x1080, green screen, Original layout | `brian-FULL-1920x1080.mp4` | broll-clips/ |
| HeyGen Short | Vertical 1080x1920, green screen, Original layout | `brian-SHORT-1080x1920.mp4` | broll-clips/ |
| Canva B-roll clips | Vertical 1080x1920, NO text/headers baked in, ~6 sec each | `stat-01-[topic].mp4` | broll-clips/ |
| Canva Stat clips (annotated) | Keep for LinkedIn/Instagram posts | keep original name | social/ |

**The dimensions are always in the filename. No guessing.**

---

## FILE LOCATIONS

| What | Where |
|---|---|
| Full video template | `video-builder/TEMPLATE-FULL-VIDEO.json` |
| Short video template | `video-builder/TEMPLATE-SHORT-VIDEO.json` |
| Render script | `video-builder/lmt-video-overlay.py` |
| Finished videos | `02-LINKEDIN/articles/[article]/YOUTUBE/` |
| All platform formats | `02-LINKEDIN/articles/[article]/YOUTUBE/ALL-FORMATS/` |
| Chrome layer PNG | `video-builder/layers/chrome/header-footer-1920x1080.png` |
| Navy background PNG | `video-builder/layers/base/navy-1920x1080.png` |

---

## THE SALT RULE
Every file has one home. Always findable. No duplicates.
- Scripts → stay with the article folder
- Finished videos → YOUTUBE/ subfolder
- Templates → video-builder/
- Raw clips → broll-clips/
