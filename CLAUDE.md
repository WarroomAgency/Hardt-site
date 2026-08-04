# HARDT — working notes for Claude

Static marketing site for **HARDT** (hardtrealestate.com), a d/b/a of
Fluid Developments LLC. (DBA was going to be "HARDT Real Estate"; per Michael,
2026-08-04, it will likely be plain "HARDT". Site copy uses HARDT throughout.) Client is Peter Eberhardt. Agency is War Room.
Read this before writing any code or copy in this repo.

Companion docs: `BUILD-NOTES.md` (placeholders + blockers).

---

## What this is

Peter buys houses as-is, as a principal, across four Southern California
counties. He does not broker, does not represent anyone, and does not assign
contracts. The site's job is to rank locally, earn a call from someone having a
bad year, and read as a person rather than a lead-gen funnel.

Stack is deliberately plain: hand-written HTML, one stylesheet, no framework, no
build step. Netlify serves the repo root. Do not add a bundler, a CSS framework,
or a JS dependency without a specific reason — the whole competitive advantage
here is being faster and cleaner than the template farms.

---

## Non-negotiables

These come from the locked brand book and from FTC/DRE exposure. Breaking one is
a bug, not a style preference.

### Content integrity

- **Never publish a number that isn't verified.** Peter's intake contained
  conflicting figures (see `BUILD-NOTES.md`). Until they're reconciled, the only
  claims allowed are: *Since 2021*, *Four counties*, *~14 days*, *No assignments*.
- **No testimonials or reviews** until they exist on a platform where they can be
  verified, with attribution. FTC endorsement rules apply.
- **Stock photography: free stock only (Pexels/Unsplash), hand-picked, licence
  checked.** Michael's ruling, 2026-08-04, superseding the older blanket ban.
  Generic slots (hero, county streets) may use free stock; anything implying
  it's Peter's work — portrait, before/after, project-1..4 — stays illustrated
  until his real photos land. Sources logged in `photos-in/SOURCES.md`. The
  cliché bans in `PHOTO-BRIEF.md` still apply in full.
- **The proof point is a policy, never a statistic.** Write it exactly:
  *"We don't assign contracts. If it doesn't close, we buy it ourselves."*
  Never convert it to a percentage. (Was "I buy it myself" — changed to team
  voice per Michael, 2026-08-04.)

### Legal

Every page carries the principal-buyer line in the footer. Peter holds **no DRE
licence**, so this states the exemption he operates under (kept even with the
plain "HARDT" DBA — he is still buying real estate without a licence):

> HARDT buys property as a principal for its own account. We are not
> a licensed real estate brokerage, we do not represent buyers or sellers, and we
> do not provide legal, tax or financial advice.

The `/stop-foreclosure/` pages are compliance-sensitive — California Civil Code
§§1695 and 2945 govern equity purchases and foreclosure consulting. Those pages
educate and state options. They never offer foreclosure consulting services.
Blair at API Law reviews them before they go live.

### Voice

Direct, warm, never salesy. Plain sentences, honest numbers, no jargon, no
pressure. Bad news arrives at the same volume as the good — when listing is the
better move for a seller, the site says so.

Never: exclamation marks, all-caps urgency, countdown timers, "act now",
"limited time", fake scarcity. The brand book's *don't sound like this* example
is literally a competitor's meta description.

Always **HARDT** in all caps. Never Hardt or hardt.

**Team voice, not solo-operator voice** (Michael, 2026-08-04). Operational copy
says "we / us / our team", never "I come look at it myself". Three exceptions
keep first-person singular: the founder story (About + the homepage founder
blurb — it's Peter's own narrative), FAQ questions written in the homeowner's
voice ("Do I pay transfer tax?"), and the visitor-facing CTA "Get my offer".

---

## Design system

Everything lives in `assets/site.css`. Use the tokens; don't hardcode colour.

| Token | Value | Use |
|---|---|---|
| `--charcoal` | `#1A1A1A` | Dark bands, headings |
| `--cream` | `#F0EBE4` | Page background — leads |
| `--bronze` | `#8B7355` | **Logo hairline and focus rings only.** Never recoloured. |
| `--bronze-ink` | `#7D674C` | Small bronze text on cream — 4.52:1 |
| `--bronze-light` | `#9B815F` | Small bronze text on charcoal — 4.72:1 |
| `--gray` | `#666666` | Secondary copy |

The two bronze tints exist because `#8B7355` on cream is 3.78:1 and fails AA for
small text. **Do not "simplify" them back to one bronze** — that reintroduces the
failure. The logo hairline stays exactly `#8B7355`.

**The 85/15 rule.** Cream leads, charcoal frames the one moment that matters. If
a page is more than about a third dark, it's drifting. The homepage runs 30%
after Peter asked for more colour balance — that's near the ceiling, so new dark
bands should replace existing ones rather than add to them.

**The serif rule.** `Source Serif 4 Italic` marks exactly **one** line per page —
the warmest sentence on the surface. Never headlines, never body copy, never
bold, never caps. Sentence case only.

**Type rhythm:** eyebrow (RHD 800, caps, bronze) → headline (RHD 900) → body
(DM Sans) → the one serif line. That order is the brand's fingerprint.

Fonts are self-hosted in `assets/fonts/` — three variable WOFF2 files, 87KB.
**Do not add a Google Fonts link**; it undoes the performance work and adds a
third party to the critical path.

---

## Page conventions

Every page needs, without exception:

- Exactly one `<h1>`, no skipped heading levels
- Self-referencing canonical, unique title (50–60 chars) and meta description
  (140–158), unique OG image
