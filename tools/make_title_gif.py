#!/usr/bin/env python3
"""Render the official OMARCHY wordmark as a glyphfx-gradient GIF title.

The official logo (omarchy.org/brand/omarchy-wordmark.svg, pixel-rect SVG) is
rasterized to a bitmap mask. glyphfx's colorshift effect is probed on a solid
line in its native terminal habitat and the captured per-column color sequence
is painted across the logo mask per animation frame, with an "x Jev" tagline
beneath. Output: docs/assets/omarchy-triage.gif.

Usage: python3 tools/make_title_gif.py
"""

import os
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT_GIF = ROOT / "docs" / "assets" / "omarchy-triage.gif"
WORDMARK_SVG = Path(__file__).resolve().parent / "omarchy-wordmark.svg"

EFFECT = "colorshift"
PROBE_W = 54  # probe line width (glyphfx-native habitat)
FRAME_RATE = 24
MAX_FRAMES = 60
TAGLINE = "x Jev"
BG = (0x16, 0x16, 0x1E)
DEFAULT_FG = (0xC0, 0xCA, 0xF5)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
TAG_FONT_SIZE = 46
LOGO_W_PX = 1500  # logo render width; height follows the 4131:950 aspect
PAD_X, PAD_Y, TAG_GAP = 30, 26, 30


# ---------------------------------------------------------------------------
# glyphfx probe: capture the traveling gradient as per-column colors per frame
# ---------------------------------------------------------------------------

