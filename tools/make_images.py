#!/usr/bin/env python3
"""
Illustration set for hardtrealestate.com.

These are ORIGINAL vector illustrations, not stock and not photography.
They exist because the brand book forbids stock imagery and Peter's real
project photos haven't been shot yet.

They're built to read as deliberate art direction: warm Southern
California light, layered depth, real architectural detail — bungalows,
ranch houses, palms, long shadows. Swap for real photography when it
lands and delete this file.

  python3 tools/make_images.py
"""
import os, math, random

OUT = "assets/img"
os.makedirs(OUT, exist_ok=True)

# Brand-family palette. Warm, desaturated, nothing outside the family.
INK      = "#1A1A1A"
CREAM    = "#F0EBE4"
BRONZE   = "#8B7355"
SKY_HI   = "#F6EFE4"
SKY_LO   = "#E3D6C4"
SUN      = "#E8CFA8"
HILL_FAR = "#CFC3B2"
HILL_MID = "#BBAE9B"
TERRA    = "#B08268"
SAGE     = "#8E9280"
STUCCO   = ["#EDE5D9", "#E4D9CA", "#DCCFBE", "#E9DED0"]
ROOF     = ["#8A7663", "#7A6857", "#94806C", "#6F5F50"]
GLASS    = "#6E6355"


def svg(w, h, body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
            f'height="{h}" role="img" preserveAspectRatio="xMidYMid slice">'
            f'<defs>{defs}</defs>{body}</svg>')


def sky(w, h, hi=SKY_HI, lo=SKY_LO, gid="sky"):
    d = (f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{hi}"/><stop offset="1" stop-color="{lo}"/></linearGradient>')
    return d, f'<rect width="{w}" height="{h}" fill="url(#{gid})"/>'


def sun(cx, cy, r, gid="sun"):
    d = (f'<radialGradient id="{gid}"><stop offset="0" stop-color="{SUN}" stop-opacity=".95"/>'
         f'<stop offset="1" stop-color="{SUN}" stop-opacity="0"/></radialGradient>')
    return d, f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{gid})"/>'


def hills(w, base, amp, fill, seed, op=1.0):
    r = random.Random(seed)
    pts, x = [], -20
    while x < w + 40:
        pts.append((x, base - abs(math.sin(x / (w * r.uniform(.12, .22))) * amp) - r.uniform(0, amp * .22)))
        x += w / 22
    d = f"M-20,{base + 400} L" + " L".join(f"{p[0]:.0f},{p[1]:.0f}" for p in pts) + f" L{w + 40},{base + 400} Z"
    return f'<path d="{d}" fill="{fill}" opacity="{op}"/>'


def window(x, y, w, h, lit=False, r=None):
    """A framed window with a sill and mullions."""
    g = [f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{SUN if lit else GLASS}" '
         f'opacity="{.85 if lit else .5}"/>',
         f'<rect x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="none" stroke="{CREAM}" stroke-width="2"/>',
         f'<line x1="{x + w/2:.0f}" y1="{y:.0f}" x2="{x + w/2:.0f}" y2="{y + h:.0f}" stroke="{CREAM}" stroke-width="1.6"/>',
         f'<line x1="{x:.0f}" y1="{y + h/2:.0f}" x2="{x + w:.0f}" y2="{y + h/2:.0f}" stroke="{CREAM}" stroke-width="1.6"/>',
         f'<rect x="{x-3:.0f}" y="{y + h:.0f}" width="{w+6:.0f}" height="3" fill="{CREAM}" opacity=".8"/>']
    return "".join(g)


def gable_house(x, base, w, hgt, seed, stucco=None, roof=None, lit_bias=.5):
    """A gable-fronted house: body, pitched roof, door, windows, chimney."""
    r = random.Random(seed)
    st = stucco or r.choice(STUCCO)
    rf = roof or r.choice(ROOF)
    peak = hgt * r.uniform(.34, .46)
    g = []
    # chimney behind the roof
    if r.random() < .55:
        cw = w * .09
        cx = x + w * r.uniform(.62, .78)
        g.append(f'<rect x="{cx:.0f}" y="{base-hgt-peak*.86:.0f}" width="{cw:.0f}" height="{peak*.9:.0f}" fill="{rf}"/>')
    # body
    g.append(f'<rect x="{x:.0f}" y="{base-hgt:.0f}" width="{w:.0f}" height="{hgt:.0f}" fill="{st}"/>')
    # shaded side, so it reads three-dimensional
    g.append(f'<rect x="{x:.0f}" y="{base-hgt:.0f}" width="{w*.17:.0f}" height="{hgt:.0f}" fill="{INK}" opacity=".07"/>')
    # roof with eave overhang
    ov = w * .06
    g.append(f'<polygon points="{x-ov:.0f},{base-hgt:.0f} {x+w/2:.0f},{base-hgt-peak:.0f} '
             f'{x+w+ov:.0f},{base-hgt:.0f}" fill="{rf}"/>')
    g.append(f'<polygon points="{x+w/2:.0f},{base-hgt-peak:.0f} {x+w+ov:.0f},{base-hgt:.0f} '
             f'{x+w*.62:.0f},{base-hgt:.0f}" fill="{INK}" opacity=".10"/>')
    # door
    dw, dh = w * .19, hgt * .48
    dx = x + w * r.uniform(.12, .26)
    g.append(f'<rect x="{dx:.0f}" y="{base-dh:.0f}" width="{dw:.0f}" height="{dh:.0f}" fill="{rf}"/>')
    g.append(f'<rect x="{dx:.0f}" y="{base-dh:.0f}" width="{dw:.0f}" height="{dh:.0f}" fill="none" stroke="{CREAM}" stroke-width="1.8"/>')
    g.append(f'<circle cx="{dx+dw*.8:.0f}" cy="{base-dh*.5:.0f}" r="2" fill="{CREAM}"/>')
    # windows
    ww, wh = w * .17, hgt * .27
    for i in range(2):
        wx = x + w * (.44 + i * .26)
        if wx + ww < x + w * .98:
            g.append(window(wx, base - hgt * .74, ww, wh, r.random() < lit_bias, r))
    return "".join(g)


