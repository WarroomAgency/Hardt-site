#!/usr/bin/env python3
"""Content for every page. Run: python3 tools/pages.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build import (write, cta, faq_block, pic, og_img, SERVICES, COUNTIES,
                   PHONE_DISPLAY, PHONE_HREF, EMAIL, PHONE_ICON, SITE)
from research import RESEARCH, TENANT, FORECLOSURE_STATE, CHECKED, sources_line
from matrix import M, FAQ_EXTRA, NARR_EXTRA

P = []


def _srcset(slot, ext):
    """1x always; 2x only when the file actually exists. A srcset that
    promises a 2x that isn't there breaks the image entirely on retina
    displays — the browser requests the 404 and renders nothing."""
    import os
    one = f"/assets/img/{slot}.{ext}"
    two = f"/assets/img/{slot}@2x.{ext}"
    return f"{one} 1x, {two} 2x" if os.path.exists(two.lstrip("/")) else one


def hero_img():
    """Hero art is positioned by .hero__bg itself, so no .media wrapper."""
    import os
    if os.path.exists("assets/img/hero.webp"):
        return (f'<picture><source type="image/webp" srcset="{_srcset("hero", "webp")}">'
                f'<img src="/assets/img/hero.jpg" srcset="{_srcset("hero", "jpg")}" '
                'alt="" width="1800" height="1150" fetchpriority="high"></picture>')
    return '<img src="/assets/img/hero.svg" alt="" width="1800" height="1150" fetchpriority="high">'


def ba_img(slot, alt):
    """The comparison slider needs bare <img> with its own class, no wrapper."""
    import os
    cls = "ba__" + slot
    if os.path.exists(f"assets/img/{slot}.webp"):
        return (f'<img class="{cls}" src="/assets/img/{slot}.jpg" '
                f'srcset="{_srcset(slot, "jpg")}" '
                f'alt="{alt}" width="1200" height="800">')
    return f'<img class="{cls}" src="/assets/img/{slot}.svg" alt="{alt}" width="1200" height="800">'


TEL = f'<a class="tel" href="{PHONE_HREF}">{PHONE_ICON}{PHONE_DISPLAY}</a>'

# ══════════════════════════════════════════════ HOME
P.append(dict(
    url="/", title="Sell Your House As-Is in Southern California | HARDT",
    desc="Founder-led home buying across San Diego, Riverside, San Bernardino and Kern counties. We don't assign contracts. One walkthrough, one honest number.",
    body=f"""
<section class="hero hero--art" data-hero>
  <div class="hero__bg">{hero_img()}</div>
  <div class="shell">
    <p class="eyebrow">San&nbsp;Diego &middot; Riverside &middot; San&nbsp;Bernardino &middot; Kern</p>
    <h1 class="h-hero">Sell your house as&#8209;is, anywhere in Southern California.</h1>
    <p class="hero__promise">One walkthrough. One honest number. And every option on the table, including the ones that don&rsquo;t involve us.</p>
    <p class="hero__note">No repairs, no cleaning out, no showings. Tenants in place is fine. So is a house full of forty years of somebody&rsquo;s life.</p>
    <div class="btnrow">
      <a class="btn btn--primary btn--lg" href="/contact/">Get my offer</a>
      <a class="btn btn--ghost btn--lg" href="/how-it-works/">See how it works</a>
    </div>
    <div class="trust">
      <div class="trust__i"><span class="trust__k">Since 2021</span><span class="trust__v">Buying and renovating across Southern California</span></div>
      <div class="trust__i"><span class="trust__k">Four counties</span><span class="trust__v">San Diego, Riverside, San Bernardino and Kern</span></div>
      <div class="trust__i"><span class="trust__k">~14 days</span><span class="trust__v">Typical time from first call to close</span></div>
      <div class="trust__i"><span class="trust__k">No assignments</span><span class="trust__v">We don&rsquo;t sell your contract to somebody else</span></div>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="shell">
    <p class="eyebrow" data-reveal>What we handle</p>
    <h2 class="h-sect" data-reveal>When a house becomes a problem, everyone shows up with an offer. Nobody shows up with a conversation.</h2>
    <p class="lede" data-reveal>Four situations we deal with constantly. If yours isn&rsquo;t here, call anyway. It probably still has a way forward.</p>
    <div class="grid grid--4" style="margin-top:46px">
      <a class="card" href="/sell-my-house-fast/" data-reveal><h3 class="h-card">The house needs work</h3><p>Deferred maintenance, a failed inspection, damage you&rsquo;d rather not pay to fix. As&#8209;is means as&#8209;is.</p><span class="card__link">Selling as-is</span></a>
      <a class="card" href="/inherited-house/" data-reveal data-reveal-delay="80"><h3 class="h-card">You inherited it</h3><p>Probate, siblings, and a house that can come with everything still in it. We&rsquo;ll carry the heavy part.</p><span class="card__link">Inherited &amp; probate</span></a>
      <a class="card" href="/stop-foreclosure/" data-reveal data-reveal-delay="160"><h3 class="h-card">You&rsquo;re behind on payments</h3><p>A Notice of Default isn&rsquo;t the end of the road. There are more options than most people are told.</p><span class="card__link">Foreclosure &amp; liens</span></a>
      <a class="card" href="/sell-rental-property/" data-reveal data-reveal-delay="240"><h3 class="h-card">You&rsquo;re done being a landlord</h3><p>Tenants in place is fine. Truly. Occupied, mid&#8209;lease, deferred maintenance and all.</p><span class="card__link">Selling a rental</span></a>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell split">
    <div>
      <p class="eyebrow" data-reveal>The work</p>
      <h2 class="h-sect" data-reveal>We buy the house, then we actually fix it.</h2>
      <p data-reveal style="margin-top:22px">Every house we take on gets renovated and put back into use. That&rsquo;s the business, not paperwork, not flipping a contract to whoever answers first.</p>
      <p data-reveal>It also means the number we give you is real. We&rsquo;re pricing a project we have to finish ourselves, so there&rsquo;s no incentive to promise something now and renegotiate later.</p>
      <p data-reveal><a href="/what-we-buy/">See exactly what we buy &rarr;</a></p>
    </div>
    <div data-reveal>
      <div class="ba" data-compare>
        {ba_img("before","A house before renovation")}
        {ba_img("after","The same house after renovation")}
        <span class="ba__lbl ba__lbl--b">Before</span><span class="ba__lbl ba__lbl--a">After</span>
        <button class="ba__handle" type="button" role="slider" tabindex="0"
          aria-label="Compare before and after" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50"></button>
      </div>
      <p class="small" style="margin-top:12px">Drag to compare. Placeholder art. Real project photography is being shot.</p>
    </div>
  </div>
</section>

<section class="band dark">
  <div class="shell">
    <p class="eyebrow" data-reveal>How it works</p>
    <h2 class="h-sect" data-reveal>Three steps, and a number you can check.</h2>
    <div class="grid grid--3" style="margin-top:46px">
      <div data-reveal><span class="step__n">Step 01</span><h3 class="h-card">Tell us the situation</h3><p>A conversation, not a pitch. What the house is, what&rsquo;s going on, what you&rsquo;d want to happen. No pressure and no countdown.</p></div>
      <div data-reveal data-reveal-delay="90"><span class="step__n">Step 02</span><h3 class="h-card">One walkthrough</h3><p>We come look at it in person. You don&rsquo;t clean, repair, or move anything. It takes about half an hour.</p></div>
      <div data-reveal data-reveal-delay="180"><span class="step__n">Step 03</span><h3 class="h-card">One honest number</h3><p>With the math shown. Take it, leave it, or take it to somebody else to check.</p></div>
    </div>
    <div class="btnrow"><a class="btn btn--ghost" href="/how-it-works/">The full process</a></div>
  </div>
</section>

<section class="band paper">
  <div class="shell">
    <p class="eyebrow" data-reveal>The honest math</p>
    <h2 class="h-sect" data-reveal>Sometimes listing it is the better answer. When it is, we&rsquo;ll tell you.</h2>
    <p class="lede" data-reveal>A cash sale isn&rsquo;t right for every house or every person. Here&rsquo;s how we&rsquo;d think about it if it were our own family.</p>
    <div class="compare" style="margin-top:42px" data-reveal>
      <div class="compare__col">
        <p class="h-kicker" style="color:var(--bronze-ink)">List it on the open market when</p>
        <ul><li>You have the time to wait for the right buyer</li><li>The house is in good condition and doesn&rsquo;t need repairs</li><li>You want the highest gross price on paper, and you&rsquo;re fine paying commissions, title and escrow fees, and any repairs the buyer asks for out of that number</li></ul>
      </div>
      <div class="compare__col">
        <p class="h-kicker">Talk to us when</p>
        <ul><li>The house needs work you don&rsquo;t want to pay for or manage</li><li>The timeline matters more than the last few thousand dollars</li><li>There are tenants, contents, liens, or a probate in the middle of it</li><li>You want one number and one person, start to finish</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="band--tight band dark">
  <div class="shell quote">
    <p class="tagline serif" data-reveal>Every situation has a way forward.</p>
    <p class="quote__proof" data-reveal>We don&rsquo;t assign contracts. If it doesn&rsquo;t close, we buy it ourselves.</p>
    <p class="quote__attr" data-reveal>Peter Eberhardt &middot; Founder</p>
  </div>
</section>

<section class="band">
  <div class="shell split">
    <div>
      <p class="eyebrow" data-reveal>Who you&rsquo;re dealing with</p>
      <h2 class="h-sect" data-reveal>The name on the company is my name.</h2>
      <p data-reveal style="margin-top:22px">Through my twenties I chased an Olympic dream in BMX racing. Real estate started as a detour: a way to buy the time and money to keep racing. What I found instead was the thing I&rsquo;d actually been missing: purpose, impact, and people.</p>
      <p data-reveal>I also found a corner of this business that nobody regulates, where distressed homeowners don&rsquo;t know what their options are, what questions to ask, or who to ask them to. I thought there could be a better way to do it.</p>
      <div class="btnrow"><a class="btn btn--ghost" href="/about/">More about Peter</a></div>
    </div>
    <div data-reveal>{pic("portrait","Peter Eberhardt, founder of HARDT","media media--4x5",tag="Portrait to be shot",w=900,h=1150)}</div>
  </div>
</section>

<section class="band paper">
  <div class="shell">
    <p class="eyebrow" data-reveal>Recent work</p>
    <h2 class="h-sect" data-reveal>Houses we bought, fixed, and put back into use.</h2>
    <p class="lede" data-reveal>Five of the most recent. Photography from each of these is being prepared: the illustrations below are standing in until it lands.</p>
    <div class="grid grid--4" style="margin-top:44px">
      <div class="card" style="padding:0;overflow:hidden" data-reveal>
        {pic("project-1","A Bakersfield house bought and renovated by HARDT","media media--4x3",tag="Photo to come",w=1000,h=750)}
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Shenandoah Drive</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="70">
        {pic("project-2","A Bakersfield house bought and renovated by HARDT","media media--4x3",tag="Photo to come",w=1000,h=750)}
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Cale Court</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="140">
        {pic("project-3","A Bakersfield house bought and renovated by HARDT","media media--4x3",tag="Photo to come",w=1000,h=750)}
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Terrace Way &amp; Huskey Drive</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="210">
        {pic("project-4","A Lancaster house bought and renovated by HARDT","media media--4x3",tag="Photo to come",w=1000,h=750)}
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Lancaster</p><p style="margin:0">Graphic Street</p></div>
      </div>
    </div>
    <div class="btnrow" data-reveal><a class="btn btn--ghost" href="/how-weve-helped/">The stories behind these houses</a></div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>Where we buy</p>
    <h2 class="h-sect" data-reveal>Four counties, and we drive to all of them.</h2>
    <p class="lede" data-reveal>Boots on the ground from the border to Bakersfield, and we do the walkthrough in person in every one of them.</p>
    <div class="grid grid--4" style="margin-top:42px">
      {"".join(f'''<a class="county" href="/{s}/" data-reveal data-reveal-delay="{i*70}" style="padding:0;overflow:hidden">
        {pic(f"county-{img}", f"A residential street in {n}", "media media--4x3", w=1000, h=750)}
        <div style="padding:22px 24px 26px"><p class="county__name">{n}</p><p class="county__cities">{c}</p>
        <span class="card__link" style="margin-top:14px;display:inline-block">Selling here</span></div></a>''' for i,(s,n,img,c) in enumerate(COUNTIES))}
    </div>
  </div>
