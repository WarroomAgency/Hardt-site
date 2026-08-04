#!/usr/bin/env python3
"""Content for every page. Run: python3 tools/pages.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build import (write, cta, faq_block, SERVICES, COUNTIES,
                   PHONE_DISPLAY, PHONE_HREF, EMAIL, PHONE_ICON)

P = []
TEL = f'<a class="tel" href="{PHONE_HREF}">{PHONE_ICON}{PHONE_DISPLAY}</a>'

# ══════════════════════════════════════════════ HOME
P.append(dict(
    url="/", title="Sell Your House As-Is in Southern California | HARDT",
    desc="Founder-led home buying across San Diego, Riverside, San Bernardino and Kern counties. We don't assign contracts. One walkthrough, one honest number.",
    body=f"""
<section class="hero hero--art" data-hero>
  <div class="hero__bg"><img src="/assets/img/hero.svg" alt="" width="1600" height="1100" fetchpriority="high"></div>
  <div class="shell" style="padding-block:clamp(66px,11vw,132px) clamp(56px,8vw,96px)">
    <p class="eyebrow">San&nbsp;Diego &middot; Riverside &middot; San&nbsp;Bernardino &middot; Kern</p>
    <h1 class="h-hero">Sell your house as&#8209;is, anywhere in Southern California.</h1>
    <p class="hero__promise">One walkthrough. One honest number. And every option on the table &mdash; including the ones that don&rsquo;t involve me.</p>
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
    <p class="lede" data-reveal>Four situations we deal with constantly. If yours isn&rsquo;t here, call anyway &mdash; it probably still has a way forward.</p>
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
      <p data-reveal style="margin-top:22px">Every house we take on gets renovated and put back into use. That&rsquo;s the business &mdash; not paperwork, not flipping a contract to whoever answers first.</p>
      <p data-reveal>It also means the number we give you is real. We&rsquo;re pricing a project we have to finish ourselves, so there&rsquo;s no incentive to promise something now and renegotiate later.</p>
      <p data-reveal><a href="/what-we-buy/">See exactly what we buy &rarr;</a></p>
    </div>
    <div data-reveal>
      <div class="ba" data-compare>
        <img class="ba__before" src="/assets/img/before.svg" alt="A tired house before renovation" width="1200" height="800">
        <img class="ba__after"  src="/assets/img/after.svg"  alt="The same house after renovation" width="1200" height="800">
        <span class="ba__lbl ba__lbl--b">Before</span><span class="ba__lbl ba__lbl--a">After</span>
        <button class="ba__handle" type="button" role="slider" tabindex="0"
          aria-label="Compare before and after" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50"></button>
      </div>
      <p class="small" style="margin-top:12px">Drag to compare. Placeholder art &mdash; real project photography is being shot.</p>
    </div>
  </div>
</section>

<section class="band dark">
  <div class="shell">
    <p class="eyebrow" data-reveal>How it works</p>
    <h2 class="h-sect" data-reveal>Three steps, and a number you can check.</h2>
    <div class="grid grid--3" style="margin-top:46px">
      <div data-reveal><span class="step__n">Step 01</span><h3 class="h-card">Tell me the situation</h3><p>A conversation, not a pitch. What the house is, what&rsquo;s going on, what you&rsquo;d want to happen. No pressure and no countdown.</p></div>
      <div data-reveal data-reveal-delay="90"><span class="step__n">Step 02</span><h3 class="h-card">One walkthrough</h3><p>I come look at it myself. You don&rsquo;t clean, repair, or move anything. It takes about half an hour.</p></div>
      <div data-reveal data-reveal-delay="180"><span class="step__n">Step 03</span><h3 class="h-card">One honest number</h3><p>With the math shown. Take it, leave it, or take it to somebody else to check.</p></div>
    </div>
    <div class="btnrow"><a class="btn btn--ghost" href="/how-it-works/">The full process</a></div>
  </div>
</section>

