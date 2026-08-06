#!/usr/bin/env python3
"""
Social share cards: 1200x630, one per surface that gets shared.

Why these are generated rather than hand-made: a share card is the first
thing anyone sees when the link is pasted into a text, and an unbranded
photograph says nothing about who sent it. Every card here composites a
real photograph with the brand scrim, the lockup and one line, so the
card a seller sees in Messages matches the hero they land on.

Composition mirrors the site hero deliberately: type sits in a readable
column on the left, photography breathes on the right.

    python3 tools/make_og.py        # regenerates assets/img/og-*.jpg
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1200, 630
CHARCOAL = (26, 26, 26)
CREAM = (240, 235, 228)
BRONZE = (139, 115, 85)          # logo hairline, exactly
BRONZE_LIGHT = (155, 129, 95)    # AA on charcoal

FD = os.path.join(os.path.dirname(__file__), "fonts")
DISPLAY = os.path.join(FD, "RedHatDisplay-ExtraBold.ttf")
BODY = os.path.join(FD, "DMSans-Regular.ttf")
SERIF = os.path.join(FD, "SourceSerif4-Italic.ttf")

# slot -> (source photo, the one line)
# NB: project-2 is deliberately not used here. Its front elevation shows a
# legible house number, and no property address appears anywhere public.
CARDS = {
    "og-home":                 ("project-5", "Every situation has a way forward."),
    "og-situations":           ("project-1", "However you got here, there is a way through it."),
    "og-helped":               ("after",     "Houses we bought, fixed, and put back into use."),
    "og-san-diego-county":     ("county-san-diego", "San Diego County"),
    "og-riverside-county":     ("county-riverside", "Riverside County"),
    "og-san-bernardino-county":("county-san-bernardino", "San Bernardino County"),
    "og-kern-county":          ("county-kern", "Kern County"),
}
PLACE_CARDS = {"og-san-diego-county", "og-riverside-county",
               "og-san-bernardino-county", "og-kern-county"}


def _bg(slot):
    """Photo, cover-cropped to the card. Falls back to flat charcoal so a
    missing photo degrades to a plain brand card rather than crashing."""
    for ext in ("jpg", "png"):
        p = f"assets/img/{slot}.{ext}"
        if os.path.exists(p):
            im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
            return ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.62, 0.45))
    return Image.new("RGB", (W, H), CHARCOAL)


PANEL = 516          # solid brand panel width; the rest is photograph


def _compose(im):
    """A solid charcoal brand panel, a bronze hairline, then the photograph.

    An earlier version laid type over a gradient scrim. It read as a photo
    with words on it rather than as a brand asset, which is the opposite of
    what a share card is for. A hard panel and the logo's own hairline make
    the card unmistakably HARDT at thumbnail size, and the photograph still
    does the work of showing a real house.
    """
    card = Image.new("RGB", (W, H), CHARCOAL)
    photo = ImageOps.fit(im, (W - PANEL, H), Image.LANCZOS, centering=(0.5, 0.45))
    # ease the photo very slightly toward the panel so the seam is a join,
    # not a collision
    card.paste(photo, (PANEL, 0))
    d = ImageDraw.Draw(card)
    d.rectangle([PANEL - 1, 0, PANEL, H], fill=BRONZE)      # the hairline
    return card


def _tracked(d, xy, text, font, fill, track):
    """Letter-spaced text. The wordmark carries wide tracking in the brand
    and PIL has no spacing control, so glyphs are placed individually."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + track
    return x


def _mark(d, x, cy, m):
    """The H mark, traced from the site's inline SVG rather than approximated.

    Same viewBox geometry (0..100), same angled shoulders on both uprights,
    and the same 3-unit stroke the SVG carries, which fattens every shape by
    1.5 units a side. Drawn centred on cy so it shares an axis with the
    hairline and the wordmark, exactly as .lockup does with align-items:center.
    """
    u = m / 100.0
    top = cy - 50 * u                       # glyph spans 0..100 in the viewBox
    P = lambda pts: [(x + px * u, top + py * u) for px, py in pts]
    sw = max(1, round(3 * u))
    left  = [(20, 21), (27, 14), (33, 14), (33, 86), (27, 86), (20, 79)]
    right = [(80, 21), (73, 14), (67, 14), (67, 86), (73, 86), (80, 79)]
    for poly in (left, right):
        d.polygon(P(poly), fill=CREAM, outline=CREAM, width=sw)
    d.rectangle(P([(39, 44), (61, 56)]), fill=CREAM, outline=CREAM, width=sw)


def _lockup(d, x, cy, m=62):
    """Mark, bronze hairline, wordmark: one horizontal lockup on a shared
    centre line. Every proportion is the site's own, scaled from the mark:
    gap 14/30, hairline 1x26/30, wordmark 20/30 at .27em tracking."""
    k = m / 30.0                            # the site draws the mark at 30px
    gap, hair_w, hair_h = 14 * k, max(1, round(1 * k)), 26 * k
    size = round(20 * k)
    f = ImageFont.truetype(DISPLAY, size)
    track = 0.27 * size

    _mark(d, x, cy, m)
    hx = x + m + gap
    d.rectangle([hx, cy - hair_h / 2, hx + hair_w, cy + hair_h / 2], fill=BRONZE)

    wx = hx + hair_w + gap + 2 * k          # .lockup__word padding-left:2px
    # centre the wordmark by its own ink box, not by its line box
    x0, y0, x1, y1 = f.getbbox("HARDT")
    _tracked(d, (wx, cy - (y0 + y1) / 2), "HARDT", f, CREAM, track)
    return cy + hair_h / 2


def build(slot, photo, line, is_place):
    im = _compose(_bg(photo))
    d = ImageDraw.Draw(im)
    f_line = ImageFont.truetype(SERIF, 34)
    f_place = ImageFont.truetype(DISPLAY, 38)
    f_url = ImageFont.truetype(DISPLAY, 20)

    x = 74
    lock_cy = 196                    # lockup sits on this centre line
    _lockup(d, x, lock_cy, 62)

    # one line: the serif tagline, or the place name in display caps
    ly = lock_cy + 62
    if is_place:
        d.text((x, ly), line.upper(), font=f_place, fill=CREAM)
        d.text((x, ly + 58), "We buy houses here, as-is.",
               font=ImageFont.truetype(BODY, 25), fill=(198, 192, 184))
    else:
        # wrap the serif line at a comfortable measure
        words, cur, lines = line.split(), "", []
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f_line) > 372 and cur:
                lines.append(cur); cur = w
            else:
                cur = t
        lines.append(cur)
        for i, l in enumerate(lines):
            d.text((x, ly + i * 46), l, font=f_line, fill=BRONZE_LIGHT)
        ly += (len(lines) - 1) * 46

    # bronze rule and the domain, anchored to the lockup's left edge
    ry = 452
    d.rectangle([x, ry, x + 54, ry + 2], fill=BRONZE)
    _tracked(d, (x, ry + 26), "HARDTREALESTATE.COM", f_url, (182, 175, 166), 2.2)

    out = f"assets/img/{slot}.jpg"
    im.save(out, "JPEG", quality=88, optimize=True, progressive=True)
    return out, os.path.getsize(out)


if __name__ == "__main__":
    if not os.path.exists("assets/img"):
        raise SystemExit("run from the repo root")
    for slot, (photo, line) in CARDS.items():
        p, size = build(slot, photo, line, slot in PLACE_CARDS)
        print(f"  ✓  {p:38} {size // 1024:>4} KB   from {photo}")
    print(f"\n{len(CARDS)} share cards written")
