# HARDT — build notes

What's real, what's a placeholder, and what's blocking the next pages.
Read this before touching copy.

---

## Live in this build

| File | State |
|---|---|
| `index.html` | Homepage, complete |
| `thank-you/index.html` | Post-submit page, noindexed |
| `assets/site.css` | Full design system — every page inherits it |
| `assets/fonts.css` + `assets/fonts/` | Self-hosted brand faces, 87KB, 3 variable WOFF2 |
| `netlify.toml` | Headers, HSTS, cache policy, noindex on `/thank-you/` |
| `robots.txt`, `sitemap.xml` | Sitemap lists only live URLs — add each page as it ships |

Verified in Chromium at 1440px and 390px: one `<h1>`, clean heading order,
zero horizontal overflow, no JS errors, valid JSON-LD, **zero WCAG AA contrast
failures**, no tap target under 24px. Dark coverage is 17% — inside the brand's
85/15 rule.

---

## Placeholders — must be replaced before launch

**Phone number.** `(619) 000-0000` / `+1-619-000-0000` appears in the header,
the offer section, the footer, the thank-you page, and twice in the JSON-LD.
Deliberately invalid so it can't route anywhere real if it slips out. This is
the canonical NAP number — once Peter confirms it, it must match GBP and every
citation byte for byte.

```
grep -rn "000-0000\|0000000" .
```

**Founder portrait.** `.shot` slot in the founder section renders an honest
placeholder rather than stock. Peter has a studio headshot on a dark background;
it does **not** meet the brand spec (warm daylight, work clothes, at the front
door of a finished project). Needs shooting.

**Social image.** `/assets/img/og-home.jpg` is referenced but not created.
1200×630, charcoal ground, cream lockup.

**Favicon set.** `/assets/img/favicon.ico` and `apple-touch-icon.png` are
referenced but not present — they exist in `HARDT Brand Package/05 Favicon &
Social/` and just need copying in. `mark.svg` is already in place.

---

## Deliberately NOT on the page

Everything here was available in the intake and left off on purpose.

- **No homes-bought count.** The intake said "5+ homes bought" but also "12
  families helped", "2 years operating" against a 2021 start, and "3 counties"
  against a project list covering two. Nothing gets published until the real
  figures come back. The trust strip uses only what's verifiable: *Since 2021*,
  *Four counties*, *~14 days*, *No assignments*.
- **No reviews or testimonials.** One Google review exists on the Fluid
  Developments profile. Nothing goes on-site until it's verifiable and
  attributed. FTC rules apply.
- **No project photos or case studies.** All five projects Peter listed are in
  Kern (4) and Lancaster (1). None in San Diego, Riverside or San Bernardino.
- **No stock photography anywhere.** Brand rule, and the page is built to work
  on type and colour alone so it never becomes tempting.

---

## Copy that came straight from Peter

Used close to verbatim because it's better than anything we'd write for him:

- The whole **"list it on the open market when…"** column — his answer to when
  a seller should *not* sell to him. Nobody in this category publishes this.
- The **"I don't buy"** list — his exact criteria, published so people don't
  waste an afternoon finding out on a call.
- The **founder section** — condensed from his BMX-to-real-estate story,
  wording preserved.

His story ends "HARDT homes was born." Now that the DBA is **HARDT Real
Estate**, that line needs his sign-off on the About page wording.

---

## Legal line in the footer

> HARDT Real Estate buys property as a principal for its own account. We are not
> a licensed real estate brokerage, we do not represent buyers or sellers, and we
> do not provide legal, tax or financial advice.

Added because the DBA contains "Real Estate" while Peter holds no DRE licence.
It states the exemption he actually operates under, in plain language, on every
page. **Blair at API Law should read this line** along with the foreclosure page.

---

## Lead form

Posts to Netlify Forms as `hardt-lead`, honeypot on `company`, redirects to
`/thank-you/`. Field order is deliberate: **address first, situation second,
contact last** — the address is the lowest-commitment question and the one most
likely to get a distressed seller started at 11pm.

After first deploy: **Site configuration → Forms → Form notifications**, add
email + the RESimpli push. Peter wants text-on-lead and a RESimpli record with
lead source `website` and campaign `website`. RESimpli has no native capture, so
that's a Zapier or webhook hop — not built yet.

---

## Next pages, in order

1. `/how-it-works/`, `/about/`, `/contact/`, `/what-we-buy/` — the spine
2. Four service hubs — `/sell-my-house-fast/`, `/inherited-house/`,
   `/stop-foreclosure/`, `/sell-rental-property/`
3. Four county hubs, then the 16 county×service matrix pages
4. Legal: `/privacy/`, `/terms/`, `/accessibility/`

The header and footer already link to all of these, so **they 404 until built**.
Fine on a preview URL, not fine on a live domain — either finish the spine before
DNS cutover or temporarily trim the nav.

---

## Still blocking

1. **Phone number** — canonical NAP, blocks GBP and every citation
2. **Real numbers** — blocks the trust strip and the About page
3. **LA County yes/no** — Peter checked it and has the Lancaster project;
   would add a fifth county hub and four matrix pages
4. **Hours** — GBP answer said Mon–Sat 8–6, response-time answer said 7 days.
   The site currently says Mon–Sat, matching the GBP answer
5. **Founder photography** — blocks the About page and every county page's proof
   block
6. **County research** — recorder, probate court, transfer tax, housing stock per
   county. This is what keeps the matrix pages off the doorway-page pile