def xterm256(idx):
    base = [0, 95, 135, 175, 215, 255]
    pal = [(0, 0, 0), (205, 0, 0), (0, 205, 0), (205, 205, 0),
           (0, 0, 238), (205, 0, 205), (0, 205, 205), (229, 229, 229)]
    for r in base:
        for g in base:
            for b in base:
                pal.append((r, g, b))
    for v in (95, 135, 175, 215, 255):
        pal.append((v // 2,) * 3)
    return pal[idx % 256]


class Grid:
    """Minimal terminal grid: SGR truecolor/256, CUP/CUU/CUF/EL/ED, ESC 7/8."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.cells = [[(" ", None) for _ in range(w)] for _ in range(h)]
        self.row = self.col = 0
        self.fg = None
        self.saved = (0, 0)

    def sgr(self, params):
        if not params:
            params = [0]
        i = 0
        while i < len(params):
            p = params[i] or 0
            if p in (0, 39):
                self.fg = None
            elif p == 38 and i + 2 < len(params):
                if params[i + 1] == 2:
                    self.fg = (params[i + 2], params[i + 3], params[i + 4])
                    i += 4
                elif params[i + 1] == 5:
                    self.fg = xterm256(params[i + 2])
                    i += 2
            i += 1

    def csi(self, private, params, final):
        if private:
            return
        nums = [int(p) if p else 0 for p in params.split(";")] if params else []
        n = nums[0] if nums else 1
        if final == "m":
            self.sgr(nums)
        elif final in "Hf":
            r = nums[0] if nums and nums[0] else 1
            c = nums[1] if len(nums) > 1 and nums[1] else 1
            self.row, self.col = r - 1, c - 1
        elif final == "A":
            self.row = max(0, self.row - max(1, n))
        elif final == "C":
            self.col = min(self.w - 1, self.col + max(1, n))
        elif final == "D":
            self.col = max(0, self.col - max(1, n))
        elif final == "G":
            self.col = max(0, (nums[0] if nums and nums[0] else 1) - 1)
        elif final == "K":
            mode = nums[0] if nums else 0
            if mode == 0:
                for c in range(self.col, self.w):
                    self.cells[self.row][c] = (" ", None)
            elif mode == 2:
                self.cells[self.row] = [(" ", None) for _ in range(self.w)]
        elif final == "J":
            self.cells = [[(" ", None) for _ in range(self.w)] for _ in range(self.h)]
            self.row = self.col = 0

    def snapshot(self):
        return tuple(tuple(row) for row in self.cells)


def parse_snapshots(data: bytes, w: int, h: int):
    """Walk the ANSI stream; snapshot at every cursor-home (frame repaint)."""
    grid = Grid(w, h)
    snaps = [grid.snapshot()]
    i, n = 0, len(data)
    while i < n:
        b = data[i]
        if b == 0x1B and i + 1 < n and data[i + 1] == ord("["):
            j = i + 2
            private = ""
            if j < n and data[j:j + 1] in (b"?", b">", b"=", b"<"):
                private = chr(data[j])
                j += 1
            k = j
            while k < n and not (0x40 <= data[k] <= 0x7E):
                k += 1
            if k >= n:
                break
            final = chr(data[k])
            params = data[j:k].decode("ascii", "replace")
            nums = [int(p) if p else 0 for p in params.split(";")] if params else []
            home = (not private and final == "H" and (not nums or nums[0] <= 1))
            grid.csi(private, params, final)
            if home:
                snaps.append(grid.snapshot())
            i = k + 1
            continue
        if b == 0x1B and i + 1 < n and data[i + 1] in (ord("7"), ord("8")):
            if data[i + 1] == ord("7"):
                grid.saved = (grid.row, grid.col)
            else:
                grid.row, grid.col = grid.saved
                if grid.row == 0 and grid.col == 0:
                    snaps.append(grid.snapshot())
            i += 2
            continue
        if b == 0x0D:
            grid.col = 0
            i += 1
            continue
        if b == 0x0A:
            i += 1
            continue
        length = 4 if b >= 0xF0 else 3 if b >= 0xE0 else 2 if b >= 0xC0 else 1
        ch = data[i:i + length].decode("utf-8", "replace")
        if grid.row < h and grid.col < w:
            grid.cells[grid.row][grid.col] = (ch, grid.fg)
        grid.col += 1
        if grid.col >= w:
            grid.col = 0
            grid.row = min(h - 1, grid.row + 1)
        i += length
    return snaps


def probe_gradient():
    """glyphfx on a solid line -> list of per-frame column colors (len PROBE_W)."""
    os.environ.setdefault("TERM", "xterm-256color")
    cap = subprocess.run(
        ["glyphfx", "--canvas-width", str(PROBE_W), "--canvas-height", "1",
         "--frame-rate", str(FRAME_RATE), "--no-restore-cursor",
         EFFECT, "--no-loop", "--cycles", "1"],
        input=("M" * PROBE_W).encode(), capture_output=True, timeout=120,
    )
    if cap.returncode != 0 or len(cap.stdout) < 500:
        sys.exit(f"glyphfx failed rc={cap.returncode}: {cap.stderr[:300]}")
    frames = []
    seen = set()
    for snap in parse_snapshots(cap.stdout, PROBE_W, 1):
        key = hash(snap)
        if key in seen:
            continue
        seen.add(key)
        frames.append([fg for _, fg in snap[0]])
    blank = lambda row: all(fg is None for fg in row)
    while frames and blank(frames[0]):
        frames.pop(0)
    while frames and blank(frames[-1]):
        frames.pop()
    return frames


# ---------------------------------------------------------------------------
# Wordmark mask + frame composition
# ---------------------------------------------------------------------------

def logo_mask():
    subprocess.run(
        ["rsvg-convert", "-w", str(LOGO_W_PX), "-o", "/tmp/wordmark.png", str(WORDMARK_SVG)],
        check=True,
    )
    im = Image.open("/tmp/wordmark.png").convert("RGBA")
    alpha = np.asarray(im)[:, :, 3]
    return alpha > 32  # HxW bool mask of the wordmark


def compose(frames):
    mask = logo_mask()
    mh, mw = mask.shape
    tag_font = ImageFont.truetype(FONT_PATH, TAG_FONT_SIZE)
    tag_box = tag_font.getbbox(TAGLINE)
    tag_w = tag_box[2] - tag_box[0]
    W = max(mw, tag_w) + 2 * PAD_X
    H = PAD_Y + mh + TAG_GAP + TAG_FONT_SIZE + PAD_Y
    ox = (W - mw) // 2
    out = []
    for col_colors in frames:
        # logo: paint the glyphfx gradient across the mask, sampled per column
        color_cols = np.zeros((mw, 3), dtype=np.uint8)
        for c in range(mw):
            fg = col_colors[int(c * PROBE_W / mw) % PROBE_W]
            color_cols[c] = fg if fg is not None else DEFAULT_FG
        img = Image.new("RGB", (W, H), BG)
        arr = np.asarray(img).copy()
        ys, xs = np.nonzero(mask)
        arr[ys + PAD_Y, xs + ox] = color_cols[xs]
        img = Image.fromarray(arr)
        # tagline: centered under the logo, probe's mid color
        d = ImageDraw.Draw(img)
        mid = col_colors[PROBE_W // 2] or DEFAULT_FG
        d.text(((W - tag_w) // 2 - tag_box[0], PAD_Y + mh + TAG_GAP),
               TAGLINE, font=tag_font, fill=tuple(mid))
        out.append(img)
    while len(out) > 8 and out[-1].tobytes() == out[-2].tobytes():
        out.pop()
    if len(out) > MAX_FRAMES:
        step = len(out) / MAX_FRAMES
        out = [out[int(i * step)] for i in range(MAX_FRAMES)]
    return out


def main():
    frames = probe_gradient()
    print(f"probed gradient frames: {len(frames)}")
    imgs = compose(frames)
    OUT_GIF.parent.mkdir(parents=True, exist_ok=True)
    imgs[0].save(
        OUT_GIF, save_all=True, append_images=imgs[1:],
        duration=int(1000 / FRAME_RATE), loop=0, optimize=True,
    )
    print(f"frames kept: {len(imgs)} | size: {imgs[0].width}x{imgs[0].height} | "
          f"file: {OUT_GIF.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