</section>

{cta("Tell us about the house.", "Three questions, no obligation, and nobody else gets your information.")}
"""))

# ══════════════════════════════════════════════ HOW IT WORKS
HOW_FAQ = [
        ("Do I need to clean or repair anything first?",
         "<p>No. Leave it exactly as it is. You don't need to clear the house out, fix anything, or stage it. If there are contents you don't want, leave those too. We handle it.</p>"),
        ("How is the number worked out?",
         "<p>We look at what the house is worth once it's renovated, subtract what the renovation actually costs, subtract the cost of holding and reselling it, and leave a margin. We show you those figures. If you want to take them to an agent or a contractor to check, that's a reasonable thing to do.</p>"),
        ("How fast can this close?",
         "<p>Around two weeks is typical from the first call. Faster is sometimes possible. Slower is completely fine. If you need sixty days to find your next place, we set the date for sixty days.</p>"),
        ("What does it cost me?",
         "<p>Nothing. No commission, no fees to us, and we cover standard closing costs. What we offer is what you walk away with, minus anything owed on the property such as a mortgage payoff or liens.</p>"),
        ("Am I committed once I send the form?",
         "<p>No. Sending the form starts a conversation. You're not committed to anything until you sign a purchase agreement, and you can stop at any point before that without owing anyone an explanation.</p>"),
]
P.append(dict(
    url="/how-it-works/", active="/how-it-works/",
    trail=[("/how-it-works/", "How it works")],
    title="How Selling to HARDT Works | HARDT",
    desc="A conversation, one walkthrough, one number with the math shown. Typical close is about 14 days, and the date is yours. No repairs, no showings, no assignments.",
    faq=HOW_FAQ,
    body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>The process</p>
    <h1 class="h-sect" data-reveal>No pressure, no repairs, and a number with the math shown.</h1>
    <p class="lede" data-reveal>Most people who call have never sold a house this way before. Here is exactly what happens, step by step, so there are no surprises.</p>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell">
    <div class="grid grid--2" style="align-items:start">
      <div data-reveal>
        <span class="step__n">Step 01</span><h2 class="h-card" style="font-size:1.5rem">You tell us the situation</h2>
        <p>Call, text, or send the form. We talk for ten minutes about the house and what's going on around it: a probate, a tenant, a job in another state, a repair bill you don't want.</p>
        <p>This is a conversation, not a qualification script. If it becomes clear a cash sale isn't your best move, we'll say so on this call rather than three weeks from now.</p>
      </div>
      <div data-reveal data-reveal-delay="90">
        <span class="step__n">Step 02</span><h2 class="h-card" style="font-size:1.5rem">One walkthrough, about half an hour</h2>
        <p>We come and look at the house in person, not an inspector, not a photographer, not a team. You don't clean, fix, or move anything, and you don't need to be embarrassed about any of it. We've seen houses in every condition there is.</p>
        <p>If the property is tenant-occupied we work around the tenant's schedule and their legal notice period.</p>
      </div>
      <div data-reveal>
        <span class="step__n">Step 03</span><h2 class="h-card" style="font-size:1.5rem">One number, and the math behind it</h2>
        <p>Usually within a day. You get the figure and the reasoning: what we think it's worth finished, what the work costs, what holding and reselling costs, and the margin left over.</p>
        <p>Take it, leave it, or take it to an agent for a second opinion. It doesn't expire because a timer ran out.</p>
      </div>
      <div data-reveal data-reveal-delay="90">
        <span class="step__n">Step 04</span><h2 class="h-card" style="font-size:1.5rem">You pick the closing date</h2>
        <p>We open escrow with a title company and they handle the money and the paperwork. Title gets cleared. That's their job and ours, not yours.</p>
        <p>About two weeks is typical. If you need longer to sort out your next place, say so and we set the date around you.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <h2 class="h-sect" data-reveal>What you don&rsquo;t have to do</h2>
    <div class="figrow" style="margin-top:36px" data-reveal>
      <div><p class="h-kicker">No repairs</p><p class="small">Not the roof, not the plumbing, not the thing the last inspector flagged.</p></div>
      <div><p class="h-kicker">No cleaning out</p><p class="small">Take what you want. Leave the rest, including furniture and everything in the garage.</p></div>
      <div><p class="h-kicker">No showings</p><p class="small">One visit from one person. No lockbox, no strangers walking through on a Sunday.</p></div>
      <div><p class="h-kicker">No commissions</p><p class="small">There's no agent in the middle, so there's no commission coming out of your number.</p></div>
      <div><p class="h-kicker">No financing risk</p><p class="small">No lender means no appraisal gap and no loan falling through a week before closing.</p></div>
      <div><p class="h-kicker">No assignment</p><p class="small">Your contract doesn't get sold to a stranger. If it doesn't close, we buy it ourselves.</p></div>
    </div>
  </div>
</section>

<section class="band dark">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Questions people actually ask</p>
    <h2 class="h-sect" data-reveal>Straight answers.</h2>
    <div style="margin-top:38px" data-reveal>{faq_block(HOW_FAQ)}</div>
  </div>
</section>

{cta("Ready to see a number?", "Send the address and we'll come look at it in person.")}
"""))

# ══════════════════════════════════════════════ WHAT WE BUY
P.append(dict(
    url="/what-we-buy/", active="/what-we-buy/",
    trail=[("/what-we-buy/", "What we buy")],
    title="What We Buy, and What We Don't | HARDT",
    desc="Single and multi-family up to about $1.2M, in any condition, across four Southern California counties. Our buying criteria, published in full.",
    body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>Straight answers</p>
    <h1 class="h-sect" data-reveal>What we buy, and what we don&rsquo;t.</h1>
    <p class="lede" data-reveal>Published so you don&rsquo;t waste an afternoon finding out on a phone call. If your property falls outside this, we&rsquo;ll usually still know someone worth calling.</p>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell">
    <div class="grid grid--2">
      <div class="card" data-reveal>
        <p class="h-kicker">We buy</p>
        <ul class="checks" style="margin-top:6px">
          <li>Single family and multi&#8209;family, up to about <strong>$1.2M</strong></li>
          <li>Houses needing major work, including fire and water damage</li>
          <li>Inherited and probate property</li>
          <li>Pre&#8209;foreclosure, Notice of Default, liens and title problems</li>
          <li>Tenant&#8209;occupied rentals, mid&#8209;lease and Section 8</li>
          <li>Houses still full of contents</li>
          <li>Divorce, relocation and estate situations</li>
        </ul>
      </div>
      <div class="card" data-reveal data-reveal-delay="90">
        <p class="h-kicker" style="color:var(--gray)">We don&rsquo;t buy</p>
        <ul class="nots" style="margin-top:6px">
          <li>Anything under $100,000</li>
          <li>Houses with less than about 50% equity</li>
          <li>Subject&#8209;to deals with no equity</li>
          <li>Vacant land or lots</li>
          <li>Commercial buildings</li>
          <li>Timeshares</li>
          <li>Anything where we can&rsquo;t clear title for you</li>
        </ul>
      </div>
    </div>
    <p class="small" style="margin-top:26px;max-width:62ch">That last one matters more than it sounds. If the title can&rsquo;t be cleared, you can&rsquo;t actually sell the house to anybody, and a buyer who tells you otherwise is setting up a problem for later.</p>
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>Condition is not a problem</p>
    <h2 class="h-sect" data-reveal>&ldquo;As&#8209;is&rdquo; means what it says.</h2>
    <div class="grid grid--3" style="margin-top:42px">
      <div class="card" data-reveal><h3 class="h-card">Structural and systems</h3><p>Foundation movement, roof at end of life, failed plumbing or electrical, an HVAC that hasn&rsquo;t run in years.</p></div>
      <div class="card" data-reveal data-reveal-delay="80"><h3 class="h-card">Damage</h3><p>Fire, water, mould, storm damage, or a house that&rsquo;s simply sat empty for a long time.</p></div>
      <div class="card" data-reveal data-reveal-delay="160"><h3 class="h-card">Contents</h3><p>Full garages, full rooms, a lifetime of belongings. Take what matters to you and leave the rest.</p></div>
      <div class="card" data-reveal><h3 class="h-card">Permits</h3><p>Unpermitted additions, converted garages, work a previous owner did over a weekend in 1988.</p></div>
      <div class="card" data-reveal data-reveal-delay="80"><h3 class="h-card">Occupancy</h3><p>Tenants who are staying, tenants who won&rsquo;t leave, family members living there, or squatters.</p></div>
      <div class="card" data-reveal data-reveal-delay="160"><h3 class="h-card">Paperwork</h3><p>Probate, liens, back taxes, a Notice of Default, or heirs who don&rsquo;t entirely agree with each other.</p></div>
    </div>
  </div>
</section>

{cta("Not sure if yours fits?", "Send it over. A ten minute call costs you nothing and we'll tell you straight.")}
"""))

# ══════════════════════════════════════════════ AREAS
P.append(dict(
    url="/areas/", active="/areas/",
    trail=[("/areas/", "Where we buy")],
    title="Where We Buy: Four Southern California Counties | HARDT",
    desc="HARDT buys houses across San Diego, Riverside, San Bernardino and Kern counties, from the border up to Bakersfield, with the walkthrough done in person every time.",
    body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>Where we buy</p>
    <h1 class="h-sect" data-reveal>Four counties, and we drive to all of them.</h1>
    <p class="lede" data-reveal>We&rsquo;ll drive about four hours for a walkthrough, which covers everything from the border up to Bakersfield.</p>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell">
    <div class="grid grid--2">
      {"".join(f'''<a class="county" href="/{s}/" data-reveal data-reveal-delay="{i*80}" style="padding:0;overflow:hidden">
        {pic(f"county-{img}", f"A residential street in {n}", "media media--4x3", w=1000, h=750)}
        <div style="padding:26px 28px"><p class="county__name">{n}</p><p class="county__cities">{c}</p>
        <span class="card__link" style="margin-top:14px;display:inline-block">Selling in {n.replace(" County","")}</span></div></a>''' for i,(s,n,img,c) in enumerate(COUNTIES))}
    </div>
  </div>
</section>

<section class="band">
  <div class="shell shell--narrow">
    <h2 class="h-sect" data-reveal>Places we&rsquo;d rather be honest about</h2>
    <p data-reveal style="margin-top:20px">There are mountain communities we don&rsquo;t buy in: Big Bear, Lake Arrowhead, Crestline, Bear Valley Springs, Frazier Park and Pine Mountain Club among them. The market up there behaves differently enough that we&rsquo;d be guessing, and guessing with somebody&rsquo;s house is how people get hurt.</p>
    <p data-reveal>If that&rsquo;s where your property is, tell us anyway. We&rsquo;d rather point you to someone who actually knows that market than pretend we do.</p>
  </div>
</section>

{cta("Not sure if you're in range?", "Send the address. If it's outside what we cover, we'll tell you in one message.")}
"""))

