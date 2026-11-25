#!/usr/bin/env python3
"""Build static GitHub Pages bundle from videolezioni/.

Generates:
- Clean per-chapter URLs (<lesson-id>/index.html) with dedicated Open Graph & Twitter meta tags
- High-contrast 1200x630 PNG preview covers (og/home.png and og/<lesson-id>.png)
- Optional parallel WAV -> MP3 audio transcoding via ffmpeg (updates built lesson.json paths)
- Styled 404.html with smart path recovery, favicon.svg, sitemap.xml, robots.txt, and .nojekyll
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import html
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Any
from urllib.parse import urlparse

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:  # pragma: no cover
    Image = None
    ImageDraw = None
    ImageFilter = None
    ImageFont = None


SCRIPT_DIR = Path(__file__).resolve().parent
VIDEOLEZIONI_DIR = SCRIPT_DIR.parent
REPO_ROOT = VIDEOLEZIONI_DIR.parent
DEFAULT_BASE_URL = "https://example.github.io/lectio-course/"


def load_course_config() -> dict[str, Any]:
    cfg_path = REPO_ROOT / "course.config.json"
    if cfg_path.is_file():
        try:
            return json.loads(cfg_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}

OG_WIDTH = 1200
OG_HEIGHT = 630

PART_ACCENTS: dict[str, tuple[str, str]] = {
    "frontmatter": ("#1D4ED8", "#15803D"),
    "parte-1": ("#1D4ED8", "#0F766E"),
    "parte-2": ("#1D4ED8", "#C82829"),
    "parte-3": ("#B45309", "#C82829"),
    "parte-4": ("#C82829", "#1D4ED8"),
    "parte-5": ("#15803D", "#1D4ED8"),
    "parte-6": ("#6D28D9", "#1D4ED8"),
}


def normalize_base_url(raw: str) -> str:
    url = raw.strip()
    if not url.endswith("/"):
        url += "/"
    return url


def format_hours(total_min: int) -> str:
    if not total_min:
        return "0 min"
    h = total_min // 60
    m = total_min % 60
    return f"{h}h {m:02d}m" if h > 0 else f"{m} min"


def hex_to_rgba(color: str, alpha: int = 255) -> tuple[int, int, int, int]:
    c = color.lstrip("#")
    return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), alpha)


def find_font(bold: bool = False) -> str | None:
    if bold:
        candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
            "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf",
            "C:/Windows/Fonts/segoeuib.ttf",
            "C:/Windows/Fonts/arialbd.ttf",
            "C:/Windows/Fonts/calibrib.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        ]
    else:
        candidates = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
            "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
            "C:/Windows/Fonts/segoeui.ttf",
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/calibri.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
        ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    return None


def load_font(size: int, bold: bool = False) -> Any:
    path = find_font(bold=bold)
    if path:
        return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def wrap_text(draw: Any, text: str, font: Any, max_width: int, max_lines: int) -> list[str]:
    words = text.split()
    if not words:
        return []
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        bbox = draw.textbbox((0, 0), candidate, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = word
            if len(lines) == max_lines:
                break
    if len(lines) < max_lines:
        lines.append(current)
    elif len(lines) == max_lines and current:
        # Check if we dropped remaining words
        reconstructed = " ".join(lines)
        if reconstructed != text:
            last = lines[-1]
            while last and draw.textbbox((0, 0), last + "…", font=font)[2] > max_width:
                last = last.rsplit(" ", 1)[0] if " " in last else last[:-1]
            lines[-1] = (last.rstrip(".,;: ") + "…") if last else "…"
    return lines


def draw_pill(
    draw: Any,
    x: int,
    y: int,
    text: str,
    font: Any,
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int],
    text_color: tuple[int, int, int, int],
    pad_x: int = 18,
    pad_y: int = 9,
) -> int:
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    w = tw + pad_x * 2
    h = th + pad_y * 2
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=fill, outline=outline, width=2)
    draw.text((x + pad_x, y + pad_y - bbox[1]), text, font=font, fill=text_color)
    return x + w


def blend_hex(fg: str, bg: str, ratio: float) -> tuple[int, int, int, int]:
    fr, fg_c, fb, _ = hex_to_rgba(fg)
    br, bg_c, bb, _ = hex_to_rgba(bg)
    return (
        int(fr * ratio + br * (1.0 - ratio)),
        int(fg_c * ratio + bg_c * (1.0 - ratio)),
        int(fb * ratio + bb * (1.0 - ratio)),
        255,
    )


def load_lia_frame(frame_idx: int = 5, size: int = 240, spritesheet_rel: str = "assets/lia-spritesheet.png") -> Any | None:
    """Load a crisp frame of the configured tutor avatar from videolezioni/<spritesheet_rel>."""
    rel = str(spritesheet_rel or "assets/lia-spritesheet.png").lstrip("/\\")
    sheet_path = VIDEOLEZIONI_DIR / rel
    if not sheet_path.is_file():
        sheet_path = VIDEOLEZIONI_DIR / "assets" / "lia-spritesheet.png"
    if not sheet_path.is_file():
        return None
    sheet = Image.open(sheet_path).convert("RGBA")
    fw = sheet.width // 6
    idx = max(0, min(5, frame_idx))
    frame = sheet.crop((idx * fw, 0, (idx + 1) * fw, sheet.height))
    return frame.resize((size, size), Image.NEAREST)


def load_circle_photo(filename: str, size: int = 48, border_color: str = "#CECEC7") -> Any | None:
    """Load a circular portrait from videolezioni/assets/ with crisp border."""
    p = VIDEOLEZIONI_DIR / "assets" / filename
    if not p.is_file():
        return None
    im = Image.open(p).convert("RGBA").resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse([1, 1, size - 2, size - 2], fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    ImageDraw.Draw(out, "RGBA").ellipse([1, 1, size - 2, size - 2], outline=hex_to_rgba(border_color, 255), width=2)
    return out


def _draw_dashed_line(d: Any, p1: tuple[float, float], p2: tuple[float, float], fill: Any, width: int = 4, dash: int = 16, gap: int = 12) -> None:
    x1, y1 = p1
    x2, y2 = p2
    dist = math.hypot(x2 - x1, y2 - y1)
    if dist < 1:
        return
    ux, uy = (x2 - x1) / dist, (y2 - y1) / dist
    cur = 0.0
    while cur < dist:
        nxt = min(dist, cur + dash)
        d.line([(x1 + ux * cur, y1 + uy * cur), (x1 + ux * nxt, y1 + uy * nxt)], fill=fill, width=width)
        cur = nxt + gap


def _draw_arrow(d: Any, p1: tuple[float, float], p2: tuple[float, float], fill: Any, width: int = 5, head: int = 18) -> None:
    x1, y1 = p1
    x2, y2 = p2
    d.line([(x1, y1), (x2, y2)], fill=fill, width=width)
    ang = math.atan2(y2 - y1, x2 - x1)
    a1 = ang + math.pi * 0.82
    a2 = ang - math.pi * 0.82
    pts = [
        (x2, y2),
        (x2 + head * math.cos(a1), y2 + head * math.sin(a1)),
        (x2 + head * math.cos(a2), y2 + head * math.sin(a2)),
    ]
    d.polygon(pts, fill=fill)


def _draw_axes(d: Any, ox: int, oy: int, w: int, h: int, ink: Any) -> None:
    _draw_arrow(d, (ox, oy), (ox + w, oy), ink, width=4, head=14)
    _draw_arrow(d, (ox, oy), (ox, oy - h), ink, width=4, head=14)


def draw_chapter_visual(chapter: int, width: int = 380, height: int = 350) -> Any:
    """Render a crisp 2x-supersampled topic-specific ASE software-engineering diagram for chapter 0..15."""
    S = 2
    W, H = width * S, height * S
    canvas = Image.new("RGBA", (W, H), hex_to_rgba("#FAFAF7", 255))
    d = ImageDraw.Draw(canvas, "RGBA")

    # Subtle architectural graph-paper grid
    grid_c = hex_to_rgba("#E8E8E1", 170)
    for gx in range(44, W, 44):
        d.line([(gx, 16), (gx, H - 16)], fill=grid_c, width=2)
    for gy in range(44, H, 44):
        d.line([(16, gy), (W - 16, gy)], fill=grid_c, width=2)

    INK = hex_to_rgba("#141413", 255)
    SOFT = hex_to_rgba("#57564F", 220)
    MUTED = hex_to_rgba("#9A9990", 210)
    BLUE = hex_to_rgba("#1D4ED8", 255)
    BLUE_S = blend_hex("#1D4ED8", "#FAFAF7", 0.13)
    RED = hex_to_rgba("#C82829", 255)
    RED_S = blend_hex("#C82829", "#FAFAF7", 0.13)
    GREEN = hex_to_rgba("#15803D", 255)
    GREEN_S = blend_hex("#15803D", "#FAFAF7", 0.14)
    AMBER = hex_to_rgba("#D97706", 255)
    AMBER_S = blend_hex("#D97706", "#FAFAF7", 0.15)
    PURPLE = hex_to_rgba("#6D28D9", 255)
    PURPLE_S = blend_hex("#6D28D9", "#FAFAF7", 0.15)
    WHITE = hex_to_rgba("#FFFFFF", 255)

    f_lbl = load_font(28, bold=True)
    f_sm = load_font(22, bold=False)

    if chapter == 0:
        # 4-Part ASE Roadmap
        pts = [(120, 500), (285, 360), (470, 390), (630, 195)]
        d.line(pts, fill=BLUE, width=7)
        cols = [BLUE, GREEN, AMBER, RED]
        for i, (px, py) in enumerate(pts):
            d.ellipse([px - 36, py - 36, px + 36, py + 36], fill=WHITE, outline=cols[i], width=6)
            lbl = f"P{i + 1}"
            bb = d.textbbox((0, 0), lbl, font=f_lbl)
            d.text((px - (bb[2] - bb[0]) // 2, py - (bb[3] - bb[1]) // 2 - bb[1]), lbl, font=f_lbl, fill=cols[i])
        d.text((76, 84), "Percorso ASE", font=f_lbl, fill=INK)

    elif chapter == 1:
        # Software Products: Stand-alone -> Hybrid -> SaaS shift
        cols_spec = [
            (72, "Stand-alone", "UI + Logic\n+ Data", "Updates", BLUE, BLUE_S, False),
            (286, "Hybrid", "UI + Partial\n+ Data", "Backup + API", AMBER, AMBER_S, True),
            (500, "SaaS", "Browser\n/ App", "Logic + Data\n(Cloud)", GREEN, GREEN_S, True),
        ]
        _draw_dashed_line(d, (55, 360), (705, 360), MUTED, width=3)
        for x0, head, top_t, bot_t, col, bg, bidir in cols_spec:
            d.text((x0 + 18, 96), head, font=f_sm, fill=col)
            d.rounded_rectangle([x0, 145, x0 + 188, 295], radius=18, fill=bg, outline=col, width=5)
            d.multiline_text((x0 + 22, 185), top_t, font=f_sm, fill=INK, spacing=6)
            d.rounded_rectangle([x0, 415, x0 + 188, 555], radius=18, fill=WHITE, outline=col, width=5)
            d.multiline_text((x0 + 22, 455), bot_t, font=f_sm, fill=SOFT, spacing=6)
            mx = x0 + 94
            _draw_arrow(d, (mx, 405), (mx, 305), col, width=5, head=14)
            if bidir:
                _draw_arrow(d, (mx, 315), (mx, 405), col, width=5, head=14)

    elif chapter in (2, 3):
        # Agile Sprint loop & Backlog -> Stories -> Release
        boxes = [(65, 250, 230, 415, "Backlog", AMBER, AMBER_S), (295, 235, 470, 430, "Sprint", BLUE, BLUE_S), (535, 250, 695, 415, "Release", GREEN, GREEN_S)]
        for x0, y0, x1, y1, txt, col, bg in boxes:
            d.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=bg, outline=col, width=6)
            bb = d.textbbox((0, 0), txt, font=f_lbl)
            d.text(((x0 + x1 - (bb[2] - bb[0])) // 2, (y0 + y1 - (bb[3] - bb[1])) // 2 - bb[1]), txt, font=f_lbl, fill=INK)
        _draw_arrow(d, (236, 332), (288, 332), INK, width=6, head=18)
        _draw_arrow(d, (476, 332), (528, 332), INK, width=6, head=18)
        d.line([(615, 425), (615, 535), (382, 535)], fill=BLUE, width=6)
        _draw_arrow(d, (382, 535), (382, 438), BLUE, width=6, head=18)
        d.text((425, 550), "Feedback continuo", font=f_sm, fill=BLUE)

    elif chapter == 4:
        # Layered Software Architecture
        layers = [(130, "Presentation / UI", BLUE, BLUE_S), (275, "Application Logic", AMBER, AMBER_S), (420, "Data & Infrastructure", GREEN, GREEN_S)]
        for y0, lbl, col, bg in layers:
            d.rounded_rectangle([120, y0, 640, y0 + 102], radius=20, fill=bg, outline=col, width=6)
            bb = d.textbbox((0, 0), lbl, font=f_lbl)
            d.text(((760 - (bb[2] - bb[0])) // 2, y0 + 34), lbl, font=f_lbl, fill=INK)
        _draw_arrow(d, (380, 232), (380, 272), INK, width=5, head=14)
        _draw_arrow(d, (380, 377), (380, 417), INK, width=5, head=14)

    elif chapter in (5, 6, 10):
        # Containers / Cloud / Kubernetes Pods
        d.rounded_rectangle([90, 120, 670, 560], radius=26, fill=BLUE_S, outline=BLUE, width=6)
        d.text((130, 148), "Cluster / Cloud Runtime", font=f_lbl, fill=BLUE)
        for idx, (x0, col, bg, lbl) in enumerate([
            (130, GREEN, GREEN_S, "Pod A"),
            (315, AMBER, AMBER_S, "Pod B"),
            (500, PURPLE, PURPLE_S, "Pod C"),
        ]):
            d.rounded_rectangle([x0, 235, x0 + 140, 415], radius=18, fill=bg, outline=col, width=5)
            bb = d.textbbox((0, 0), lbl, font=f_sm)
            d.text((x0 + (140 - (bb[2] - bb[0])) // 2, 310), lbl, font=f_sm, fill=INK)
        d.rounded_rectangle([130, 455, 640, 528], radius=14, fill=WHITE, outline=SOFT, width=4)
        d.text((240, 476), "Container Engine & Network", font=f_sm, fill=SOFT)

    elif chapter in (7, 8, 9):
        # Microservices Mesh / Splitting Monolith
        nodes = [(380, 175, "API GW", BLUE, BLUE_S), (185, 365, "Svc A", GREEN, GREEN_S), (380, 365, "Svc B", AMBER, AMBER_S), (575, 365, "Svc C", PURPLE, PURPLE_S)]
        for nx, ny, _, col, _ in nodes[1:]:
            d.line([(380, 225), (nx, ny - 48)], fill=SOFT, width=5)
        for nx, ny, lbl, col, bg in nodes:
            d.rounded_rectangle([nx - 72, ny - 48, nx + 72, ny + 48], radius=20, fill=bg, outline=col, width=6)
            bb = d.textbbox((0, 0), lbl, font=f_sm)
            d.text((nx - (bb[2] - bb[0]) // 2, ny - 14), lbl, font=f_sm, fill=INK)
            if ny > 250:
                d.ellipse([nx - 34, ny + 86, nx + 34, ny + 132], fill=WHITE, outline=col, width=4)
                d.line([(nx, ny + 48), (nx, ny + 86)], fill=col, width=4)
                d.text((nx - 16, ny + 96), "DB", font=f_sm, fill=col)

    elif chapter in (11, 12):
        # Testing & DevOps CI/CD Pipeline
        stages = [(75, "Build", BLUE, BLUE_S), (245, "Test", GREEN, GREEN_S), (415, "Deploy", AMBER, AMBER_S), (585, "Monitor", PURPLE, PURPLE_S)]
        for i, (x0, lbl, col, bg) in enumerate(stages):
            d.rounded_rectangle([x0, 270, x0 + 130, 410], radius=20, fill=bg, outline=col, width=6)
            bb = d.textbbox((0, 0), lbl, font=f_sm)
            d.text((x0 + (130 - (bb[2] - bb[0])) // 2, 326), lbl, font=f_sm, fill=INK)
            if i < len(stages) - 1:
                _draw_arrow(d, (x0 + 136, 340), (stages[i + 1][0] - 6, 340), INK, width=5, head=14)
        d.text((235, 165), "CI / CD & Testing", font=f_lbl, fill=INK)

    elif chapter in (13, 14):
        # Security & Zero-Trust Shield
        shield = [(380, 125), (565, 200), (535, 435), (380, 565), (225, 435), (195, 200)]
        d.polygon(shield, fill=RED_S, outline=RED)
        d.line(shield + [shield[0]], fill=RED, width=7)
        d.rounded_rectangle([318, 305, 442, 415], radius=16, fill=WHITE, outline=INK, width=6)
        d.arc([340, 245, 420, 345], start=180, end=0, fill=INK, width=7)
        d.text((235, 585), "TLS · AuthN · AuthZ", font=f_sm, fill=RED)

    else:
        # Chapter 15: Quantum Software Engineering (Qubit Bloch sphere)
        cx, cy, r = 380, 345, 175
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=PURPLE_S, outline=PURPLE, width=6)
        d.ellipse([cx - r, cy - 58, cx + r, cy + 58], outline=PURPLE, width=4)
        _draw_arrow(d, (cx, cy), (cx + 115, cy - 115), AMBER, width=8, head=22)
        d.text((cx - 24, cy - r - 48), "|0>", font=f_lbl, fill=INK)
        d.text((cx - 24, cy + r + 14), "|1>", font=f_lbl, fill=INK)
        d.text((cx + 122, cy - 142), "|ψ>", font=f_lbl, fill=AMBER)

    return canvas.resize((width, height), Image.LANCZOS)


def generate_og_card(
    out_path: Path,
    eyebrow: str,
    part_label: str,
    title: str,
    description: str,
    chips: list[str],
    footer_right: str,
    accent_a: str = "#1D4ED8",
    accent_b: str = "#15803D",
    seed: int = 0,
    chapter: int | None = None,
    is_home: bool = False,
    course_cfg: dict[str, Any] | None = None,
) -> None:
    if Image is None:
        raise RuntimeError("Pillow non installato: installa `pillow` per generare le immagini Open Graph.")

    cfg = course_cfg or {}
    eyebrow_parts = [str(x).strip() for x in cfg.get("eyebrow", []) if str(x).strip()]
    tutor_cfg = cfg.get("tutor_avatar") or {}
    tutor_enabled = tutor_cfg.get("enabled", True) is not False
    tutor_name = str(tutor_cfg.get("name") or "Lia").strip() or "Lia"
    tutor_sheet = str(tutor_cfg.get("spritesheet") or "assets/lia-spritesheet.png").strip()
    author_cfg = cfg.get("author") or {}
    prof_cfg = cfg.get("professor") or {}
    course_title = str(cfg.get("title") or title or "Videolezioni").strip()
    course_subtitle = str(cfg.get("subtitle") or "Videolezioni Interattive").strip()

    # Clean Studio Light canvas (matches website default theme, zero AI slop)
    img = Image.new("RGBA", (OG_WIDTH, OG_HEIGHT), hex_to_rgba("#F6F6F3", 255))

    margin = 34
    card_box = [margin, margin, OG_WIDTH - margin, OG_HEIGHT - margin]

    # Soft realistic card elevation shadow
    shadow = Image.new("RGBA", (OG_WIDTH, OG_HEIGHT), (0, 0, 0, 0))
    ImageDraw.Draw(shadow, "RGBA").rounded_rectangle(
        [margin, margin + 8, OG_WIDTH - margin, OG_HEIGHT - margin + 10],
        radius=26,
        fill=(20, 20, 19, 18),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=16))
    img = Image.alpha_composite(img, shadow)

    # Pure white editorial card surface
    card_layer = Image.new("RGBA", (OG_WIDTH, OG_HEIGHT), (0, 0, 0, 0))
    ImageDraw.Draw(card_layer, "RGBA").rounded_rectangle(
        card_box,
        radius=26,
        fill=hex_to_rgba("#FFFFFF", 255),
        outline=hex_to_rgba("#E5E5E0", 255),
        width=2,
    )
    img = Image.alpha_composite(img, card_layer)
    draw = ImageDraw.Draw(img, "RGBA")

    f_eyebrow = load_font(21, bold=False)
    f_kicker = load_font(22, bold=True)
    f_title = load_font(54 if is_home else 50, bold=True)
    f_desc = load_font(24, bold=False)
    f_chip = load_font(19, bold=True)
    f_foot = load_font(18, bold=False)
    f_name = load_font(21, bold=True)
    f_sub = load_font(17, bold=False)

    left = margin + 46
    top = margin + 38
    right_edge = OG_WIDTH - margin - 46

    # Clean editorial eyebrow from course.config.json
    if is_home:
        eyebrow_line = "  /  ".join(eyebrow_parts) if eyebrow_parts else course_subtitle
    else:
        chap_eyebrow = list(eyebrow_parts[:2])
        if part_label:
            chap_eyebrow.append(part_label)
        eyebrow_line = "  /  ".join(chap_eyebrow) if chap_eyebrow else course_title
    draw.text((left, top), eyebrow_line, font=f_eyebrow, fill=hex_to_rgba("#73736D", 255))

    # Right-hand visual panel (Lia hero showcase on Home if enabled, geometric visual on chapters)
    panel_w, panel_h = 376, 344
    panel_x = right_edge - panel_w
    panel_y = top + 46
    panel_box = [panel_x, panel_y, panel_x + panel_w, panel_y + panel_h]

    if is_home and tutor_enabled:
        # Warm Studio stage featuring Lia front-and-center
        draw.rounded_rectangle(
            panel_box,
            radius=22,
            fill=hex_to_rgba("#F6F6F3", 255),
            outline=hex_to_rgba("#E5E5E0", 255),
            width=2,
        )
        lia_big = load_lia_frame(frame_idx=5, size=310, spritesheet_rel=tutor_sheet)
        if lia_big is not None:
            lx = panel_x + (panel_w - 310) // 2
            ly = panel_y + panel_h - 306
            # Clip Lia cleanly inside rounded panel
            pmask = Image.new("L", (OG_WIDTH, OG_HEIGHT), 0)
            ImageDraw.Draw(pmask).rounded_rectangle(panel_box, radius=22, fill=255)
            lia_layer = Image.new("RGBA", (OG_WIDTH, OG_HEIGHT), (0, 0, 0, 0))
            lia_layer.paste(lia_big, (lx, ly), lia_big)
            clipped_lia = Image.new("RGBA", (OG_WIDTH, OG_HEIGHT), (0, 0, 0, 0))
            clipped_lia.paste(lia_layer, (0, 0), pmask)
            img = Image.alpha_composite(img, clipped_lia)
            draw = ImageDraw.Draw(img, "RGBA")
    else:
        vis_idx = (chapter if chapter is not None else 0) % 20
        visual = draw_chapter_visual(vis_idx, width=panel_w, height=panel_h)
        pmask = Image.new("L", (panel_w, panel_h), 0)
        ImageDraw.Draw(pmask).rounded_rectangle([0, 0, panel_w - 1, panel_h - 1], radius=20, fill=255)
        img.paste(visual, (panel_x, panel_y), pmask)
        draw = ImageDraw.Draw(img, "RGBA")
        draw.rounded_rectangle(panel_box, radius=20, fill=None, outline=hex_to_rgba("#E5E5E0", 255), width=2)

    # Left column typography
    max_text_w = panel_x - left - 36
    y = top + 52

    if eyebrow and not is_home:
        draw.text((left, y), eyebrow.upper(), font=f_kicker, fill=hex_to_rgba(accent_a, 255))
        y += 38

    title_lines = wrap_text(draw, title, f_title, max_text_w, max_lines=2)
    if len(title_lines) == 2 and len(title) > 36:
        f_title = load_font(44, bold=True)
        title_lines = wrap_text(draw, title, f_title, max_text_w, max_lines=2)
    line_step = 62 if f_title.size >= 50 else 54
    for line in title_lines:
        draw.text((left, y), line, font=f_title, fill=hex_to_rgba("#141413", 255))
        y += line_step

    if is_home:
        author_name = str(author_cfg.get("name") or "").strip()
        author_prefix = str(author_cfg.get("label_prefix") or "Appunti di").strip()
        author_gh = str(author_cfg.get("github_username") or "").strip()
        author_avatar = str(author_cfg.get("avatar") or "").strip().replace("assets/", "")
        prof_name = str(prof_cfg.get("name") or "").strip()
        prof_role = str(prof_cfg.get("role") or "Docente del corso").strip()
        prof_avatar = str(prof_cfg.get("avatar") or "").strip().replace("assets/", "")

        if author_name:
            y += 18
            author_img = load_circle_photo(author_avatar, size=52) if author_avatar else None
            if author_img is not None:
                img.alpha_composite(author_img, (left, y))
            tx = left + (66 if author_img else 0)
            author_line = f"{author_prefix} {author_name}".strip() if author_prefix else author_name
            draw.text((tx, y + 3), author_line, font=f_name, fill=hex_to_rgba("#141413", 255))
            sub_line = f"github.com/{author_gh}" if author_gh else course_subtitle
            draw.text((tx, y + 29), sub_line, font=f_sub, fill=hex_to_rgba("#73736D", 255))
            y += 66
        elif description:
            y += 12
            for line in wrap_text(draw, description, f_desc, max_text_w, max_lines=2):
                draw.text((left, y), line, font=f_desc, fill=hex_to_rgba("#464642", 255))
                y += 35

        if prof_name:
            y += 6
            prof_img = load_circle_photo(prof_avatar, size=52) if prof_avatar else None
            if prof_img is not None:
                img.alpha_composite(prof_img, (left, y))
            tx = left + (66 if prof_img else 0)
            draw.text((tx, y + 3), prof_name, font=f_name, fill=hex_to_rgba("#141413", 255))
            draw.text((tx, y + 29), prof_role, font=f_sub, fill=hex_to_rgba("#73736D", 255))
            y += 68

        # Clean summary pills below credits
        y += 16
        cx_chip = left
        for chip in chips:
            cx_chip = draw_pill(
                draw,
                cx_chip,
                y,
                chip,
                f_chip,
                fill=hex_to_rgba("#EFEFEC", 255),
                outline=hex_to_rgba("#E5E5E0", 255),
                text_color=hex_to_rgba("#141413", 255),
                pad_x=16,
                pad_y=8,
            ) + 12
    else:
        y += 12
        desc_lines = wrap_text(draw, description, f_desc, max_text_w, max_lines=3)
        for line in desc_lines:
            draw.text((left, y), line, font=f_desc, fill=hex_to_rgba("#464642", 255))
            y += 35

        # Subtle duration/topic chips
        y += 18
        cx_chip = left
        for chip in chips:
            cx_chip = draw_pill(
                draw,
                cx_chip,
                y,
                chip,
                f_chip,
                fill=hex_to_rgba("#EFEFEC", 255),
                outline=hex_to_rgba("#E5E5E0", 255),
                text_color=hex_to_rgba("#141413", 255),
                pad_x=15,
                pad_y=7,
            ) + 10

    # Bottom hairline divider + course/tutor signature & domain
    div_y = OG_HEIGHT - margin - 94
    draw.line([(left, div_y), (right_edge, div_y)], fill=hex_to_rgba("#E5E5E0", 255), width=2)

    foot_y = div_y + 18
    if not is_home:
        credit_parts = []
        if author_cfg.get("name"):
            ap = str(author_cfg.get("label_prefix") or "Appunti di").strip()
            credit_parts.append(f"{ap} {author_cfg['name']}".strip())
        if prof_cfg.get("name"):
            credit_parts.append(str(prof_cfg["name"]).strip())
        credit_line = " · ".join(credit_parts) if credit_parts else course_title

        lia_mini = load_lia_frame(frame_idx=5, size=56, spritesheet_rel=tutor_sheet) if tutor_enabled else None
        if lia_mini is not None:
            badge_box = [left, foot_y, left + 56, foot_y + 56]
            draw.rounded_rectangle(badge_box, radius=14, fill=hex_to_rgba("#F6F6F3", 255), outline=hex_to_rgba("#E5E5E0", 255), width=2)
            bmask = Image.new("L", (56, 56), 0)
            ImageDraw.Draw(bmask).rounded_rectangle([1, 1, 54, 54], radius=13, fill=255)
            img.paste(lia_mini, (left, foot_y), bmask)
            draw = ImageDraw.Draw(img, "RGBA")
            draw.text((left + 70, foot_y + 6), f"{tutor_name} · Videolezione guidata", font=load_font(19, bold=True), fill=hex_to_rgba("#141413", 255))
            draw.text((left + 70, foot_y + 31), credit_line, font=f_sub, fill=hex_to_rgba("#73736D", 255))
        else:
            draw.text((left, foot_y + 6), course_title, font=load_font(19, bold=True), fill=hex_to_rgba("#141413", 255))
            draw.text((left, foot_y + 31), credit_line, font=f_sub, fill=hex_to_rgba("#73736D", 255))
    else:
        draw.text((left, foot_y + 16), "Diagrammi vettoriali, schemi e voce guidata", font=f_foot, fill=hex_to_rgba("#73736D", 255))

    f_foot_r = load_font(16, bold=False) if len(footer_right) > 36 else f_foot
    fbbox = draw.textbbox((0, 0), footer_right, font=f_foot_r)
    fw = fbbox[2] - fbbox[0]
    draw.text(
        (right_edge - fw, foot_y + (31 if not is_home else 17)),
        footer_right,
        font=f_foot_r,
        fill=hex_to_rgba("#73736D", 255),
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(out_path, format="PNG", optimize=True)


def write_favicon(out_dir: Path) -> None:
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="16" fill="#090D16"/>
  <rect x="2" y="2" width="60" height="60" rx="14" fill="none" stroke="#38BDF8" stroke-opacity="0.45" stroke-width="2.5"/>
  <g stroke="#38BDF8" stroke-width="2.4" stroke-linecap="round" opacity="0.75">
    <line x1="17" y1="22" x2="32" y2="32"/>
    <line x1="17" y1="42" x2="32" y2="32"/>
    <line x1="32" y1="32" x2="47" y2="20"/>
    <line x1="32" y1="32" x2="47" y2="44"/>
  </g>
  <circle cx="17" cy="22" r="5" fill="#090D16" stroke="#38BDF8" stroke-width="3"/>
  <circle cx="17" cy="42" r="5" fill="#090D16" stroke="#38BDF8" stroke-width="3"/>
  <circle cx="32" cy="32" r="6" fill="#38BDF8"/>
  <circle cx="47" cy="20" r="5" fill="#090D16" stroke="#FB7185" stroke-width="3"/>
  <circle cx="47" cy="44" r="5" fill="#090D16" stroke="#34D399" stroke-width="3"/>
</svg>
"""
    (out_dir / "favicon.svg").write_text(svg, encoding="utf-8")


