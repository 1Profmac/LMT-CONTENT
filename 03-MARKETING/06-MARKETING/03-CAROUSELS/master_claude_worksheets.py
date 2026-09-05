from PIL import Image, ImageDraw, ImageFont
import os

W, H = 2550, 3300  # 8.5x11 at 300dpi
DARK_BG = (27, 42, 74)
GOLD = (200, 164, 44)
WHITE = (255, 255, 255)
LIGHT_GRAY = (240, 240, 240)
MED_GRAY = (180, 180, 180)
BLACK = (30, 30, 30)
LINE_COLOR = (160, 160, 160)

def get_font(size, bold=False):
    fp = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
    if os.path.exists(fp):
        return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

font_header = get_font(72, bold=True)
font_subheader = get_font(48, bold=True)
font_section = get_font(40, bold=True)
font_body = get_font(36)
font_body_bold = get_font(36, bold=True)
font_small = get_font(30)
font_tiny = get_font(24)
font_label = get_font(28, bold=True)

def new_worksheet():
    img = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(img)
    # Header bar
    draw.rectangle([0, 0, W, 160], fill=DARK_BG)
    draw.rectangle([0, 160, W, 170], fill=GOLD)
    # Footer
    draw.rectangle([0, H-100, W, H], fill=DARK_BG)
    draw.text((100, H-80), "50+TechBridge  |  How to Keep Your Job Over 50  |  learnmoretechnologies.com", fill=GOLD, font=font_tiny)
    return img, draw

def checkbox(draw, x, y, size=40):
    draw.rectangle([x, y, x+size, y+size], outline=LINE_COLOR, width=3)

def write_line(draw, x, y, width, label=None):
    if label:
        draw.text((x, y-40), label, fill=BLACK, font=font_label)
    draw.line([(x, y+10), (x+width, y+10)], fill=LINE_COLOR, width=2)

def draw_wrapped(draw, text, x, y, max_width, font, fill=BLACK, line_spacing=8):
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0,0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    cy = y
    for line in lines:
        draw.text((x, cy), line, fill=fill, font=font)
        bbox = draw.textbbox((0,0), line, font=font)
        cy += (bbox[3] - bbox[1]) + line_spacing
    return cy

worksheets = []

# ═══════════════════════════════════════════════════
# WORKSHEET 1: My Claude Setup Checklist
# ═══════════════════════════════════════════════════
img, draw = new_worksheet()
draw.text((100, 40), "Worksheet 1: My Claude Setup Checklist", fill=WHITE, font=font_header)
draw.text((100, 210), "Name: ________________________    Date: ____________", fill=BLACK, font=font_body)
draw.text((100, 280), "Track your progress through all 10 steps. Check each box when complete.", fill=MED_GRAY, font=font_small)

steps = [
    ("Download the desktop app from claude.com/download", "Pro account active?  Y / N"),
    ("Open Cowork mode (not Chat)", "Mode I'll use most: ___________"),
    ("Create Claude-Cowork folder with 4 subfolders", "Folder location: _______________"),
    ("Write about-me.md", "See Worksheet 2"),
    ("Write anti-ai-style.md", "See Worksheet 3"),
    ("Build my prompt template", "Saved as text shortcut?  Y / N"),
    ("Try letting Claude prompt me", "How did it go? _______________"),
    ("Install one plugin", "Plugin name: _________________"),
    ("Connect one tool via Connectors", "Tool connected: ______________"),
    ("Build one Project", "Project name: ________________"),
    ("Schedule one automated task", "Task: ________________________"),
]

y = 370
for i, (step, note) in enumerate(steps, 1):
    checkbox(draw, 100, y)
    draw.text((160, y), f"Step {i}: {step}", fill=BLACK, font=font_body)
    draw.text((200, y+55), note, fill=MED_GRAY, font=font_small)
    y += 130
    if i < len(steps):
        draw.line([(100, y-20), (W-200, y-20)], fill=(230,230,230), width=1)