# ══════════════════════════════════════════════ ABOUT
P.append(dict(
    url="/about/", active="/about/", ogtype="profile",
    trail=[("/about/", "About Peter")],
    title="About Peter Eberhardt, Founder | HARDT",
    desc="HARDT is founder-led. Peter Eberhardt buys, renovates and rebuilds houses across Southern California, and refuses to take advantage of people having a hard year.",
    body=f"""
<section class="band band--tight">
  <div class="shell split">
    <div>
      <p class="eyebrow" data-reveal>Who you&rsquo;re dealing with</p>
      <h1 class="h-sect" data-reveal>The name on the company is my name.</h1>
      <p class="lede" data-reveal>Peter Eberhardt &middot; Founder, HARDT &middot; Southern California</p>
    </div>
    <div data-reveal>{pic("portrait","Peter Eberhardt, founder of HARDT","media media--4x5",tag="Portrait to be shot",eager=True,w=900,h=1150)}</div>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell shell--narrow">
    <p data-reveal>Through my twenties I chased an Olympic dream in the sport of BMX racing. Getting into real estate started out as a short detour from that dream: a tool that would give me more time and money to chase the Olympic path.</p>
    <p data-reveal>I realised fairly quickly that I was missing much more than time and money. I was missing purpose, impact, and relationships.</p>
    <p data-reveal>Getting into real estate, I also discovered how unregulated the space is where distressed homes get bought and sold. I watched homeowners in situations where they didn&rsquo;t know what all their options were, didn&rsquo;t know the right questions to ask, and didn&rsquo;t know who to ask them to.</p>
    <p data-reveal>I wondered whether there could be a better way. A better service. A better impact: something that could actually get a homeowner out of the situation they were in and show them a way forward to the next chapter.</p>
    <p data-reveal>That&rsquo;s what HARDT is. We refuse to take advantage of homeowners, and we believe every situation has a way forward.</p>
    <p class="serif" style="font-size:1.4rem;color:var(--bronze-ink);margin-top:32px" data-reveal>Every situation has a way forward.</p>
  </div>
</section>

<section class="band dark">
  <div class="shell">
    <p class="eyebrow" data-reveal>How we operate</p>
    <h2 class="h-sect" data-reveal>Four things that don&rsquo;t change.</h2>
    <div class="grid grid--2" style="margin-top:42px">
      <div data-reveal><h3 class="h-card">You talk to us</h3><p>Every enquiry comes to our team directly. Not a call centre, not a script, and never a lead that gets sold to four investors at once.</p></div>
      <div data-reveal data-reveal-delay="80"><h3 class="h-card">We don&rsquo;t assign contracts</h3><p>Some buyers put a house under contract and then sell that contract on. We don&rsquo;t. If it doesn&rsquo;t close, we buy it ourselves.</p></div>
      <div data-reveal><h3 class="h-card">The math is shown</h3><p>You see how the number was reached: finished value, cost of work, cost of holding and reselling, margin. Check it with anyone you like.</p></div>
      <div data-reveal data-reveal-delay="80"><h3 class="h-card">Bad news arrives at the same volume</h3><p>If listing with an agent would put more money in your pocket, we&rsquo;ll say so on the first call. It costs us deals. It&rsquo;s still the right thing.</p></div>
    </div>
    <div class="btnrow"><a class="btn btn--ghost" href="/how-weve-helped/">See how this plays out</a></div>
  </div>
</section>

<section class="band">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>The business</p>
    <h2 class="h-sect" data-reveal>Plainly stated.</h2>
    <p data-reveal style="margin-top:22px">HARDT is a d/b/a of Fluid Developments LLC, operating across San Diego, Riverside, San Bernardino and Kern counties since 2021. We buy houses with our own money, renovate them using local subcontractors, and put them back into use.</p>
    <p data-reveal>We buy as a principal for our own account. We are not a licensed real estate brokerage, we don&rsquo;t represent buyers or sellers, and we don&rsquo;t give legal, tax or financial advice. When you need that kind of advice (in a probate or a foreclosure you often do), we&rsquo;ll tell you to go get it.</p>
  </div>
</section>

{cta("Want to talk it through?", "Call us directly, or send the address and we'll come look at it.")}
"""))

# ══════════════════════════════════════════════ CONTACT
P.append(dict(
    url="/contact/", active="/contact/",
    trail=[("/contact/", "Contact")],
    title="Get Your Offer | HARDT",
    desc="Three questions and we'll be in touch, usually within 15 minutes between 8am and 6pm. No obligation, no pressure, and nobody else gets your information.",
    body=f"""
<section class="band dark" id="offer">
  <div class="shell split">
    <div>
      <p class="eyebrow" data-reveal>Start here</p>
      <h1 class="h-sect" data-reveal>Tell us about the house.</h1>
      <p class="lede" data-reveal>Three questions. No obligation, no pressure, and no one else gets your information.</p>
      <ul class="rail" style="margin-top:36px" data-reveal>
        <li><strong>You talk to our team, not a call centre.</strong> Every lead comes straight to us.</li>
        <li><strong>A reply within 15 minutes</strong>, 8am&ndash;6pm. Outside those hours, first thing next morning.</li>
        <li><strong>We don&rsquo;t assign contracts.</strong> If it doesn&rsquo;t close, we buy it ourselves.</li>
        <li><strong>No countdown clocks.</strong> The offer doesn&rsquo;t expire because a timer ran out.</li>
      </ul>
      <p class="small" style="margin-top:34px">Would rather just talk? {TEL}</p>
    </div>
    <form class="form" name="hardt-lead" method="POST" data-netlify="true" netlify-honeypot="company" action="/thank-you/" data-validate data-reveal>
      <input type="hidden" name="form-name" value="hardt-lead">
      <p class="hp"><label>Leave this empty <input name="company" tabindex="-1" autocomplete="off"></label></p>
      <div class="field"><label for="address">Property address</label><span class="help">Street and city is plenty to start.</span>
        <input type="text" id="address" name="Property address" autocomplete="street-address" required></div>
      <div class="field"><label for="situation">What&rsquo;s going on with it?</label>
        <select id="situation" name="Situation" required>
          <option value="">Choose the closest one&hellip;</option>
          <option>It needs work I don&rsquo;t want to do</option>
          <option>I inherited it / it&rsquo;s in probate</option>
          <option>I&rsquo;m behind on payments</option>
          <option>It&rsquo;s a rental and I&rsquo;m done</option>
          <option>Divorce, relocation, or a life change</option>
          <option>Something else</option>
        </select></div>
      <div class="field"><label for="name">Your name</label>
        <input type="text" id="name" name="Name" autocomplete="name" required></div>
      <div class="field"><label for="phone">Phone or email</label><span class="help">Whichever you&rsquo;d rather we use.</span>
        <input type="text" id="phone" name="Phone or email" autocomplete="tel" required></div>
      <div class="field"><label for="notes">Anything else? <span style="font-weight:400;color:var(--gray)">(optional)</span></label>
        <textarea id="notes" name="Notes" rows="3"></textarea></div>
      <button class="btn btn--primary btn--lg" type="submit" style="width:100%;margin-top:6px">Get my offer</button>
      <p class="small" style="margin:16px 0 0;text-align:center">No obligation. We never sell your information.</p>
    </form>
  </div>
</section>

<section class="band">
  <div class="shell">
    <div class="figrow" data-reveal>
      <div><p class="h-kicker">Phone</p><p>{TEL}</p><p class="small">Call or text. It reaches us, not an answering service.</p></div>
      <div><p class="h-kicker">Email</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p class="small">Fine for documents and photos.</p></div>
      <div><p class="h-kicker">Hours</p><p>Monday&ndash;Saturday, 8am&ndash;6pm</p><p class="small">Outside those hours we&rsquo;ll reply first thing the next morning.</p></div>
    </div>
    <p class="small" style="margin-top:28px">HARDT &middot; a d/b/a of Fluid Developments LLC. We buy across San Diego, Riverside, San Bernardino and Kern counties.</p>
  </div>
</section>
"""))

