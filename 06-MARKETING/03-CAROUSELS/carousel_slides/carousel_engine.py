"""
LMT Carousel Engine — Reusable LinkedIn carousel generator
Usage: Import and call build_carousel() with slide data, or run a content script that uses this.

Brand: 50+TechBridge / #agentic50
Colors: Navy #1B2A4A, Gold #C8A42C, White, Light #F0F0F0
Size: 1080x1350 (LinkedIn carousel)
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Brand constants
W, H = 1080, 1350
NAVY = (27, 42, 74)
GOLD = (200, 164, 44)
WHITE = (255, 255, 255)
LIGHT = (240, 240, 240)
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

# Font presets — sized for mobile readability
FONT_TITLE = get_font(64, bold=True)
FONT_SUBTITLE = get_font(48, bold=True)
FONT_BODY = get_font(40)
FONT_BODY_BOLD = get_font(40, bold=True)
FONT_SMALL = get_font(32)
FONT_TAG = get_font(28)
FONT_SERIES = get_font(22, bold=True)

def draw_wrapped(draw, text, x, y, max_width, font, fill=WHITE, line_spacing=10):
    """Draw text with word wrapping. Returns y position after text."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
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
        bbox = draw.textbbox((0, 0), line, font=font)
        cy += (bbox[3] - bbox[1]) + line_spacing
    return cy

def gold_bar(draw, y):
    """Draw a horizontal gold accent line."""
    draw.rectangle([60, y, W - 60, y + 4], fill=GOLD)

LOGO_PATH = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\04-ASSETS\logos\lmt-podcast-cover.png"

def _add_logo(img):
    """Add AI AFTER 50+ logo mark to bottom-right of slide."""
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert("RGBA")
        # Crop to top 48% — mic icon + AI AFTER 50+ + The Pioneers Podcast
        logo = logo.crop((0, 0, logo.width, int(logo.height * 0.48)))
        # Scale to 180px wide
        max_w = 180
        ratio = max_w / logo.width
        logo = logo.resize((int(logo.width * ratio), int(logo.height * ratio)), Image.LANCZOS)
        # Position: right side, well above bottom edge (LinkedIn crops bottom)
        x = W - logo.width - 60
        y = H - logo.height - 200
        img.paste(logo, (x, y), logo)

def new_slide(bg=NAVY, series_tag=None, logo=False):
    """Create a new blank slide with optional series tag and logo."""
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)
    if series_tag:
        draw.text((60, 30), series_tag, fill=GOLD, font=FONT_SERIES)
        draw.rectangle([60, 58, W - 60, 62], fill=GOLD)
    if logo:
        _add_logo(img)
    return img, draw

def slide_cover(title_lines, subtitle_lines, series_tag=None):
    """Slide 1: Hook/cover slide. title_lines = list of (text, color) tuples."""
    img, draw = new_slide(series_tag=series_tag, logo=True)
    y = 220
    for text, color in title_lines:
        y = draw_wrapped(draw, text, 100, y, 880, FONT_TITLE, fill=color)
        y += 5
    gold_bar(draw, y + 10)
    y += 50
    for text, color in subtitle_lines:
        y = draw_wrapped(draw, text, 100, y, 880, FONT_BODY, fill=color)
        y += 5
    draw_wrapped(draw, "Brian McKinney | 50+TechBridge", 100, 1150, 880, FONT_SMALL, fill=GOLD)
    draw_wrapped(draw, "#agentic50  #AgeTech  #DigitalInclusion", 100, 1190, 880, FONT_TAG, fill=GOLD)
    return img

def slide_text(headline, body_lines, bg=NAVY, headline_color=GOLD, series_tag=None):
    """Standard text slide with headline + body lines."""
    img, draw = new_slide(bg=bg, series_tag=series_tag)
    text_color = WHITE if bg == NAVY else NAVY
    y = 120
    y = draw_wrapped(draw, headline, 100, y, 880, FONT_TITLE, fill=headline_color)
    gold_bar(draw, y + 10)
    y += 50
    for line in body_lines:
        if line == "":
            y += 20
            continue
        if line.startswith("**"):
            clean = line.strip("*")
            y = draw_wrapped(draw, clean, 100, y, 880, FONT_BODY_BOLD, fill=GOLD if bg == NAVY else NAVY)
        else:
            y = draw_wrapped(draw, line, 100, y, 880, FONT_BODY, fill=text_color)
        y += 8
    return img

def slide_stat(big_number, label, context_lines, series_tag=None):
    """Big stat slide — large number with context."""
    img, draw = new_slide(series_tag=series_tag)
    y = 200
    draw_wrapped(draw, big_number, 100, y, 880, get_font(96, bold=True), fill=GOLD)
    y = 340
    y = draw_wrapped(draw, label, 100, y, 880, FONT_SUBTITLE, fill=WHITE)
    gold_bar(draw, y + 15)
    y += 55
    for line in context_lines:
        if line == "":
            y += 20
            continue
        y = draw_wrapped(draw, line, 100, y, 880, FONT_BODY, fill=WHITE)
        y += 8
    return img