y += 30
draw.rectangle([80, y, W-80, y+250], outline=GOLD, width=3)
draw.text((120, y+20), "NOTES / QUESTIONS FOR NEXT SESSION:", fill=DARK_BG, font=font_label)
for i in range(3):
    write_line(draw, 120, y+90+i*55, W-320)

worksheets.append(img)

# ═══════════════════════════════════════════════════
# WORKSHEET 2: About Me File Builder
# ═══════════════════════════════════════════════════
img, draw = new_worksheet()
draw.text((100, 40), "Worksheet 2: My About Me File Builder", fill=WHITE, font=font_header)
draw.text((100, 210), "Name: ________________________    Date: ____________", fill=BLACK, font=font_body)
draw.text((100, 280), "Fill in each section. This becomes your about-me.md file.", fill=MED_GRAY, font=font_small)

sections = [
    ("WHO I AM", [
        ("My name and title:", 1),
        ("My company/organization:", 1),
        ("What I do in one sentence:", 2),
    ]),
    ("WHAT I'M WORKING ON NOW", [
        ("My top 3 priorities right now:", 3),
    ]),
    ("HOW I COMMUNICATE", [
        ("My writing style (formal, casual, direct, warm):", 1),
        ("Words I use often:", 2),
        ("My audience (who am I writing for?):", 1),
    ]),
    ("WHAT MATTERS TO ME", [
        ("Values that should come through in my work:", 2),
        ("Topics I'm an expert in:", 2),
    ]),
    ("RULES FOR CLAUDE", [
        ("Always do this:", 2),
        ("Never do this:", 2),
    ])
]

y = 360
for section_title, fields in sections:
    draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
    draw.text((100, y+5), section_title, fill=GOLD, font=font_section)
    y += 70
    for label, num_lines in fields:
        draw.text((120, y), label, fill=BLACK, font=font_body)
        y += 50
        for _ in range(num_lines):
            draw.line([(120, y+15), (W-200, y+15)], fill=LINE_COLOR, width=2)
            y += 50
        y += 15
    y += 10

worksheets.append(img)

# ═══════════════════════════════════════════════════
# WORKSHEET 3: Anti-AI Style Guide
# ═══════════════════════════════════════════════════
img, draw = new_worksheet()
draw.text((100, 40), "Worksheet 3: My Anti-AI Style Guide", fill=WHITE, font=font_header)
draw.text((100, 210), "Name: ________________________    Date: ____________", fill=BLACK, font=font_body)
draw.text((100, 280), "List every word and phrase Claude must NEVER use in your content.", fill=MED_GRAY, font=font_small)

y = 380
draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "COMMON AI PHRASES TO BAN (circle any that apply)", fill=GOLD, font=font_section)
y += 70

banned = [
    '"boundaries"     "delve"     "navigate"     "leverage"     "utilize"',
    '"it\'s worth noting"     "in today\'s world"     "at the end of the day"',
    '"game-changer"     "deep dive"     "unpack"     "robust"     "landscape"',
    '"streamline"     "synergy"     "pivot"     "holistic"     "empower"',
    '"cutting-edge"     "paradigm shift"     "move the needle"     "circle back"',
]
for phrase_line in banned:
    draw.text((120, y), phrase_line, fill=BLACK, font=font_body)
    y += 55

y += 30
draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "MY ADDITIONAL BANNED PHRASES", fill=GOLD, font=font_section)
y += 70

for i in range(10):
    draw.text((120, y), f"{i+1}.", fill=MED_GRAY, font=font_body)
    draw.line([(180, y+40), (W-200, y+40)], fill=LINE_COLOR, width=2)
    y += 70

y += 20
draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "PHRASES I WANT CLAUDE TO USE INSTEAD", fill=GOLD, font=font_section)
y += 70

for i in range(6):
    draw.text((120, y), "Instead of:", fill=MED_GRAY, font=font_small)
    draw.line([(320, y+10), (1100, y+10)], fill=LINE_COLOR, width=2)
    draw.text((1150, y), "Say:", fill=MED_GRAY, font=font_small)
    draw.line([(1280, y+10), (W-200, y+10)], fill=LINE_COLOR, width=2)
    y += 60

