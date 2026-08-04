# HARDT — handoff to Claude Code

Everything needed to pick this up and finish it. Read `CLAUDE.md` first for
the rules that must not be broken; this file is state and next actions.

Repo: `github.com/WarroomAgency/Hardt-site` · Deploy: Netlify from `main`
Client: Peter Eberhardt · Agency: War Room · Site: hardtrealestate.com

---

## Start here

```bash
git clone https://github.com/WarroomAgency/Hardt-site.git
cd Hardt-site
python3 -m http.server 8000     # no build step, no dependencies
```

Pages are **generated**. Never hand-edit HTML — it's overwritten:

```bash
python3 tools/pages.py          # content -> 18 pages
python3 tools/make_images.py    # placeholder illustrations
python3 tools/process_photos.py # real photos from photos-in/ (see below)
```

`tools/build.py` = the shell (head, header, footer, breadcrumbs, schema).
`tools/pages.py` = the content. That split is deliberate: it's why all 18 pages
have identical chrome and no page is missing a canonical.

---

## Three things you can do that the previous environment couldn't

This is why the work was handed over. Please actually use these.

1. **Push directly.** No zip round-trip. Commit and push as normal.
2. **Download images.** The previous environment had no network path for
   binaries. You do. This unblocks the single biggest gap — see *Photography*.
3. **Run and inspect locally.** Playwright is used throughout for verification;
   keep doing it (see *Verify before committing* in `CLAUDE.md`).

---

## State

**Live and verified:** 18 pages — home, how it works, what we buy, where we buy,
about, contact, four service hubs, four county hubs, three legal pages,
thank-you. No 404s. Design system, self-hosted fonts (87KB, 3 variable WOFF2),
motion layer, mobile nav, before/after slider, FAQ accordions, lead form.

Every page: one `<h1>`, no heading skips, no horizontal overflow at 390px,
**zero WCAG AA contrast failures**, valid JSON-LD, no console errors.

SEO: per-page title/description/canonical/OG. `Organization`, `LocalBusiness`,
`Person`, `WebSite`, `WebPage` sitewide; `BreadcrumbList` below root; `Service`
on the four hubs; `FAQPage` on nine pages where the Q&A is genuinely visible.

**Not built:** the 16 county×service matrix pages, and the local-research layer
that makes the county hubs defensible.

---

## Blocked on Peter — chase these

1. **Reconciled numbers.** His intake says "2 years operating" against a 2021
   start, "5+ homes bought" against "12 families helped", "3 counties worked"
   against a project list covering two. Nothing is published until these are
   real. The trust strip currently runs on the only four defensible claims:
   *Since 2021 · Four counties · ~14 days · No assignments.*
2. **LA County — yes or no.** He ticked it as a service area and the Lancaster
   project is there, but it isn't in the site's four counties. Adding it means a
   fifth county hub and four more matrix pages.
3. **Hours conflict.** GBP answer said Mon–Sat 8–6; the response-time answer
   said 7 days. Site and schema currently say Mon–Sat. This must match the GBP
   exactly.
4. **DBA filing + Blair's read.** DBA is "HARDT Real Estate", not yet filed
   (San Diego County Clerk, $54, publish in an approved newspaper within 45 days
   for 4 consecutive weeks). Blair at API Law should confirm the name is clean
   given Peter holds no DRE licence, and read `/stop-foreclosure/` plus the
   footer's principal-buyer line.
5. **Photos.** He has before/during/after of all five projects, per his intake.
   Six of thirteen slots, free, already in his phone.

**Peter's phone is (707) 489-6236** and it's live sitewide including JSON-LD.
That's the canonical NAP — the GBP and every citation must match that exact
format, character for character.

---

## Next work, in priority order

### 1. Photography — biggest visual gap, and you can actually do it

Every image is currently an original SVG illustration. They're art-directed and
they hold, but they're not photographs.

The pipeline is built. Drop files in `photos-in/` named for their slot, then:

```bash
python3 tools/process_photos.py && python3 tools/pages.py
```

Crops to the right ratio per slot, honours EXIF rotation, never upscales, writes
WebP + JPEG at 1x/2x. `build.pic()` emits `<picture>` for any slot with a photo
and falls back to the illustration for the rest — **slots fill independently.**

Thirteen slots and what each needs: `PHOTO-BRIEF.md`.

Order of preference: Peter's own photos → hand-picked free stock (Pexels,
Unsplash) → paid. **Check licences.** Pexels/Unsplash are free for commercial
use; iStock and Getty are not, and an unlicensed image on a lead-gen site is a
bill waiting to arrive.

