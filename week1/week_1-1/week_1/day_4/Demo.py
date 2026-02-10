#!/usr/bin/env python3
"""
magic_supernova_simple_color.py

32-frame terminal animation (ANSI color):
twinkle -> 5-point magic star + pentagram outline grows -> supernova ring expands -> fade.

Usage:
  python magic_supernova_simple_color.py
  python magic_supernova_simple_color.py --fps 30 --repeat 2
  python magic_supernova_simple_color.py --no-unicode
"""

from __future__ import annotations

import argparse
import math
import shutil
import sys
import time
from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

Point = Tuple[int, int]

ANSI_CLEAR = "\033[2J\033[H"
ANSI_HIDE_CURSOR = "\033[?25l"
ANSI_SHOW_CURSOR = "\033[?25h"
ANSI_RESET = "\033[0m"


def c256(n: int) -> str:
    return f"\033[38;5;{n}m"


COLORS = {
    "core": c256(225),   # light pink
    "star": c256(141),   # purple
    "ring": c256(51),    # cyan
    "dust": c256(213),   # magenta/pink
    "dim": c256(245),    # gray
}


@dataclass(frozen=True)
class Config:
    fps: float
    repeat: int
    use_unicode: bool


def clamp(v: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, v))


def term_size() -> tuple[int, int]:
    s = shutil.get_terminal_size(fallback=(80, 24))
    return s.columns, s.lines