<section class="band paper">
  <div class="shell">
    <p class="eyebrow" data-reveal>The honest math</p>
    <h2 class="h-sect" data-reveal>Sometimes listing it is the better answer. When it is, I&rsquo;ll tell you.</h2>
    <p class="lede" data-reveal>A cash sale isn&rsquo;t right for every house or every person. Here&rsquo;s how I&rsquo;d think about it if it were my family.</p>
    <div class="compare" style="margin-top:42px" data-reveal>
      <div class="compare__col">
        <p class="h-kicker" style="color:var(--bronze-ink)">List it on the open market when</p>
        <ul><li>You have the time to wait for the right buyer</li><li>The house is in good condition and doesn&rsquo;t need repairs</li><li>You want the highest gross price on paper, and you&rsquo;re fine paying commissions, title and escrow fees, and any repairs the buyer asks for out of that number</li></ul>
      </div>
      <div class="compare__col">
        <p class="h-kicker">Talk to me when</p>
        <ul><li>The house needs work you don&rsquo;t want to pay for or manage</li><li>The timeline matters more than the last few thousand dollars</li><li>There are tenants, contents, liens, or a probate in the middle of it</li><li>You want one number and one person, start to finish</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="band--tight band dark">
  <div class="shell quote">
    <p class="tagline serif" data-reveal>Every situation has a way forward.</p>
    <p class="quote__proof" data-reveal>We don&rsquo;t assign contracts. If it doesn&rsquo;t close, I buy it myself.</p>
    <p class="quote__attr" data-reveal>Peter Eberhardt &middot; Founder</p>
  </div>
</section>

<section class="band">
  <div class="shell split">
    <div>
      <p class="eyebrow" data-reveal>Who you&rsquo;re dealing with</p>
      <h2 class="h-sect" data-reveal>The name on the company is my name.</h2>
      <p data-reveal style="margin-top:22px">Through my twenties I chased an Olympic dream in BMX racing. Real estate started as a detour &mdash; a way to buy the time and money to keep racing. What I found instead was the thing I&rsquo;d actually been missing: purpose, impact, and people.</p>
      <p data-reveal>I also found a corner of this business that nobody regulates, where distressed homeowners don&rsquo;t know what their options are, what questions to ask, or who to ask them to. I thought there could be a better way to do it.</p>
      <div class="btnrow"><a class="btn btn--ghost" href="/about/">More about Peter</a></div>
    </div>
    <div class="media media--4x5" data-reveal>
      <img src="/assets/img/portrait.svg" alt="Placeholder for a portrait of founder Peter Eberhardt" width="900" height="1150" loading="lazy">
      <span class="media__tag">Portrait to be shot</span>
    </div>
  </div>
</section>

<section class="band paper">
  <div class="shell">
    <p class="eyebrow" data-reveal>Recent work</p>
    <h2 class="h-sect" data-reveal>Houses we bought, fixed, and put back into use.</h2>
    <p class="lede" data-reveal>Five of the most recent. Photography from each of these is being prepared &mdash; the illustrations below are standing in until it lands.</p>
    <div class="grid grid--4" style="margin-top:44px">
      <div class="card" style="padding:0;overflow:hidden" data-reveal>
        <div class="media media--4x3"><img src="/assets/img/project-1.svg" alt="Illustration of a Bakersfield street" width="1200" height="900" loading="lazy"></div>
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Shenandoah Drive</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="70">
        <div class="media media--4x3"><img src="/assets/img/project-2.svg" alt="Illustration of a Bakersfield street" width="1200" height="900" loading="lazy"></div>
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Cale Court</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="140">
        <div class="media media--4x3"><img src="/assets/img/project-3.svg" alt="Illustration of a Bakersfield street" width="1200" height="900" loading="lazy"></div>
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Bakersfield</p><p style="margin:0">Terrace Way &amp; Huskey Drive</p></div>
      </div>
      <div class="card" style="padding:0;overflow:hidden" data-reveal data-reveal-delay="210">
        <div class="media media--4x3"><img src="/assets/img/project-4.svg" alt="Illustration of a Lancaster street" width="1200" height="900" loading="lazy"></div>
        <div style="padding:20px 22px 24px"><p class="h-kicker" style="margin-bottom:5px">Lancaster</p><p style="margin:0">Graphic Street</p></div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell">
    <p class="eyebrow" data-reveal>Where we buy</p>
    <h2 class="h-sect" data-reveal>Four counties, and I drive to all of them.</h2>
    <p class="lede" data-reveal>Based in El Cajon. Boots on the ground from the border to Bakersfield.</p>
    <div class="grid grid--4" style="margin-top:42px">
      {"".join(f'''<a class="county" href="/{s}/" data-reveal data-reveal-delay="{i*70}" style="padding:0;overflow:hidden">
        <div class="media media--4x3"><img src="/assets/img/county-{img}.svg" alt="Illustration of {n}" width="1400" height="640" loading="lazy"></div>
        <div style="padding:22px 24px 26px"><p class="county__name">{n}</p><p class="county__cities">{c}</p>
        <span class="card__link" style="margin-top:14px;display:inline-block">Selling here</span></div></a>''' for i,(s,n,img,c) in enumerate(COUNTIES))}
    </div>
  </div>
</section>