def ranch_house(x, base, w, hgt, seed, stucco=None, roof=None, lit_bias=.4):
    """Low-slung ranch — the dominant stock across these counties."""
    r = random.Random(seed)
    st = stucco or r.choice(STUCCO)
    rf = roof or r.choice(ROOF)
    g = [f'<rect x="{x:.0f}" y="{base-hgt:.0f}" width="{w:.0f}" height="{hgt:.0f}" fill="{st}"/>',
         f'<rect x="{x:.0f}" y="{base-hgt:.0f}" width="{w*.13:.0f}" height="{hgt:.0f}" fill="{INK}" opacity=".06"/>']
    ov = w * .04
    rh = hgt * .30
    g.append(f'<polygon points="{x-ov:.0f},{base-hgt:.0f} {x+w*.30:.0f},{base-hgt-rh:.0f} '
             f'{x+w*.72:.0f},{base-hgt-rh:.0f} {x+w+ov:.0f},{base-hgt:.0f}" fill="{rf}"/>')
    dw, dh = w * .12, hgt * .55
    dx = x + w * .58
    g.append(f'<rect x="{dx:.0f}" y="{base-dh:.0f}" width="{dw:.0f}" height="{dh:.0f}" fill="{rf}"/>')
    ww, wh = w * .20, hgt * .30
    for i in range(2):
        g.append(window(x + w * (.09 + i * .26), base - hgt * .70, ww, wh, r.random() < lit_bias, r))
    # carport posts — very SoCal
    g.append(f'<rect x="{x+w*.80:.0f}" y="{base-hgt*.62:.0f}" width="3" height="{hgt*.62:.0f}" fill="{rf}"/>')
    return "".join(g)


def palm(x, base, h, seed, op=1.0):
    r = random.Random(seed)
    g = [f'<path d="M{x},{base} C{x-3},{base-h*.5} {x+4},{base-h*.75} {x},{base-h}" '
         f'stroke="{ROOF[1]}" stroke-width="{max(3,h*.035):.1f}" fill="none" opacity="{op}"/>']
    for i in range(7):
        a = -math.pi * .92 + (math.pi * .84) * i / 6
        L = h * r.uniform(.24, .34)
        ex, ey = x + math.cos(a) * L, base - h + math.sin(a) * L * .62
        g.append(f'<path d="M{x},{base-h} Q{(x+ex)/2:.0f},{base-h-abs(L)*.28:.0f} {ex:.0f},{ey:.0f}" '
                 f'stroke="{SAGE}" stroke-width="{max(2.4,h*.026):.1f}" fill="none" stroke-linecap="round" opacity="{op}"/>')
    return "".join(g)


def shrub(x, base, w, seed, fill=SAGE, op=.85):
    r = random.Random(seed)
    return "".join(f'<circle cx="{x + r.uniform(-w*.35, w*.35):.0f}" cy="{base - r.uniform(w*.12, w*.42):.0f}" '
                   f'r="{r.uniform(w*.24, w*.42):.0f}" fill="{fill}" opacity="{op}"/>' for _ in range(4))


def ground(w, base, h, fill):
    return f'<rect y="{base:.0f}" width="{w}" height="{h}" fill="{fill}"/>'


def shadow(x, base, w, skew=.5, op=.10):
    return (f'<polygon points="{x:.0f},{base:.0f} {x+w:.0f},{base:.0f} '
            f'{x+w+w*skew:.0f},{base+w*.16:.0f} {x+w*skew:.0f},{base+w*.16:.0f}" fill="{INK}" opacity="{op}"/>')