# ══════════════════════════════════════════════ SERVICES
SVC = {
 "sell-my-house-fast": dict(
   h1="Sell your house as&#8209;is, in any condition.",
   title="Sell Your House Fast As-Is in Southern California | HARDT",
   desc="Sell a house that needs work, without repairs, showings or commissions. One walkthrough, one number with the math shown, and a closing date you choose.",
   lede="Deferred maintenance, a failed inspection, damage you don't want to pay to fix. None of it disqualifies a house here.",
   body_intro="<p>The most common reason people call is simple: the house needs more work than they want to take on. Sometimes that's a roof and a kitchen. Sometimes it's a house that's been empty three years and everything in it has failed at once.</p><p>You don't need to fix any of it. We price the house as it stands today, and the work becomes our problem.</p>",
   points=["Roofs, foundations, plumbing and electrical at end of life",
           "Fire, water, mould and storm damage",
           "Unpermitted additions and converted garages",
           "Houses that have sat vacant for years",
           "Hoarding situations and full contents"],
   faq=[("Is the house too far gone?","<p>Almost certainly not. Condition changes the number, not whether we're interested. The only real disqualifiers are on our <a href=\"/what-we-buy/\">what we buy</a> page, and none of them are about condition.</p>"),
        ("Do I have to clear it out?","<p>No. Take what matters to you and leave everything else, including furniture, tools and whatever's in the garage.</p>"),
        ("Will you lowball me because it needs work?","<p>You'll see the math: finished value, cost of the work, cost of holding and reselling, and the margin. If the repair estimate looks high to you, get a contractor to check it. That's a reasonable thing to do and we'd rather you did.</p>")]),
 "inherited-house": dict(
   h1="You inherited a house. Now what?",
   title="Selling an Inherited House in California | HARDT",
   desc="Probate-fluent, patient, and willing to carry the heavy part, including the contents. Sell an inherited house in Southern California without repairs or showings.",
   lede="Probate, siblings, and a house that can come with everything still in it. This is the situation we're asked about most, and the one people are least prepared for.",
   body_intro="<p>Inheriting a house usually arrives alongside a death, which means the paperwork lands at the worst possible time. Most people have never been through probate and don't know what they're allowed to do or when.</p><p>We deal with this constantly. There's rarely a rush from our side, and we're comfortable waiting for the court where waiting is what's needed.</p>",
   points=["Property still going through probate",
           "Several heirs who don't entirely agree",
           "A house full of a lifetime of belongings",
           "Out-of-state executors who can't get here",
           "Deferred maintenance from the last years of someone's life"],
   faq=[("Can I sell before probate finishes?","<p>Sometimes, depending on the authority the court has granted and how the property was held. It's a legal question, not a marketing one: the honest answer is that you should ask a probate attorney, and we'll work to whatever timeline they give you.</p>"),
        ("What about everything still in the house?","<p>Leave it. Take the things that matter to your family and we'll deal with the rest. Nobody should have to empty a parent's house on a deadline.</p>"),
        ("There are four of us and we don't agree. Can you help?","<p>We can be patient and we can put the same clear number in front of everyone, which sometimes helps. What we can't do is mediate, and if the disagreement is serious, that's a job for an attorney.</p>")]),
 "stop-foreclosure": dict(
   h1="A Notice of Default isn&rsquo;t the end of the road.",
   title="Facing Foreclosure in Southern California? | HARDT",
   desc="Understand the California trustee-sale timeline and every option on the table, including the ones that don't involve selling. Straight information, no pressure.",
   lede="If you're behind on payments, the most valuable thing you can have right now is accurate information about your options, not another offer.",
   body_intro="<p>People in this situation usually get a stack of letters and a lot of pressure. What they rarely get is a plain explanation of how the process actually works and how much time is genuinely left.</p><p>So that's what this conversation is. Sometimes the answer is a reinstatement, a loan modification, or a short sale with your lender. Sometimes it's selling before the sale date. Occasionally it's letting it go, and if that's genuinely your best outcome, we'll say so.</p>",
   points=["Behind on payments but not yet in default",
           "A Notice of Default has been recorded",
           "A trustee sale date has been set",
           "Property tax arrears or a tax lien",
           "Mechanic's liens or judgments clouding title"],
   faq=[("How much time do I actually have?","<p>California's non-judicial foreclosure process runs on statutory timelines from the recording of a Notice of Default through to a trustee's sale. The specifics depend on your lender and what's already been recorded, so the first thing to do is find out exactly where in that process you are.</p>"),
        ("Will selling hurt my credit less than foreclosure?","<p>Often, yes, but this is a question for a HUD-approved housing counsellor or an attorney, not for a buyer. We're not going to advise you on your credit in order to buy your house.</p>"),
        ("Do you charge for this conversation?","<p>No, and we don't charge for anything else either. We're not foreclosure consultants and we don't take fees to help with a default. We buy houses. If buying yours is the right answer we'll make an offer; if it isn't, we'll tell you what we'd do.</p>")],
   legal="<p class=\"small\" style=\"margin-top:26px;max-width:70ch\">This page is general information, not legal or financial advice. California law regulates foreclosure consultants and equity purchasers. HARDT is not a foreclosure consultant, does not charge fees for foreclosure assistance, and buys property only as a principal. If you are facing foreclosure, speak with a HUD-approved housing counsellor or an attorney about your specific situation.</p>"),
 "sell-rental-property": dict(
   h1="Tenants in place is fine. Truly.",
   title="Sell a Rental Property With Tenants in Place | HARDT",
   desc="Sell a tenant-occupied rental in Southern California as-is: mid-lease, Section 8, deferred maintenance and all. No showings, no evictions, no repairs.",
   lede="Most buyers want the property vacant, cleaned and repaired. That means evicting someone, and it means months of work before you can even list.",
   body_intro="<p>The usual advice to a landlord who wants out is to get the tenant out first. That's slow, expensive, and hard on somebody who probably hasn't done anything wrong.</p><p>We buy occupied. The tenancy transfers with the property, and in many cases the tenant simply stays, which is better for everyone and considerably faster for you.</p>",
   points=["Tenants mid-lease or month-to-month",
           "Section 8 and other assisted tenancies",
           "Non-paying tenants and eviction already in progress",
           "Years of deferred maintenance between turnovers",
           "Small multi-family and duplexes"],
   faq=[("Do I have to evict anyone first?","<p>No. We'd generally rather you didn't. We buy the property with the tenancy in place and take on the landlord's obligations at close.</p>"),
        ("What if the tenant won't allow a walkthrough?","<p>We work within the notice period the law requires and around the tenant's schedule. If access genuinely can't be arranged we can often work from what you can tell us plus exterior condition.</p>"),
        ("What about the security deposit and prepaid rent?","<p>Handled through escrow as part of closing, the same as any other credit or proration. It doesn't come out of your pocket at the table.</p>")]),
}

for slug, label, longname in SERVICES:
    d = SVC[slug]
    others = "".join(
        f'<a class="card" href="/{s2}/"><h3 class="h-card">{n2}</h3><span class="card__link">Read more</span></a>'
        for s2, n2, _ in SERVICES if s2 != slug)
    counties = "".join(f'<a class="pill" href="/{s2}/{slug}/" style="text-decoration:none">{n2}</a>'
                       for s2, n2, _, _ in COUNTIES)
    P.append(dict(
        url=f"/{slug}/", trail=[(f"/{slug}/", label)], title=d["title"], desc=d["desc"],
        service=longname, faq=d["faq"],
        body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>{label}</p>
    <h1 class="h-sect" data-reveal>{d['h1']}</h1>
    <p class="lede" data-reveal>{d['lede']}</p>
    <div class="btnrow" data-reveal><a class="btn btn--primary" href="/contact/">Get my offer</a>{TEL}</div>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell split">
    <div data-reveal>{d['body_intro']}</div>
    <div data-reveal>
      <p class="h-kicker">Situations we see</p>
      <ul class="checks">{"".join(f"<li>{x}</li>" for x in d['points'])}</ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>How it goes</p>
    <h2 class="h-sect" data-reveal>The same three steps, whatever the situation.</h2>
    <div class="figrow" style="margin-top:36px" data-reveal>
      <div><p class="h-kicker">01 &middot; The conversation</p><p class="small">Ten minutes on the phone. What the property is and what's happening around it.</p></div>
      <div><p class="h-kicker">02 &middot; One walkthrough</p><p class="small">Half an hour, in person, no cleaning or repairs first.</p></div>
      <div><p class="h-kicker">03 &middot; One number</p><p class="small">With the math shown, and a closing date you choose.</p></div>
    </div>
    {d.get('legal','')}
  </div>
</section>

<section class="band dark">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Questions</p>
    <h2 class="h-sect" data-reveal>Straight answers.</h2>
    <div style="margin-top:38px" data-reveal>{faq_block(d['faq'])}</div>
  </div>
</section>

<section class="band paper">
  <div class="shell">
    <p class="eyebrow" data-reveal>Where</p>
    <h2 class="h-sect" data-reveal>We handle this across all four counties.</h2>
    <p style="margin-top:20px" data-reveal>{counties}</p>
    <p class="eyebrow" style="margin-top:48px" data-reveal>Other situations</p>
    <div class="grid grid--3" style="margin-top:16px">{others}</div>
  </div>
</section>

{cta("Tell us about the property.", "Three questions, no obligation, and you talk to us directly.")}
"""))

# ══════════════════════════════════════════════ COUNTIES
CTY = {
 "san-diego-county": ("our home county",
   "San Diego County is the heart of where we work. Anything here is a short drive and usually a same-week walkthrough.",
   "Coastal North County, the inland valleys and the East County foothills are three different housing markets wearing one county's name. A 1950s East County ranch and a 1990s Chula Vista tract house need completely different work, and the number reflects that."),
 "riverside-county": ("the corridor",
   "Riverside County runs from the Inland Empire down through the Temecula Valley, and we cover the western and southwestern side of it.",
   "Newer subdivisions here often carry Mello-Roos assessments and solar or PACE liens attached to the property rather than the owner. Those don't stop a sale, but they have to be found early. They're a common reason a deal falls apart late with another buyer."),
 "san-bernardino-county": ("the inland empire",
   "From the older neighbourhoods of San Bernardino and Redlands out through Fontana, Rancho Cucamonga and Highland.",
   "The housing stock varies enormously by decade here, which matters for what's behind the walls: galvanised plumbing, aluminium wiring and panels that no longer pass inspection are all common in the older parts of the county."),
 "kern-county": ("the north end",
   "Bakersfield and the surrounding towns are the northern end of what we cover. It's a long drive from the southern end of our territory, and we make it regularly.",
   "Kern is where a good deal of our renovation work has been. Prices are lower than the coastal counties, which changes the arithmetic on what's worth doing to a house: a full renovation that pencils in Chula Vista may not pencil in Wasco, and vice versa."),
}

for slug, name, img, cities in COUNTIES:
    kicker, intro, local = CTY[slug]
    cfaq = [(f"Which {name.replace(' County','')} cities do you buy in?",
             f"<p>{cities}, plus the smaller communities around them. If you're not sure whether you're in range, send the address and we'll tell you in one message.</p>"),
            ("Do you buy houses that need work here?",
             "<p>Yes. That's most of what we do. Condition changes the number, not whether we're interested.</p>"),
            ("How quickly can you see the property?",
             "<p>Usually within a day or two, since this is home.</p>" if slug=="san-diego-county"
             else "<p>Usually within a few days. We batch trips to the area, so tell us your timing and we will work around it.</p>")]
    short = name.replace(" County", "")
    # Situation cards on a county hub link to that county's matrix pages —
    # the hub is the county's front door, the matrix pages are the rooms.
    svc_cards = "".join(
        f'<a class="card" href="/{slug}/{s2}/"><h3 class="h-card">{n2}</h3><span class="card__link">In {short}</span></a>'
        for s2, n2, _ in SERVICES)
    r = RESEARCH[slug]
    local_cards = "".join(
        f'<div class="card" data-reveal><p class="h-kicker">{r[k]["h"]}</p><p>{r[k]["html"]}</p></div>'
        for k in ("recorder", "dtt", "probate", "stock", "killers"))
    P.append(dict(
        url=f"/{slug}/", trail=[("/areas/", "Where we buy"), (f"/{slug}/", name)],
        title=f"We Buy Houses in {name}, CA | HARDT",
        desc=f"Sell a house as-is in {name}: {cities.split(',')[0]} and across the county. No repairs, no showings, no commissions. One walkthrough and one honest number.",
        og=og_img(f"county-{img}"),
        faq=cfaq,
        body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>{kicker}</p>
    <h1 class="h-sect" data-reveal>We buy houses in {name}.</h1>
    <p class="lede" data-reveal>{intro}</p>
    <div class="btnrow" data-reveal><a class="btn btn--primary" href="/contact/">Get my offer</a>{TEL}</div>
  </div>
</section>

<section class="band--tight">
  <div class="shell">
    <div data-reveal>{pic(f"county-{img}", f"A residential street in {name}", "media media--wide", tag="Illustration &middot; local photography to come", eager=True, w=1400, h=640)}</div>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell split">
    <div data-reveal>
      <p class="h-kicker">Cities we cover</p>
      <p>{cities}.</p>
      <p class="small">Not listed? Send the address anyway. The line on a map matters less than the drive.</p>
    </div>
    <div data-reveal>
      <p class="h-kicker">What&rsquo;s different here</p>
      <p>{local}</p>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>The local details</p>
    <h2 class="h-sect" data-reveal>How {short} actually works when you sell.</h2>
    <p class="lede" data-reveal>The courthouse, the recorder, the tax line and the housing stock: the specifics that decide how a {short} sale really goes.</p>
    <div class="grid grid--2" style="margin-top:42px">{local_cards}</div>
    {sources_line(slug)}
  </div>
</section>

<section class="band paper">
  <div class="shell">
    <p class="eyebrow" data-reveal>Situations</p>
    <h2 class="h-sect" data-reveal>What we handle in {short}.</h2>
    <div class="grid grid--4" style="margin-top:42px">{svc_cards}</div>
  </div>
</section>

<section class="band dark">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>{short} questions</p>
    <h2 class="h-sect" data-reveal>Straight answers.</h2>
    <div style="margin-top:38px" data-reveal>{faq_block(cfaq)}</div>
  </div>
</section>

{cta(f"Have a house in {short}?", "Send the address and we'll come look at it in person.")}
"""))

# ══════════════════════════════════════════════ COUNTY × SERVICE MATRIX
# The ranking engine: /{county}/{service}/. Copy lives in tools/matrix.py,
# local facts in tools/research.py — every figure sourced and dated.
CTY_BY_SLUG = {s: (n, img, cities) for s, n, img, cities in COUNTIES}
SVC_BY_SLUG = {s: (label, longname) for s, label, longname in SERVICES}

