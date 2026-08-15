# AI Tools — When and How to Use Each One
**Brian McKinney | Learn More Technologies**
**The goal: right tool, right job, minimum cost.**

---

## THE SIMPLE RULE

| If you're... | Use... |
|---|---|
| Thinking, writing, planning | Claude.ai |
| Running, rendering, executing | Claude Code |
| Recording talking head video | HeyGen |
| Building B-roll clips | Canva |
| Cloning your voice | ElevenLabs |
| Storing finished work | GitHub |

---

## CLAUDE.AI
**app.claude.ai — Conversation and content creation**

**Use it for:**
- Writing scripts (HeyGen talking head scripts)
- Writing articles and LinkedIn posts
- Planning video structure and slide content
- Generating YouTube metadata (title, description, tags)
- Drafting email sequences and outreach
- Thinking through strategy and decisions
- Asking "what should I do next?"
- Generating config file content (slides, bullets, timing)

**Do NOT use it for:**
- Running renders
- Moving files
- Git commits
- Anything that requires touching your actual computer

**Cost tip:**
- Use Projects to store your brand context — saves you re-explaining every session
- Keep conversations focused — one topic per conversation
- Draft in Claude.ai, execute in Claude Code

---

## CLAUDE CODE
**This tool — Execution and file operations**

**Use it for:**
- Running video renders (`python lmt-video-overlay.py config.json`)
- Moving, renaming, organizing files
- Git commits and pushes to GitHub
- Fixing bugs in scripts
- Probing video files for format/dimensions
- Running the render after Claude.ai gives you the config

**Do NOT use it for:**
- Writing content from scratch — that's Claude.ai
- Long back-and-forth planning sessions — every message costs tokens
- Figuring out what you want to do — decide first, then come here

**Cost tip:**
- Come here with everything ready: recording path, clips path, script
- One session should be: drop files → render → done
- Say "check Git for the template" not "figure out how to make a video"

**The right way to start a session:**
> "New full video. Recording: [path]. Clips: [path]. Use TEMPLATE-FULL-VIDEO."

That's it. 3 lines. Render starts in 2 messages.

---

## HEYGEN
**app.heygen.com — Brian's talking head recordings**

**Use it for:**
- Recording Brian talking head videos (full and short)
- Green screen export for video overlay

**Settings that matter:**
| Setting | Full Video | YouTube Short |
|---|---|---|
| Layout | **Original** (never Circle) | **Original** (never Circle) |
| Background | Green screen | Green screen |
| Resolution | 1920x1080 landscape | 1080x1920 vertical |
| File name on export | `brian-FULL-1920x1080.mp4` | `brian-SHORT-1080x1920.mp4` |

**Where to save:** `02-LINKEDIN/articles/[article]/broll-clips/`

**Cost tip:**
- Record once, use everywhere — the render system handles all formats
- Always use Original layout — Circle layout makes you a tiny avatar

---

## CANVA
**canva.com — B-roll video clips**

**Use it for:**
- Building background B-roll clips for full videos
- Building stat clips for YouTube Shorts

**Export rules:**
| Video Type | Canva Size | What to include |
|---|---|---|
| Full video B-roll | 1920x1080 (landscape) | Background video ONLY — no text, no headers |
| Short B-roll | 1080x1920 (vertical) | Background video ONLY — no text, no headers |
| Standalone stat posts | 1080x1920 (vertical) | Text + headers baked in = post directly |

**Critical rule:** If text or headers are baked into the clip, the render script will double them. Export clean background video only for B-roll. Save the annotated versions for direct social posting.

**Naming on export:**
- `stat-01-[topic].mp4`, `stat-02-[topic].mp4` etc.
- Drop in `broll-clips/` folder

---

## ELEVENLABS
**elevenlabs.io — Brian's voice clone**

**Use it for:**
- Generating podcast episode audio
- Voiceover for content where Brian hasn't recorded

**When to use:**
- Podcast episodes from existing article content
- Social audio clips
- NOT needed if Brian records in HeyGen (use HeyGen audio instead)

**Voice ID:** `uAs0vN0GLLpz7FM7JVkz`

---

## GITHUB
**github.com/1Profmac/50techbridge-content**

**Use it for:**
- Storing all scripts, configs, and skill files
- Reference point for "what worked before"
- Never loses proven work

**The rule:** Any config that renders successfully gets committed immediately.

**When Claude Code session starts on a new video, say:**
> "Check Git for the last working config"

That one sentence saves hours.

---

## THE COMPLETE WORKFLOW — NEW VIDEO

```
1. CLAUDE.AI
   → Write HeyGen script (text only, no annotations)
   → Generate slides content and YouTube metadata

2. HEYGEN
   → Record using the script
   → Export green screen, Original layout
   → Name file: brian-FULL-1920x1080.mp4 or brian-SHORT-1080x1920.mp4
   → Drop in broll-clips/ folder

3. CANVA
   → Build 6 background B-roll clips (no text baked in)
   → Export at correct resolution
   → Name: stat-01 through stat-06
   → Drop in broll-clips/ folder

4. CLAUDE CODE
   → "New full video. Use TEMPLATE-FULL-VIDEO."
   → Fill in paths and slide content from Claude.ai output
   → Render → done

5. GITHUB
   → Commit the config immediately after successful render
```

---

## WHAT EACH TOOL COSTS

| Tool | Cost Model | Minimize by... |
|---|---|---|
| Claude.ai | Per token | Keep conversations focused, one topic |
| Claude Code | Per token | Come ready, minimal back-and-forth |
| HeyGen | Per video minute | Record right the first time |
| Canva | Monthly flat | Export correctly the first time |
| ElevenLabs | Per character | Use only when HeyGen audio isn't available |
| GitHub | Free | Always use it |

**Biggest waste:** Using Claude Code to figure out what you want. Decide in Claude.ai (cheaper exploration). Execute in Claude Code (fast, focused).

---

*Saved to LMT-CONTENT. Update this file whenever you learn a better way.*