def street(w, h, seed, rows=3, dusk=False, mono=False):
    """A whole scene: sky, sun, hills, a row of houses, planting, shadows."""
    r = random.Random(seed)
    hi, lo = ("#3A342C", "#241F1A") if dusk else (SKY_HI, SKY_LO)
    d1, s1 = sky(w, h, hi, lo, f"sk{seed}")
    d2, s2 = sun(w * r.uniform(.62, .86), h * .17, h * .46, f"sn{seed}")
    base = h * .78
    g = [s1, s2,
         hills(w, base - h * .10, h * .13, HILL_FAR, seed, .55),
         hills(w, base - h * .04, h * .09, HILL_MID, seed + 1, .5),
         ground(w, base, h - base, "#D8CDBC" if not dusk else "#2A251F")]
    # back row, smaller and hazier
    x = -w * .04
    while x < w:
        bw = r.uniform(w * .13, w * .19)
        g.append(gable_house(x, base - h * .045, bw, r.uniform(h * .17, h * .24), int(x) + seed,
                             lit_bias=.75 if dusk else .25))
        x += bw * r.uniform(1.05, 1.3)
    g.append(f'<rect width="{w}" height="{base:.0f}" fill="{lo}" opacity=".30"/>')
    # front row
    x = -w * .06
    i = 0
    while x < w:
        bw = r.uniform(w * .20, w * .30)
        hh = r.uniform(h * .24, h * .33)
        maker = ranch_house if i % 2 else gable_house
        g.append(shadow(x, base, bw, .42, .09))
        g.append(maker(x, base, bw, hh, int(x) * 7 + seed, lit_bias=.8 if dusk else .3))
        if r.random() < .5:
            g.append(palm(x + bw * r.uniform(1.0, 1.1), base, h * r.uniform(.26, .40), int(x) + seed))
        g.append(shrub(x + bw * r.uniform(.05, .3), base, w * .05, int(x) + seed + 3))
        x += bw * r.uniform(1.16, 1.34)
        i += 1
    # foreground kerb
    g.append(f'<rect y="{h*.94:.0f}" width="{w}" height="{h*.06:.0f}" fill="{INK}" opacity="{.10 if not dusk else .3}"/>')
    if mono:
        g.append(f'<rect width="{w}" height="{h}" fill="#7D7469" opacity=".55"/>')
        g.append(f'<rect width="{w}" height="{h}" fill="{INK}" opacity=".08"/>')
    return svg(w, h, "".join(g), d1 + d2)


def theCut(x, y, s, ink, op=1.0):
    k = s / 100
    return (f'<g transform="translate({x},{y}) scale({k})" fill="{ink}" stroke="{ink}" stroke-width="3" '
            f'stroke-linejoin="round" opacity="{op}"><path d="M20 21 L27 14 H33 V86 H27 L20 79 Z"/>'
            f'<path d="M80 21 L73 14 H67 V86 H73 L80 79 Z"/><rect x="39" y="44" width="22" height="12"/></g>')


files = {}

# hero — dusk, so cream type sits on it cleanly
files["hero.svg"] = street(1800, 1150, 7, dusk=True)

# project cards
for i, seed in enumerate([21, 34, 47, 58], 1):
    files[f"project-{i}.svg"] = street(1200, 900, seed)

# before / after — same seed, so it is visibly the same street
files["before.svg"] = street(1200, 800, 91, mono=True)
files["after.svg"] = street(1200, 800, 91)

# county banners
for slug, seed in [("san-diego", 101), ("riverside", 202), ("san-bernardino", 303), ("kern", 404)]:
    files[f"county-{slug}.svg"] = street(1400, 640, seed)

# founder portrait slot — a dusk street at portrait crop, mark held quietly
_pt = street(900, 1150, 12, dusk=True)
files["portrait.svg"] = _pt.replace("</svg>", theCut(900*.5-90, 1150*.14, 180, CREAM, .12) + "</svg>")

# social card
W, H = 1200, 630
d1, s1 = sky(W, H, "#2E2822", "#191614", "og")
d2, s2 = sun(W * .82, H * .2, H * .7, "ogs")
files["og-home.svg"] = svg(W, H, s1 + s2
    + hills(W, H * .82, H * .12, "#3A342C", 9, .8)
    + theCut(92, H * .5 - 76, 152, CREAM)
    + f'<rect x="282" y="{H*.5-40:.0f}" width="1" height="80" fill="{BRONZE}"/>'
    + f'<text x="322" y="{H*.5+20:.0f}" font-family="Red Hat Display,Arial,sans-serif" font-weight="900" '
      f'font-size="70" letter-spacing="18" fill="{CREAM}">HARDT</text>'
    + f'<text x="94" y="{H-64:.0f}" font-family="Georgia,serif" font-style="italic" font-size="29" '
      f'fill="{BRONZE}">Every situation has a way forward.</text>', d1 + d2)

total = 0
for name, s in files.items():
    open(os.path.join(OUT, name), "w").write(s)
    total += len(s)
    print(f"  {len(s)/1024:6.1f} KB  {name}")
print(f"\n{len(files)} illustrations, {total/1024:.0f} KB")
