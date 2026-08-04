#!/usr/bin/env python3
"""
Placeholder art for hardtrealestate.com.

Brand rule: never stock photography. So until Peter's real project photos
land, these stand in — abstract architectural forms drawn in the brand
palette. They read as deliberate art direction rather than a grey box,
and they're a few KB of vector each.

Every file written here is a PLACEHOLDER. Swap for real photography and
delete this script.
"""
import os, math, random

OUT = "assets/img"
os.makedirs(OUT, exist_ok=True)

CHARCOAL = "#1A1A1A"
CREAM    = "#F0EBE4"
BRONZE   = "#8B7355"
WARM     = "#E6E0D7"
DEEP     = "#232323"


def shell(w, h, body, bg):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" role="img" preserveAspectRatio="xMidYMid slice">'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>{body}</svg>')


def grain(w, h, seed, n=340, op=.05):
    """Fine speckle so large flat fields don't band on wide screens."""
    r = random.Random(seed)
    return "".join(
        f'<circle cx="{r.uniform(0,w):.0f}" cy="{r.uniform(0,h):.0f}" '
        f'r="{r.uniform(.4,1.5):.1f}" fill="{CHARCOAL}" opacity="{op:.3f}"/>'
        for _ in range(n))


def rooflines(w, h, seed, ink, op=.16):
    """Overlapping gable silhouettes — a skyline of small houses."""
    r = random.Random(seed)
    out, x = [], -60
    while x < w + 60:
        bw = r.uniform(w * .16, w * .30)
        bh = r.uniform(h * .26, h * .52)
        peak = r.uniform(bh * .28, bh * .48)
        base = h
        pts = (f"{x:.0f},{base:.0f} {x:.0f},{base-bh:.0f} "
               f"{x+bw/2:.0f},{base-bh-peak:.0f} {x+bw:.0f},{base-bh:.0f} {x+bw:.0f},{base:.0f}")
        out.append(f'<polygon points="{pts}" fill="{ink}" opacity="{op:.2f}"/>')
        x += bw * r.uniform(.62, .84)
    return "".join(out)


def windows(w, h, seed, ink, op=.5):
    """A grid of lit apertures — reads as a facade at any crop."""
    r = random.Random(seed)
    out, cols, rows = [], 6, 4
    cw, ch = w / (cols + 2), h / (rows + 2)
    for i in range(cols):
        for j in range(rows):
            if r.random() < .28:
                continue
            x = cw * (i + 1) + cw * .12
            y = ch * (j + 1) + ch * .12
            out.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{cw*.62:.0f}" '
                       f'height="{ch*.68:.0f}" fill="{ink}" opacity="{op*r.uniform(.35,1):.2f}"/>')
    return "".join(out)


def sunrays(w, h, cx, cy, ink, n=13, op=.07):
    """Warm daylight, abstracted. The brand's lighting note, as geometry."""
    out = []
    for i in range(n):
        a = -math.pi * .96 + (math.pi * .92) * i / (n - 1)
        L = max(w, h) * 1.7
        x2, y2 = cx + math.cos(a) * L, cy + math.sin(a) * L
        spread = 13
        x3 = cx + math.cos(a + spread / 900) * L
        y3 = cy + math.sin(a + spread / 900) * L
        out.append(f'<polygon points="{cx},{cy} {x2:.0f},{y2:.0f} {x3:.0f},{y3:.0f}" '
                   f'fill="{ink}" opacity="{op:.3f}"/>')
    return "".join(out)


def theCut(x, y, s, ink, op=1.0):
    """The mark itself, used as a large quiet watermark."""
    k = s / 100
    return (f'<g transform="translate({x},{y}) scale({k})" fill="{ink}" stroke="{ink}" '
            f'stroke-width="3" stroke-linejoin="round" opacity="{op}">'
            f'<path d="M20 21 L27 14 H33 V86 H27 L20 79 Z"/>'
            f'<path d="M80 21 L73 14 H67 V86 H73 L80 79 Z"/>'
            f'<rect x="39" y="44" width="22" height="12"/></g>')


files = {}