The cliches to avoid matter more than what to pick: no handshakes, no sold
signs, no couples holding keys, no hard hat pointing at a clipboard. That's the
visual language of the category HARDT is defined against.

### 2. County research — what makes the site defensible

The county hubs are structurally complete but thin. They need the local layer,
and so do the 16 matrix pages built on top:

- County recorder — location, recording turnaround, e-recording
- Superior Court probate division — where it sits, typical calendar wait
- Documentary transfer tax, county **and** any city add-on
- California trustee-sale timeline as it plays out locally
- Permit department reality for unpermitted additions
- Dominant housing stock and era, and what that means at inspection
  (galvanised plumbing, aluminium wiring, Federal Pacific panels)
- Local deal-killers: well and septic in the High Desert; Mello-Roos and
  solar/PACE liens in southwest Riverside; coastal permits and ADU potential in
  San Diego; ag-adjacent parcels and water in Kern

**Every figure gets a source and a date, refreshed quarterly.** Do not invent
numbers — that's the one rule that ends the project if broken.

### 3. The 16 matrix pages

`/{county}/{service}/` — the actual ranking engine. Template and internal
linking are ready; they need the research from step 2 first.

**The 40% rule:** at least 40% of each page unique to that county-and-service.
Test: *if you could swap the county name and the page is still accurate, it
isn't finished.* Target 1,100–1,600 words. This is what separates these from the
doorway-page farms Google filters.

### 4. Google Business Profile

Blocked on the DBA filing. When it's ready:

- **Rename the existing Fluid Developments LLC profile** rather than creating a
  new one — preserves its review and profile age, avoids a duplicate flag
- Address hidden (service-area business)
- **Never put keywords in the name field** — the top suspension cause in this
  category
- Primary category picked from what's actually in the picker; test candidates
  against what ranks locally. Not "Real estate agency" — he isn't a brokerage
- **Kern gets no map presence.** Google caps service areas at roughly a two-hour
  drive and Bakersfield is well beyond that. Kern is website-only. Don't try to
  stretch it; that's a suspension risk

### 5. Lead routing

Form posts to Netlify Forms as `hardt-lead`, honeypot on `company`, redirects to
`/thank-you/`.

- **Turn on form notifications in the Netlify UI** — off by default, submissions
  pile up silently
- Peter wants: text on every lead, plus a RESimpli record with lead source
  `website` and campaign `website`. RESimpli has no native capture, so it needs a
  Zapier or webhook hop. Not built.

### 6. Smaller items

- Favicon set — `favicon.ico`, `apple-touch-icon.png` exist in the brand package
  (`05 Favicon & Social/`), just need copying into `assets/img/`
- About page still carries his line "HARDT homes was born" — needs his sign-off
  on the wording now the DBA is HARDT Real Estate
- Resources hub — probate timeline, NOD explainer, Prop 19, selling with tenants.
  Link bait and LLM-citation fodder
- The honest-math calculator (cash offer vs list-and-repair, side by side).
  Nothing in the category does this; natural link magnet and entirely on-brand

---

## Gotchas that cost time

**Never hand-edit HTML.** Regenerated on every run.

**Assets are content-hashed** (`site.css?v=<md5>`) by `rev()` in `build.py`. This
exists because a 7-day cache on an unfingerprinted `site.css` shipped new HTML
against a stale stylesheet and made the deployed hero look broken. Don't remove
it.

**The two bronze tints are not redundant.** `#8B7355` on cream is 3.78:1 and
fails AA for small text. `--bronze-ink` (#7D674C) is for cream backgrounds,
`--bronze-light` (#9B815F) for charcoal. Collapsing them back to one reintroduces
the failure. The logo hairline stays exactly `#8B7355`.

**Dark coverage is ~28–30%**, near the brand's "no more than a third dark"
ceiling. New dark bands should replace existing ones, not add.

**Never publish Peter's base city.** The site speaks in counties. El Cajon may
appear as a city he *buys in*, never as his location — and `addressLocality` is
deliberately absent from the schema for the same reason. The GBP verification
address is separate and stays hidden there.

**Contrast-check every text node against its computed background**, not just the
tokens. That check caught form labels inheriting cream onto a white card
(invisible) and a tint sitting exactly on the 4.5 threshold.

---

## Content that is Peter's, not ours

Used close to verbatim because it's better than anything we'd write:

- The **"list it on the open market when…"** column — his answer to when a
  seller should *not* sell to him. Nobody in this category publishes this
- The **"I don't buy"** list — his exact criteria
- The **founder story** — condensed from his BMX-to-real-estate account,
  wording preserved

Don't smooth these into marketing copy. The unpolished specificity is the point.