def build_meta_tags(
    *,
    title: str,
    description: str,
    canonical_url: str,
    og_image_url: str,
    og_image_alt: str,
    og_type: str,
    root_prefix: str,
    site_name: str = "Lectio",
    locale: str = "it_IT",
) -> str:
    e = lambda s: html.escape(s, quote=True)
    return "\n".join(
        [
            f'  <meta name="description" content="{e(description)}" />',
            f'  <link rel="canonical" href="{e(canonical_url)}" />',
            f'  <meta property="og:type" content="{e(og_type)}" />',
            f'  <meta property="og:locale" content="{e(locale)}" />',
            f'  <meta property="og:site_name" content="{e(site_name)}" />',
            f'  <meta property="og:title" content="{e(title)}" />',
            f'  <meta property="og:description" content="{e(description)}" />',
            f'  <meta property="og:url" content="{e(canonical_url)}" />',
            f'  <meta property="og:image" content="{e(og_image_url)}" />',
            '  <meta property="og:image:type" content="image/png" />',
            f'  <meta property="og:image:width" content="{OG_WIDTH}" />',
            f'  <meta property="og:image:height" content="{OG_HEIGHT}" />',
            f'  <meta property="og:image:alt" content="{e(og_image_alt)}" />',
            '  <meta name="twitter:card" content="summary_large_image" />',
            f'  <meta name="twitter:title" content="{e(title)}" />',
            f'  <meta name="twitter:description" content="{e(description)}" />',
            f'  <meta name="twitter:image" content="{e(og_image_url)}" />',
            f'  <meta name="twitter:image:alt" content="{e(og_image_alt)}" />',
        ]
    )


