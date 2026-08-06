#!/usr/bin/env python3
"""
Generates every page of hardtrealestate.com from one shared shell.

Why a generator rather than 17 hand-written files: the header, footer,
schema graph and metadata rules have to be identical everywhere. Hand
copying them is how sites end up with three different footers and two
missing canonicals.

Run from the repo root:  python3 tools/build.py
"""
import os, json, re, html, hashlib


def pic(slot, alt, cls="media media--4x3", tag=None, eager=False, w=1200, h=900):
    """A <picture> for one image slot.

    Uses assets/img/<slot>.webp|jpg once a real photo has been processed in
    (tools/process_photos.py), and falls back to assets/img/<slot>.svg
    otherwise — so photography can arrive one image at a time without
    touching any page markup.
    """
    d = "assets/img"
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'

    if os.path.exists(f"{d}/{slot}.webp"):
        def srcset(ext):
            one, two = f"/assets/img/{slot}.{ext}", f"/assets/img/{slot}@2x.{ext}"
            return f'{one} 1x, {two} 2x' if os.path.exists(f"{d}/{slot}@2x.{ext}") else one
        inner = (f'<picture>'
                 f'<source type="image/webp" srcset="{srcset("webp")}">'
                 f'<img src="/assets/img/{slot}.jpg" srcset="{srcset("jpg")}" '
                 f'alt="{alt}" width="{w}" height="{h}" {load}>'
                 f'</picture>')
        badge = ""                       # a real photo needs no disclaimer
    else:
        inner = f'<img src="/assets/img/{slot}.svg" alt="{alt}" width="{w}" height="{h}" {load}>'
        badge = f'<span class="media__tag">{tag}</span>' if tag else ""

    return f'<div class="{cls}">{inner}{badge}</div>'


def og_img(slot):
    """OG image for a slot: the processed photo if one exists, else the svg."""
    return (f"/assets/img/{slot}.jpg" if os.path.exists(f"assets/img/{slot}.jpg")
            else f"/assets/img/{slot}.svg")


def rev(path):
    """Content hash appended as a query string.

    Netlify caches /assets/*.css for a week. Without this, a deploy ships new
    HTML against a stale stylesheet — which is exactly how the hero ended up
    rendering above the headline instead of behind it.
    """
    try:
        h = hashlib.md5(open(path.lstrip("/"), "rb").read()).hexdigest()[:8]
        return f"{path}?v={h}"
    except OSError:
        return path

# ─── The canonical origin ────────────────────────────────────────────────
# Every absolute URL on the site is built from this: canonical, og:url and
# og:image. It MUST be a host that actually serves the site, because link
# previews fetch og:image over the network. Pointing it at a domain that is
# still parked is what made iMessage fall back to scraping a random photo
# off the page instead of showing the share card.
#
# Cutover completed Aug 2026: the domain resolves to Netlify with a valid
# certificate, so this is the live origin and the staging noindex is gone.
# Override for a preview build:  HARDT_SITE_URL=https://example.com python3 tools/pages.py
SITE = os.environ.get("HARDT_SITE_URL", "https://hardtrealestate.com").rstrip("/")
PHONE_DISPLAY = "(707) 489-6236"
PHONE_E164 = "+1-707-489-6236"
PHONE_HREF = "tel:+17074896236"
EMAIL = "peter@hardtrealestate.com"

SERVICES = [
    ("sell-my-house-fast", "Sell as-is",          "Sell Your House As-Is"),
    ("inherited-house",    "Inherited &amp; probate", "Inherited &amp; Probate Property"),
    ("stop-foreclosure",   "Foreclosure &amp; liens", "Foreclosure, Liens &amp; Title Problems"),
    ("sell-rental-property","Selling a rental",   "Selling a Tenant-Occupied Rental"),
]
COUNTIES = [
    ("san-diego-county",      "San Diego County",      "san-diego",
     "San Diego, Chula Vista, Escondido, El Cajon, La Mesa, Santee, Lemon Grove, National City and Ramona"),
    ("riverside-county",      "Riverside County",      "riverside",
     "Riverside, Temecula, Murrieta and Perris"),
    ("san-bernardino-county", "San Bernardino County", "san-bernardino",
     "San Bernardino, Fontana, Rancho Cucamonga, Redlands and Highland"),
    ("kern-county",           "Kern County",           "kern",
     "Bakersfield, Shafter, Wasco, Tehachapi and Ridgecrest"),
]