def center_lines(lines: Iterable[str], cols: int, rows: int) -> List[str]:
    ls = list(lines)
    top_pad = max(0, (rows - len(ls)) // 2)
    out = [""] * top_pad
    for line in ls:
        s = line.rstrip("\n")
        left_pad = max(0, (cols - len(s)) // 2)
        out.append((" " * left_pad) + s)
    return out


def render(lines: List[str]) -> None:
    cols, rows = term_size()
    sys.stdout.write(ANSI_CLEAR)
    sys.stdout.write("\n".join(center_lines(lines, cols, rows)) + "\n")
    sys.stdout.flush()


def lcg(seed: int) -> int:
    return (1103515245 * seed + 12345) & 0x7FFFFFFF


def bresenham(points: Dict[Point, str], x0: int, y0: int, x1: int, y1: int, ch: str) -> None:
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    x, y = x0, y0
    while True:
        points[(x, y)] = ch
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx
        if e2 <= dx:
            err += dx
            y += sy


def glyphs(use_unicode: bool) -> Dict[str, str]:
    if use_unicode:
        return {"spark": "✦", "shine": "✨", "dot": "·", "ring": "◌"}
    return {"spark": "*", "shine": "*", "dot": ".", "ring": "o"}


def empty_canvas(w: int, h: int) -> List[List[str]]:
    return [[" " for _ in range(w)] for _ in range(h)]


def draw(canvas: List[List[str]], points: Dict[Point, str]) -> None:
    h = len(canvas)
    w = len(canvas[0]) if h else 0
    for (x, y), ch in points.items():
        if 0 <= x < w and 0 <= y < h:
            canvas[y][x] = ch


def to_lines(canvas: List[List[str]]) -> List[str]:
    return ["".join(row).rstrip() for row in canvas]


def add_ring(points: Dict[Point, str], cx: int, cy: int, radius: int, ring_ch: str) -> None:
    if radius <= 0:
        return
    samples = max(24, radius * 12)
    for k in range(samples):
        a = 2 * math.pi * (k / samples)
        x = int(round(cx + math.cos(a) * radius))
        y = int(round(cy + math.sin(a) * radius * 0.55))
        points[(x, y)] = ring_ch


def add_star_and_pentagram(points: Dict[Point, str], cx: int, cy: int, r: int, ch_star: str, ch_penta: str, t: int) -> None:
    if r <= 0:
        return

    rot = (t - 7) * 0.05
    y_aspect = 0.55
    verts: List[Point] = []
    for i in range(5):
        a = rot + (-math.pi / 2) + i * (2 * math.pi / 5)
        x = int(round(cx + math.cos(a) * r))
        y = int(round(cy + math.sin(a) * r * y_aspect))
        verts.append((x, y))
        bresenham(points, cx, cy, x, y, ch_star)

    for i in range(5):
        x0, y0 = verts[i]
        x1, y1 = verts[(i + 2) % 5]
        bresenham(points, x0, y0, x1, y1, ch_penta)

    if r >= 9:
        for (x, y) in verts:
            points[(x + 1, y)] = ch_penta
            points[(x - 1, y)] = ch_penta


def build_frame(t: int, w: int, h: int, g: Dict[str, str]) -> List[str]:
    canvas = empty_canvas(w, h)
    cx, cy = w // 2, h // 2
    pts: Dict[Point, str] = {}

    if t == 0:
        return to_lines(canvas)

    if t <= 6:
        pulse = [
            COLORS["dim"] + g["dot"] + ANSI_RESET,
            COLORS["core"] + g["spark"] + ANSI_RESET,
            COLORS["core"] + g["shine"] + ANSI_RESET,
            COLORS["core"] + g["spark"] + ANSI_RESET,
            COLORS["dim"] + g["dot"] + ANSI_RESET,
        ]
        pts[(cx, cy)] = pulse[t % len(pulse)]

    if 7 <= t <= 17:
        r = 1 + (t - 7)
        star_ch = COLORS["star"] + g["spark"] + ANSI_RESET
        penta_ch = COLORS["star"] + g["dot"] + ANSI_RESET
        add_star_and_pentagram(pts, cx, cy, r=r, ch_star=star_ch, ch_penta=penta_ch, t=t)
        pts[(cx, cy)] = COLORS["core"] + g["shine"] + ANSI_RESET

    if 12 <= t <= 24:
        radius = 1 + (t - 12)
        ring_ch = COLORS["ring"] + g["ring"] + ANSI_RESET
        add_ring(pts, cx, cy, radius=radius, ring_ch=ring_ch)
        if t >= 16:
            add_ring(pts, cx, cy, radius=max(1, radius - 3), ring_ch=ring_ch)

    if t >= 18:
        count = (t - 17) * 4
        base = 9001 + t * 7777
        max_r = min(w, h) // 2
        dust_ch = COLORS["dust"] + g["dot"] + ANSI_RESET
        for i in range(count):
            s1 = lcg(base + i * 31)
            s2 = lcg(s1 + 101)
            ang = (s1 % 6283) / 1000.0
            r = 2 + (s2 % max(1, (max_r - 2)))
            r2 = int(r * (0.35 + (t - 18) / 18.0))
            x = int(round(cx + math.cos(ang) * r2))
            y = int(round(cy + math.sin(ang) * r2 * 0.55))
            pts[(x, y)] = dust_ch

    if t >= 26:
        fade = t - 26
        dimmed: Dict[Point, str] = {}
        for (x, y), ch in pts.items():
            if fade >= 3:
                keep = ((x * 131 + y * 313) & 7) != 0
                if not keep:
                    continue
            if fade >= 2:
                dimmed[(x, y)] = COLORS["dim"] + g["dot"] + ANSI_RESET
            else:
                dimmed[(x, y)] = ch
        pts = dimmed

    draw(canvas, pts)
    return to_lines(canvas)


def parse_args(argv: List[str]) -> Config:
    p = argparse.ArgumentParser(description="Simple colored 32-frame magic star supernova animation.")
    p.add_argument("--fps", type=float, default=24.0, help="Frames per second.")
    p.add_argument("--repeat", type=int, default=1, help="Times to replay.")
    p.add_argument("--no-unicode", action="store_true", help="ASCII-only mode.")
    a = p.parse_args(argv)
    if a.fps <= 0:
        raise SystemExit("--fps must be > 0")
    if a.repeat <= 0:
        raise SystemExit("--repeat must be >= 1")
    return Config(fps=a.fps, repeat=a.repeat, use_unicode=not a.no_unicode)


def main(argv: List[str]) -> int:
    cfg = parse_args(argv)
    g = glyphs(cfg.use_unicode)

    cols, rows = term_size()
    w = clamp(min(cols - 2, 61), 31, 61)
    h = clamp(min(rows - 2, 23), 15, 23)

    delay = 1.0 / cfg.fps

    sys.stdout.write(ANSI_HIDE_CURSOR)
    sys.stdout.flush()
    try:
        for _ in range(cfg.repeat):
            for t in range(32):
                render(build_frame(t, w, h, g))
                time.sleep(delay)
            time.sleep(delay * 2)
    finally:
        sys.stdout.write(ANSI_SHOW_CURSOR + ANSI_RESET)
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