worksheets.append(img)

# ═══════════════════════════════════════════════════
# WORKSHEET 4: My Plugin & Tools Planner
# ═══════════════════════════════════════════════════
img, draw = new_worksheet()
draw.text((100, 40), "Worksheet 4: My Plugin & Tools Planner", fill=WHITE, font=font_header)
draw.text((100, 210), "Name: ________________________    Date: ____________", fill=BLACK, font=font_body)

y = 310
draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "WHAT DO I SPEND MOST OF MY TIME DOING?", fill=GOLD, font=font_section)
y += 70

tasks = [
    "Writing emails, reports, or content",
    "Analyzing data or spreadsheets",
    "Reviewing documents or contracts",
    "Managing projects or teams",
    "Creating presentations",
    "Customer communication",
]
for task in tasks:
    checkbox(draw, 120, y)
    draw.text((180, y+2), task, fill=BLACK, font=font_body)
    y += 60

draw.text((120, y+10), "Other:", fill=BLACK, font=font_body)
draw.line([(280, y+50), (W-200, y+50)], fill=LINE_COLOR, width=2)
y += 90

draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "MY FIRST PLUGIN (based on answers above)", fill=GOLD, font=font_section)
y += 70
draw.text((120, y), "Plugin category:", fill=BLACK, font=font_body)
draw.line([(500, y+40), (W-200, y+40)], fill=LINE_COLOR, width=2)
y += 80
draw.text((120, y), "Why this one first:", fill=BLACK, font=font_body)
draw.line([(500, y+40), (W-200, y+40)], fill=LINE_COLOR, width=2)
y += 100

draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "MY TOOLS TO CONNECT (Connectors)", fill=GOLD, font=font_section)
y += 70

tools = ["Gmail / Email", "Google Docs / Drive", "Slack", "Notion", "Calendar", "Other: ________"]
for tool in tools:
    checkbox(draw, 120, y)
    draw.text((180, y+2), tool, fill=BLACK, font=font_body)
    y += 55

y += 30
draw.text((120, y), "First connector I'll set up:", fill=BLACK, font=font_body)
draw.line([(700, y+40), (W-200, y+40)], fill=LINE_COLOR, width=2)
y += 80
draw.text((120, y), "What I want Claude to do with it:", fill=BLACK, font=font_body)
y += 50
for _ in range(3):
    draw.line([(120, y+15), (W-200, y+15)], fill=LINE_COLOR, width=2)
    y += 50

worksheets.append(img)

# ═══════════════════════════════════════════════════
# WORKSHEET 5: My First Project Planner
# ═══════════════════════════════════════════════════
img, draw = new_worksheet()
draw.text((100, 40), "Worksheet 5: My First Project Planner", fill=WHITE, font=font_header)
draw.text((100, 210), "Name: ________________________    Date: ____________", fill=BLACK, font=font_body)

y = 310
draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "PROJECT BASICS", fill=GOLD, font=font_section)
y += 70
fields = [
    "Project name:",
    "What does this project produce? (newsletter, report, proposal, etc.):",
    "How often? (weekly, monthly, per client):",
    "Who is the audience?:",
]
for field in fields:
    draw.text((120, y), field, fill=BLACK, font=font_body)
    y += 50
    draw.line([(120, y+10), (W-200, y+10)], fill=LINE_COLOR, width=2)
    y += 50

y += 20
draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "FOLDER STRUCTURE FOR THIS PROJECT", fill=GOLD, font=font_section)
y += 70
draw.text((120, y), "Claude-Cowork/", fill=BLACK, font=font_body_bold)
y += 45
draw.text((180, y), "PROJECTS/", fill=BLACK, font=font_body_bold)
y += 45
draw.text((240, y), "[ Project Name ]/", fill=GOLD, font=font_body_bold)
y += 55
sub_items = ["brief.md  —  What is this project about?",
             "references/  —  Examples, past versions, source material",
             "drafts/  —  Work in progress"]
for item in sub_items:
    draw.text((300, y), item, fill=BLACK, font=font_body)
    y += 50

