#!/usr/bin/env python3
"""Compose a 1024x1024 newspaper front page (entry.png) from hero.png.

Fresh build for news-image-20261125. All headlines verified against live
news reports dated 25 November 2026.
"""
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
W, H = 1024, 1024
MARGIN = 36
INK = (18, 18, 18)
GREY = (90, 90, 90)
RULE = (30, 30, 30)
ACCENT = (150, 20, 20)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_wrapped(draw, xy, text, fnt, max_w, fill=INK, spacing=4):
    """Draw text wrapped to max_w pixels; return y after last line."""
    x, y = xy
    # wrap by measuring words with the font
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def text_height(draw, text, fnt, max_w, spacing=4):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return len(lines) * (fnt.size + spacing)


def main():
    page = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(page)
    inner = W - 2 * MARGIN  # 952

    # ---------- masthead ----------
    mast = font(SERIF_B, 74)
    title = "THE DAILY GLOBE"
    tw = d.textlength(title, font=mast)
    d.text(((W - tw) / 2, 18), title, font=mast, fill=INK)

    date_f = font(SANS, 19)
    date_line = "Wednesday 25 November 2026  ·  World News in One Page  ·  Price: Free"
    dw = d.textlength(date_line, font=date_f)
    d.text(((W - dw) / 2, 108), date_line, font=date_f, fill=GREY)

    d.line([(MARGIN, 142), (W - MARGIN, 142)], fill=RULE, width=3)
    d.line([(MARGIN, 148), (W - MARGIN, 148)], fill=RULE, width=1)

    # ---------- hero ----------
    hero = Image.open(BASE / "hero.png").convert("RGB")
    hero_w, hero_h = inner, 300
    # centre-crop to target aspect
    src_w, src_h = hero.size
    target = hero_w / hero_h
    if src_w / src_h > target:
        new_w = int(src_h * target)
        x0 = (src_w - new_w) // 2
        hero = hero.crop((x0, 0, x0 + new_w, src_h))
    else:
        new_h = int(src_w / target)
        y0 = (src_h - new_h) // 2
        hero = hero.crop((0, y0, src_w, y0 + new_h))
    hero = hero.resize((hero_w, hero_h), Image.LANCZOS)
    page.paste(hero, (MARGIN, 158))
    cap_f = font(SANS, 15)
    d.text((MARGIN, 462), "Nvidia headquarters, Santa Clara, at dusk. The chipmaker's shares soared 31% on Monday.",
           font=cap_f, fill=GREY)

    # ---------- lead story ----------
    y = 490
    lead_h = font(SERIF_B, 36)
    lead = "Huang apologises at first all-hands as Nvidia comeback rally fades"
    y = draw_wrapped(d, (MARGIN, y), lead, lead_h, inner, spacing=2)
    y += 2
    deck_f = font(SERIF, 19)
    deck = ("Reinstated chief Jensen Huang tells staff he made \u201csome terrible mistakes\u201d "
            "and is in therapy, 11 days after resigning amid a \u2018spy\u2019 row \u2014 after "
            "President Trump intervened and the board restored him on Monday. Shares regained "
            "roughly $900 billion in value; he testifies before Congress in early December.")
    y = draw_wrapped(d, (MARGIN, y), deck, deck_f, inner, spacing=3)

    d.line([(MARGIN, y + 8), (W - MARGIN, y + 8)], fill=RULE, width=1)
    y += 18

    # ---------- two secondary columns ----------
    col_w = (inner - 24) // 2
    head_f = font(SANS_B, 19)
    body_f = font(SERIF, 15)
    stories = [
        ("CIA AND SPY CHIEFS HIT BY BREACH",
         "The CIA and the Office of the Director of National Intelligence suffered a "
         "breach of some unclassified information, reported on 24 November."),
        ("CHINA PROBE SHOCKS; HUAWEI GUILTY",
         "Beijing opens a shock corruption probe into a Politburo member; a US jury "
         "finds Huawei guilty of trade-secret theft and bank fraud."),
        ("NATO ANSWERS SATELLITE WARNING",
         "NATO responds to reports Russia may launch a nuclear-armed satellite, with "
         "Moscow said to be planning a satellite-destroying launch within weeks."),
        ("UKRAINE SEA-DRONE FALLOUT GROWS",
         "A senior Libyan official wants Zelensky on a terrorism watchlist over strikes "
         "off Libya; Ukraine says its sea drones sank a Russian warship off Benghazi."),
    ]
    left_y, right_y = y, y
    for i, (head, body) in enumerate(stories):
        x = MARGIN if i % 2 == 0 else MARGIN + col_w + 24
        cy = left_y if i % 2 == 0 else right_y
        cy = draw_wrapped(d, (x, cy), head, head_f, col_w, fill=ACCENT, spacing=2)
        cy = draw_wrapped(d, (x, cy + 2), body, body_f, col_w, spacing=2)
        cy += 12
        if i % 2 == 0:
            left_y = cy
        else:
            right_y = cy
    y = max(left_y, right_y)

    # ---------- IN BRIEF band ----------
    d.rectangle([MARGIN, y, W - MARGIN, y + 2], fill=RULE)
    y += 10
    brief_head = font(SANS_B, 17)
    d.text((MARGIN, y), "IN BRIEF", font=brief_head, fill=ACCENT)
    y += 26
    brief_f = font(SANS, 14)
    briefs = [
        "Hamas security chief killed in an Israeli air strike on Gaza City; floods swamp tens of thousands in Gaza.",
        "Saudi Arabia condemns a \u2018terrorist attack\u2019 after the Riyadh PIF skyscraper was hit twice in a week.",
        "Trump awards Rudy Giuliani the Medal of Freedom and outlines a Cuba plan.",
        "Over 400,000 workers strike across Germany; storms and a radar issue at Chicago O\u2019Hare threaten Thanksgiving travel.",
        "Senegal gets the AFCON title back after a CAS ruling; UK police arrest two men after a break-in at Prince William\u2019s Norfolk home.",
    ]
    for item in briefs:
        y = draw_wrapped(d, (MARGIN + 14, y), "\u2022  " + item, brief_f, inner - 14, spacing=1)
        y += 3
    print(f"briefs end at y={y}, footer rule at {H - 44}")
    assert y <= H - 50, f"layout overflow: briefs end at {y}"

    # ---------- footer ----------
    foot_f = font(SANS, 14)
    foot = "All headlines checked against reports dated 25 November 2026.  ·  THE DAILY GLOBE  ·  Page 1"
    fw = d.textlength(foot, font=foot_f)
    d.line([(MARGIN, H - 44), (W - MARGIN, H - 44)], fill=RULE, width=1)
    d.text(((W - fw) / 2, H - 36), foot, font=foot_f, fill=GREY)

    out = BASE / "entry.png"
    page.save(out, "PNG", optimize=True)
    print(f"wrote {out} {page.size}")


if __name__ == "__main__":
    main()
