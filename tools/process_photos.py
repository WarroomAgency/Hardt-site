#!/usr/bin/env python3
"""
Turns raw photos into web-ready assets, correctly cropped and compressed.

Drop files into  photos-in/  named for the slot they fill, then run:

    python3 tools/process_photos.py
    python3 tools/pages.py

Any extension works (.jpg .jpeg .png .heic-converted .webp). The name
before the extension is what matters:

    photos-in/hero.jpg              -> the homepage hero
    photos-in/portrait.jpg          -> Peter, on About and the homepage
    photos-in/before.jpg            -> left side of the comparison slider
    photos-in/after.jpg             -> right side (shoot from the SAME spot)
    photos-in/project-1.jpg ... -4  -> the recent-work strip
    photos-in/county-san-diego.jpg
    photos-in/county-riverside.jpg
    photos-in/county-san-bernardino.jpg
    photos-in/county-kern.jpg
    photos-in/og-home.jpg           -> the social share card

For each one this writes a WebP and a JPEG fallback at 1x and 2x, cropped
to the aspect ratio that slot actually uses. build.py then emits a
<picture> element automatically for any slot that has a real photo, and
falls back to the illustration for any that doesn't — so you can add them
one at a time.
"""
import os, sys, glob

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is required:  pip install Pillow --break-system-packages")

IN, OUT = "photos-in", "assets/img"
os.makedirs(IN, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

# slot -> (aspect ratio, width at 1x). Ratios match the CSS .media--* classes.
SLOTS = {
    "hero":                  (16 / 10, 1800),
    "portrait":              (4 / 5,    900),
    "before":                (3 / 2,   1200),
    "after":                 (3 / 2,   1200),
    "project-1":             (4 / 3,   1000),
    "project-2":             (4 / 3,   1000),
    "project-3":             (4 / 3,   1000),
    "project-4":             (4 / 3,   1000),
    "county-san-diego":      (4 / 3,   1000),
    "county-riverside":      (4 / 3,   1000),
    "county-san-bernardino": (4 / 3,   1000),
    "county-kern":           (4 / 3,   1000),
    "og-home":               (1200 / 630, 1200),
    # Team headshots — square crop for the About team cards. Peter and
    # Frances both have studio headshots (dark background, off the brand
    # spec) that serve as stopgaps until front-of-project shots exist.
    "team-peter":            (1 / 1,    800),
    "team-frances":          (1 / 1,    800),
}


def crop_to(im, ratio):
    """Centre-crop to an exact aspect ratio without squashing anything."""
    w, h = im.size
    if w / h > ratio:                      # too wide — trim the sides
        nw = int(h * ratio)
        box = ((w - nw) // 2, 0, (w - nw) // 2 + nw, h)
    else:                                  # too tall — trim top and bottom,
        nh = int(w / ratio)                # biased upward so faces and rooflines survive
        top = int((h - nh) * 0.38)
        box = (0, top, w, top + nh)
    return im.crop(box)


def process(path, slot):
    ratio, base_w = SLOTS[slot]
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)       # honour phone rotation
    if im.mode not in ("RGB", "L"):
        im = im.convert("RGB")
    im = crop_to(im, ratio)

    written = []
    for mult, suffix in ((1, ""), (2, "@2x")):
        w = base_w * mult
        if im.width < w and mult == 2:
            continue                       # never upscale
        h = int(w / ratio)
        r = im.resize((w, h), Image.LANCZOS)
        for ext, kw in (("webp", dict(quality=82, method=6)),
                        ("jpg",  dict(quality=84, optimize=True, progressive=True))):
            p = os.path.join(OUT, f"{slot}{suffix}.{ext}")
            r.save(p, **kw)
            written.append((p, os.path.getsize(p)))
    return written


def main():
    found = 0
    for f in sorted(glob.glob(os.path.join(IN, "*"))):
        slot = os.path.splitext(os.path.basename(f))[0]
        if slot.startswith("."):
            continue
        if slot not in SLOTS:
            print(f"  ?  {os.path.basename(f)} — no slot called '{slot}', skipped")
            print(f"     valid: {', '.join(sorted(SLOTS))}")
            continue
        try:
            out = process(f, slot)
        except Exception as e:
            print(f"  ✗  {slot}: {e}")
            continue
        found += 1
        kb = sum(s for _, s in out) / 1024
        print(f"  ✓  {slot:22} {len(out)} files, {kb:6.0f} KB total")

    if not found:
        print(f"Nothing in {IN}/ yet.\n")
        print("Drop photos in there named for their slot, then run this again:")
        for s in sorted(SLOTS):
            print(f"   {IN}/{s}.jpg")
    else:
        print(f"\n{found} slot(s) processed. Now run: python3 tools/pages.py")
        print("Pages will use the photo wherever one exists and the illustration everywhere else.")


if __name__ == "__main__":
    main()