# ---- hero: wide, charcoal, warm light raking across a roofline ----
W, H = 1600, 1100
files["hero.svg"] = shell(W, H,
    f'<defs><linearGradient id="g" x1="0" y1="0" x2=".35" y2="1">'
    f'<stop offset="0" stop-color="#2A2724"/><stop offset="1" stop-color="{CHARCOAL}"/>'
    f'</linearGradient></defs>'
    f'<rect width="{W}" height="{H}" fill="url(#g)"/>'
    + sunrays(W, H, W * .78, H * .06, BRONZE, 15, .085)
    + rooflines(W, H, 7, CREAM, .09)
    + f'<rect y="{H*.86:.0f}" width="{W}" height="{H*.14:.0f}" fill="{CHARCOAL}" opacity=".5"/>'
    + theCut(W * .5 - 150, H * .5 - 150, 300, CREAM, .05)
    + grain(W, H, 3, 420, .05), CHARCOAL)

# ---- project cards: cream/warm, four variants so a grid never repeats ----
for i, (seed, tint) in enumerate([(11, WARM), (23, "#EFE9E1"), (37, "#E3DCD2"), (51, "#EAE4DB")], 1):
    W, H = 1200, 900
    files[f"project-{i}.svg"] = shell(W, H,
        sunrays(W, H, W * (.2 + .2 * i), -H * .1, BRONZE, 11, .05)
        + rooflines(W, H, seed, CHARCOAL, .13)
        + windows(W, H * .8, seed + 5, CHARCOAL, .10)
        + f'<rect y="{H*.9:.0f}" width="{W}" height="{H*.1:.0f}" fill="{CHARCOAL}" opacity=".07"/>'
        + grain(W, H, seed, 300, .045), tint)

# ---- before / after pair: same geometry, different treatment ----
W, H = 1200, 800
_geo = rooflines(W, H, 91, CHARCOAL, .17) + windows(W, H * .82, 91, CHARCOAL, .12)
files["before.svg"] = shell(W, H,
    _geo + f'<rect width="{W}" height="{H}" fill="#6E6A64" opacity=".30"/>'
    + grain(W, H, 91, 620, .10), "#C9C3BA")
files["after.svg"] = shell(W, H,
    sunrays(W, H, W * .8, -H * .05, BRONZE, 13, .07) + _geo
    + grain(W, H, 92, 240, .035), CREAM)

# ---- founder portrait slot: tall, charcoal, the mark held quietly ----
W, H = 900, 1150
files["portrait.svg"] = shell(W, H,
    sunrays(W, H, W * .1, H * .02, BRONZE, 11, .075)
    + f'<rect y="{H*.62:.0f}" width="{W}" height="{H*.38:.0f}" fill="#000" opacity=".22"/>'
    + theCut(W * .5 - 110, H * .40, 220, CREAM, .10)
    + grain(W, H, 61, 330, .06), "#26231F")

# ---- county banners: one per county, distinct seed so none repeat ----
for slug, seed in [("san-diego", 101), ("riverside", 202),
                   ("san-bernardino", 303), ("kern", 404)]:
    W, H = 1400, 620
    files[f"county-{slug}.svg"] = shell(W, H,
        sunrays(W, H, W * .85, -H * .2, BRONZE, 13, .07)
        + rooflines(W, H, seed, CHARCOAL, .12)
        + grain(W, H, seed, 260, .04), WARM)

# ---- social card: charcoal, the lockup, nothing else ----
W, H = 1200, 630
files["og-home.svg"] = shell(W, H,
    sunrays(W, H, W * .82, -H * .1, BRONZE, 13, .085)
    + theCut(96, H * .5 - 78, 156, CREAM)
    + f'<rect x="286" y="{H*.5-42:.0f}" width="1" height="84" fill="{BRONZE}"/>'
    + f'<text x="326" y="{H*.5+22:.0f}" font-family="Red Hat Display,Arial,sans-serif" '
    f'font-weight="900" font-size="72" letter-spacing="19" fill="{CREAM}">HARDT</text>'
    + f'<text x="98" y="{H-72:.0f}" font-family="Georgia,serif" font-style="italic" '
    f'font-size="30" fill="{BRONZE}">Every situation has a way forward.</text>'
    + grain(W, H, 5, 200, .05), CHARCOAL)

total = 0
for name, svg in files.items():
    p = os.path.join(OUT, name)
    open(p, "w").write(svg)
    total += os.path.getsize(p)
    print(f"  {os.path.getsize(p)/1024:6.1f} KB  {name}")
print(f"\n{len(files)} placeholders, {total/1024:.0f} KB total")