MARK_DARK = ('<svg width="30" height="30" viewBox="0 0 100 100" aria-hidden="true" focusable="false">'
 '<g fill="#1A1A1A" stroke="#1A1A1A" stroke-width="3" stroke-linejoin="round">'
 '<path d="M20 21 L27 14 H33 V86 H27 L20 79 Z"/><path d="M80 21 L73 14 H67 V86 H73 L80 79 Z"/>'
 '<rect x="39" y="44" width="22" height="12"/></g></svg>')
MARK_LIGHT = MARK_DARK.replace('#1A1A1A', '#F0EBE4').replace('width="30" height="30"', 'width="26" height="26"')

PHONE_ICON = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
 'stroke-width="2.1" stroke-linecap="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 '
 '19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 '
 '.4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.1a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 '
 '1.7 2Z"/></svg>')


# ───────────────────────────────────────────── shell
def head(p):
    og = p.get("og", og_img("og-home"))
    extra = p.get("head", "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<link rel="canonical" href="{SITE}{p['url']}">
{'<meta name="robots" content="noindex, nofollow">' if p.get('noindex') else ''}
<meta property="og:type" content="{p.get('ogtype','website')}">
<meta property="og:site_name" content="HARDT">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:url" content="{SITE}{p['url']}">
<meta property="og:image" content="{SITE}{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{p.get('ogalt', 'HARDT. Every situation has a way forward.')}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image:alt" content="{p.get('ogalt', 'HARDT. Every situation has a way forward.')}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/img/mark.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<meta name="theme-color" content="#1A1A1A">
<link rel="preload" href="/assets/fonts/red-hat-display-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/dm-sans-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{rev("/assets/fonts.css")}">
<link rel="stylesheet" href="{rev("/assets/site.css")}">
<noscript><style>[data-reveal]{{opacity:1!important;transform:none!important}}</style></noscript>
{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(active=""):
    nav = [("/how-it-works/", "How it works"), ("/what-we-buy/", "What we buy"),
           ("/areas/", "Where we buy"), ("/resources/", "Resources"), ("/about/", "About us")]
    def _a(u, t):
        cur = ' aria-current="page"' if u == active else ''
        return f'<a href="{u}"{cur}>{t}</a>'
    links = "".join(_a(u, t) for u, t in nav)
    msvc = "".join(f'<a href="/{s}/">{n}</a>' for s, n, _ in SERVICES)
    mcty = "".join(f'<a href="/{s}/">{n}</a>' for s, n, _, _ in COUNTIES)
    return f"""<header class="site-head">
  <div class="shell site-head__in">
    <a class="lockup" href="/" aria-label="HARDT home">{MARK_DARK}<span class="lockup__hair"></span><span class="lockup__word">HARDT</span></a>
    <nav class="nav" aria-label="Main">{links}</nav>
    <div class="head-actions">
      <a class="tel" href="{PHONE_HREF}">{PHONE_ICON}{PHONE_DISPLAY}</a>
      <a class="btn btn--primary" href="/contact/">Get my offer</a>
      <button class="burger" type="button" data-nav-toggle aria-expanded="false" aria-controls="mobile-nav" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
<div class="mobile-nav" id="mobile-nav" hidden>
  {links}
  <a href="/situations/">Situations we handle</a>
  <a href="/how-weve-helped/">How we&rsquo;ve helped</a>
  <a href="/contact/">Get my offer</a>
  <p class="mn-h">Situations</p><div class="mn-sub">{msvc}</div>
  <p class="mn-h">Counties</p><div class="mn-sub">{mcty}</div>
  <p class="mn-h">Reach us</p><div class="mn-sub"><a href="{PHONE_HREF}">{PHONE_DISPLAY}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div>
"""


def crumbs(trail):
    if not trail:
        return ""
    items = ['<li><a href="/">Home</a></li>']
    for i, (u, t) in enumerate(trail):
        items.append(f'<li><a href="{u}">{t}</a></li>' if i < len(trail) - 1 else f'<li>{t}</li>')
    return f'<nav class="breadcrumb shell" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def footer():
    svc = "".join(f'<li><a href="/{s}/">{n}</a></li>' for s, n, _ in SERVICES)
    cty = "".join(f'<li><a href="/{s}/">{n}</a></li>' for s, n, _, _ in COUNTIES)
    return f"""<footer class="site-foot">
  <div class="shell">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="lockup" href="/" aria-label="HARDT home">{MARK_LIGHT}<span class="lockup__hair"></span><span class="lockup__word" style="color:#F0EBE4;font-size:17px">HARDT</span></a>
        <p style="margin-top:16px;max-width:30ch">Founder&#8209;led home buying across San Diego, Riverside, San Bernardino and Kern counties.</p>
        <p class="serif" style="color:var(--bronze-light);font-size:1.05rem;margin-top:20px">Built on Integrity.</p>
      </div>
      <div><p class="foot-h">Situations</p><ul class="foot-list">{svc}</ul></div>
      <div><p class="foot-h">Counties</p><ul class="foot-list">{cty}</ul></div>
      <div>
        <p class="foot-h">Company</p>
        <ul class="foot-list">
          <li><a href="/about/">About us</a></li><li><a href="/how-it-works/">How it works</a></li>
          <li><a href="/what-we-buy/">What we buy</a></li><li><a href="/situations/">Situations we handle</a></li>
          <li><a href="/how-weve-helped/">How we&rsquo;ve helped</a></li>
          <li><a href="/resources/">Resources</a></li><li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
      <div>
        <p class="foot-h">Reach us</p>
        <ul class="foot-list">
          <li><a href="{PHONE_HREF}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Mon&ndash;Sat, 8am&ndash;6pm</li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <div>&copy; 2026 HARDT &middot; a d/b/a of Fluid Developments LLC &middot; Southern California</div>
      <div><a href="/privacy/">Privacy</a> &nbsp;&middot;&nbsp; <a href="/terms/">Terms</a> &nbsp;&middot;&nbsp; <a href="/accessibility/">Accessibility</a></div>
    </div>
    <p class="small" style="margin-top:26px;max-width:78ch;color:rgba(240,235,228,.38);font-size:.79rem">
      HARDT buys property as a principal for its own account. We are not a licensed real estate
      brokerage, we do not represent buyers or sellers, and we do not provide legal, tax or financial advice.
    </p>
  </div>
</footer>
<div class="callbar" data-callbar>
  <a class="btn btn--ghost" href="{PHONE_HREF}">Call</a>
  <a class="btn btn--primary" href="/contact/">Get my offer</a>
</div>
<script src="{rev("/assets/site.js")}" defer></script>
"""


# ───────────────────────────────────────────── schema
def graph(p):
    org = {
        "@type": "Organization", "@id": f"{SITE}/#org", "name": "HARDT",
        "legalName": "Fluid Developments LLC", "alternateName": "HARDT",
        "url": f"{SITE}/", "logo": f"{SITE}/assets/img/mark.svg", "foundingDate": "2021",
        "slogan": "Every situation has a way forward.",
        "description": ("Founder-led home buying and renovation across Southern California. HARDT buys "
                        "houses as-is directly from owners, as a principal, without assigning contracts."),
        "founder": {"@id": f"{SITE}/#peter"},
        "areaServed": [{"@type": "AdministrativeArea", "name": f"{n}, California"} for _, n, _, _ in COUNTIES],
        "contactPoint": {"@type": "ContactPoint", "telephone": PHONE_E164, "contactType": "sales",
                         "areaServed": "US-CA", "availableLanguage": "English"},
    }
    biz = {
        "@type": "LocalBusiness", "@id": f"{SITE}/#business", "name": "HARDT",
        "parentOrganization": {"@id": f"{SITE}/#org"}, "url": f"{SITE}/",
        "image": SITE + og_img("og-home"), "telephone": PHONE_E164, "email": EMAIL,
        "priceRange": "$$",
        # Service-area business: no locality published. The verification address
        # lives on the Google Business Profile and is hidden there.
        "address": {"@type": "PostalAddress", "addressRegion": "CA", "addressCountry": "US"},
        "areaServed": [{"@type": "AdministrativeArea", "name": f"{n}, California"} for _, n, _, _ in COUNTIES],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
            "opens": "08:00", "closes": "18:00"}],
    }
    person = {
        "@type": "Person", "@id": f"{SITE}/#peter", "name": "Peter Eberhardt",
        "jobTitle": "Founder", "worksFor": {"@id": f"{SITE}/#org"},
        "knowsAbout": ["Buying houses as-is", "Probate and inherited property sales in California",
                       "Pre-foreclosure and Notice of Default", "Tenant-occupied property sales",
                       "Residential renovation"],
    }
    site = {"@type": "WebSite", "@id": f"{SITE}/#site", "url": f"{SITE}/", "name": "HARDT",
            "publisher": {"@id": f"{SITE}/#org"}, "inLanguage": "en-US"}
    page = {"@type": "WebPage", "@id": f"{SITE}{p['url']}#webpage", "url": f"{SITE}{p['url']}",
            "name": p["title"], "description": p["desc"], "isPartOf": {"@id": f"{SITE}/#site"},
            "about": {"@id": f"{SITE}/#org"}}

    nodes = [org, biz, person, site, page]

    if p.get("trail"):
        elems = [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"}]
        for i, (u, t) in enumerate(p["trail"], start=2):
            elems.append({"@type": "ListItem", "position": i, "name": re.sub("&amp;", "&", t),
                          "item": f"{SITE}{u}"})
        nodes.append({"@type": "BreadcrumbList", "@id": f"{SITE}{p['url']}#crumbs", "itemListElement": elems})

    if p.get("service"):
        # Matrix pages pass service_area to scope the Service to one county;
        # the four service hubs cover all four.
        area = ([{"@type": "AdministrativeArea", "name": f"{p['service_area']}, California"}]
                if p.get("service_area") else
                [{"@type": "AdministrativeArea", "name": f"{n}, California"}
                 for _, n, _, _ in COUNTIES])
        nodes.append({"@type": "Service", "@id": f"{SITE}{p['url']}#service",
            "serviceType": re.sub("&amp;", "&", p["service"]),
            "provider": {"@id": f"{SITE}/#org"},
            "areaServed": area,
            "description": p["desc"]})

    if p.get("faq"):
        nodes.append({"@type": "FAQPage", "@id": f"{SITE}{p['url']}#faq",
            "mainEntity": [{"@type": "Question", "name": re.sub("<[^>]+>", "", q),
                            "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
                           for q, a in p["faq"]]})

    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": nodes}, indent=None,
                         separators=(",", ":"))
            + "</script>")