for (cslug, sslug), d in M.items():
    cname, cimg, ccities = CTY_BY_SLUG[cslug]
    slabel, slongname = SVC_BY_SLUG[sslug]
    cshort = cname.replace(" County", "")
    r = RESEARCH[cslug]

    # Four local-fact cards: the three the entry chose, plus the most
    # relevant remaining dimension (probate only where already chosen).
    fkeys = list(d["facts"])
    for k in ("recorder", "dtt", "stock", "killers"):
        if k not in fkeys and len(fkeys) < 4:
            fkeys.append(k)
    fact_cards = "".join(
        f'<div class="card" data-reveal><p class="h-kicker">{r[k]["h"]}</p><p>{r[k]["html"]}</p></div>'
        for k in fkeys)

    faqs = d["faq"] + [FAQ_EXTRA[(cslug, sslug)]]

    # Walkthrough timing is genuinely different per county — say so.
    visit = {
        "san-diego-county": "Usually within a day or two. This county is home.",
        "riverside-county": "Within a few days. We batch southwest-county trips and work around your timing.",
        "san-bernardino-county": "Within a few days, valley or High Desert. Tell us your timing and we&rsquo;ll route the trip around it.",
        "kern-county": "We&rsquo;re in Kern regularly. Walkthroughs usually land within the week, Ridgecrest included.",
    }[cslug]

    # Service-flavoured extras: the statutory clock on foreclosure pages,
    # the tenant-rules layer on rental pages.
    narr_extra = ""
    if sslug == "stop-foreclosure":
        narr_extra = f'<p>{FORECLOSURE_STATE}</p>'
    elif sslug == "sell-rental-property":
        narr_extra = f'<p>{TENANT[cslug]}</p>'
    narr_extra += NARR_EXTRA.get((cslug, sslug), "")
    # Service-level practical note, shared across counties for one service.
    SVC_NOTE = {
        "inherited-house": (
            "<p>The single biggest fork in any California probate sale is the representative&rsquo;s "
            "authority. <strong>Full authority</strong> under the Independent Administration of Estates "
            "Act usually means the representative can sell with notice to the heirs and no court "
            "hearing; <strong>limited authority</strong> means the sale is confirmed in court, which "
            "adds weeks and an overbid step. It&rsquo;s printed on the Letters. Look before you plan, "
            "and if probate hasn&rsquo;t been opened yet, tell your attorney you&rsquo;d like full authority "
            "requested. It routinely saves an estate a month or more.</p>"),
        "sell-my-house-fast": (
            "<p>What to have handy for the first call, none of it mandatory: roughly what you owe "
            "on the house, any insurance or inspection paperwork from recent years, and a sense of "
            "your ideal date to be done. That&rsquo;s it. The walkthrough needs no preparation at all. "
            "We have seen every version of &ldquo;I didn&rsquo;t have time to clean,&rdquo; and we are not "
            "grading.</p>"),
        "sell-rental-property": (
            "<p>Paper to gather when you&rsquo;re ready: the lease or a note of the verbal terms, the "
            "deposit amount, and the last tax bill. Everything else (estoppel, prorations, the "
            "housing-authority transfer where one applies) is escrow&rsquo;s routine, not yours.</p>"),
    }
    narr_extra += SVC_NOTE.get(sslug, "")

    legal_note = ""
    if d.get("legal"):
        legal_note = ('<p class="small" style="margin-top:26px;max-width:70ch">This page is general '
          'information, not legal or financial advice. California law regulates foreclosure '
          'consultants and equity purchasers. HARDT is not a foreclosure consultant, does not '
          'charge fees for foreclosure assistance, and buys property only as a principal. If you '
          'are facing foreclosure, speak with a HUD-approved housing counsellor or an attorney '
          'about your specific situation.</p>')

    same_svc = "".join(
        f'<a class="card" href="/{c2}/{sslug}/"><h3 class="h-card">{n2.replace(" County","")}</h3>'
        f'<span class="card__link">Same situation, {n2.replace(" County","")}</span></a>'
        for c2, n2, _, _ in COUNTIES if c2 != cslug)
    other_svc = "".join(
        f'<a class="card" href="/{cslug}/{s2}/"><h3 class="h-card">{n2}</h3>'
        f'<span class="card__link">In {cshort}</span></a>'
        for s2, n2, _ in SERVICES if s2 != sslug)

    P.append(dict(
        url=f"/{cslug}/{sslug}/",
        trail=[("/areas/", "Where we buy"), (f"/{cslug}/", cname), (f"/{cslug}/{sslug}/", slabel)],
        title=d["title"], desc=d["desc"],
        service=f"{slongname} in {cname}", service_area=cname,
        og=og_img(f"county-{cimg}"),
        faq=faqs,
        body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>{cshort} &middot; {slabel}</p>
    <h1 class="h-sect" data-reveal>{d['h1']}</h1>
    <p class="lede" data-reveal>{d['lede']}</p>
    <div class="btnrow" data-reveal><a class="btn btn--primary" href="/contact/">Get my offer</a>{TEL}</div>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell split">
    <div data-reveal>{d['intro']}</div>
    <div data-reveal>
      <p class="h-kicker">Where we buy in {cshort}</p>
      <p>{ccities}, plus the smaller communities around them.</p>
      <p class="small">Not listed? Send the address anyway: the line on a map matters less than the drive.</p>
      <p class="h-kicker" style="margin-top:26px">The ground rules</p>
      <ul class="checks"><li>No repairs, no cleaning out, no showings</li>
      <li>One walkthrough, not an inspector parade</li>
      <li>One number, with the math shown</li>
      <li>We don&rsquo;t assign contracts. If it doesn&rsquo;t close, we buy it ourselves.</li></ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>The local details</p>
    <h2 class="h-sect" data-reveal>What&rsquo;s specific to {cshort}.</h2>
    <div class="grid grid--2" style="margin-top:42px">{fact_cards}</div>
    {sources_line(cslug, fkeys)}
  </div>
</section>

<section class="band paper">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>On the ground</p>
    <h2 class="h-sect" data-reveal>{d['narr_h']}</h2>
    <div style="margin-top:24px" data-reveal>{d['narr']}{narr_extra}</div>
    {legal_note}
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>How it goes</p>
    <h2 class="h-sect" data-reveal>The same three steps, {cshort} timing.</h2>
    <div class="figrow" style="margin-top:36px" data-reveal>
      <div><p class="h-kicker">01 &middot; The conversation</p><p class="small">Ten minutes on the phone. What the property is and what&rsquo;s happening around it. You talk to us, not a call centre.</p></div>
      <div><p class="h-kicker">02 &middot; One walkthrough</p><p class="small">{visit} Half an hour, no cleaning or repairs first.</p></div>
      <div><p class="h-kicker">03 &middot; One number</p><p class="small">With the math shown: finished value, work budget, margin, and a closing date you choose.</p></div>
    </div>
  </div>
</section>

<section class="band dark">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>{cshort} questions</p>
    <h2 class="h-sect" data-reveal>Straight answers.</h2>
    <div style="margin-top:38px" data-reveal>{faq_block(faqs)}</div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>Nearby</p>
    <h2 class="h-sect" data-reveal>The same situation, county by county.</h2>
    <div class="grid grid--3" style="margin-top:36px">{same_svc}</div>
    <p class="eyebrow" style="margin-top:48px" data-reveal>Other situations in {cshort}</p>
    <div class="grid grid--3" style="margin-top:16px">{other_svc}</div>
  </div>
</section>

{cta(f"Have a house in {cshort}?", "Send the address and we'll come look at it in person.")}
"""))

# ══════════════════════════════════════════════ HOW WE'VE HELPED
# Story-led proof, not a portfolio. Every fact below comes from Peter's
# intake (06 · Proof and 07 · Reviews): the foreclosure save, the Huskey
# Drive close, Graphic Street, and the five project addresses. Nothing
# is embellished; where we don't know a detail, the story doesn't claim
# one. Names are withheld until Peter confirms each person is happy to
# be named (chase item in CLIENT-ACTIONS.md). No Review/testimonial
# JSON-LD on purpose: these are our accounts, not endorsements.
P.append(dict(
    url="/how-weve-helped/",
    trail=[("/how-weve-helped/", "How we've helped")],
    title="How We've Helped Homeowners | HARDT",
    desc="Real situations we've been part of: a homeowner who kept his house, a sale that was falling apart, a house 250 miles from anywhere. Told plainly, not as ads.",
    og=og_img("after"),
    body=f"""
<section class="band band--tight">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>How we&rsquo;ve helped</p>
    <h1 class="h-sect" data-reveal>Some situations we&rsquo;ve been part of.</h1>
    <p class="lede" data-reveal>Most people who call us are somewhere in the middle of a hard year. These are a few of the situations we&rsquo;ve helped with, told the way they actually went. No names until each person has said they&rsquo;re comfortable being named, and no dressing anything up.</p>
    <p class="serif" data-reveal style="font-size:1.15rem;color:var(--bronze-ink);margin-top:18px">Every situation has a way forward.</p>
  </div>
</section>

<section class="band paper">
  <div class="shell shell--narrow">
    <p class="h-kicker" data-reveal>Behind on payments, auction date approaching</p>
    <h2 class="h-card" data-reveal style="font-size:1.5rem">He kept his house.</h2>
    <div data-reveal>
      <p style="margin-top:14px">A homeowner came to us in default, with the foreclosure clock already running. The easy thing, and the profitable thing, would have been to buy the house.</p>
      <p>It wasn&rsquo;t the right answer. Once we walked through his numbers and his options together, there was a route that let him catch up and stay. We helped him take it.</p>
      <p>He still lives there. We never bought anything, and that&rsquo;s the point: the first conversation is about your options, not our offer. Sometimes the way forward doesn&rsquo;t involve us, and we&rsquo;ll be the ones to say so.</p>
    </div>
    <p class="small" data-reveal style="margin-top:10px">If you&rsquo;re behind on payments, start with <a href="/resources/notice-of-default/">what a Notice of Default actually means</a>. It&rsquo;s free and it applies whether or not you ever talk to us.</p>
  </div>
</section>

<section class="band">
  <div class="shell shell--narrow">
    <p class="h-kicker" data-reveal>A sale collapsing a week before closing</p>
    <h2 class="h-card" data-reveal style="font-size:1.5rem">Huskey Drive, Bakersfield.</h2>
    <div data-reveal>
      <p style="margin-top:14px">The seller had a deal in hand, and the deal was dying. The buyer who&rsquo;d put the house under contract couldn&rsquo;t perform, which usually means the seller starts over from zero: new listing, new waiting, new uncertainty, with whatever deadline pushed them to sell still ticking.</p>
      <p>We stepped in, bought the house ourselves, and closed. The seller got the exit he&rsquo;d already planned around instead of a restart.</p>
      <p>This is what &ldquo;we don&rsquo;t assign contracts&rdquo; means in practice. When we sign, we&rsquo;re the ones on the hook to finish, and Huskey Drive is one of the houses we&rsquo;ve since renovated and put back into use.</p>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="shell shell--narrow">
    <p class="h-kicker" data-reveal>A long way from anywhere</p>
    <h2 class="h-card" data-reveal style="font-size:1.5rem">Graphic Street, Lancaster.</h2>
    <div data-reveal>
      <p style="margin-top:14px">Some houses sit where the usual buyers don&rsquo;t bother going. Graphic Street is in Lancaster, in the Antelope Valley: a long drive from the coastal markets where most cash buyers concentrate, and the kind of address that gets lowballed by mail and then ignored in person.</p>
      <p>We drove up, walked it, and bought it from its owner directly. Then we renovated it, the same as we do everywhere else. Distance changes the drive time, not the standard of work and not how straight the number is.</p>
    </div>
  </div>
</section>

<section class="band dark">
  <div class="shell split">
    <div>
      <p class="eyebrow" data-reveal>Before and after</p>
      <h2 class="h-sect" data-reveal>The work is the proof.</h2>
      <p data-reveal style="margin-top:20px">Every house we buy gets renovated and put back into use. Drag the slider: this is the part of the business we&rsquo;re actually in.</p>
      <p data-reveal class="small">Photography from all five recent projects is being prepared. As it lands, this page fills in with the real before-and-afters, house by house.</p>
    </div>
    <div data-reveal>
      <div class="ba" data-compare>
        {ba_img("before","A house before renovation")}
        {ba_img("after","The same house after renovation")}
        <span class="ba__lbl ba__lbl--b">Before</span><span class="ba__lbl ba__lbl--a">After</span>
        <button class="ba__handle" type="button" role="slider" tabindex="0"
          aria-label="Compare before and after" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50"></button>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>The list so far</p>
    <h2 class="h-sect" data-reveal>Five recent projects.</h2>
    <div class="grid grid--4" style="margin-top:42px">
      <div class="card" style="padding:0;overflow:hidden" data-reveal>
        {pic("project-1","A Bakersfield house bought and renovated by HARDT","media media--4x3",tag="Photo to come",w=1000,h=750)}
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Shenandoah Drive</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="70">
        {pic("project-2","A Bakersfield house bought and renovated by HARDT","media media--4x3",tag="Photo to come",w=1000,h=750)}
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Cale Court</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="140">
        {pic("project-3","A Bakersfield house bought and renovated by HARDT","media media--4x3",tag="Photo to come",w=1000,h=750)}
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Terrace Way &amp; Huskey Drive</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="210">
        {pic("project-4","A Lancaster house bought and renovated by HARDT","media media--4x3",tag="Photo to come",w=1000,h=750)}
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Lancaster</p><p style="margin:0">Graphic Street</p></div>
      </div>
    </div>
    <p class="small" data-reveal style="margin-top:22px">That&rsquo;s the whole list, not highlights. We&rsquo;d rather show you five real houses than imply fifty.</p>
  </div>
</section>

{cta("In the middle of something like this?", "Tell us the situation. The first conversation is about your options, not our offer.")}
"""))

# ══════════════════════════════════════════════ LEGAL
LEGAL = {
 "privacy": ("Privacy Policy", "How HARDT collects, uses and protects the information you send through this website.", f"""
<p>HARDT, a d/b/a of Fluid Developments LLC, operates this website. This policy explains what we collect and what we do with it.</p>
<h2 class="h-card" style="margin-top:34px">What we collect</h2>
<p>Only what you send us: the property address, the situation you select, your name, a phone number or email address, and any notes you add. We also collect standard analytics such as pages viewed and approximate location, which is not tied to your name.</p>
<h2 class="h-card" style="margin-top:30px">What we do with it</h2>
<p>We use it to contact you about your property and to prepare an offer. That's it.</p>
<h2 class="h-card" style="margin-top:30px">What we don't do</h2>
<p><strong>We do not sell your information, and we do not share it with other investors or lead buyers.</strong> This is common practice in our industry and we don't do it. We share information only with the parties needed to complete a transaction you have chosen to proceed with: a title company, an escrow officer, and where the law requires it.</p>
<h2 class="h-card" style="margin-top:30px">Your rights in California</h2>
<p>Under the CCPA and CPRA you can ask what personal information we hold about you, ask us to delete it, and ask us to correct it. We don't sell personal information, so there is nothing to opt out of on that front. To make a request, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2 class="h-card" style="margin-top:30px">Contact by phone and text</h2>
<p>If you give us a phone number we may call or text you about your property. You can tell us to stop at any time and we will.</p>
<h2 class="h-card" style="margin-top:30px">Cookies</h2>
<p>We use minimal analytics cookies to understand which pages are useful. We do not run advertising trackers on this site.</p>
<p class="small" style="margin-top:34px">Questions about any of this: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
 "terms": ("Terms of Use", "Terms governing use of the HARDT website, including our position as a principal buyer rather than a licensed brokerage.", f"""
<p>By using this website you agree to these terms.</p>
<h2 class="h-card" style="margin-top:34px">Who we are</h2>
<p>HARDT is a d/b/a of Fluid Developments LLC, operating in Southern California. <strong>We buy property as a principal for our own account.</strong> We are not a licensed real estate brokerage, we do not represent buyers or sellers in transactions, and we do not act as agents for anyone.</p>
<h2 class="h-card" style="margin-top:30px">Not advice</h2>
<p>Nothing on this site is legal, tax, financial or real estate advice. Content about probate, foreclosure, liens and title is general information and your situation will differ. Consult a qualified attorney, tax professional or HUD-approved housing counsellor about your circumstances.</p>
<h2 class="h-card" style="margin-top:30px">No offer is made here</h2>
<p>Nothing on this website constitutes an offer to purchase any property. Any offer will be made in writing, specific to a property, after a conversation and a walkthrough.</p>
<h2 class="h-card" style="margin-top:30px">Accuracy</h2>
<p>We work to keep this site accurate and current, but we make no warranty that it is free of errors. Market information changes.</p>
<h2 class="h-card" style="margin-top:30px">Your submissions</h2>
<p>When you send information through a form you confirm it is accurate to the best of your knowledge and that you have the authority to discuss the property.</p>
<p class="small" style="margin-top:34px">Governed by the laws of the State of California. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
 "accessibility": ("Accessibility", "Our commitment to WCAG 2.1 AA, what we've done to meet it, and how to tell us when we've fallen short.", f"""
<p>People reach this site in difficult circumstances, sometimes on an old phone and sometimes at two in the morning. It should work for everyone.</p>
<h2 class="h-card" style="margin-top:34px">The standard we build to</h2>
<p>We target <strong>WCAG 2.1 Level AA</strong>.</p>
<h2 class="h-card" style="margin-top:30px">What that means here</h2>
<ul class="checks" style="margin-top:14px">
  <li>Every text and background pairing on this site is tested to meet AA contrast. We adjusted our own brand colours to get there rather than the other way round</li>
  <li>The site works end to end with a keyboard, and focus is always visible</li>
  <li>Headings run in order, images carry alternative text, and form fields have real labels</li>
  <li>Animation is removed entirely for anyone whose system requests reduced motion</li>
  <li>Tap targets meet the minimum size on phones</li>
  <li>Text can be resized without breaking the layout</li>
</ul>
<h2 class="h-card" style="margin-top:30px">Where we know we fall short</h2>
<p>This site is under active construction and some sections still use placeholder artwork. If you find something that doesn't work with your assistive technology, we want to hear about it. That's a bug, not a preference.</p>
<h2 class="h-card" style="margin-top:30px">Tell us</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE_DISPLAY}. Describe what happened and what you were using, and we'll fix it. If you need to give us information about a property in another format, we'll take it however works for you, including over the phone.</p>"""),
}
for slug, (name, desc, body) in LEGAL.items():
    P.append(dict(url=f"/{slug}/", trail=[(f"/{slug}/", name)],
        title=f"{name} | HARDT", desc=desc,
        body=f"""<section class="band band--tight"><div class="shell shell--narrow">
  <p class="eyebrow" data-reveal>Legal</p><h1 class="h-sect" data-reveal>{name}</h1>
  <p class="small" style="margin-top:16px">Last updated August 2026</p>
</div></section>
<section class="band band--tight paper"><div class="shell shell--narrow" data-reveal>{body}</div></section>"""))


# ══════════════════════════════════════════════ RESOURCES
# Plain-English explainers. Educational, sourced, no sales pressure — these
# exist to be genuinely useful, linked to, and cited. Figures follow the same
# rule as everything else: sourced and dated, refreshed quarterly.

RES_ITEMS = [
    ("probate-timeline", "The California probate timeline",
     "What actually happens, in what order, and how long each step takes."),
    ("notice-of-default", "You got a Notice of Default. Now what?",
     "The statutory clock, your reinstatement rights, and the options at each stage."),
    ("prop-19", "Prop 19 and the house you inherited",
     "Why inheriting a house changed in 2021, and what it means for the property-tax bill."),
    ("selling-with-tenants", "Selling a rental with tenants in place",
     "The rules that protect your tenant, and how a sale works without anyone moving out."),
    ("cash-offer-vs-listing", "The honest math: cash offer vs. listing",
     "Side by side, with every cost on the table. Run your own numbers."),
]

P.append(dict(
    url="/resources/", active="/resources/",
    trail=[("/resources/", "Resources")],
    title="Homeowner Resources & Plain-English Guides | HARDT",
    desc="Plain-English guides to probate, foreclosure notices, Prop 19 and tenant-occupied sales in California, written to be useful, not to sell you anything.",
    body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>Resources</p>
    <h1 class="h-sect" data-reveal>The information, without the pitch.</h1>
    <p class="lede" data-reveal>Plain-English guides to the situations we get asked about most. Every figure is sourced and dated. None of it requires talking to us.</p>
  </div>
</section>
<section class="band band--tight paper">
  <div class="shell">
    <div class="grid grid--2" style="margin-top:8px">
      {"".join(f'''<a class="card" href="/resources/{s}/" data-reveal><h2 class="h-card">{t}</h2><p>{d}</p><span class="card__link">Read the guide</span></a>''' for s, t, d in RES_ITEMS)}
    </div>
    <p class="small" style="margin-top:34px">These guides are general information, not legal, tax or financial advice. For advice on your situation, talk to a licensed professional, and for foreclosure, a HUD-approved housing counsellor is free.</p>
  </div>
</section>
{cta("Rather just talk it through?", "Call us directly, or send the address and we'll come look at it in person.")}
"""))