- JSON-LD appropriate to the page type. Sitewide: `Organization`, `WebSite`.
  Per page: `LocalBusiness` on county/contact, `Service` on service and matrix
  pages, `FAQPage` only where the Q&A is visibly on the page, `Person` on About.
  **Never mark up something the page doesn't show.**
- The shared header and footer, copied verbatim from `index.html`
- Added to `sitemap.xml` **when it ships, not before** — a sitemap full of 404s
  wastes crawl budget

### County × service matrix pages

The ranking engine, and the easiest thing to get wrong. Sixteen pages at
`/{county}/{service}/`.

**The 40% rule:** at least 40% of each page must be unique to that county and
service — not find-and-replaced. The test: *if you could swap the county name and
the page would still be accurate, it isn't finished.* That single test is what
separates this from the doorway-page farms Google filters.

Unique material per county: recorder's office and recording turnaround, Superior
Court probate division and typical wait, documentary transfer tax including city
add-ons, trustee-sale timeline, permit department reality for unpermitted
additions, dominant housing stock and era, local deal-killers (well and septic in
the High Desert, Mello-Roos and solar/PACE liens in southwest Riverside, coastal
permits and ADU potential in San Diego, ag-adjacent parcels and water in Kern).

Every market figure gets a source and a date, and is refreshed quarterly.

Target 1,100–1,600 words. Padding reads as padding to Google and to homeowners.

---

## Verify before committing

Run these. They have each caught a real bug already.

```bash
python3 -m http.server 8100 &
# then, per page: render at 1440 and 390 and check
```

- Single `<h1>`, clean heading order
- Zero horizontal overflow at 390px
- **Contrast: walk every text node against its computed background.** This caught
  form labels inheriting cream onto a white card (invisible), and a bronze tint
  sitting exactly on the 4.5 threshold.
- No tap target under 24px (WCAG 2.2 AA)
- JSON-LD parses; types are what you intended
- No console errors
- `grep -rn "000-0000"` — the placeholder phone must not reach production

---

## Facts about the business

Do not invent these. They come from Peter's intake.

**Counties and cities.** San Diego (San Diego, Chula Vista, Escondido, El Cajon,
La Mesa, Santee, Lemon Grove, National City, Ramona) · Riverside (Riverside,
Temecula, Murrieta, Perris) · San Bernardino (San Bernardino, Fontana, Rancho
Cucamonga, Redlands, Highland) · Kern (Bakersfield, Shafter, Wasco, Tehachapi,
Ridgecrest).

**Won't buy:** under $100k · under ~50% equity · subject-to with no equity ·
vacant land · commercial · timeshares · anything where title can't be cleared.

**Will buy:** up to ~$1.2M, single and multi-family, major work including fire
and water damage, inherited and probate, pre-foreclosure and NOD, liens and title
problems, tenant-occupied, houses full of contents.

**Operations.** Do not publish where Peter is based, or name any city as his
location — the site speaks in counties only. El Cajon may appear as a city he
*buys in*, never as a base. Subcontracts all renovation. ~14 days to close.
Responds within 15 minutes, 8am–6pm. Handles ~50 web leads/month. Every lead goes
to Peter directly — no call centre, no assistant screening.

**Kern has no map presence.** Google caps a service area at roughly a two-hour
drive from where he actually operates, and Bakersfield is well beyond that.
Kern is covered by the website only.
Do not write copy implying a Bakersfield office.

---

## Deploy

Netlify, repo root, no build command. `netlify.toml` sets headers, HSTS, cache
policy and noindex on `/thank-you/`. Push to `main` redeploys.

The lead form posts to Netlify Forms as `hardt-lead` with a honeypot on
`company`. Form notifications must be enabled in the Netlify UI — they're off by
default and submissions pile up silently.

---

## How pages are generated

**Do not hand-edit the HTML.** Every page is generated:

```bash
python3 tools/pages.py      # content -> 18 pages
python3 tools/make_images.py # placeholder art (delete once real photos land)
```

`tools/build.py` holds the shell — head, header, footer, breadcrumbs, schema
graph. `tools/pages.py` holds the content. Editing `index.html` directly means
your change is gone on the next run, and the shared chrome silently drifts.

Interaction lives in `assets/site.js` — reveals, mobile drawer, before/after
slider, accordions, sticky call bar. Vanilla, no dependencies. Everything must
keep working with JS disabled.

## State

Built: 40 pages — the original 18, plus the sixteen county×service matrix
pages, a Resources hub with four explainers, and the honest-math calculator
(`/resources/cash-offer-vs-listing/`, progressive enhancement in `site.js`).
The county research layer lives in `tools/research.py` — every figure has a
source URL and a check date (**refresh quarterly**; a refresh is an edit
there plus a re-run, not a copy hunt). Matrix copy lives in
`tools/matrix.py`; each page is 1,100+ words and ≥75% unique vs its
siblings (the 40% rule, measured, with margin). `sitemap.xml` is now
generated by `tools/pages.py` from the page list — never hand-edit it.

Photography: hero + four county slots carry hand-picked Pexels photos
(sources and licence notes in `photos-in/SOURCES.md`). Portrait,
before/after and project slots remain illustrations pending Peter's photos.
Favicons and the og-home social card are real (og-home.jpg is generated in
brand type from the package fonts).

Blocking (all on Peter — see CLIENT-ACTIONS.md for the chase email):
reconciled numbers, LA County yes/no, hours conflict, DBA filing + Blair's
legal read, his project photos. Ops: Netlify form notifications + the
RESimpli hop are documented in CLIENT-ACTIONS.md and not yet set up.
