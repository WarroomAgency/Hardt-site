"""/hello/ — the landing page behind the QR code on HARDT job-site signs.

Someone standing on the sidewalk scans the sign and gets one question:
what do you want to do? Four answers, nothing else competing for the tap.

Deliberately different from every other page:
  * noindex, and out of the sitemap — it only makes sense after a scan.
  * Stripped-down chrome (lockup + phone in, one line out) instead of the
    full header/footer, so the four choices are the whole page.
  * Uses the SIGN number, (661) 493-9127, not the canonical NAP number.
    That's the number printed on the sign; a scanner should see the same
    one. Because the page is noindexed, it doesn't touch the NAP that
    Google and the citations see. Change SIGN_PHONE_* below if Peter
    ever wants the signs on the main line.
  * Its own Netlify form, `property-inquiry`, for neighbours and buyers
    asking about the house the sign is on. Turn on notifications for it in
    the Netlify UI (Forms → property-inquiry), same as hardt-lead.
  * GA4 event `hello_choice` records which option people pick.
"""
from build import MARK_DARK, PHONE_ICON, rev, og_img

SIGN_PHONE_DISPLAY = "(661) 493-9127"
SIGN_PHONE_TEL = "tel:+16614939127"
SIGN_PHONE_SMS = "sms:+16614939127"

ARROW_R = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="square" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>')
ARROW_D = ('<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
           'stroke-linecap="square" aria-hidden="true"><path d="M12 4v15M6 13l6 6 6-6"/></svg>')

CSS = """
<style>
  /* /hello/ only. Everything else comes from site.css. */
  .hello-head{border-bottom:1px solid var(--line)}
  .hello-head .shell{display:flex;align-items:center;justify-content:space-between;padding-block:16px}
  .hello-head .tel{font-family:var(--display);font-weight:800;font-size:15px;color:var(--charcoal);text-decoration:none;display:inline-flex;align-items:center;gap:8px;min-height:44px}
  .hello-hero{padding-block:clamp(40px,7vw,80px) clamp(22px,3.5vw,36px)}
  .hello-hero h1{font-size:clamp(2.1rem,6.4vw,3.4rem);max-width:16ch}
  .hello-hero .lede{margin-top:14px}
  .choices{display:grid;gap:14px;grid-template-columns:1fr;padding-bottom:clamp(56px,8vw,96px)}
  @media(min-width:760px){.choices{grid-template-columns:repeat(2,1fr);gap:18px}}
  .choice{position:relative;display:flex;flex-direction:column;background:var(--white);border:1px solid var(--line);
    border-radius:var(--radius);padding:clamp(22px,3vw,30px);color:var(--charcoal);text-decoration:none;
    transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease}
  a.choice:hover,a.choice:focus-visible{border-color:var(--charcoal);box-shadow:0 10px 30px rgba(26,26,26,.08);transform:translateY(-2px);color:var(--charcoal)}
  .choice__num{font-family:var(--display);font-weight:800;font-size:12px;letter-spacing:.16em;color:var(--bronze-ink);margin:0 0 14px}
  .choice__title{font-family:var(--display);font-weight:900;font-size:clamp(1.35rem,2.6vw,1.6rem);letter-spacing:-.02em;line-height:1.1;
    margin:0 0 8px;display:flex;align-items:center;justify-content:space-between;gap:12px}
  .choice__title svg{flex:none;color:var(--bronze)}
  .choice p{color:var(--gray);margin:0;font-size:16px}
  .choice--primary{background:var(--charcoal);border-color:var(--charcoal);color:var(--cream)}
  .choice--primary .choice__num{color:var(--bronze-light)}
  .choice--primary p{color:rgba(240,235,228,.74)}
  a.choice--primary:hover,a.choice--primary:focus-visible{color:var(--cream);border-color:var(--bronze)}
  .choice__actions{display:flex;gap:10px;margin-top:18px;flex-wrap:wrap}
  .choice__actions .btn{flex:1 1 140px;justify-content:center}
  .choice__links{display:flex;flex-direction:column;gap:6px;margin-top:16px}
  .choice__links a{font-weight:500;color:var(--charcoal);padding-block:4px}
  .choice__links a:hover{color:var(--bronze-ink)}
  .ask{scroll-margin-top:20px}
  .ask .form{max-width:640px}
  .ask .h-sect{max-width:18ch}
  .hello-foot{border-top:1px solid var(--line);padding-block:28px 40px}
  .hello-foot p{margin:0 0 8px}
</style>
"""