y += 30
draw.rectangle([80, y, W-80, y+50], fill=DARK_BG)
draw.text((100, y+5), "MY PROJECT BRIEF (draft it here)", fill=GOLD, font=font_section)
y += 70
brief_fields = [
    "Goal of this project:",
    "Key deliverable:",
    "Tone / style:",
    "Must include:",
    "Must avoid:",
    "Success looks like:",
]
for field in brief_fields:
    draw.text((120, y), field, fill=BLACK, font=font_body)
    y += 50
    draw.line([(120, y+10), (W-200, y+10)], fill=LINE_COLOR, width=2)
    y += 50

worksheets.append(img)

# ═══════════════════════════════════════════════════
# WORKSHEET 6: 7-Day Implementation Tracker
# ═══════════════════════════════════════════════════
img, draw = new_worksheet()
draw.text((100, 40), "Worksheet 6: 7-Day Implementation Tracker", fill=WHITE, font=font_header)
draw.text((100, 210), "Name: ________________________    Start Date: ____________", fill=BLACK, font=font_body)
draw.text((100, 280), "Check off each day as you complete it. Bring this to your next consulting session.", fill=MED_GRAY, font=font_small)

days = [
    ("DAY 1", "Steps 1-2", "Download app + learn modes", [
        "Downloaded desktop app",
        "Created Pro account",
        "Opened Cowork mode",
        "Explored the interface for 15 min"
    ]),
    ("DAY 2", "Step 3", "Build folder structure", [
        "Created Claude-Cowork parent folder",
        "Created ABOUT ME subfolder",
        "Created PROJECTS subfolder",
        "Created TEMPLATES subfolder",
        "Created CLAUDE OUTPUTS subfolder"
    ]),
    ("DAY 3", "Step 4", "Write core files", [
        "Completed Worksheet 2 (About Me)",
        "Completed Worksheet 3 (Anti-AI Style)",
        "Typed both files as .md and saved"
    ]),
    ("DAY 4", "Steps 5-6", "Templates + Claude prompting", [
        "Built my prompt template",
        "Ran first task using template",
        "Let Claude prompt me on a task"
    ]),
    ("DAY 5", "Steps 7-8", "Plugin + Connector", [
        "Completed Worksheet 4 (Plugin Planner)",
        "Installed one plugin",
        "Connected one tool via Connectors"
    ]),
    ("DAY 6", "Step 9", "First project", [
        "Completed Worksheet 5 (Project Planner)",
        "Created project folder with brief",
        "Ran first deliverable through project"
    ]),
    ("DAY 7", "Step 10", "Automation", [
        "Scheduled one automated task",
        "Verified it ran successfully",
        "Reviewed output quality"
    ]),
]

y = 370
for day_label, steps_label, desc, checklist in days:
    draw.rectangle([80, y, W-80, y+45], fill=DARK_BG)
    draw.text((100, y+3), f"{day_label}  |  {steps_label}  |  {desc}", fill=GOLD, font=font_section)
    y += 60
    for item in checklist:
        checkbox(draw, 120, y, 32)
        draw.text((170, y-2), item, fill=BLACK, font=font_small)
        y += 45
    y += 25

worksheets.append(img)

# ─── Save all worksheets ───
outdir = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\06-MARKETING\worksheets"
os.makedirs(outdir, exist_ok=True)

names = [
    "WS1_Setup_Checklist",
    "WS2_About_Me_Builder",
    "WS3_Anti_AI_Style_Guide",
    "WS4_Plugin_Tools_Planner",
    "WS5_First_Project_Planner",
    "WS6_7Day_Tracker"
]

for i, (ws, name) in enumerate(zip(worksheets, names)):
    ws.save(os.path.join(outdir, f"{name}.png"), "PNG")

# Combined PDF
pdf_path = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\06-MARKETING\Master_Claude_Worksheets.pdf"
worksheets[0].save(pdf_path, "PDF", save_all=True, append_images=worksheets[1:])
print(f"Worksheets PDF saved: {pdf_path} ({len(worksheets)} pages)")
print(f"Individual worksheets saved to: {outdir}")
