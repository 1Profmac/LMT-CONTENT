"""
Generate Agentic50 text logo — matches LMT brand style
Saves as transparent PNG for overlay on carousel slides
"""

from PIL import Image, ImageDraw, ImageFont
import os

def get_font(size, bold=False):
    font_paths = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

GOLD = (200, 164, 44)
WHITE = (255, 255, 255)
NAVY = (27, 42, 74)

# Logo on transparent background for overlay
logo_w, logo_h = 400, 80
img = Image.new("RGBA", (logo_w, logo_h), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

font_agentic = get_font(36, bold=True)
font_50 = get_font(36, bold=True)
font_weekly = get_font(14, bold=True)

# Draw "AGENTIC" in white, "50" in gold
text_agentic = "AGENTIC"
bbox_a = draw.textbbox((0, 0), text_agentic, font=font_agentic)
w_a = bbox_a[2] - bbox_a[0]

draw.text((10, 10), text_agentic, fill=WHITE, font=font_agentic)
draw.text((10 + w_a + 5, 10), "50", fill=GOLD, font=font_50)

# Gold bar underneath
draw.rectangle([10, 55, 250, 58], fill=GOLD)

# "WEEKLY" small text
draw.text((10, 62), "WEEKLY", fill=GOLD, font=font_weekly)

logo_path = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\04-ASSETS\logos\agentic50-logo.png"
img.save(logo_path, "PNG")
print(f"Logo saved: {logo_path}")

# Also save a navy background version for standalone use
img_bg = Image.new("RGBA", (logo_w, logo_h), NAVY + (255,))
img_bg.paste(img, (0, 0), img)
bg_path = r"C:\Users\Jordyn\Desktop\LMT-CONTENT\04-ASSETS\logos\agentic50-logo-navy.png"
img_bg.save(bg_path, "PNG")
print(f"Navy version saved: {bg_path}")