TOP = f"""<header class="hello-head">
  <div class="shell">
    <a class="lockup" href="/" aria-label="HARDT home">{MARK_DARK}<span class="lockup__hair"></span><span class="lockup__word">HARDT</span></a>
    <a class="tel" href="{SIGN_PHONE_TEL}" data-choice="header-call">{PHONE_ICON}{SIGN_PHONE_DISPLAY}</a>
  </div>
</header>
"""


def bottom(serif):
    return f"""<footer class="hello-foot">
  <div class="shell">
    <p class="serif" style="color:var(--bronze-ink);font-size:1.1rem;margin-bottom:12px">{serif}</p>
    <p class="small">HARDT &middot; a d/b/a of Fluid Developments LLC &middot; <a href="/">hardtrealestate.com</a> &middot; <a href="/privacy/">Privacy</a></p>
    <p class="small" style="max-width:78ch;font-size:.79rem">HARDT buys property as a principal for its own account. We are not a licensed real estate
      brokerage, we do not represent buyers or sellers, and we do not provide legal, tax or financial advice.</p>
  </div>
</footer>
<script src="{rev("/assets/site.js")}" defer></script>
<script>
  /* Which option people pick after scanning: GA4 event "hello_choice". */
  document.addEventListener('click', function (e) {{
    var el = e.target.closest('[data-choice]');
    if (el && window.gtag) gtag('event', 'hello_choice', {{ choice: el.getAttribute('data-choice') }});
  }});
</script>
"""