RES_TRAIL = [("/resources/", "Resources")]

P.append(dict(
    url="/resources/probate-timeline/", trail=RES_TRAIL + [("/resources/probate-timeline/", "Probate timeline")],
    title="California Probate Timeline, Step by Step | HARDT",
    desc="How long California probate takes and what happens at each step: filing, letters, the four-month creditor window, inventory, and final distribution.",
    body=f"""
<section class="band band--tight">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Resources</p>
    <h1 class="h-sect" data-reveal>The California probate timeline, step by step.</h1>
    <p class="lede" data-reveal>Most heirs have never done this before. Here&rsquo;s the whole shape of it: what happens, in what order, and where the time actually goes.</p>
  </div>
</section>
<section class="band band--tight paper">
  <div class="shell shell--narrow" data-reveal>
    <p>Probate is the court process for transferring a person&rsquo;s property after death when there&rsquo;s no trust (or the trust doesn&rsquo;t cover everything). In California it runs through the Superior Court of the county where the person lived, and it runs on the court&rsquo;s calendar, which is the part nobody warns you about.</p>

    <h2 class="h-card" style="margin-top:34px">1. Filing the petition</h2>
    <p>Someone, usually the person named in the will or a close relative, files a Petition for Probate with the county&rsquo;s probate court. The base court filing fee is $435 statewide, and some counties add local surcharges. The court sets a hearing date, typically several weeks out depending on the county&rsquo;s calendar.</p>

    <h2 class="h-card" style="margin-top:30px">2. Notice, hearing, and Letters</h2>
    <p>Notice of the hearing is published and mailed to heirs. If nobody objects and the paperwork is clean, the court appoints a personal representative and issues &ldquo;Letters&rdquo;: the document that gives them legal authority to act. Paperwork problems are flagged in the court&rsquo;s <em>probate notes</em> before the hearing; clearing them early is the single best way to keep your date.</p>

    <h2 class="h-card" style="margin-top:30px">3. The four-month creditor window</h2>
    <p>Once Letters issue, creditors get four months to file claims against the estate. This window is statutory: the estate generally can&rsquo;t close before it runs, which is why even a simple, uncontested California probate lasts the better part of a year.</p>

    <h2 class="h-card" style="margin-top:30px">4. Inventory and appraisal</h2>
    <p>The representative files an Inventory &amp; Appraisal of estate assets, generally due within four months of Letters. Real property is valued by a court-appointed probate referee, not by a real-estate agent&rsquo;s opinion.</p>

    <h2 class="h-card" style="margin-top:30px">5. Selling the house, if the estate sells</h2>
    <p>Whether the house can be sold before the estate closes depends on the representative&rsquo;s authority. With <strong>full authority</strong> under the Independent Administration of Estates Act, the representative can usually sell with notice to heirs but without a court hearing. With <strong>limited authority</strong>, the sale is confirmed in court, and in some counties the confirmation hearing includes open overbidding, where competing buyers can raise the price on the spot. That&rsquo;s not a bug; it can only raise what the estate receives.</p>

    <h2 class="h-card" style="margin-top:30px">6. Accounting and distribution</h2>
    <p>After the creditor window closes and taxes and debts are handled, the representative petitions for final distribution. The court approves the accounting, assets distribute, and the estate closes. Statutory fees for the representative and attorney are set by the Probate Code as percentages of the estate: 4% of the first $100,000, 3% of the next $100,000, 2% of the next $800,000, and down from there.</p>

    <h2 class="h-card" style="margin-top:30px">How long, all in?</h2>
    <p>A clean, uncontested probate with a house in it typically runs nine months to eighteen. Contested estates, lost heirs, or title problems run longer. The court is rarely the villain: the calendar is simply the calendar, and the estates that move fastest are the ones whose paperwork clears the examiner&rsquo;s notes the first time.</p>

    <p class="small" style="margin-top:34px">Sources: California Probate Code &sect;&sect;8000&ndash;12252 (petition, letters, creditor claims, inventory) and &sect;10810 (statutory fees), at <a href="https://leginfo.legislature.ca.gov" rel="noopener">leginfo.legislature.ca.gov</a>; filing fee per Government Code &sect;70650; California Courts self-help guide at <a href="https://selfhelp.courts.ca.gov/probate" rel="noopener">selfhelp.courts.ca.gov/probate</a>. Checked {CHECKED}. This is general information, not legal advice. Probate practice varies by county, and a probate attorney is the right person for your specifics.</p>
  </div>
</section>
{cta("Dealing with an estate house?", "We buy inherited houses as-is, on the court's timeline, contents and all.", href="/inherited-house/", label="How we handle probate")}
"""))