def transcode_wav_to_mp3(src_wav: Path, dst_mp3: Path, bitrate: str) -> None:
    dst_mp3.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(src_wav),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "24000",
        "-c:a",
        "libmp3lame",
        "-b:a",
        bitrate,
        str(dst_mp3),
    ]
    subprocess.run(cmd, check=True)


def write_404_page(out_dir: Path, base_url: str, ready_ids: list[str], course_title: str = "Lectio") -> None:
    parsed = urlparse(base_url)
    base_path = parsed.path if parsed.path.endswith("/") else parsed.path + "/"
    ready_json = json.dumps(ready_ids)
    page = f"""<!DOCTYPE html>
<html lang="it" data-theme="studio">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pagina non trovata — {html.escape(course_title)}</title>
  <meta name="theme-color" content="#F6F6F3" />
  <link rel="icon" type="image/png" sizes="64x64" href="{base_path}assets/favicon-fabio.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="{base_path}assets/apple-touch-icon.png" />
  <script>
    (function () {{
      var BASE = {json.dumps(base_path)};
      var READY = {ready_json};
      var path = window.location.pathname || "";
      var rel = path.indexOf(BASE) === 0 ? path.slice(BASE.length) : path.replace(/^\\/+/, "");
      rel = rel.replace(/^videolezioni\\/+/, "").replace(/\\/+$/, "").replace(/\\.html$/i, "");
      if (READY.indexOf(rel) !== -1) {{
        window.location.replace(BASE + rel + "/" + window.location.search + window.location.hash);
      }}
    }})();
  </script>
  <style>
    :root {{ color-scheme: light; }}
    body {{
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: #F6F6F3;
      color: #141413;
      font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      padding: 24px;
    }}
    .card {{
      max-width: 520px;
      width: 100%;
      background: #FFFFFF;
      border: 1px solid #E5E5E0;
      border-radius: 20px;
      padding: 36px;
      box-shadow: 0 1px 2px rgba(20, 20, 19, 0.04), 0 16px 40px rgba(20, 20, 19, 0.06);
    }}
    .badge {{
      display: inline-block;
      padding: 5px 12px;
      border-radius: 999px;
      background: rgba(29, 78, 216, 0.08);
      color: #1D4ED8;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.04em;
    }}
    h1 {{ margin: 18px 0 10px; font-size: 28px; letter-spacing: -0.025em; }}
    p {{ margin: 0 0 26px; color: #464642; line-height: 1.55; }}
    a.btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 11px 20px;
      border-radius: 999px;
      background: #141413;
      color: #FFFFFF;
      font-weight: 600;
      text-decoration: none;
    }}
    a.btn:hover {{ background: #1D4ED8; }}
  </style>
</head>
<body>
  <main class="card">
    <span class="badge">ERRORE 404 · {html.escape(course_title.upper())}</span>
    <h1>Lezione o pagina non trovata</h1>
    <p>Il link potrebbe appartenere a un capitolo ancora in preparazione oppure contenere un indirizzo non valido.</p>
    <a class="btn" href="{base_path}">Torna al catalogo del corso</a>
  </main>
</body>
</html>
"""
    (out_dir / "404.html").write_text(page, encoding="utf-8")