{cta("Tell me about the house.", "Three questions, no obligation, and nobody else gets your information.")}
"""))

# ══════════════════════════════════════════════ HOW IT WORKS
HOW_FAQ = [
        ("Do I need to clean or repair anything first?",
         "<p>No. Leave it exactly as it is. You don't need to clear the house out, fix anything, or stage it. If there are contents you don't want, leave those too &mdash; we handle it.</p>"),
        ("How is the number worked out?",
         "<p>We look at what the house is worth once it's renovated, subtract what the renovation actually costs, subtract the cost of holding and reselling it, and leave a margin. We show you those figures. If you want to take them to an agent or a contractor to check, that's a reasonable thing to do.</p>"),
        ("How fast can this close?",
         "<p>Around two weeks is typical from the first call. Faster is sometimes possible. Slower is completely fine &mdash; if you need sixty days to find your next place, we set the date for sixty days.</p>"),
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
        <span class="step__n">Step 01</span><h2 class="h-card" style="font-size:1.5rem">You tell me the situation</h2>
        <p>Call, text, or send the form. We talk for ten minutes about the house and what's going on around it &mdash; a probate, a tenant, a job in another state, a repair bill you don't want.</p>
        <p>This is a conversation, not a qualification script. If it becomes clear a cash sale isn't your best move, I'll say so on this call rather than three weeks from now.</p>
      </div>
      <div data-reveal data-reveal-delay="90">
        <span class="step__n">Step 02</span><h2 class="h-card" style="font-size:1.5rem">One walkthrough, about half an hour</h2>
        <p>I come and look at the house myself &mdash; not an inspector, not a photographer, not a team. You don't clean, fix, or move anything, and you don't need to be embarrassed about any of it. I've seen houses in every condition there is.</p>
        <p>If the property is tenant-occupied we work around the tenant's schedule and their legal notice period.</p>
      </div>
      <div data-reveal>
        <span class="step__n">Step 03</span><h2 class="h-card" style="font-size:1.5rem">One number, and the math behind it</h2>
        <p>Usually within a day. You get the figure and the reasoning: what I think it's worth finished, what the work costs, what holding and reselling costs, and the margin left over.</p>
        <p>Take it, leave it, or take it to an agent for a second opinion. It doesn't expire because a timer ran out.</p>
      </div>
      <div data-reveal data-reveal-delay="90">
        <span class="step__n">Step 04</span><h2 class="h-card" style="font-size:1.5rem">You pick the closing date</h2>
        <p>We open escrow with a title company and they handle the money and the paperwork. Title gets cleared &mdash; that's their job and ours, not yours.</p>
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
      <div><p class="h-kicker">No assignment</p><p class="small">Your contract doesn't get sold to a stranger. If it doesn't close, I buy it myself.</p></div>
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

{cta("Ready to see a number?", "Send the address and I'll come look at it myself.")}
"""))

