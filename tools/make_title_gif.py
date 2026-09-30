#!/usr/bin/env python3
"""Render "OMARCHY TRIAGE x Jev" as a GIF title using glyphfx.

glyphfx (native binary) animates in the terminal via ANSI; this script captures
its stdout, parses the frame stream (SGR truecolor + cursor ops), and rasterizes
each frame with Pillow into docs/assets/omarchy-triage.gif.

Usage: python3 tools/make_title_gif.py
"""

import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT_GIF = ROOT / "docs" / "assets" / "omarchy-triage.gif"

TEXT = "OMARCHY TRIAGE x JEV"
EFFECT = "colorshift"
CANVAS_W = len(TEXT) + 6
CANVAS_H = 4
FRAME_RATE = 24
MAX_FRAMES = 260
BG = (0x16, 0x16, 0x1E)
DEFAULT_FG = (0xC0, 0xCA, 0xF5)

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
FONT_SIZE = 72

# xterm 256-color palette (indices 16..255) for 38;5;n fallback
def xterm_palette():
    base = [0, 95, 135, 175, 215, 255]
    pal = [(0, 0, 0), (205, 0, 0), (0, 205, 0), (205, 205, 0), (0, 0, 238), (205, 0, 205), (0, 205, 205), (229, 229, 229)]
    for r in base:
        for g in base:
            for b in base:
                pal.append((r, g, b))
    for v in (95, 135, 175, 215, 255):
        pal.append((v // 2,) * 3)
    return pal

PALETTE = xterm_palette()


class Grid:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.reset()

    def reset(self):
        self.cells = [[(" ", None, None) for _ in range(self.w)] for _ in range(self.h)]
        self.row = self.col = 0
        self.fg = None
        self.bg = None
        self.saved = (0, 0)

    def put(self, ch):
        if self.row < self.h and self.col < self.w:
            self.cells[self.row][self.col] = (ch, self.fg, self.bg)
        self.col += 1

    def sgr(self, params):
        if not params:
            params = [0]
        i = 0
        while i < len(params):
            p = params[i] or 0
            if p == 0:
                self.fg = self.bg = None
            elif p == 39:
                self.fg = None
            elif p == 49:
                self.bg = None
            elif p in (38, 48):
                if i + 1 < len(params) and params[i + 1] == 2:
                    r, g, b = params[i + 2 : i + 5]
                    color = (r, g, b)
                    i += 4
                elif i + 1 < len(params) and params[i + 1] == 5:
                    color = PALETTE[params[i + 2] % 256]
                    i += 2
                else:
                    color = None
                if color is not None:
                    if p == 38:
                        self.fg = color
                    else:
                        self.bg = color
            i += 1

    def csi(self, private, params, final):
        nums = [int(p) if p else 0 for p in params.split(";")] if params else []
        n = nums[0] if nums else 1
        if private:
            return
        if final == "m":
            self.sgr(nums)
        elif final in "Hf":
            r = nums[0] if nums and nums[0] else 1
            c = nums[1] if len(nums) > 1 and nums[1] else 1
            self.row, self.col = r - 1, c - 1
        elif final == "A":
            self.row = max(0, self.row - max(1, n))
        elif final == "B":
            self.row = min(self.h - 1, self.row + max(1, n))
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
                    self.cells[self.row][c] = (" ", None, None)
            elif mode == 2:
                self.cells[self.row] = [(" ", None, None) for _ in range(self.w)]
        elif final == "J":
            self.reset()
        elif final == "d":
            self.row = max(0, (nums[0] if nums and nums[0] else 1) - 1)

    def snapshot(self):
        return tuple(tuple(row) for row in self.cells)


def parse_frames(data: bytes, w: int, h: int):
    grid = Grid(w, h)
    frames = []
    i, n = 0, len(data)

    def emit():
        frames.append(grid.snapshot())

    emit()  # initial blank
    while i < n:
        b = data[i]
        if b == 0x1B:
            if i + 1 >= n:
                break
            nxt = data[i + 1]
            if nxt == ord("["):
                j = i + 2
                private = ""
                if j < n and data[j:j+1] in (b"?", b">", b"=", b"<"):
                    private = chr(data[j]); j += 1
                k = j
                while k < n and not (0x40 <= data[k] <= 0x7E):
                    k += 1
                if k >= n:
                    break
                final = chr(data[k])
                params = data[j:k].decode("ascii", "replace")
                if final in "78":  # DECSC/DECRC arrive as ESC 7 (no bracket) — handled below
                    pass
                grid.csi(private, params, final)
                i = k + 1
                continue
            elif nxt in (ord("7"), ord("8")):
                if nxt == ord("7"):
                    grid.saved = (grid.row, grid.col)
                else:
                    grid.row, grid.col = grid.saved
                i += 2
                continue
            elif nxt == ord("]"):  # OSC — skip to BEL or ST
                j = i + 2
                while j < n and data[j] != 0x07 and not (data[j:j+2] == b"\x1b\\"):
                    j += 1
                i = j + (2 if data[j:j+2] == b"\x1b\\" else 1)
                continue
            elif nxt in (ord("M"), ord("D")):
                grid.row = max(0, grid.row - 1)
                i += 2
                continue
            elif nxt in (ord("E"),):
                grid.row = min(h - 1, grid.row + 1); grid.col = 0
                i += 2
                continue
            else:
                i += 2
                continue
        if b == 0x0D:
            grid.col = 0
            i += 1
            continue
        if b == 0x0A:
            grid.row = min(h - 1, grid.row + 1)
            i += 1
            continue
        # printable — decode one UTF-8 char
        length = 1
        if b >= 0xF0: length = 4
        elif b >= 0xE0: length = 3
        elif b >= 0xC0: length = 2
        ch = data[i : i + length].decode("utf-8", "replace")
        grid.put(ch)
        i += length
        # frame boundary heuristic is unnecessary: glyphfx repaints via cursor
        # homing + full-line redraws; we snapshot on every cursor-home instead.
        if grid.col >= w:
            grid.col = 0
            grid.row = min(h - 1, grid.row + 1)
    # Snapshot strategy: capture screen state at every frame delimiter seen in the
    # stream. Simpler robust approach: re-walk and snapshot after each ESC[4A-like
    # homing sequence. Implemented via callback in csi through a wrapper below.
    return frames


def parse_frames_with_snapshots(data: bytes, w: int, h: int):
    """Same parser, but snapshots at every cursor-home (frame repaint)."""
    grid = Grid(w, h)
    frames = [grid.snapshot()]
    i, n = 0, len(data)
    while i < n:
        b = data[i]
        if b == 0x1B and i + 1 < n and data[i + 1] == ord("["):
            j = i + 2
            private = ""
            if j < n and data[j:j+1] in (b"?", b">", b"=", b"<"):
                private = chr(data[j]); j += 1
            k = j
            while k < n and not (0x40 <= data[k] <= 0x7E):
                k += 1
            if k >= n:
                break
            final = chr(data[k])
            params = data[j:k].decode("ascii", "replace")
            nums = [int(p) if p else 0 for p in params.split(";")] if params else []
            # homing = move to row 1 (ESC[1H / ESC[H) or CUU reaching row 0
            home = (not private and final == "H" and (not nums or nums[0] <= 1))
            grid.csi(private, params, final)
            if home or (grid.row == 0 and grid.col == 0 and final == "A"):
                frames.append(grid.snapshot())
            i = k + 1
            continue
        if b == 0x1B and i + 1 < n and data[i + 1] in (ord("7"), ord("8")):
            if data[i + 1] == ord("7"):
                grid.saved = (grid.row, grid.col)
            else:
                grid.row, grid.col = grid.saved
                if grid.row == 0 and grid.col == 0:
                    frames.append(grid.snapshot())
            i += 2
            continue
        # reuse simple char handling
        if b == 0x0D:
            grid.col = 0; i += 1; continue
        if b == 0x0A:
            grid.row = min(h - 1, grid.row + 1); i += 1; continue
        length = 4 if b >= 0xF0 else 3 if b >= 0xE0 else 2 if b >= 0xC0 else 1
        ch = data[i : i + length].decode("utf-8", "replace")
        grid.put(ch)
        if grid.col >= w:
            grid.col = 0
            grid.row = min(h - 1, grid.row + 1)
        i += length
    return frames


def render(frames, w, h):
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    advance = font.getlength("M")
    cell_h = int(FONT_SIZE * 1.3)
    W, H = int(round(w * advance)), h * cell_h
    imgs = []
    seen = set()
    for snap in frames:
        key = hash(snap)
        if key in seen:
            continue
        seen.add(key)
        img = Image.new("RGB", (W, H), BG)
        d = ImageDraw.Draw(img)
        for r, row in enumerate(snap):
            for c, (ch, fg, bg) in enumerate(row):
                x, y = int(c * advance), r * cell_h
                if bg is not None:
                    d.rectangle([x, y, x + int(advance) - 1, y + cell_h - 1], fill=bg)
                if ch != " ":
                    color = tuple(fg) if fg else DEFAULT_FG
                    d.text((x, y + (cell_h - FONT_SIZE) // 2 - FONT_SIZE * 0.18), ch, font=font, fill=color)
        imgs.append(img)
    # crop to the union content bbox so the title fills the frame
    from PIL import ImageChops

    pad_x, pad_y = 18, 14
    bbox = [W, H, 0, 0]
    bg_img = Image.new("RGB", (W, H), BG)
    for img in imgs:
        bb = ImageChops.difference(img, bg_img).getbbox()
        if bb:
            bbox[0] = min(bbox[0], bb[0]); bbox[1] = min(bbox[1], bb[1])
            bbox[2] = max(bbox[2], bb[2]); bbox[3] = max(bbox[3], bb[3])
    if bbox[2] > bbox[0] and bbox[3] > bbox[1]:
        box = (max(0, bbox[0] - pad_x), max(0, bbox[1] - pad_y),
               min(W, bbox[2] + pad_x), min(H, bbox[3] + pad_y))
        imgs = [img.crop(box) for img in imgs]
    return imgs


def main():
    os.environ.setdefault("TERM", "xterm-256color")
    cap = subprocess.run(
        ["glyphfx", "--canvas-width", str(CANVAS_W), "--canvas-height", str(CANVAS_H),
         "--frame-rate", str(FRAME_RATE), "--no-restore-cursor", EFFECT, "--no-loop", "--cycles", "1"],
        input=TEXT.encode(), capture_output=True, timeout=120,
    )
    if cap.returncode != 0 or len(cap.stdout) < 500:
        sys.exit(f"glyphfx failed rc={cap.returncode}: {cap.stderr[:300]}")
    frames = parse_frames_with_snapshots(cap.stdout, CANVAS_W, CANVAS_H)
    if len(frames) > MAX_FRAMES:
        step = len(frames) / MAX_FRAMES
        frames = [frames[int(i * step)] for i in range(MAX_FRAMES)]
    imgs = render(frames, CANVAS_W, CANVAS_H)
    OUT_GIF.parent.mkdir(parents=True, exist_ok=True)
    imgs[0].save(
        OUT_GIF, save_all=True, append_images=imgs[1:],
        duration=int(1000 / FRAME_RATE), loop=0, optimize=True,
    )
    n_colors = len({px for img in imgs[::12] for px in img.getdata() if px != BG})
    print(f"frames kept: {len(imgs)} | size: {imgs[0].width}x{imgs[0].height} | "
          f"file: {OUT_GIF.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