P.append(dict(
    url="/resources/notice-of-default/", trail=RES_TRAIL + [("/resources/notice-of-default/", "Notice of Default")],
    title="Notice of Default in California: What Happens Now | HARDT",
    desc="What a California Notice of Default actually starts: the 3-month clock, your right to reinstate, the trustee-sale notice, and every option you still have.",
    body=f"""
<section class="band band--tight">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Resources</p>
    <h1 class="h-sect" data-reveal>You got a Notice of Default. Here&rsquo;s what it actually means.</h1>
    <p class="lede" data-reveal>It is not a sale date, and it is not next week. It&rsquo;s the start of a statutory clock with real rights attached, and the earlier you act, the more of them you keep.</p>
  </div>
</section>
<section class="band band--tight paper">
  <div class="shell shell--narrow" data-reveal>
    <h2 class="h-card">What the NOD is</h2>
    <p>In California, most home loans foreclose <em>non-judicially</em>: no lawsuit, no judge, just a recorded process governed by Civil Code &sect;2924. The Notice of Default is the first recorded step. From its recording date, a minimum of <strong>three months</strong> must pass before the next step can even be taken.</p>

    <h2 class="h-card" style="margin-top:30px">The clock, in full</h2>
    <p><strong>Day 0:</strong> NOD records with the county recorder. <strong>Months 0&ndash;3:</strong> the reinstatement period. You can stop the process by paying the missed amounts plus fees (not the whole loan). <strong>After month 3:</strong> a Notice of Trustee&rsquo;s Sale can be recorded, posted and mailed, with the auction no sooner than 20 days later, or about <strong>111 days minimum</strong> from NOD to auction, and in practice usually longer. Your right to reinstate actually continues until five business days before the sale date.</p>

    <h2 class="h-card" style="margin-top:30px">Rights worth knowing by name</h2>
    <p>The <strong>Homeowner Bill of Rights</strong> requires your servicer to give you a single point of contact and generally prohibits &ldquo;dual tracking&rdquo;: foreclosing while a complete modification application is under review. And under <strong>SB&nbsp;1079</strong>, even after an auction of a 1&ndash;4 unit home, eligible owner-occupant bidders and tenants get a window to match or beat the winning bid.</p>

    <h2 class="h-card" style="margin-top:30px">Your options, plainly</h2>
    <p><strong>Reinstate</strong> if you can find the arrears: the process ends. <strong>Modify or forbear:</strong> ask the servicer&rsquo;s loss-mitigation department, in writing, early. <strong>Sell before the sale date:</strong> if you have equity, a controlled sale protects it in a way an auction never will. <strong>Get counselled:</strong> HUD-approved housing counsellors are free, at <a href="https://www.hud.gov/findacounselor" rel="noopener">hud.gov/findacounselor</a> or (800)&nbsp;569-4287. <strong>Beware of rescue offers:</strong> California law strictly regulates foreclosure consultants and equity purchasers because homeowners in default are heavily targeted. Anyone charging fees up front, or proposing you deed the house over &ldquo;temporarily,&rdquo; is a red flag with legs.</p>

    <h2 class="h-card" style="margin-top:30px">The one thing to do today</h2>
    <p>Find out exactly what&rsquo;s been recorded against your house and when: the NOD and any sale notice are public records at your county recorder. Dates from the record beat dates from collection letters, every time. Then pick your option with weeks in hand instead of days.</p>

    <p class="small" style="margin-top:34px">Sources: Civil Code &sect;&sect;2924, 2924c (reinstatement), 2924f (sale notice), 2924m (SB&nbsp;1079) and &sect;2923.7 (single point of contact), at <a href="https://leginfo.legislature.ca.gov" rel="noopener">leginfo.legislature.ca.gov</a>. Checked {CHECKED}. This is general information, not legal advice. HARDT is not a foreclosure consultant, charges no fees, and buys property only as a principal.</p>
  </div>
</section>
{cta("Want the straight version for your situation?", "No fees, no pressure, and if selling isn't your best move we'll say so.", href="/stop-foreclosure/", label="Foreclosure options")}
"""))

P.append(dict(
    url="/resources/prop-19/", trail=RES_TRAIL + [("/resources/prop-19/", "Prop 19")],
    title="Prop 19 and Inherited Houses in California | HARDT",
    desc="Since February 2021, inheriting a California house usually means a property-tax reassessment. What Prop 19 changed, who's exempt, and the math to run.",
    body=f"""
<section class="band band--tight">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Resources</p>
    <h1 class="h-sect" data-reveal>Prop 19 changed what inheriting a house means.</h1>
    <p class="lede" data-reveal>Before 2021, heirs generally kept the parents&rsquo; low property-tax bill. Now, most don&rsquo;t, and the difference changes the keep-or-sell math entirely.</p>
  </div>
</section>
<section class="band band--tight paper">
  <div class="shell shell--narrow" data-reveal>
    <h2 class="h-card">The old rule, briefly</h2>
    <p>California property taxes are based on a property&rsquo;s assessed value at purchase, growing at most 2% a year (Prop 13). For decades, parents could pass a house &mdash; any house &mdash; to children with that low assessed value intact. A house bought in 1978 could carry a 1978-based tax bill into a third generation.</p>

    <h2 class="h-card" style="margin-top:30px">What Prop 19 did</h2>
    <p>For deaths and transfers on or after <strong>February 16, 2021</strong>, the parent-child exclusion survives only when <strong>the child moves into the house as their principal residence</strong>, generally claiming it within a year, and even then, only the first $1&nbsp;million or so of the gap between the old assessed value and market value stays excluded (the cap adjusts over time). A rental, a second home, or an inherited house the heirs don&rsquo;t live in gets <strong>reassessed to market value</strong> as of the transfer.</p>

    <h2 class="h-card" style="margin-top:30px">What that looks like in practice</h2>
    <p>Say the family house has an assessed value of $95,000 and a market value of $850,000. Under the old rules, heirs kept a tax bill near $1,200 a year. Under Prop 19, if nobody moves in, the bill resets to roughly 1&ndash;1.25% of $850,000 (call it $9,000&ndash;$10,000 a year) from the date of death. Heirs planning to keep the house as a rental discover the yield they imagined included a tax bill that no longer exists.</p>

    <h2 class="h-card" style="margin-top:30px">The decisions it forces</h2>
    <p><strong>Move in:</strong> one heir occupying as a principal residence can preserve much of the exclusion. Workable for one heir, complicated for four. <strong>Keep as a rental:</strong> run the numbers with the <em>new</em> tax bill, not the old one. <strong>Sell:</strong> often the cleanest split, and note that heirs also generally receive a <em>stepped-up income-tax basis</em> to date-of-death value, so a prompt sale frequently owes little or no capital-gains tax. The property-tax reset and the income-tax step-up point in opposite directions, which is exactly why estates should run both sets of numbers before deciding.</p>

    <h2 class="h-card" style="margin-top:30px">Deadlines matter</h2>
    <p>Reassessment runs from the date of death, not the date anyone gets around to paperwork, and supplemental bills arrive retroactively. File the claim forms with the county assessor promptly if an heir is moving in; talk to a CPA or estate attorney before choosing a path.</p>

    <p class="small" style="margin-top:34px">Sources: California Board of Equalization Prop 19 guidance at <a href="https://www.boe.ca.gov/prop19/" rel="noopener">boe.ca.gov/prop19</a>; Revenue &amp; Taxation Code &sect;63.2. Checked {CHECKED}. This is general information, not tax or legal advice: the numbers above are illustrative, and a CPA should run yours.</p>
  </div>
</section>
{cta("Inherited a house and weighing it up?", "We'll put an honest as-is number next to your keep-it math, no pressure either way.", href="/inherited-house/", label="Inherited & probate")}
"""))