HELLO = dict(
    url="/hello/", noindex=True,
    title="What Can We Help You With? | HARDT Southern California",
    desc=("You scanned a HARDT sign. Sell a house, ask about the property the sign is on, "
          "call or text our team directly, or see how we work. One tap, no pressure."),
    og=og_img("og-hello"), ogalt="HARDT. What can we help you with?",
    head=CSS, chrome_top=TOP, chrome_bottom=bottom("Another quality project."),
    body=f"""
<section class="hello-hero">
  <div class="shell">
    <p class="eyebrow">Thanks for scanning</p>
    <h1>What can we help you with?</h1>
    <p class="lede">Pick whichever fits. You&rsquo;ll reach our team directly, not a call centre.</p>
  </div>
</section>

<section>
  <div class="shell choices">
    <a class="choice choice--primary" href="/contact/" data-choice="sell">
      <p class="choice__num">01</p>
      <h2 class="choice__title">I want to sell my house {ARROW_R}</h2>
      <p>Get a cash offer on your own property. Three quick questions, no obligation.</p>
    </a>
    <a class="choice" href="#ask" data-choice="ask">
      <p class="choice__num">02</p>
      <h2 class="choice__title">Ask about this property {ARROW_D}</h2>
      <p>Curious about the house this sign is on, the work being done, or when it&rsquo;s available? Send us a note.</p>
    </a>
    <div class="choice">
      <p class="choice__num">03</p>
      <h2 class="choice__title">Talk to Peter</h2>
      <p>Call or text. It comes straight to us. Mon&ndash;Sat, 8am&ndash;6pm.</p>
      <div class="choice__actions">
        <a class="btn btn--primary" href="{SIGN_PHONE_TEL}" data-choice="call">Call</a>
        <a class="btn btn--ghost" href="{SIGN_PHONE_SMS}" data-choice="text">Text</a>
      </div>
    </div>
    <div class="choice">
      <p class="choice__num">04</p>
      <h2 class="choice__title">See how we work</h2>
      <p>Just looking? Here&rsquo;s how we buy, and some of the people we&rsquo;ve helped.</p>
      <div class="choice__links">
        <a href="/how-it-works/" data-choice="how-it-works">How it works &rarr;</a>
        <a href="/how-weve-helped/" data-choice="how-weve-helped">How we&rsquo;ve helped &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="band dark ask" id="ask">
  <div class="shell">
    <p class="eyebrow">Ask about this property</p>
    <h2 class="h-sect">Tell us what you&rsquo;d like to know.</h2>
    <p class="lede" style="margin-bottom:34px">We&rsquo;ll get back to you, usually within 15 minutes between 8am and 6pm.</p>
    <form class="form" name="property-inquiry" method="POST" data-netlify="true" netlify-honeypot="company" action="/hello/thanks/" data-validate>
      <input type="hidden" name="form-name" value="property-inquiry">
      <input type="hidden" name="Source" value="Job-site sign QR">
      <p class="hp"><label>Leave this empty <input name="company" tabindex="-1" autocomplete="off"></label></p>
      <div class="field"><label for="q-where">Where did you see the sign?</label><span class="help">The street name is plenty.</span>
        <input type="text" id="q-where" name="Sign location" autocomplete="off" required></div>
      <div class="field"><label for="q-about">What are you interested in?</label>
        <select id="q-about" name="Interested in" required>
          <option value="">Choose one&hellip;</option>
          <option>Buying or renting this home</option>
          <option>The work being done here</option>
          <option>Selling a home of my own nearby</option>
          <option>I&rsquo;m an agent or investor</option>
          <option>Just curious</option>
        </select></div>
      <div class="field"><label for="q-name">Your name</label>
        <input type="text" id="q-name" name="Name" autocomplete="name" required></div>
      <div class="field"><label for="q-contact">Phone or email</label><span class="help">Whichever you&rsquo;d rather we use.</span>
        <input type="text" id="q-contact" name="Phone or email" autocomplete="tel" required></div>
      <div class="field"><label for="q-notes">Your question <span style="font-weight:400;color:var(--gray)">(optional)</span></label>
        <textarea id="q-notes" name="Question" rows="3"></textarea></div>
      <button class="btn btn--primary btn--lg" type="submit" style="width:100%;margin-top:6px">Send my question</button>
      <p class="small" style="margin:16px 0 0;text-align:center">We never sell your information. Sending this means we may call or text you about your question; tell us to stop at any time and we will.</p>
    </form>
  </div>
</section>
""")


HELLO_THANKS = dict(
    url="/hello/thanks/", noindex=True,
    title="Thanks, We've Got Your Question | HARDT Southern California",
    desc=("Your question about the property is in. We usually reply within 15 minutes between "
          "8am and 6pm, Monday to Saturday, and first thing next morning otherwise."),
    og=og_img("og-hello"), ogalt="HARDT. What can we help you with?",
    head=CSS, chrome_top=TOP, chrome_bottom=bottom("Every situation has a way forward."),
    body=f"""
<section class="hello-hero">
  <div class="shell shell--narrow">
    <p class="eyebrow">Got it</p>
    <h1>Thanks. We&rsquo;ve got your question.</h1>
    <p class="lede">We usually reply within 15 minutes between 8am and 6pm, Monday to Saturday. Later than that, first thing the next morning.</p>
    <p style="margin-top:28px"><strong>Need us sooner?</strong> Call or text <a href="{SIGN_PHONE_TEL}" style="white-space:nowrap">{SIGN_PHONE_DISPLAY}</a>.</p>
    <div class="btnrow">
      <a class="btn btn--ghost" href="/hello/">Back</a>
      <a class="btn btn--ghost" href="/">Visit the site</a>
    </div>
  </div>
</section>
""")

PAGES = [HELLO, HELLO_THANKS]