# ══════════════════════════════════════════════ WHAT WE BUY
P.append(dict(
    url="/what-we-buy/", active="/what-we-buy/",
    trail=[("/what-we-buy/", "What we buy")],
    title="What We Buy &mdash; And What We Don't | HARDT",
    desc="Single and multi-family up to about $1.2M, in any condition, across four Southern California counties. Our buying criteria, published in full.",
    body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>Straight answers</p>
    <h1 class="h-sect" data-reveal>What I buy, and what I don&rsquo;t.</h1>
    <p class="lede" data-reveal>Published so you don&rsquo;t waste an afternoon finding out on a phone call. If your property falls outside this, I&rsquo;ll usually still know someone worth calling.</p>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell">
    <div class="grid grid--2">
      <div class="card" data-reveal>
        <p class="h-kicker">I buy</p>
        <ul class="checks" style="margin-top:6px">
          <li>Single family and multi&#8209;family, up to about <strong>$1.2M</strong></li>
          <li>Houses needing major work &mdash; including fire and water damage</li>
          <li>Inherited and probate property</li>
          <li>Pre&#8209;foreclosure, Notice of Default, liens and title problems</li>
          <li>Tenant&#8209;occupied rentals, mid&#8209;lease and Section 8</li>
          <li>Houses still full of contents</li>
          <li>Divorce, relocation and estate situations</li>
        </ul>
      </div>
      <div class="card" data-reveal data-reveal-delay="90">
        <p class="h-kicker" style="color:var(--gray)">I don&rsquo;t buy</p>
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
    <p class="small" style="margin-top:26px;max-width:62ch">That last one matters more than it sounds. If the title can&rsquo;t be cleared, you can&rsquo;t actually sell the house to anybody &mdash; and a buyer who tells you otherwise is setting up a problem for later.</p>
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

{cta("Not sure if yours fits?", "Send it over. A ten minute call costs you nothing and I'll tell you straight.")}
"""))

# ══════════════════════════════════════════════ AREAS
P.append(dict(
    url="/areas/", active="/areas/",
    trail=[("/areas/", "Where we buy")],
    title="Where We Buy — Four Southern California Counties | HARDT",
    desc="HARDT buys houses across San Diego, Riverside, San Bernardino and Kern counties. Based in El Cajon, with boots on the ground from the border to Bakersfield.",
    body=f"""
<section class="band band--tight">
  <div class="shell">
    <p class="eyebrow" data-reveal>Where we buy</p>
    <h1 class="h-sect" data-reveal>Four counties, and I drive to all of them.</h1>
    <p class="lede" data-reveal>Based in El Cajon. I&rsquo;ll go about four hours for a walkthrough, which covers everything from the border up to Bakersfield.</p>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell">
    <div class="grid grid--2">
      {"".join(f'''<a class="county" href="/{s}/" data-reveal data-reveal-delay="{i*80}" style="padding:0;overflow:hidden">
        <div class="media media--16x9"><img src="/assets/img/county-{img}.svg" alt="" width="1400" height="620" loading="lazy"></div>
        <div style="padding:26px 28px"><p class="county__name">{n}</p><p class="county__cities">{c}</p>
        <span class="card__link" style="margin-top:14px;display:inline-block">Selling in {n.replace(" County","")}</span></div></a>''' for i,(s,n,img,c) in enumerate(COUNTIES))}
    </div>
  </div>
</section>

<section class="band">
  <div class="shell shell--narrow">
    <h2 class="h-sect" data-reveal>Places I&rsquo;d rather be honest about</h2>
    <p data-reveal style="margin-top:20px">There are mountain communities I don&rsquo;t buy in &mdash; Big Bear, Lake Arrowhead, Crestline, Bear Valley Springs, Frazier Park and Pine Mountain Club among them. The market up there behaves differently enough that I&rsquo;d be guessing, and guessing with somebody&rsquo;s house is how people get hurt.</p>
    <p data-reveal>If that&rsquo;s where your property is, tell me anyway. I&rsquo;d rather point you to someone who actually knows that market than pretend I do.</p>
  </div>
</section>

{cta("Not sure if you're in range?", "Send the address. If it's outside what I cover, I'll tell you in one message.")}
"""))

# ══════════════════════════════════════════════ ABOUT
P.append(dict(
    url="/about/", active="/about/", ogtype="profile",
    trail=[("/about/", "About Peter")],
    title="About Peter Eberhardt, Founder | HARDT",
    desc="HARDT is founder-led. Peter Eberhardt buys, renovates and rebuilds houses across Southern California — and refuses to take advantage of people having a hard year.",
    body=f"""
<section class="band band--tight">
  <div class="shell split">
    <div>
      <p class="eyebrow" data-reveal>Who you&rsquo;re dealing with</p>
      <h1 class="h-sect" data-reveal>The name on the company is my name.</h1>
      <p class="lede" data-reveal>Peter Eberhardt &middot; Founder, HARDT Real Estate &middot; El Cajon, California</p>
    </div>
    <div class="media media--4x5" data-reveal>
      <img src="/assets/img/portrait.svg" alt="Placeholder for a portrait of founder Peter Eberhardt" width="900" height="1150">
      <span class="media__tag">Portrait to be shot</span>
    </div>
  </div>
</section>

<section class="band band--tight paper">
  <div class="shell shell--narrow">
    <p data-reveal>Through my twenties I chased an Olympic dream in the sport of BMX racing. Getting into real estate started out as a short detour from that dream &mdash; a tool that would give me more time and money to chase the Olympic path.</p>
    <p data-reveal>I realised fairly quickly that I was missing much more than time and money. I was missing purpose, impact, and relationships.</p>
    <p data-reveal>Getting into real estate, I also discovered how unregulated the space is where distressed homes get bought and sold. I watched homeowners in situations where they didn&rsquo;t know what all their options were, didn&rsquo;t know the right questions to ask, and didn&rsquo;t know who to ask them to.</p>
    <p data-reveal>I wondered whether there could be a better way. A better service. A better impact &mdash; something that could actually get a homeowner out of the situation they were in and show them a way forward to the next chapter.</p>
    <p data-reveal>That&rsquo;s what HARDT is. We refuse to take advantage of homeowners, and we believe every situation has a way forward.</p>
    <p class="serif" style="font-size:1.4rem;color:var(--bronze-ink);margin-top:32px" data-reveal>Every situation has a way forward.</p>
  </div>
</section>

<section class="band dark">
  <div class="shell">
    <p class="eyebrow" data-reveal>How we operate</p>
    <h2 class="h-sect" data-reveal>Four things that don&rsquo;t change.</h2>
    <div class="grid grid--2" style="margin-top:42px">
      <div data-reveal><h3 class="h-card">You talk to me</h3><p>Every enquiry comes to me directly. Not a call centre, not an acquisitions rep working a script, not a lead that gets sold to four investors at once.</p></div>
      <div data-reveal data-reveal-delay="80"><h3 class="h-card">We don&rsquo;t assign contracts</h3><p>Some buyers put a house under contract and then sell that contract on. We don&rsquo;t. If it doesn&rsquo;t close, I buy it myself.</p></div>
      <div data-reveal><h3 class="h-card">The math is shown</h3><p>You see how the number was reached &mdash; finished value, cost of work, cost of holding and reselling, margin. Check it with anyone you like.</p></div>
      <div data-reveal data-reveal-delay="80"><h3 class="h-card">Bad news arrives at the same volume</h3><p>If listing with an agent would put more money in your pocket, I&rsquo;ll say so on the first call. It costs me deals. It&rsquo;s still the right thing.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>The business</p>
    <h2 class="h-sect" data-reveal>Plainly stated.</h2>
    <p data-reveal style="margin-top:22px">HARDT Real Estate is a d/b/a of Fluid Developments LLC, based in El Cajon and operating across San Diego, Riverside, San Bernardino and Kern counties since 2021. We buy houses with our own money, renovate them using local subcontractors, and put them back into use.</p>
    <p data-reveal>We buy as a principal for our own account. We are not a licensed real estate brokerage, we don&rsquo;t represent buyers or sellers, and we don&rsquo;t give legal, tax or financial advice. When you need that kind of advice &mdash; and in a probate or a foreclosure you often do &mdash; we&rsquo;ll tell you to go get it.</p>
  </div>
</section>

{cta("Want to talk it through?", "Call me directly, or send the address and I'll come look at it.")}
"""))

# ══════════════════════════════════════════════ CONTACT
P.append(dict(
    url="/contact/", active="/contact/",
    trail=[("/contact/", "Contact")],
    title="Get Your Offer | HARDT",
    desc="Three questions and I'll be in touch — usually within 15 minutes between 8am and 6pm. No obligation, no pressure, and nobody else gets your information.",
    body=f"""
<section class="band dark" id="offer">
  <div class="shell split">
    <div>
      <p class="eyebrow" data-reveal>Start here</p>
      <h1 class="h-sect" data-reveal>Tell me about the house.</h1>
      <p class="lede" data-reveal>Three questions. No obligation, no pressure, and no one else gets your information.</p>
      <ul class="rail" style="margin-top:36px" data-reveal>
        <li><strong>You talk to me, not a call center.</strong> Every lead comes to me directly.</li>
        <li><strong>A reply within 15 minutes</strong>, 8am&ndash;6pm. Outside those hours, first thing next morning.</li>
        <li><strong>We don&rsquo;t assign contracts.</strong> If it doesn&rsquo;t close, I buy it myself.</li>
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
      <div class="field"><label for="phone">Phone or email</label><span class="help">Whichever you&rsquo;d rather I use.</span>
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
      <div><p class="h-kicker">Phone</p><p>{TEL}</p><p class="small">Call or text. It reaches me, not an assistant.</p></div>
      <div><p class="h-kicker">Email</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p class="small">Fine for documents and photos.</p></div>
      <div><p class="h-kicker">Hours</p><p>Monday&ndash;Saturday, 8am&ndash;6pm</p><p class="small">Outside those hours I&rsquo;ll reply first thing the next morning.</p></div>
    </div>
    <p class="small" style="margin-top:28px">HARDT Real Estate &middot; a d/b/a of Fluid Developments LLC &middot; El Cajon, California. We buy across San Diego, Riverside, San Bernardino and Kern counties.</p>
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
        ("Will you lowball me because it needs work?","<p>You'll see the math &mdash; finished value, cost of the work, cost of holding and reselling, and the margin. If the repair estimate looks high to you, get a contractor to check it. That's a reasonable thing to do and I'd rather you did.</p>")]),
 "inherited-house": dict(
   h1="You inherited a house. Now what?",
   title="Selling an Inherited House in California | HARDT",
   desc="Probate-fluent, patient, and willing to carry the heavy part — including the contents. Sell an inherited house in Southern California without repairs or showings.",
   lede="Probate, siblings, and a house that can come with everything still in it. This is the situation we're asked about most, and the one people are least prepared for.",
   body_intro="<p>Inheriting a house usually arrives alongside a death, which means the paperwork lands at the worst possible time. Most people have never been through probate and don't know what they're allowed to do or when.</p><p>We deal with this constantly. There's rarely a rush from our side, and we're comfortable waiting for the court where waiting is what's needed.</p>",
   points=["Property still going through probate",
           "Several heirs who don't entirely agree",
           "A house full of a lifetime of belongings",
           "Out-of-state executors who can't get here",
           "Deferred maintenance from the last years of someone's life"],
   faq=[("Can I sell before probate finishes?","<p>Sometimes, depending on the authority the court has granted and how the property was held. It's a legal question, not a marketing one &mdash; the honest answer is that you should ask a probate attorney, and we'll work to whatever timeline they give you.</p>"),
        ("What about everything still in the house?","<p>Leave it. Take the things that matter to your family and we'll deal with the rest. Nobody should have to empty a parent's house on a deadline.</p>"),
        ("There are four of us and we don't agree. Can you help?","<p>We can be patient and we can put the same clear number in front of everyone, which sometimes helps. What we can't do is mediate &mdash; and if the disagreement is serious, that's a job for an attorney.</p>")]),
 "stop-foreclosure": dict(
   h1="A Notice of Default isn&rsquo;t the end of the road.",
   title="Facing Foreclosure in Southern California? | HARDT",
   desc="Understand the California trustee-sale timeline and every option on the table — including the ones that don't involve selling. Straight information, no pressure.",
   lede="If you're behind on payments, the most valuable thing you can have right now is accurate information about your options — not another offer.",
   body_intro="<p>People in this situation usually get a stack of letters and a lot of pressure. What they rarely get is a plain explanation of how the process actually works and how much time is genuinely left.</p><p>So that's what this conversation is. Sometimes the answer is a reinstatement, a loan modification, or a short sale with your lender. Sometimes it's selling before the sale date. Occasionally it's letting it go &mdash; and if that's genuinely your best outcome, I'll say so.</p>",
   points=["Behind on payments but not yet in default",
           "A Notice of Default has been recorded",
           "A trustee sale date has been set",
           "Property tax arrears or a tax lien",
           "Mechanic's liens or judgments clouding title"],
   faq=[("How much time do I actually have?","<p>California's non-judicial foreclosure process runs on statutory timelines from the recording of a Notice of Default through to a trustee's sale. The specifics depend on your lender and what's already been recorded, so the first thing to do is find out exactly where in that process you are.</p>"),
        ("Will selling hurt my credit less than foreclosure?","<p>Often, yes &mdash; but this is a question for a HUD-approved housing counsellor or an attorney, not for a buyer. We're not going to advise you on your credit in order to buy your house.</p>"),
        ("Do you charge for this conversation?","<p>No, and we don't charge for anything else either. We're not foreclosure consultants and we don't take fees to help with a default. We buy houses. If buying yours is the right answer we'll make an offer; if it isn't, we'll tell you what we'd do.</p>")],
   legal="<p class=\"small\" style=\"margin-top:26px;max-width:70ch\">This page is general information, not legal or financial advice. California law regulates foreclosure consultants and equity purchasers. HARDT is not a foreclosure consultant, does not charge fees for foreclosure assistance, and buys property only as a principal. If you are facing foreclosure, speak with a HUD-approved housing counsellor or an attorney about your specific situation.</p>"),
 "sell-rental-property": dict(
   h1="Tenants in place is fine. Truly.",
   title="Sell a Rental Property With Tenants in Place | HARDT",
   desc="Sell a tenant-occupied rental in Southern California as-is — mid-lease, Section 8, deferred maintenance and all. No showings, no evictions, no repairs.",
   lede="Most buyers want the property vacant, cleaned and repaired. That means evicting someone, and it means months of work before you can even list.",
   body_intro="<p>The usual advice to a landlord who wants out is to get the tenant out first. That's slow, expensive, and hard on somebody who probably hasn't done anything wrong.</p><p>We buy occupied. The tenancy transfers with the property, and in many cases the tenant simply stays &mdash; which is better for everyone and considerably faster for you.</p>",
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
    counties = "".join(f'<a class="pill" href="/{s2}/" style="text-decoration:none">{n2}</a>'
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
      <div><p class="h-kicker">02 &middot; One walkthrough</p><p class="small">Half an hour, me, no cleaning or repairs first.</p></div>
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

{cta("Tell me about the property.", "Three questions, no obligation, and you talk to me directly.")}
"""))

# ══════════════════════════════════════════════ COUNTIES
CTY = {
 "san-diego-county": ("home county",
   "This is home. I live in El Cajon, so anything in San Diego County is a short drive and usually a same-week walkthrough.",
   "Coastal North County, the inland valleys and the East County foothills are three different housing markets wearing one county's name. A 1950s East County ranch and a 1990s Chula Vista tract house need completely different work, and the number reflects that."),
 "riverside-county": ("the corridor",
   "Riverside County runs from the Inland Empire down through the Temecula Valley, and I cover the western and southwestern side of it.",
   "Newer subdivisions here often carry Mello-Roos assessments and solar or PACE liens attached to the property rather than the owner. Those don't stop a sale, but they have to be found early &mdash; they're a common reason a deal falls apart late with another buyer."),
 "san-bernardino-county": ("the inland empire",
   "From the older neighbourhoods of San Bernardino and Redlands out through Fontana, Rancho Cucamonga and Highland.",
   "The housing stock varies enormously by decade here, which matters for what's behind the walls &mdash; galvanised plumbing, aluminium wiring and panels that no longer pass inspection are all common in the older parts of the county."),
 "kern-county": ("the north end",
   "Bakersfield and the surrounding towns are the northern end of what I cover. It's a four hour drive from El Cajon and I make it regularly.",
   "Kern is where a good deal of our renovation work has been. Prices are lower than the coastal counties, which changes the arithmetic on what's worth doing to a house &mdash; a full renovation that pencils in Chula Vista may not pencil in Wasco, and vice versa."),
}

for slug, name, img, cities in COUNTIES:
    kicker, intro, local = CTY[slug]
    cfaq = [(f"Which {name.replace(' County','')} cities do you buy in?",
             f"<p>{cities}, plus the smaller communities around them. If you're not sure whether you're in range, send the address and I'll tell you in one message.</p>"),
            ("Do you buy houses that need work here?",
             "<p>Yes &mdash; that's most of what we do. Condition changes the number, not whether we're interested.</p>"),
            ("How quickly can you see the property?",
             "<p>Usually within a day or two, since this is home.</p>" if slug=="san-diego-county"
             else "<p>Usually within a few days. I batch trips to the area, so tell me your timing and I will work around it.</p>")]
    short = name.replace(" County", "")
    svc_cards = "".join(
        f'<a class="card" href="/{s2}/"><h3 class="h-card">{n2}</h3><span class="card__link">In {short}</span></a>'
        for s2, n2, _ in SERVICES)
    P.append(dict(
        url=f"/{slug}/", trail=[("/areas/", "Where we buy"), (f"/{slug}/", name)],
        title=f"We Buy Houses in {name}, CA | HARDT",
        desc=f"Sell a house as-is in {name} — {cities.split(',')[0]} and across the county. No repairs, no showings, no commissions. One walkthrough and one honest number.",
        og=f"/assets/img/county-{img}.svg",
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
    <div class="media media--wide" data-reveal><img src="/assets/img/county-{img}.svg" alt="" width="1400" height="620"><span class="media__tag">Placeholder &mdash; local project photography to come</span></div>
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

{cta(f"Have a house in {short}?", "Send the address and I'll come look at it myself.")}
"""))