P.append(dict(
    url="/resources/selling-with-tenants/", trail=RES_TRAIL + [("/resources/selling-with-tenants/", "Selling with tenants")],
    title="Selling a Tenant-Occupied Rental in California | HARDT",
    desc="California just-cause rules, entry notice, deposits and local ordinances: what a landlord can and can't do when selling, and how an occupied sale works.",
    body=f"""
<section class="band band--tight">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Resources</p>
    <h1 class="h-sect" data-reveal>Selling a rental with tenants in place: the actual rules.</h1>
    <p class="lede" data-reveal>You can sell an occupied rental in California. What you mostly can&rsquo;t do cheaply is empty it first, and the good news is you don&rsquo;t need to.</p>
  </div>
</section>
<section class="band band--tight paper">
  <div class="shell shell--narrow" data-reveal>
    <h2 class="h-card">The tenancy survives the sale</h2>
    <p>A lease follows the property, not the landlord. When an occupied rental sells, the buyer steps into the lease as-is: same rent, same terms, same deposit obligations. Nothing about a sale, by itself, ends a tenancy or changes its terms.</p>

    <h2 class="h-card" style="margin-top:30px">State law: AB 1482</h2>
    <p>The Tenant Protection Act (Civil Code &sect;1946.2) covers most California rentals older than 15 years: after 12 months&rsquo; occupancy, terminating requires <em>just cause</em>. &ldquo;I&rsquo;m selling&rdquo; is not on the just-cause list. No-fault causes (owner move-in, withdrawal from the rental market, substantial remodel) exist but come with relocation assistance: generally one month&rsquo;s rent at the state level, and with paperwork that has to be right.</p>

    <h2 class="h-card" style="margin-top:30px">Local layers</h2>
    <p>Cities can and do add stricter rules. The city of San Diego&rsquo;s 2023 Tenant Protections Ordinance, for example, tightens no-fault terminations and generally doubles relocation to two months&rsquo; rent. Always check the city&rsquo;s rules, not just the state&rsquo;s: the answer changes at municipal boundaries.</p>

    <h2 class="h-card" style="margin-top:30px">Showings and entry</h2>
    <p>Entry to show the property requires proper notice: generally 24 hours, in writing, at reasonable times (Civil Code &sect;1954). Tenants don&rsquo;t have to make the place pretty, accommodate open houses, or tolerate a parade. This is a real friction of listing an occupied property on the open market, and essentially a non-issue in a direct sale with one scheduled walkthrough.</p>

    <h2 class="h-card" style="margin-top:30px">Deposits, rent and paperwork at closing</h2>
    <p>Security deposits transfer to the buyer through escrow (Civil Code &sect;1950.5), rent prorates to the closing date, and the tenancy&rsquo;s terms get documented: typically with an estoppel certificate the tenant confirms. Section 8 tenancies add the housing-authority contract, which transfers with ownership; the tenant&rsquo;s voucher is unaffected by a sale.</p>

    <h2 class="h-card" style="margin-top:30px">The two honest paths</h2>
    <p><strong>List it vacant:</strong> lawful where a no-fault ground genuinely applies, but slow and expensive once relocation, vacancy, turnover work and commissions stack up, and hard on a tenant who did nothing wrong. <strong>Sell it occupied:</strong> tenancy transfers intact, nobody is displaced, and the price reflects the building and the actual rent. Investors buy occupied buildings every day; the trick is finding one who&rsquo;ll show you the math.</p>

    <p class="small" style="margin-top:34px">Sources: Civil Code &sect;&sect;1946.2 (just cause), 1954 (entry), 1950.5 (deposits) at <a href="https://leginfo.legislature.ca.gov" rel="noopener">leginfo.legislature.ca.gov</a>; City of San Diego Tenant Protections Ordinance (2023). Checked {CHECKED}. General information, not legal advice. Landlord-tenant law is fact-specific and locally variable.</p>
  </div>
</section>
{cta("Done being a landlord?", "We buy occupied: mid-lease, Section 8, arrears and all. Nobody gets displaced.", href="/sell-rental-property/", label="Selling a rental")}
"""))

# The honest-math calculator. Progressive enhancement: the static worked
# example is the content; the calculator upgrades it when JS is available.
P.append(dict(
    url="/resources/cash-offer-vs-listing/", trail=RES_TRAIL + [("/resources/cash-offer-vs-listing/", "Cash vs. listing")],
    title="Cash Offer vs. Listing: Run the Honest Math | HARDT",
    desc="A side-by-side calculator for the decision nobody shows you honestly: cash offer now versus repair, list and wait. Every cost on the table, yours to check.",
    head='<style>.calc input[type=number]{width:100%;padding:12px 14px;border:1px solid #d8d2c8;border-radius:8px;font:inherit;background:#fff}.calc label{display:block;font-weight:600;font-size:.92rem;margin:18px 0 6px}.calc .h-kicker{margin-top:0}.calc__out{border-top:3px solid var(--bronze);padding-top:18px;margin-top:22px}.calc__row{display:flex;justify-content:space-between;gap:12px;padding:7px 0;border-bottom:1px solid #e6e0d6;font-size:.95rem}.calc__row strong{font-variant-numeric:tabular-nums}.calc__net{font-size:1.35rem;font-weight:800;margin-top:14px;display:flex;justify-content:space-between}</style>',
    body=f"""
<section class="band band--tight">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Resources</p>
    <h1 class="h-sect" data-reveal>The honest math: cash offer vs. listing.</h1>
    <p class="lede" data-reveal>Nobody in this industry shows you this side by side, because the answer isn&rsquo;t always the one they&rsquo;re selling. Run your own numbers. Sometimes listing wins, and when it does, you should list.</p>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell">
    <div class="compare calc" data-calc>
      <div class="compare__col">
        <p class="h-kicker" style="color:var(--bronze-ink)">If you repair and list</p>
        <label for="c-arv">What it would sell for, fixed up</label>
        <input type="number" id="c-arv" data-calc-in="arv" value="600000" min="0" step="5000" inputmode="numeric">
        <label for="c-rep">Repairs to get it there</label>
        <input type="number" id="c-rep" data-calc-in="rep" value="45000" min="0" step="1000" inputmode="numeric">
        <label for="c-mo">Months until it closes (repairs + market + escrow)</label>
        <input type="number" id="c-mo" data-calc-in="mo" value="5" min="0" max="24" step="1" inputmode="numeric">
        <label for="c-carry">Monthly carrying cost (mortgage, tax, insurance, utilities)</label>
        <input type="number" id="c-carry" data-calc-in="carry" value="3200" min="0" step="100" inputmode="numeric">
        <label for="c-comm">Commissions and selling costs (% of sale)</label>
        <input type="number" id="c-comm" data-calc-in="comm" value="7" min="0" max="15" step="0.5" inputmode="decimal">
        <div class="calc__out">
          <div class="calc__row"><span>Sale price</span><strong data-calc-out="l-price">$600,000</strong></div>
          <div class="calc__row"><span>&minus; Repairs</span><strong data-calc-out="l-rep">$45,000</strong></div>
          <div class="calc__row"><span>&minus; Carrying, 5 months</span><strong data-calc-out="l-carry">$16,000</strong></div>
          <div class="calc__row"><span>&minus; Commissions &amp; costs</span><strong data-calc-out="l-comm">$42,000</strong></div>
          <div class="calc__net"><span>You net about</span><strong data-calc-out="l-net">$497,000</strong></div>
        </div>
      </div>
      <div class="compare__col">
        <p class="h-kicker">If you take a cash offer</p>
        <label for="c-offer">The offer, as-is</label>
        <input type="number" id="c-offer" data-calc-in="offer" value="510000" min="0" step="5000" inputmode="numeric">
        <label for="c-cmo">Weeks until it closes</label>
        <input type="number" id="c-cmo" data-calc-in="cwk" value="2" min="1" max="12" step="1" inputmode="numeric">
        <div class="calc__out">
          <div class="calc__row"><span>Offer</span><strong data-calc-out="r-price">$510,000</strong></div>
          <div class="calc__row"><span>&minus; Repairs</span><strong>$0</strong></div>
          <div class="calc__row"><span>&minus; Carrying, ~2 weeks</span><strong data-calc-out="r-carry">$1,600</strong></div>
          <div class="calc__row"><span>&minus; Commissions</span><strong>$0</strong></div>
          <div class="calc__net"><span>You net about</span><strong data-calc-out="r-net">$508,400</strong></div>
        </div>
        <p class="small" data-calc-out="verdict" style="margin-top:18px">In this example the difference is about $11,400, in the listing&rsquo;s favour if everything goes to plan, and to your taste whether five months of project management is worth it.</p>
      </div>
    </div>
    <p class="small" style="margin-top:30px;max-width:78ch">Defaults are illustrative, not a quote. The repair, timeline and carrying numbers are the honest variables. Ask any agent and any buyer to fill in <em>their</em> version of this table, in writing, and compare nets rather than headline prices. When our number is the smaller net, we&rsquo;ll tell you to list. That&rsquo;s the policy.</p>
  </div>
</section>
{cta("Want our line of this table for your house?", "One walkthrough, one number, with the math shown, and no hard feelings if listing wins.")}
"""))

# ══════════════════════════════════════════════ THANK YOU
P.append(dict(
    url="/thank-you/", noindex=True,
    title="Thanks, We'll Be in Touch | HARDT",
    desc="Your details are in. Here is exactly what happens next, who calls you, and how quickly.",
    body=f"""
<section class="band band--tight">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Got it</p>
    <h1 class="h-sect" data-reveal>Thanks. We&rsquo;ve got your address and we&rsquo;ll be in touch shortly.</h1>
    <p class="lede" data-reveal>Here&rsquo;s exactly what happens next, so you&rsquo;re not left wondering.</p>
  </div>
</section>
<section class="band band--tight paper">
  <div class="shell">
    <div class="grid grid--3">
      <div data-reveal><span class="step__n">First</span><h2 class="h-card">We call or text you</h2><p>Within 15 minutes between 8am and 6pm. Later than that, first thing next morning. It&rsquo;s a decision-maker, not an assistant, not a call centre.</p></div>
      <div data-reveal data-reveal-delay="90"><span class="step__n">Then</span><h2 class="h-card">We talk it through</h2><p>Ten minutes about the house and the situation. If a cash sale isn&rsquo;t your best move, we&rsquo;ll say so on that call.</p></div>
      <div data-reveal data-reveal-delay="180"><span class="step__n">If it fits</span><h2 class="h-card">One walkthrough</h2><p>Half an hour, at a time that suits you. Don&rsquo;t clean, fix or move anything. Then a number with the math shown.</p></div>
    </div>
    <hr class="rule" style="margin:48px 0 36px">
    <p style="font-size:1.06rem"><strong>Need us sooner?</strong> Call or text {TEL}, which reaches us directly.</p>
    <p class="serif" style="font-size:1.4rem;color:var(--bronze-ink);margin-top:30px">Every situation has a way forward.</p>
    <div class="btnrow"><a class="btn btn--ghost" href="/">Back to the site</a></div>
  </div>
</section>
"""))


def write_sitemap():
    """Generated from the page list, so it can never list a 404."""
    def prio(u):
        if u == "/": return "1.0"
        if u.count("/") == 2 and u.strip("/") in [s for s, _, _ in SERVICES] + ["how-it-works", "what-we-buy", "areas", "about", "contact"]:
            return "0.9"
        if u.strip("/") in [s for s, _, _, _ in COUNTIES]: return "0.8"
        if u.count("/") == 3: return "0.8"        # matrix + resource articles
        if u == "/resources/": return "0.7"
        return "0.5"
    rows = "\n".join(
        f"  <url><loc>{SITE}{p['url']}</loc><changefreq>monthly</changefreq><priority>{prio(p['url'])}</priority></url>"
        for p in P if not p.get("noindex"))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<!-- Generated by tools/pages.py — live URLs only; noindex pages excluded. -->\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + rows + "\n</urlset>\n")
    open("sitemap.xml", "w").write(xml)
    return sum(1 for p in P if not p.get("noindex"))


if __name__ == "__main__":
    for p in P:
        print("  ", write(p))
    n = write_sitemap()
    print(f"\n{len(P)} pages written, {n} in sitemap.xml")
