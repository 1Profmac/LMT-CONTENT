from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1350  # LinkedIn carousel size
DARK_BG = (27, 42, 74)
GOLD = (200, 164, 44)
WHITE = (255, 255, 255)
LIGHT_BG = (240, 240, 240)

# Try to find a good font, fall back to default
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
font_step = get_font(44, bold=True)
font_body = get_font(32)
font_body_bold = get_font(32, bold=True)
font_small = get_font(26)
font_tag = get_font(24)

def new_slide():
    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)
    return img, draw

def gold_bar(draw, y):
    draw.rectangle([60, y, W-60, y+4], fill=GOLD)

def draw_step_badge(draw, step_num, y):
    bw, bh = 180, 60
    x = 80
    draw.rounded_rectangle([x, y, x+bw, y+bh], radius=12, fill=GOLD)
    text = f"Step {step_num}"
    bbox = draw.textbbox((0,0), text, font=get_font(28, bold=True))
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((x + (bw-tw)//2, y + (bh-th)//2 - 2), text, fill=DARK_BG, font=get_font(28, bold=True))

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
gold_bar(draw, 380)
draw_wrapped(draw, "How to Master", 100, 200, 880, font_title, fill=WHITE)
draw_wrapped(draw, "Claude", 100, 270, 880, font_title, fill=GOLD)
draw_wrapped(draw, "in One Week", 100, 345, 880, font_title, fill=WHITE)
gold_bar(draw, 420)
draw_wrapped(draw, "A 10-Step Guide for", 100, 480, 880, font_body, fill=WHITE)
draw_wrapped(draw, "Professionals Over 50", 100, 525, 880, font_body, fill=WHITE)
draw_wrapped(draw, "Brian McKinney | 50+TechBridge", 100, 1150, 880, font_small, fill=GOLD)
draw_wrapped(draw, "#agentic50", 100, 1190, 880, font_tag, fill=GOLD)
slides.append(img)

# ─── SLIDE 2: The Problem ───
img, draw = new_slide()
draw_wrapped(draw, "Most People Use", 100, 120, 880, font_title, fill=WHITE)
draw_wrapped(draw, "Claude Wrong", 100, 190, 880, font_title, fill=GOLD)
gold_bar(draw, 280)
y = 340
y = draw_wrapped(draw, "They type a question.", 100, y, 880, font_body, fill=WHITE)
y = draw_wrapped(draw, "Get a generic answer.", 100, y+10, 880, font_body, fill=WHITE)
y = draw_wrapped(draw, "And wonder what the fuss is about.", 100, y+10, 880, font_body, fill=WHITE)
y += 40
y = draw_wrapped(draw, "Claude isn't a chatbot.", 100, y, 880, font_body_bold, fill=WHITE)
y = draw_wrapped(draw, "It's a digital coworker.", 100, y+10, 880, font_body_bold, fill=GOLD)
y += 30
y = draw_wrapped(draw, "But only if you set it up like one.", 100, y, 880, font_body, fill=WHITE)
slides.append(img)

# ─── Steps data ───
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
        "It executes.",
        "",
        "You're already a decision-maker."
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
    draw_step_badge(draw, i, 100)
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

# ─── CLOSING SLIDE ───
img, draw = new_slide()
draw_wrapped(draw, "The Real Point", 100, 200, 880, font_title, fill=GOLD)
gold_bar(draw, 290)
y = 360
y = draw_wrapped(draw, "AI works.", 100, y, 880, font_body_bold, fill=WHITE)
y += 10
y = draw_wrapped(draw, "You just have to build the desk before you sit down at it.", 100, y, 880, font_body, fill=WHITE)
y += 40
y = draw_wrapped(draw, "One week. Ten steps.", 100, y, 880, font_body_bold, fill=GOLD)
y = draw_wrapped(draw, "You'll never go back.", 100, y+10, 880, font_body_bold, fill=GOLD)
y += 60
y = draw_wrapped(draw, "Follow #agentic50", 100, y, 880, font_small, fill=WHITE)
y = draw_wrapped(draw, "learnmoretechnologies.com", 100, y+10, 880, font_small, fill=GOLD)
slides.append(img)

# Save as PDF (carousel)
outpath = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\06-MARKETING\Master_Claude_Carousel.pdf"
slides[0].save(outpath, "PDF", save_all=True, append_images=slides[1:])
print(f"Carousel PDF saved: {outpath} ({len(slides)} slides)")

# Also save individual images
img_dir = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\06-MARKETING\carousel_slides"
os.makedirs(img_dir, exist_ok=True)
for i, slide in enumerate(slides, 1):
    slide.save(os.path.join(img_dir, f"slide_{i:02d}.png"), "PNG")
print(f"Individual slides saved to: {img_dir}")