# ══════════════════════════════════════════════ LEGAL
LEGAL = {
 "privacy": ("Privacy Policy", "How HARDT Real Estate collects, uses and protects the information you send through this website.", f"""
<p>HARDT Real Estate, a d/b/a of Fluid Developments LLC, operates this website. This policy explains what we collect and what we do with it.</p>
<h2 class="h-card" style="margin-top:34px">What we collect</h2>
<p>Only what you send us: the property address, the situation you select, your name, a phone number or email address, and any notes you add. We also collect standard analytics such as pages viewed and approximate location, which is not tied to your name.</p>
<h2 class="h-card" style="margin-top:30px">What we do with it</h2>
<p>We use it to contact you about your property and to prepare an offer. That's it.</p>
<h2 class="h-card" style="margin-top:30px">What we don't do</h2>
<p><strong>We do not sell your information, and we do not share it with other investors or lead buyers.</strong> This is common practice in our industry and we don't do it. We share information only with the parties needed to complete a transaction you have chosen to proceed with &mdash; a title company, an escrow officer &mdash; and where the law requires it.</p>
<h2 class="h-card" style="margin-top:30px">Your rights in California</h2>
<p>Under the CCPA and CPRA you can ask what personal information we hold about you, ask us to delete it, and ask us to correct it. We don't sell personal information, so there is nothing to opt out of on that front. To make a request, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2 class="h-card" style="margin-top:30px">Contact by phone and text</h2>
<p>If you give us a phone number we may call or text you about your property. You can tell us to stop at any time and we will.</p>
<h2 class="h-card" style="margin-top:30px">Cookies</h2>
<p>We use minimal analytics cookies to understand which pages are useful. We do not run advertising trackers on this site.</p>
<p class="small" style="margin-top:34px">Questions about any of this: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""),
 "terms": ("Terms of Use", "Terms governing use of the HARDT Real Estate website, including our position as a principal buyer rather than a licensed brokerage.", f"""
<p>By using this website you agree to these terms.</p>
<h2 class="h-card" style="margin-top:34px">Who we are</h2>
<p>HARDT Real Estate is a d/b/a of Fluid Developments LLC, based in El Cajon, California. <strong>We buy property as a principal for our own account.</strong> We are not a licensed real estate brokerage, we do not represent buyers or sellers in transactions, and we do not act as agents for anyone.</p>
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
  <li>Every text and background pairing on this site is tested to meet AA contrast &mdash; we adjusted our own brand colours to get there rather than the other way round</li>
  <li>The site works end to end with a keyboard, and focus is always visible</li>
  <li>Headings run in order, images carry alternative text, and form fields have real labels</li>
  <li>Animation is removed entirely for anyone whose system requests reduced motion</li>
  <li>Tap targets meet the minimum size on phones</li>
  <li>Text can be resized without breaking the layout</li>
</ul>
<h2 class="h-card" style="margin-top:30px">Where we know we fall short</h2>
<p>This site is under active construction and some sections still use placeholder artwork. If you find something that doesn't work with your assistive technology, we want to hear about it &mdash; that's a bug, not a preference.</p>
<h2 class="h-card" style="margin-top:30px">Tell us</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or call {PHONE_DISPLAY}. Describe what happened and what you were using, and we'll fix it. If you need to give us information about a property in another format, we'll take it however works for you &mdash; including over the phone.</p>"""),
}
for slug, (name, desc, body) in LEGAL.items():
    P.append(dict(url=f"/{slug}/", trail=[(f"/{slug}/", name)],
        title=f"{name} | HARDT", desc=desc,
        body=f"""<section class="band band--tight"><div class="shell shell--narrow">
  <p class="eyebrow" data-reveal>Legal</p><h1 class="h-sect" data-reveal>{name}</h1>
  <p class="small" style="margin-top:16px">Last updated August 2026</p>
</div></section>
<section class="band band--tight paper"><div class="shell shell--narrow" data-reveal>{body}</div></section>"""))


# ══════════════════════════════════════════════ THANK YOU
P.append(dict(
    url="/thank-you/", noindex=True,
    title="Thanks — I'll be in touch | HARDT",
    desc="Your details are in. Here is exactly what happens next, who calls you, and how quickly.",
    body=f"""
<section class="band band--tight">
  <div class="shell shell--narrow">
    <p class="eyebrow" data-reveal>Got it</p>
    <h1 class="h-sect" data-reveal>Thanks. I&rsquo;ve got your address and I&rsquo;ll be in touch shortly.</h1>
    <p class="lede" data-reveal>Here&rsquo;s exactly what happens next, so you&rsquo;re not left wondering.</p>
  </div>
</section>
<section class="band band--tight paper">
  <div class="shell">
    <div class="grid grid--3">
      <div data-reveal><span class="step__n">First</span><h2 class="h-card">I call or text you</h2><p>Within 15 minutes between 8am and 6pm. Later than that, first thing next morning. It&rsquo;s me &mdash; not an assistant, not a call centre.</p></div>
      <div data-reveal data-reveal-delay="90"><span class="step__n">Then</span><h2 class="h-card">We talk it through</h2><p>Ten minutes about the house and the situation. If a cash sale isn&rsquo;t your best move, I&rsquo;ll say so on that call.</p></div>
      <div data-reveal data-reveal-delay="180"><span class="step__n">If it fits</span><h2 class="h-card">One walkthrough</h2><p>Half an hour, at a time that suits you. Don&rsquo;t clean, fix or move anything. Then a number with the math shown.</p></div>
    </div>
    <hr class="rule" style="margin:48px 0 36px">
    <p style="font-size:1.06rem"><strong>Need me sooner?</strong> Call or text {TEL} &mdash; that reaches me directly.</p>
    <p class="serif" style="font-size:1.4rem;color:var(--bronze-ink);margin-top:30px">Every situation has a way forward.</p>
    <div class="btnrow"><a class="btn btn--ghost" href="/">Back to the site</a></div>
  </div>
</section>
"""))


if __name__ == "__main__":
    for p in P:
        print("  ", write(p))
    print(f"\n{len(P)} pages written")
