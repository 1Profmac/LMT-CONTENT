from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1350
DARK_BG = (27, 42, 74)
GOLD = (200, 164, 44)
WHITE = (255, 255, 255)
LIGHT_GOLD = (232, 212, 140)
RED = (204, 51, 51)

def get_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

font_title = get_font(52, bold=True)
font_subtitle = get_font(38, bold=True)
font_body = get_font(32)
font_body_bold = get_font(32, bold=True)
font_small = get_font(26)
font_tag = get_font(24)
font_series = get_font(18, bold=True)

def new_slide():
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    # Series tag
    draw.text((60, 30), "HOW TO KEEP YOUR JOB OVER 50  |  SERIES", fill=GOLD, font=font_series)
    draw.rectangle([60, 58, W-60, 62], fill=GOLD)
    return img, draw

def gold_bar(draw, y):
    draw.rectangle([60, y, W-60, y+4], fill=GOLD)

def step_badge(draw, step_num, y):
    bw, bh = 180, 60
    x = 80
    draw.rounded_rectangle([x, y, x+bw, y+bh], radius=12, fill=GOLD)
    text = f"Step {step_num}"
    f = get_font(28, bold=True)
    bbox = draw.textbbox((0,0), text, font=f)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((x + (bw-tw)//2, y + (bh-th)//2 - 2), text, fill=DARK_BG, font=f)

def draw_wrapped(draw, text, x, y, max_width, font, fill=WHITE, line_spacing=10):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0,0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    cy = y
    for line in lines:
        draw.text((x, cy), line, fill=fill, font=font)
        bbox = draw.textbbox((0,0), line, font=font)
        cy += (bbox[3] - bbox[1]) + line_spacing
    return cy

slides = []

# ─── SLIDE 1: Cover ───
img, draw = new_slide()
draw_wrapped(draw, "How to Master", 100, 220, 880, font_title, fill=WHITE)
draw_wrapped(draw, "Claude", 100, 290, 880, font_title, fill=GOLD)
draw_wrapped(draw, "in One Week", 100, 365, 880, font_title, fill=WHITE)
gold_bar(draw, 440)
draw_wrapped(draw, "A 10-Step Guide for", 100, 500, 880, font_body, fill=WHITE)
draw_wrapped(draw, "Experienced Professionals", 100, 545, 880, font_body, fill=WHITE)
y = 700
draw_wrapped(draw, "The professionals who learn AI", 100, y, 880, font_small, fill=WHITE)
draw_wrapped(draw, "aren't replacing anyone.", 100, y+35, 880, font_small, fill=WHITE)
draw_wrapped(draw, "They're becoming irreplaceable.", 100, y+75, 880, font_body_bold, fill=GOLD)
draw_wrapped(draw, "Brian McKinney | 50+TechBridge", 100, 1150, 880, font_small, fill=GOLD)
draw_wrapped(draw, "#agentic50", 100, 1190, 880, font_tag, fill=GOLD)
slides.append(img)

# ─── SLIDE 2: The Stakes ───
img, draw = new_slide()
draw_wrapped(draw, "The Stakes Are Real", 100, 120, 880, font_title, fill=RED)
gold_bar(draw, 200)
y = 260
y = draw_wrapped(draw, "41% of employers plan to reduce staff due to AI.", 100, y, 880, font_body, fill=WHITE)
y = draw_wrapped(draw, "— World Economic Forum, 2025", 100, y+5, 880, font_small, fill=LIGHT_GOLD)
y += 40
y = draw_wrapped(draw, "The people getting cut aren't the oldest.", 100, y, 880, font_body_bold, fill=WHITE)
y += 10
y = draw_wrapped(draw, "They're the ones who never learned the tools.", 100, y, 880, font_body_bold, fill=GOLD)
y += 40
y = draw_wrapped(draw, "This isn't about age.", 100, y, 880, font_body, fill=WHITE)
y = draw_wrapped(draw, "It's about adaptability.", 100, y+10, 880, font_body_bold, fill=GOLD)
slides.append(img)

# ─── Steps ───
step_data = [
    ("Download the Desktop App", [
        "Go to claude.com/download",
        "Not the website. The actual app.",
        "Cowork only runs inside the desktop app.",
        "Mac or Windows only.",
        "Pro: $20/mo ($17 annually)",
        "",
        "Less than Netflix.",
        "This one makes you money."
    ]),
    ("Know Which Mode to Use", [
        "Chat = Quick questions",
        "Projects = Team deliverables",
        "Cowork = Deep solo work",
        "Code = Developers only",
        "",
        "Cowork is your workhorse.",
        "If you've only used Chat,",
        "you haven't seen Claude yet."
    ]),
    ("Build Your 4 Folders", [
        'Create "Claude-Cowork" with:',
        "",
        "ABOUT ME",
        "   Your identity & writing rules",
        "PROJECTS",
        "   One subfolder per live project",
        "TEMPLATES",
        "   Best past work as structure",
        "CLAUDE OUTPUTS",
        "   Only folder Claude writes to"
    ]),
    ("Write Your 2 Core Files", [
        "Two files replace 50+ prompts:",
        "",
        "about-me.md",
        "   Who you are, what you do,",
        "   what matters right now",
        "",
        "anti-ai-style.md",
        '   Kill "delve," "boundaries,"',
        '   "it\'s worth noting" forever'
    ]),
    ("Stop Writing Prompts", [
        "Build a prompt template.",
        "",
        "It tells Claude to:",
        "  1. Read ABOUT ME first",
        "  2. Write to CLAUDE OUTPUTS only",
        "  3. Name files consistently",
        "",
        "Stop thinking about how",
        "to talk to Claude.",
        "Think about what you need done."
    ]),
    ("Let Claude Prompt YOU", [
        "Flip the script.",
        "",
        "Let Claude ask the questions.",
        "Multi-select. Drag-to-rank.",
        "Click answers in under a minute.",
        "",
        "Claude plans.",
        "You approve.",
        "It executes."
    ]),
    ("Install One Plugin", [
        "Just one. Not the whole store.",
        "",
        "Marketing = content",
        "Data = spreadsheets & dashboards",
        "Legal = contract review",
        "",
        "One plugin. Learn it.",
        "Add another when ready."
    ]),
    ("Connect Your Tools", [
        "Settings > Connectors > Browse > Add",
        "",
        "Claude acts inside YOUR apps:",
        "   Search your Slack",
        "   Pull from Google Docs",
        "   Reference Notion mid-task",
        "",
        "Plugins = you use Claude's tools",
        "Connectors = Claude uses YOUR tools"
    ]),
    ("Build One Project", [
        "Shared workspace.",
        "Shared context.",
        "Consistent outputs.",
        "",
        "Even solo, use it for:",
        "   Weekly newsletter",
        "   Monthly report",
        "   Client onboarding"
    ]),
    ("Schedule Your First Task", [
        "The endgame.",
        "",
        "Set up a task that runs",
        "without you.",
        "",
        "Morning briefing.",
        "Weekly content draft.",
        "Data summary before coffee.",
        "",
        "You wake up to a",
        "finished deliverable."
    ])
]

for i, (title, bullets) in enumerate(step_data, 1):
    img, draw = new_slide()
    step_badge(draw, i, 100)
    draw_wrapped(draw, title, 300, 108, 680, font_subtitle, fill=GOLD)
    gold_bar(draw, 200)
    y = 260
    for line in bullets:
        if line == "":
            y += 20
            continue
        y = draw_wrapped(draw, line, 100, y, 880, font_body, fill=WHITE, line_spacing=8)
        y += 6
    slides.append(img)

# ─── Consulting CTA ───
img, draw = new_slide()
draw_wrapped(draw, "Need Help", 100, 140, 880, font_title, fill=WHITE)
draw_wrapped(draw, "Getting Set Up?", 100, 210, 880, font_title, fill=GOLD)
gold_bar(draw, 290)
y = 350
y = draw_wrapped(draw, "50+TechBridge Consulting:", 100, y, 880, font_body_bold, fill=WHITE)
y += 20
y = draw_wrapped(draw, "1-on-1 Setup Session", 100, y, 880, font_body_bold, fill=GOLD)
y = draw_wrapped(draw, "We build your Claude workspace together", 100, y+5, 880, font_small, fill=WHITE)
y += 20
y = draw_wrapped(draw, "Team Workshop", 100, y, 880, font_body_bold, fill=GOLD)
y = draw_wrapped(draw, "Get your department on Claude in one day", 100, y+5, 880, font_small, fill=WHITE)
y += 20
y = draw_wrapped(draw, "Ongoing Coaching", 100, y, 880, font_body_bold, fill=GOLD)
y = draw_wrapped(draw, "Weekly check-ins as you build AI into your workflow", 100, y+5, 880, font_small, fill=WHITE)
y += 40
y = draw_wrapped(draw, "Every session is customized to", 100, y, 880, font_body, fill=WHITE)
y = draw_wrapped(draw, "YOUR job. YOUR industry. YOUR goals.", 100, y+5, 880, font_body_bold, fill=GOLD)
draw_wrapped(draw, "learnmoretechnologies.com", 100, 1190, 880, font_small, fill=GOLD)
slides.append(img)

# ─── Closing ───
img, draw = new_slide()
draw_wrapped(draw, "The Real Point", 100, 200, 880, font_title, fill=GOLD)
gold_bar(draw, 280)
y = 340
y = draw_wrapped(draw, "You're not too old.", 100, y, 880, font_body_bold, fill=WHITE)
y = draw_wrapped(draw, "You're not too late.", 100, y+10, 880, font_body_bold, fill=WHITE)
y = draw_wrapped(draw, "You're next.", 100, y+10, 880, font_body_bold, fill=GOLD)
y += 50
y = draw_wrapped(draw, "AI works. You just have to build the desk before you sit down at it.", 100, y, 880, font_body, fill=WHITE)
y += 40
y = draw_wrapped(draw, "One week. Ten steps.", 100, y, 880, font_body_bold, fill=GOLD)
y = draw_wrapped(draw, "You'll never go back.", 100, y+10, 880, font_body_bold, fill=GOLD)
y += 50
draw_wrapped(draw, "Follow #agentic50", 100, 1150, 880, font_small, fill=WHITE)
draw_wrapped(draw, "learnmoretechnologies.com", 100, 1190, 880, font_small, fill=GOLD)
slides.append(img)

# Save
outpath = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\06-MARKETING\Master_Claude_Carousel_v2.pdf"
slides[0].save(outpath, "PDF", save_all=True, append_images=slides[1:])
print(f"Carousel PDF saved: {outpath} ({len(slides)} slides)")

img_dir = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\06-MARKETING\carousel_slides_v2"
os.makedirs(img_dir, exist_ok=True)
for i, slide in enumerate(slides, 1):
    slide.save(os.path.join(img_dir, f"slide_{i:02d}.png"), "PNG")
print(f"Individual slides saved to: {img_dir}")
