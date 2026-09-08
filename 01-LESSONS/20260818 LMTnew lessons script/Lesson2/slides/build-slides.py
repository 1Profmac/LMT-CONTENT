"""
Lesson 2b Slide Generator — 50+TechBridge
Builds 8 HeyGen-ready HTML slides at 1920x1080 (landscape/16:9)
Brand: Navy #0E1C2F | Gold #C8942E | White #FFFFFF

Run: python build-slides.py
Output: slide01.html through slide08.html in this folder
To use in HeyGen: open each HTML in browser, screenshot at 1920x1080, upload as background image
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_CSS = """
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1920px;
    height: 1080px;
    background: #0E1C2F;
    font-family: 'Segoe UI', Arial, sans-serif;
    position: relative;
    overflow: hidden;
  }
  .series-tag {
    position: absolute;
    top: 36px;
    left: 80px;
    font-size: 22px;
    font-weight: 700;
    color: #C8942E;
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .gold-bar-top {
    position: absolute;
    top: 70px;
    left: 80px;
    right: 80px;
    height: 4px;
    background: #C8942E;
  }
  .gold-bar-bottom {
    position: absolute;
    bottom: 70px;
    left: 80px;
    right: 80px;
    height: 4px;
    background: #C8942E;
  }
  .footer {
    position: absolute;
    bottom: 30px;
    left: 80px;
    right: 80px;
    font-size: 20px;
    color: #C8942E;
    text-align: center;
  }
  .content {
    position: absolute;
    top: 100px;
    bottom: 90px;
    left: 80px;
    right: 80px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
"""

def slide(css_extra, body, filename):
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
{BASE_CSS}
{css_extra}
</style>
</head>
<body>
  <div class="series-tag">DIGITAL PIONEER &nbsp;|&nbsp; LESSON 2B</div>
  <div class="gold-bar-top"></div>
  <div class="gold-bar-bottom"></div>
  <div class="footer">50+TechBridge &nbsp;|&nbsp; Brian McKinney &nbsp;|&nbsp; 50plustechbridge.com</div>
  <div class="content">
{body}
  </div>
</body>
</html>"""
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built: {filename}")


# ── SLIDE 01: Title / Welcome ──────────────────────────────────────────────
slide("""
  .lesson-label {
    font-size: 28px;
    color: #C8942E;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 24px;
  }
  .title {
    font-size: 96px;
    font-weight: 800;
    color: #FFFFFF;
    text-align: center;
    line-height: 1.1;
    margin-bottom: 20px;
  }
  .title span { color: #C8942E; }
  .subtitle {
    font-size: 36px;
    color: #AAAAAA;
    text-align: center;
    margin-top: 20px;
  }
""", """
    <div class="lesson-label">Lesson 2b</div>
    <div class="title">Ask Your<br><span>First Real Question</span></div>
    <div class="subtitle">5 minutes &nbsp;·&nbsp; One prompt &nbsp;·&nbsp; Your first real answer</div>
""", "slide01-title.html")


# ── SLIDE 02: How the Starter Prompt Works ────────────────────────────────
slide("""
  .heading {
    font-size: 56px;
    font-weight: 800;
    color: #FFFFFF;
    text-align: center;
    margin-bottom: 50px;
  }
  .heading span { color: #C8942E; }
  .points {
    display: flex;
    flex-direction: column;
    gap: 28px;
    width: 100%;
    max-width: 1100px;
  }
  .point {
    display: flex;
    align-items: center;
    gap: 30px;
    background: rgba(200,148,46,0.12);
    border-left: 6px solid #C8942E;
    border-radius: 8px;
    padding: 24px 40px;
  }
  .check {
    font-size: 44px;
    color: #C8942E;
    flex-shrink: 0;
  }
  .point-text {
    font-size: 36px;
    color: #FFFFFF;
    line-height: 1.3;
  }
""", """
    <div class="heading">The Starter Prompt tells AI <span>three things</span></div>
    <div class="points">
      <div class="point"><div class="check">&#10003;</div><div class="point-text">That you are <strong>new to AI</strong></div></div>
      <div class="point"><div class="check">&#10003;</div><div class="point-text">That you are <strong>over 50</strong></div></div>
      <div class="point"><div class="check">&#10003;</div><div class="point-text">Exactly <strong>how to format the answer</strong> — short steps, plain language</div></div>
    </div>
""", "slide02-how-it-works.html")


# ── SLIDE 03: The Prompt Text ─────────────────────────────────────────────
slide("""
  .instruction {
    font-size: 34px;
    color: #AAAAAA;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 36px;
  }
  .prompt-box {
    background: #FFFFFF;
    border-radius: 16px;
    border: 4px solid #C8942E;
    padding: 50px 70px;
    max-width: 1400px;
    text-align: center;
  }
  .prompt-text {
    font-size: 48px;
    color: #0E1C2F;
    line-height: 1.5;
    font-weight: 600;
  }
  .prompt-text span {
    color: #C8942E;
    font-style: italic;
  }
  .hint {
    font-size: 28px;
    color: #888888;
    margin-top: 36px;
    text-align: center;
  }
""", """
    <div class="instruction">Type this exactly</div>
    <div class="prompt-box">
      <div class="prompt-text">
        I'm new to AI and I'm over 50.<br>
        Please explain <span>[your topic]</span> in five simple steps,<br>
        using clear language.
      </div>
    </div>
    <div class="hint">Replace <em>[your topic]</em> with something you actually want to know about</div>
""", "slide03-the-prompt.html")


# ── SLIDE 04: Choose Your Topic ───────────────────────────────────────────
slide("""
  .heading {
    font-size: 52px;
    font-weight: 700;
    color: #FFFFFF;
    text-align: center;
    margin-bottom: 20px;
  }
  .sub {
    font-size: 30px;
    color: #AAAAAA;
    margin-bottom: 50px;
    text-align: center;
  }
  .examples {
    display: flex;
    gap: 40px;
    justify-content: center;
  }
  .example-card {
    background: rgba(255,255,255,0.06);
    border: 3px solid #C8942E;
    border-radius: 16px;
    padding: 40px 36px;
    width: 380px;
    text-align: center;
  }
  .example-icon { font-size: 60px; margin-bottom: 18px; }
  .example-text {
    font-size: 28px;
    color: #FFFFFF;
    line-height: 1.4;
  }
  .or-text {
    font-size: 28px;
    color: #C8942E;
    margin-top: 44px;
    text-align: center;
  }
""", """
    <div class="heading">Not sure what to ask?</div>
    <div class="sub">Use one of these — or pick something that matters to you right now.</div>
    <div class="examples">
      <div class="example-card">
        <div class="example-icon">&#128241;</div>
        <div class="example-text">how to video call my grandchildren</div>
      </div>
      <div class="example-card">
        <div class="example-icon">&#128664;</div>
        <div class="example-text">how to plan a weekend road trip</div>
      </div>
      <div class="example-card">
        <div class="example-icon">&#127807;</div>
        <div class="example-text">how to start a vegetable garden</div>
      </div>
    </div>
    <div class="or-text">There is no wrong answer.</div>
""", "slide04-examples.html")


# ── SLIDE 05: Send It ─────────────────────────────────────────────────────
slide("""
  .big-instruction {
    font-size: 80px;
    font-weight: 800;
    color: #FFFFFF;
    text-align: center;
    line-height: 1.15;
    margin-bottom: 30px;
  }
  .big-instruction span { color: #C8942E; }
  .arrow-box {
    width: 140px;
    height: 140px;
    background: #C8942E;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 70px;
    color: #FFFFFF;
    margin: 20px auto 30px;
  }
  .watch-text {
    font-size: 42px;
    color: #AAAAAA;
    text-align: center;
  }
""", """
    <div class="big-instruction">Press Enter<br>or tap the <span>arrow button.</span></div>
    <div class="arrow-box">&#10148;</div>
    <div class="watch-text">Then watch.</div>
""", "slide05-send-it.html")


# ── SLIDE 06: Watch It Write ──────────────────────────────────────────────
slide("""
  .heading {
    font-size: 64px;
    font-weight: 800;
    color: #FFFFFF;
    text-align: center;
    margin-bottom: 50px;
    line-height: 1.2;
  }
  .heading span { color: #C8942E; }
  .chat-mockup {
    background: #FFFFFF;
    border-radius: 20px;
    padding: 36px 50px;
    max-width: 1100px;
    width: 100%;
  }
  .chat-label {
    font-size: 22px;
    color: #999;
    margin-bottom: 12px;
  }
  .chat-text {
    font-size: 32px;
    color: #0E1C2F;
    line-height: 1.6;
  }
  .cursor {
    display: inline-block;
    width: 3px;
    height: 36px;
    background: #C8942E;
    margin-left: 4px;
    vertical-align: middle;
    animation: blink 1s step-end infinite;
  }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
  .note {
    font-size: 28px;
    color: #AAAAAA;
    text-align: center;
    margin-top: 36px;
  }
""", """
    <div class="heading">Text starts appearing<br><span>word by word.</span></div>
    <div class="chat-mockup">
      <div class="chat-label">ChatGPT is writing your answer now...</div>
      <div class="chat-text">Here are five simple steps to plan a weekend road trip:<br><br>Step 1: Choose your destination...<span class="cursor"></span></div>
    </div>
    <div class="note">It is writing a response just for you — not pulling up a saved article.</div>
""", "slide06-watch-it-write.html")


# ── SLIDE 07: Is This Useful? ─────────────────────────────────────────────
slide("""
  .ask-label {
    font-size: 32px;
    color: #AAAAAA;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 28px;
  }
  .big-question {
    font-size: 110px;
    font-weight: 900;
    color: #C8942E;
    text-align: center;
    line-height: 1.05;
    margin-bottom: 36px;
  }
  .not-perfect {
    font-size: 36px;
    color: #FFFFFF;
    text-align: center;
    line-height: 1.6;
  }
  .not-perfect span { color: #C8942E; font-weight: 700; }
""", """
    <div class="ask-label">Ask yourself one question</div>
    <div class="big-question">Is this useful?</div>
    <div class="not-perfect">
      Not is it <span>perfect.</span>&nbsp;&nbsp;Not is it exactly right about everything.<br>
      Just — is there something here you can actually use?
    </div>
""", "slide07-is-useful.html")


# ── SLIDE 08: Digital Pioneers Closing ───────────────────────────────────
slide("""
  .closing-top {
    font-size: 38px;
    color: #AAAAAA;
    text-align: center;
    margin-bottom: 30px;
    line-height: 1.6;
    max-width: 1200px;
  }
  .closing-main {
    font-size: 72px;
    font-weight: 900;
    color: #FFFFFF;
    text-align: center;
    line-height: 1.2;
    margin-bottom: 50px;
  }
  .closing-main span { color: #C8942E; }
  .badge {
    background: rgba(200,148,46,0.15);
    border: 3px solid #C8942E;
    border-radius: 50px;
    padding: 20px 60px;
    font-size: 36px;
    color: #C8942E;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .next {
    font-size: 28px;
    color: #888888;
    margin-top: 40px;
    text-align: center;
  }
""", """
    <div class="closing-top">
      You are doing something that most people your age have never done.<br>
      You are using one of the most powerful tools in the world.
    </div>
    <div class="closing-main">That is what<br><span>Digital Pioneers</span> do.</div>
    <div class="badge">&#11088; Digital Pioneer</div>
    <div class="next">Next: Lesson 2c — The Follow-Up. It changes everything.</div>
""", "slide08-closing.html")


print("\nAll 8 slides built successfully.")
print(f"Location: {OUTPUT_DIR}")
print("\nTo use in HeyGen:")
print("1. Open each HTML file in Chrome")
print("2. Screenshot at 1920x1080 (or use browser full-page capture)")
print("3. Upload as background image in each HeyGen scene")