# ───────────────────────────────────────────── partials
def faq_block(items, dark=False):
    rows = "".join(
        f'<div class="acc__item"><button class="acc__q" type="button">{q}</button>'
        f'<div class="acc__a">{a}</div></div>' for q, a in items)
    return f'<div class="acc" data-accordion>{rows}</div>'


def cta(head_, sub, label="Get my offer", href="/contact/"):
    """End-of-page CTA band. When it points at the contact page it
    renders an address-first mini form (GET) instead of a button, so
    every page ends with the funnel's first field rather than a link to
    it. The contact page reads ?address= and continues from there."""
    if href == "/contact/":
        action = f"""<form class="lead-mini" action="/contact/" method="get">
      <label class="sr-only" for="cta-address">Property address</label>
      <input type="text" id="cta-address" name="address" placeholder="Property address"
        autocomplete="street-address">
      <button class="btn btn--primary btn--lg" type="submit">{label}</button>
    </form>"""
    else:
        action = f'<a class="btn btn--primary btn--lg" href="{href}">{label}</a>'
    return f"""<section class="band band--tight"><div class="shell">
  <div class="cta-strip" data-reveal>
    <div><h2>{head_}</h2><p>{sub}</p></div>
    {action}
  </div></div></section>"""


def render(p):
    return (head(p) + header(p.get("active", "")) + crumbs(p.get("trail"))
            + '<main id="main">' + p["body"] + "</main>" + footer() + graph(p)
            + "\n</body>\n</html>\n")


def write(p):
    path = ("index.html" if p["url"] == "/" else p["url"].strip("/") + "/index.html")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    open(path, "w").write(render(p))
    return path
