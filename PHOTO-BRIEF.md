# Photography — what's needed and how to drop it in

Every image on the site is currently an original illustration. The site is
built so photographs can replace them **one at a time**, with no markup
changes: drop a file in, run two commands, done.

---

## The two commands

```bash
python3 tools/process_photos.py    # crops, compresses, makes WebP + JPEG at 1x and 2x
python3 tools/pages.py             # rebuilds the pages to use whatever now exists
```

`process_photos.py` reads from `photos-in/`. The **filename decides the slot**
— extension doesn't matter.

Any slot without a photo keeps its illustration, so partial batches are fine.
There is no "all or nothing" moment.

---

## The slots

| Drop this file | Where it appears | Crop | What it needs to be |
|---|---|---|---|
| `photos-in/hero.jpg` | Homepage hero, full bleed | 16:10 | A street or a house at golden hour. **Type sits on the left third**, so keep that side quiet — sky, a wall, a lawn. Detail belongs on the right. |
| `photos-in/portrait.jpg` | About + homepage | 4:5 | Peter. Warm daylight, at the front door of a finished project, work clothes not a suit. His studio headshot on a dark background does **not** fit the brand — this is the one shot worth booking properly. |
| `photos-in/before.jpg` | Comparison slider, left | 3:2 | A tired house, shot straight on. |
| `photos-in/after.jpg` | Comparison slider, right | 3:2 | **The same house, same spot, same lens, same height.** If the framing shifts the slider stops working as a comparison and starts looking like a trick. Mark the spot on the driveway. |
| `photos-in/project-1..4.jpg` | Recent-work strip | 4:3 | Finished exteriors. One per project: Shenandoah Dr, Cale Ct, Terrace Way/Huskey Dr, Graphic St. |
| `photos-in/county-san-diego.jpg` | San Diego county pages | 4:3 | A residential street that reads as that county. |
| `photos-in/county-riverside.jpg` | Riverside county pages | 4:3 | " |
| `photos-in/county-san-bernardino.jpg` | San Bernardino county pages | 4:3 | " |
| `photos-in/county-kern.jpg` | Kern county pages | 4:3 | " |
| `photos-in/og-home.jpg` | Social share card | 1200×630 | What people see when the link is pasted into a text. |

Phone photos are fine. A recent iPhone shot in good light beats a mediocre
stock image, and it's real, which is the entire point of the brand.

---

## Peter has most of this already

From his intake, word for word:

> *"I have before/during/after photos of every project listed above. I have a
> professional headshot photo of myself and my VA."*

That's `before`, `after`, and `project-1` through `4` — six of the thirteen
slots, and the six that carry the most weight. **Ask him for those first.**
They cost nothing and they're real.

The headshot he mentions is on a dark studio background, which doesn't match
the brand's photography direction. Use it as a stopgap if you want, but the
front-door shot is the one that belongs there.

---

## If you're buying stock instead

I can't download image files in this environment, so this part is manual.
Pre-filtered searches:

- [Pexels — house exterior](https://www.pexels.com/search/house%20exterior/) (free, no attribution required)
- [Pexels — modern house exterior](https://www.pexels.com/search/modern%20house%20exterior/)
- [iStock — before and after house exterior](https://www.istockphoto.com/photos/before-and-after-house-exterior) (paid, best for matched pairs)
- [iStock — house renovation](https://www.istockphoto.com/photos/house-renovation) (paid)
- [Getty — suburban ranch style home](https://www.gettyimages.com/photos/suburban-ranch-style-home) (paid)

**Search terms that fit:** *california ranch house exterior golden hour* ·
*stucco bungalow front door* · *single story home driveway afternoon light* ·
*contractor renovation interior daylight* · *suburban street palm trees california*

**What to avoid, and this matters more than what to pick.** No handshakes. No
sold signs. No smiling couple holding keys. No stock model in a hard hat
pointing at a clipboard. No cash-in-hand imagery. Those are the visual clichés
of exactly the category HARDT is positioned against, and one of them undoes
more trust than the photo buys.

Aim for houses that look like the ones he actually buys — 1950s to 1980s
single-storey stucco, a bit tired, real neighbourhoods. Not architectural
magazine work. A house that looks too expensive tells a distressed seller
this isn't for them.

**Check the licence before it ships.** Pexels and Unsplash are free for
commercial use. iStock and Getty are not, and a stock photo used without a
licence on a lead-generating site is a bill waiting to arrive.

---

## Once photos are in

`process_photos.py` handles crop, compression, WebP with a JPEG fallback, and
2x for retina. It centre-crops with a slight upward bias so rooflines and faces
survive, honours EXIF rotation from phones, and never upscales.

After that, the illustrations stay in the repo as fallbacks. Delete
`tools/make_images.py` and the `.svg` files only once **every** slot has a real
photo.