def write_seo_files(out_dir: Path, base_url: str, ready_ids: list[str]) -> None:
    urls = [base_url] + [f"{base_url}{lid}/" for lid in ready_ids]
    entries = "\n".join(f"  <url><loc>{html.escape(u)}</loc></url>" for u in urls)
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n"
        "</urlset>\n"
    )
    (out_dir / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {base_url}sitemap.xml\n"
    (out_dir / "robots.txt").write_text(robots, encoding="utf-8")
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")


def _clean_searchable_text(slide_html: str, tts_text: str) -> str:
    """Extract clean plain text from slide HTML (minus SVGs/tags) + spoken narration for Ctrl+K search."""
    no_svg = re.sub(r"<svg\b[\s\S]*?</svg>", " ", slide_html or "", flags=re.IGNORECASE)
    no_tags = re.sub(r"<[^>]+>", " ", no_svg)
    no_tags = html.unescape(no_tags)
    no_tex_cmds = re.sub(
        r"\\(?:htmlId\{[^}]*\}|text|mathrm|mathbf|mathcal|mathbb|operatorname|boxed|underbrace|frac|sum|prod|int|sqrt|left|right|big|Big|quad|qquad|dots|cdots|ldots|cdot|times|to|rightarrow|leftrightarrow|le|ge|neq|approx|sim|in|subset|setminus|cup|cap|bar|hat|tilde|norm|abs|Var|Bias|Cov|Remp)",
        " ",
        no_tags,
    )
    no_tex_braces = re.sub(r"[\\{}\[\]()$^_~]+", " ", no_tex_cmds)
    clean_tts = re.sub(r"\[[^\]]+\]", " ", tts_text or "")
    combined = f"{no_tex_braces} {clean_tts}"
    return re.sub(r"\s+", " ", combined).strip()


def build_search_index(ready_lessons: list[dict[str, Any]], lessons_root: Path) -> dict[str, Any]:
    """Build compact static global search index across all ready chapters and scenes."""
    index_lessons: list[dict[str, Any]] = []
    index_scenes: list[dict[str, Any]] = []
    for l_idx, lesson in enumerate(ready_lessons):
        lid = lesson["id"]
        index_lessons.append({
            "id": lid,
            "ch": int(lesson.get("chapter", 0)),
            "t": lesson.get("title", ""),
        })
        src_json = lessons_root / lid / "lesson.json"
        if not src_json.is_file():
            continue
        ldata = json.loads(src_json.read_text(encoding="utf-8"))
        for s_idx, scene in enumerate(ldata.get("scenes", [])):
            index_scenes.append({
                "l": l_idx,
                "i": s_idx,
                "sec": scene.get("section", ""),
                "t": scene.get("title", ""),
                "txt": _clean_searchable_text(scene.get("slide_html", ""), scene.get("tts_text", "")),
            })
    return {"lessons": index_lessons, "scenes": index_scenes}


def build_site(
    out_dir: Path,
    base_url: str,
    transcode_mp3: bool,
    require_ffmpeg: bool,
    bitrate: str,
) -> None:
    manifest_path = VIDEOLEZIONI_DIR / "lessons" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    parts_by_id = {p["id"]: p for p in manifest.get("parts", [])}
    lessons = manifest.get("lessons", [])
    ready_lessons = [l for l in lessons if l.get("status") == "ready"]
    ready_ids = [l["id"] for l in ready_lessons]

    ffmpeg_bin = shutil.which("ffmpeg")
    use_mp3 = transcode_mp3 and bool(ffmpeg_bin)
    if transcode_mp3 and not ffmpeg_bin:
        if require_ffmpeg:
            raise RuntimeError("ffmpeg richiesto (--require-ffmpeg) ma non trovato nel PATH.")
        print("[warn] ffmpeg non trovato nel PATH: mantengo i file .wav originali.")

    # Clean output directory
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Copy core static assets
    course_cfg = load_course_config()
    cfg_src = REPO_ROOT / "course.config.json"
    if cfg_src.is_file():
        shutil.copy2(cfg_src, out_dir / "course.config.json")
    shutil.copytree(VIDEOLEZIONI_DIR / "css", out_dir / "css")
    shutil.copytree(VIDEOLEZIONI_DIR / "js", out_dir / "js")
    if (VIDEOLEZIONI_DIR / "assets").is_dir():
        shutil.copytree(VIDEOLEZIONI_DIR / "assets", out_dir / "assets")
    (out_dir / "lessons").mkdir(parents=True, exist_ok=True)
    shutil.copy2(manifest_path, out_dir / "lessons" / "manifest.json")
    search_index = build_search_index(ready_lessons, VIDEOLEZIONI_DIR / "lessons")
    search_index_str = json.dumps(search_index, ensure_ascii=False, separators=(",", ":"))
    (VIDEOLEZIONI_DIR / "lessons" / "search-index.json").write_text(search_index_str, encoding="utf-8")
    (out_dir / "lessons" / "search-index.json").write_text(search_index_str, encoding="utf-8")
    write_favicon(out_dir)

    # Copy lesson JSONs, subtitles, and collect audio tasks
    transcode_jobs: list[tuple[Path, Path]] = []
    copied_audio = 0

    for lesson in ready_lessons:
        lid = lesson["id"]
        src_lesson_dir = VIDEOLEZIONI_DIR / "lessons" / lid
        dst_lesson_dir = out_dir / "lessons" / lid
        dst_lesson_dir.mkdir(parents=True, exist_ok=True)

        # Subtitles
        src_subs = src_lesson_dir / "subtitles"
        if src_subs.is_dir():
            dst_subs = dst_lesson_dir / "subtitles"
            dst_subs.mkdir(parents=True, exist_ok=True)
            for sub_file in src_subs.glob("*.json"):
                shutil.copy2(sub_file, dst_subs / sub_file.name)

        # Audio (top-level files only; skips .batches/, .chunks/, .gitkeep)
        src_audio_dir = src_lesson_dir / "audio"
        dst_audio_dir = dst_lesson_dir / "audio"
        converted_rel: set[str] = set()
        if src_audio_dir.is_dir():
            dst_audio_dir.mkdir(parents=True, exist_ok=True)
            for af in sorted(src_audio_dir.iterdir()):
                if not af.is_file() or af.name.startswith("."):
                    continue
                ext = af.suffix.lower()
                if ext == ".wav" and use_mp3:
                    dst_mp3 = dst_audio_dir / f"{af.stem}.mp3"
                    transcode_jobs.append((af, dst_mp3))
                    converted_rel.add(f"audio/{af.name}")
                elif ext in {".wav", ".mp3", ".ogg", ".m4a"}:
                    shutil.copy2(af, dst_audio_dir / af.name)
                    copied_audio += 1

        # Lesson JSON (rewrite audio_file to .mp3 when transcoded)
        src_json = src_lesson_dir / "lesson.json"
        lesson_data = json.loads(src_json.read_text(encoding="utf-8"))
        if use_mp3:
            for scene in lesson_data.get("scenes", []):
                af_rel = scene.get("audio_file", "")
                if af_rel in converted_rel and af_rel.lower().endswith(".wav"):
                    scene["audio_file"] = af_rel[:-4] + ".mp3"
        (dst_lesson_dir / "lesson.json").write_text(
            json.dumps(lesson_data, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

    if transcode_jobs:
        workers = min(8, max(2, os.cpu_count() or 4))
        print(f"Transcodifica {len(transcode_jobs)} file WAV -> MP3 ({bitrate}) con {workers} worker...")
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futs = [pool.submit(transcode_wav_to_mp3, src, dst, bitrate) for src, dst in transcode_jobs]
            for fut in as_completed(futs):
                fut.result()

    # Generate Open Graph cover images
    parsed_base = urlparse(base_url)
    display_host = (parsed_base.netloc + parsed_base.path).rstrip("/")
    og_dir = out_dir / "og"
    og_dir.mkdir(parents=True, exist_ok=True)

    total_scenes = sum(l.get("scenes_count", 0) for l in ready_lessons)
    total_mins = sum(l.get("duration_min") or l.get("estimated_minutes") or 0 for l in ready_lessons)
    course = manifest.get("course", {})
    course_title = str(course_cfg.get("title") or course.get("title") or "Il Mio Corso").strip()
    course_subtitle = str(course_cfg.get("subtitle") or "Videolezioni Interattive").strip()
    course_lang = str(course_cfg.get("language") or "it").strip().lower()
    default_theme = str(course_cfg.get("default_theme") or "studio").strip()
    og_locale = "en_US" if course_lang.startswith("en") else "it_IT"
    eyebrow_parts = [str(x).strip() for x in course_cfg.get("eyebrow", []) if str(x).strip()]
    site_name = " · ".join([course_title] + eyebrow_parts[:1]) if eyebrow_parts else course_title

    home_title = f"{course_title} — {course_subtitle}"
    desc_extras = []
    if course_cfg.get("professor", {}).get("name"):
        desc_extras.append(str(course_cfg["professor"]["name"]).strip())
    if course_cfg.get("author", {}).get("name"):
        ap = str(course_cfg["author"].get("label_prefix") or "Appunti di").strip()
        desc_extras.append(f"{ap} {course_cfg['author']['name']}".strip())
    extras_str = f" ({', '.join(desc_extras)})" if desc_extras else ""
    home_desc = (
        f"{course_title}{extras_str}: {format_hours(total_mins)} di videolezioni interattive "
        f"con formule KaTeX, grafici vettoriali e voce sincronizzata."
    )
    generate_og_card(
        og_dir / "home.png",
        eyebrow="",
        part_label=eyebrow_parts[-1] if eyebrow_parts else "",
        title=course_title,
        description=course_subtitle,
        chips=[
            f"{format_hours(total_mins)} di lezioni",
            f"{len(ready_lessons)} {'capitolo' if len(ready_lessons) == 1 else 'capitoli'}",
        ],
        footer_right=display_host,
        accent_a="#1D4ED8",
        accent_b="#15803D",
        seed=0,
        is_home=True,
        course_cfg=course_cfg,
    )

    # Render Home index.html
    index_tpl = (VIDEOLEZIONI_DIR / "index.html").read_text(encoding="utf-8")
    index_html = index_tpl.replace(
        '<html lang="it" data-theme="studio">',
        f'<html lang="{html.escape(course_lang, quote=True)}" data-theme="{html.escape(default_theme, quote=True)}" data-clean-urls="true">',
        1,
    )
    index_html = index_html.replace(
        "<title>Videolezioni Interattive — Lectio</title>",
        f"<title>{html.escape(home_title)}</title>\n"
        + build_meta_tags(
            title=home_title,
            description=home_desc,
            canonical_url=base_url,
            og_image_url=f"{base_url}og/home.png",
            og_image_alt=f"{course_title} — {course_subtitle}",
            og_type="website",
            root_prefix="",
            site_name=site_name,
            locale=og_locale,
        ),
        1,
    )
    first_ready = ready_ids[0] if ready_ids else "00-demo"
    index_html = index_html.replace(
        'href="lesson.html?id=00-demo"',
        f'href="{first_ready}/"',
    )
    (out_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Render legacy fallback lesson.html
    lesson_tpl = (VIDEOLEZIONI_DIR / "lesson.html").read_text(encoding="utf-8")
    fallback_lesson_html = lesson_tpl.replace(
        '<html lang="it" data-theme="studio">',
        f'<html lang="{html.escape(course_lang, quote=True)}" data-theme="{html.escape(default_theme, quote=True)}">',
        1,
    ).replace(
        "<title>Videolezione — Lectio</title>",
        f"<title>Videolezione — {html.escape(course_title)}</title>\n"
        + build_meta_tags(
            title=home_title,
            description=home_desc,
            canonical_url=base_url,
            og_image_url=f"{base_url}og/home.png",
            og_image_alt=f"Videolezione — {course_title}",
            og_type="website",
            root_prefix="",
            site_name=site_name,
            locale=og_locale,
        ),
        1,
    )
    (out_dir / "lesson.html").write_text(fallback_lesson_html, encoding="utf-8")

    # Render per-chapter clean pages + per-chapter OG cards
    for lesson in ready_lessons:
        lid = lesson["id"]
        chap_num = int(lesson.get("chapter", 0))
        chap_str = f"{chap_num:02d}"
        part_info = parts_by_id.get(lesson.get("part", ""), {})
        part_badge = f"{part_info.get('label', '')} · {part_info.get('title', '')}".strip(" ·")
        accent_a, accent_b = PART_ACCENTS.get(lesson.get("part", ""), ("#38BDF8", "#FB7185"))
        scenes_count = int(lesson.get("scenes_count", 0))
        dur_min = int(lesson.get("duration_min") or lesson.get("estimated_minutes") or 10)
        summary = lesson.get("summary", "").strip()

        page_title = f"Cap. {chap_str} · {lesson['title']} — {course_title}"
        og_title = f"Cap. {chap_str} · {lesson['title']}"
        og_desc = f"{summary} (~{dur_min} min · {course_title})"
        canonical = f"{base_url}{lid}/"
        og_img_url = f"{base_url}og/{lid}.png"

        generate_og_card(
            og_dir / f"{lid}.png",
            eyebrow=f"CAPITOLO {chap_str}",
            part_label=part_badge,
            title=lesson["title"],
            description=summary,
            chips=[
                f"~{dur_min} min",
                "Voce + Schemi",
            ],
            footer_right=display_host,
            accent_a=accent_a,
            accent_b=accent_b,
            seed=chap_num + 1,
            chapter=chap_num,
            is_home=False,
            course_cfg=course_cfg,
        )

        chap_html = lesson_tpl.replace(
            '<html lang="it" data-theme="studio">',
            f'<html lang="{html.escape(course_lang, quote=True)}" data-theme="{html.escape(default_theme, quote=True)}" data-lesson-id="{html.escape(lid, quote=True)}" data-root="..">',
            1,
        )
        chap_html = chap_html.replace(
            "<title>Videolezione — Lectio</title>",
            f"<title>{html.escape(page_title)}</title>\n"
            + build_meta_tags(
                title=og_title,
                description=og_desc,
                canonical_url=canonical,
                og_image_url=og_img_url,
                og_image_alt=f"{og_title} — {course_title}",
                og_type="article",
                root_prefix="../",
                site_name=site_name,
                locale=og_locale,
            ),
            1,
        )
        chap_html = (
            chap_html.replace('href="css/styles.css"', 'href="../css/styles.css"')
            .replace('href="css/themes.css"', 'href="../css/themes.css"')
            .replace('href="assets/favicon-fabio.png"', 'href="../assets/favicon-fabio.png"')
            .replace('href="assets/favicon-lia.png"', 'href="../assets/favicon-lia.png"')
            .replace('href="assets/apple-touch-icon.png"', 'href="../assets/apple-touch-icon.png"')
            .replace('href="index.html"', 'href="../"')
            .replace('src="js/player.js"', 'src="../js/player.js"')
            .replace(
                '<span id="lesson-chap-tag" class="lesson-chap-tag">Cap. --</span>',
                f'<span id="lesson-chap-tag" class="lesson-chap-tag">Cap. {chap_str}</span>',
            )
            .replace(
                '<span id="lesson-title-bar" class="lesson-title-bar">Caricamento...</span>',
                f'<span id="lesson-title-bar" class="lesson-title-bar">{html.escape(lesson["title"])}</span>',
            )
        )

        chap_dir = out_dir / lid
        chap_dir.mkdir(parents=True, exist_ok=True)
        (chap_dir / "index.html").write_text(chap_html, encoding="utf-8")

    write_404_page(out_dir, base_url, ready_ids, course_title=course_title)
    write_seo_files(out_dir, base_url, ready_ids)

    # Size summary
    total_bytes = sum(p.stat().st_size for p in out_dir.rglob("*") if p.is_file())
    print(
        f"Build completata in {out_dir}: "
        f"{len(ready_lessons)} pagine capitolo + home + {len(ready_lessons) + 1} cover OG PNG "
        f"({total_bytes / (1024 * 1024):.1f} MB, audio: "
        f"{'MP3 ' + bitrate if use_mp3 else f'WAV ({copied_audio} file)'})."
    )


def main() -> int:
    cfg = load_course_config()
    cfg_pages_url = str((cfg.get("github") or {}).get("pages_url") or "").strip()
    default_url = cfg_pages_url or DEFAULT_BASE_URL
    parser = argparse.ArgumentParser(description="Prepara il pacchetto statico GitHub Pages da videolezioni/.")
    parser.add_argument(
        "--base-url",
        default=default_url,
        help=f"URL pubblico finale del sito (default: {default_url})",
    )
    parser.add_argument(
        "--out",
        default=str(VIDEOLEZIONI_DIR / "dist"),
        help="Cartella di output (default: videolezioni/dist)",
    )
    parser.add_argument(
        "--transcode-mp3",
        action="store_true",
        help="Converte gli audio .wav in .mp3 via ffmpeg e aggiorna i lesson.json di output.",
    )
    parser.add_argument(
        "--require-ffmpeg",
        action="store_true",
        help="Fallisce se --transcode-mp3 è attivo ma ffmpeg non è presente.",
    )
    parser.add_argument(
        "--bitrate",
        default="80k",
        help="Bitrate MP3 mono 24 kHz per la voce (default: 80k).",
    )
    args = parser.parse_args()

    build_site(
        out_dir=Path(args.out).resolve(),
        base_url=normalize_base_url(args.base_url),
        transcode_mp3=args.transcode_mp3,
        require_ffmpeg=args.require_ffmpeg,
        bitrate=args.bitrate,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