def slide_consulting(services, series_tag=None):
    """Consulting CTA slide — lists service offerings. services = list of (title, description) tuples."""
    img, draw = new_slide(series_tag=series_tag, logo=True)
    draw_wrapped(draw, "Need Help", 100, 140, 880, FONT_TITLE, fill=WHITE)
    draw_wrapped(draw, "Getting Started?", 100, 210, 880, FONT_TITLE, fill=GOLD)
    gold_bar(draw, 290)
    y = 350
    y = draw_wrapped(draw, "50+TechBridge Consulting:", 100, y, 880, FONT_BODY_BOLD, fill=WHITE)
    y += 20
    for title, desc in services:
        y = draw_wrapped(draw, title, 100, y, 880, FONT_BODY_BOLD, fill=GOLD)
        y = draw_wrapped(draw, desc, 100, y + 5, 880, FONT_SMALL, fill=WHITE)
        y += 20
    y += 20
    y = draw_wrapped(draw, "Every session is customized to", 100, y, 880, FONT_BODY, fill=WHITE)
    y = draw_wrapped(draw, "YOUR job. YOUR industry. YOUR goals.", 100, y + 5, 880, FONT_BODY_BOLD, fill=GOLD)
    draw_wrapped(draw, "learnmoretechnologies.com", 100, 1190, 880, FONT_SMALL, fill=GOLD)
    return img

def slide_closing(headline, body_lines, series_tag=None):
    """Closing/inspiration slide — 'The Real Point' style."""
    img, draw = new_slide(series_tag=series_tag, logo=True)
    y = 200
    y = draw_wrapped(draw, headline, 100, y, 880, FONT_TITLE, fill=GOLD)
    gold_bar(draw, y + 10)
    y += 50
    for line in body_lines:
        if line == "":
            y += 20
            continue
        if line.startswith("**"):
            clean = line.strip("*")
            y = draw_wrapped(draw, clean, 100, y, 880, FONT_BODY_BOLD, fill=GOLD)
        elif line.startswith("^^"):
            clean = line.strip("^")
            y = draw_wrapped(draw, clean, 100, y, 880, FONT_BODY_BOLD, fill=WHITE)
        else:
            y = draw_wrapped(draw, line, 100, y, 880, FONT_BODY, fill=WHITE)
        y += 10
    draw_wrapped(draw, "Follow #agentic50", 100, 1150, 880, FONT_SMALL, fill=WHITE)
    draw_wrapped(draw, "learnmoretechnologies.com", 100, 1190, 880, FONT_SMALL, fill=GOLD)
    return img

def slide_cta(headline, body_lines, button_text, url, series_tag=None):
    """CTA slide with gold button."""
    img, draw = new_slide(series_tag=series_tag, logo=True)
    y = 200
    y = draw_wrapped(draw, headline, 100, y, 880, FONT_TITLE, fill=GOLD)
    gold_bar(draw, y + 10)
    y += 50
    for line in body_lines:
        if line == "":
            y += 20
            continue
        y = draw_wrapped(draw, line, 100, y, 880, FONT_BODY, fill=WHITE)
        y += 8
    y += 30
    # Button
    bw, bh = 600, 70
    bx = (W - bw) // 2
    draw.rounded_rectangle([bx, y, bx + bw, y + bh], radius=12, fill=GOLD)
    bbox = draw.textbbox((0, 0), button_text, font=FONT_BODY_BOLD)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((bx + (bw - tw) // 2, y + (bh - th) // 2 - 2), button_text, fill=NAVY, font=FONT_BODY_BOLD)
    y += bh + 20
    draw_wrapped(draw, url, 100, y, 880, FONT_SMALL, fill=LIGHT_GOLD)
    draw_wrapped(draw, "Brian McKinney | 50+TechBridge", 100, 1150, 880, FONT_SMALL, fill=GOLD)
    draw_wrapped(draw, "#agentic50  #AgeTech  #DigitalInclusion", 100, 1190, 880, FONT_TAG, fill=GOLD)
    return img

def build_carousel(slides, name, output_dir=r"C:\Users\Jordyn\Desktop\LMT-CONTENT\06-MARKETING"):
    """Save slides as PDF + individual PNGs."""
    pdf_path = os.path.join(output_dir, f"{name}.pdf")
    slides[0].save(pdf_path, "PDF", save_all=True, append_images=slides[1:])
    print(f"Carousel PDF saved: {pdf_path} ({len(slides)} slides)")

    img_dir = os.path.join(output_dir, f"{name}_slides")
    os.makedirs(img_dir, exist_ok=True)
    for i, slide in enumerate(slides, 1):
        slide.save(os.path.join(img_dir, f"slide_{i:02d}.png"), "PNG")
    print(f"Individual slides saved to: {img_dir}")
    return pdf_path
