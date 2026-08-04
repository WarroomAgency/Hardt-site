"""The 16 county × service matrix pages — unique copy per intersection.

The 40% rule (CLAUDE.md): at least 40% of each page must be unique to that
county AND service. The test: if you could swap the county name and the page
would still be accurate, it isn't finished. Every block below is written
against that test — the local facts come from tools/research.py, where each
figure carries a source and a check date.

Structure per entry:
  h1, title, desc, lede      — head/meta, unique
  intro                      — 2–3 paragraphs, unique to the intersection
  facts                      — which research keys to surface, in order
  narr_h, narr               — "how it plays out here" narrative, unique
  faq                        — 3 Q&As, unique to the intersection
"""

# A closing paragraph for the narrative section, unique per page. Split out
# so the main entries stay readable. Foreclosure pages don't need one — the
# statutory-clock paragraph already carries them past the word floor.
NARR_EXTRA = {
("san-diego-county", "sell-my-house-fast"):
  "<p>One more local honesty: this county&rsquo;s prices mean even a tired house is a serious asset, "
  "and you should treat offers accordingly. Get ours in writing with the math attached, then show "
  "it to an agent you trust and ask what they&rsquo;d net you after repairs, commissions and time. If "
  "their answer beats ours, take it &mdash; we mean that, and the fact that almost nobody else in this "
  "category will say it is most of why people end up calling us anyway.</p>",
("san-diego-county", "inherited-house"):
  "<p>A word on timing pressure: nothing about San Diego probate rewards rushing, and nobody "
  "should sell an estate house to the first postcard that arrives. The court&rsquo;s calendar gives "
  "you weeks to gather real numbers &mdash; ours in writing, an agent&rsquo;s in writing &mdash; and the estate "
  "owes the heirs that comparison. We&rsquo;re comfortable being compared. The buyers who aren&rsquo;t are "
  "telling you something.</p>",
("san-diego-county", "sell-rental-property"):
  "<p>If your building is in one of the county&rsquo;s other cities &mdash; Chula Vista, El Cajon, La Mesa &mdash; "
  "the city ordinance question changes at each boundary, but the economics rarely do: vacancy, "
  "turnover work and commissions cost what they cost everywhere. We&rsquo;ll tell you plainly which "
  "rules apply to your address, because we have to know anyway to buy it properly.</p>",
("riverside-county", "sell-my-house-fast"):
  "<p>Distance deserves a straight word too. Some southwest-county owners assume a San Diego&ndash;based "
  "buyer treats Temecula as a stretch. The 15 corridor is our commute, the subcontractors we use "
  "work both counties, and the comps we price from are Riverside County comps &mdash; not coastal "
  "numbers with a discount guessed on top. The walkthrough is me, in person, same as everywhere "
  "we buy.</p>",
("riverside-county", "inherited-house"):
  "<p>Estates here also collide with the county&rsquo;s commuting reality: heirs scattered between "
  "Orange County, San Diego and out of state, a house in Menifee or Murrieta nobody can check on "
  "weekly. Vacant houses in tract neighbourhoods draw attention &mdash; HOA letters first, worse "
  "occasionally. Part of what an as-is sale buys an estate is simply ending the vacancy before "
  "it becomes its own problem.</p>",
("riverside-county", "sell-rental-property"):
  "<p>And if the rental is the house you yourself lived in before moving up or out &mdash; the classic "
  "southwest-county story &mdash; check with a CPA about the capital-gains exclusion clock before "
  "deciding when to sell. The window on the old primary-residence exclusion closes a few years "
  "after you move out, and we&rsquo;ve seen owners time a sale badly by weeks. It&rsquo;s your accountant&rsquo;s "
  "question, but it belongs on your list.</p>",
("san-bernardino-county", "sell-my-house-fast"):
  "<p>Worth saying plainly: this county gets treated as the region&rsquo;s discount bin by out-of-area "
  "buyers, and owners get offers priced off that prejudice rather than off the actual house. "
  "Fontana and Rancho Cucamonga carry real values; Redlands has streets that outprice parts of "
  "San Diego. We price the house and the street it&rsquo;s actually on, and we show the comps we "
  "used &mdash; which makes lazy lowballing impossible to disguise, including ours.</p>",
("san-bernardino-county", "inherited-house"):
  "<p>One more thing heirs here run into: the family house often secured the family&rsquo;s other "
  "obligations &mdash; a reverse mortgage, a HELOC from 2006, sometimes an old judgment lien nobody "
  "mentioned. None of these stop a sale; all of them come out of the proceeds through escrow. "
  "Pull a preliminary title report early &mdash; we&rsquo;ll arrange it at no cost &mdash; so the estate plans "
  "from the real number rather than the imagined one.</p>",
("san-bernardino-county", "sell-rental-property"):
  "<p>High Desert landlords, one extra note: a rental on well and septic adds infrastructure "
  "questions to the tenancy questions, and financed investors typically want both resolved "
  "before closing. We don&rsquo;t need the well tested to a lender&rsquo;s standard to commit &mdash; we test "
  "for our own information and carry the risk ourselves, which is usually the difference "
  "between a sale that closes and a listing that expires up there. Down the hill, the same "
  "commitment just means fewer contingencies and a date that holds.</p>",
("kern-county", "sell-my-house-fast"):
  "<p>The smaller towns deserve their own sentence. Shafter and Wasco run on ag and logistics "
  "payrolls, Tehachapi on the pass economy, Ridgecrest on the base &mdash; and each has streets "
  "where the buyer pool is a handful of people a year. That thinness is exactly where a "
  "committed cash buyer changes a seller&rsquo;s outcome most: we don&rsquo;t need a second bidder to "
  "show up before we can act, and our offer doesn&rsquo;t evaporate when a lender reads the town&rsquo;s "
  "name.</p>",
("kern-county", "inherited-house"):
  "<p>Kern estates also surface a generational quirk: houses bought in the &rsquo;60s and &rsquo;70s and "
  "never refinanced, meaning title is clean but paperwork is ancient &mdash; a deed in a maiden "
  "name, a decades-old trust never funded, a co-owner long gone. Title companies here know "
  "these patterns well, and most clear with an affidavit and patience. Budget the weeks, not "
  "months &mdash; and remember the recorder&rsquo;s counter timeline when planning them.</p>",
("kern-county", "sell-rental-property"):
  "<p>The yield math cuts one more way worth naming: because Kern buildings are cheap relative "
  "to their rents, they attract buyers who&rsquo;ve never operated here and price off a spreadsheet. "
  "When their assumptions crack &mdash; a turnover, a big system bill &mdash; they renegotiate or vanish. "
  "Our renovation history in this county is the reason our number survives contact with the "
  "building. Ask us what we&rsquo;ve spent on comparable roofs here; we&rsquo;ll tell you to the dollar.</p>",
}

# A fourth FAQ per page, split out so the main entries above stay readable.
# Each is unique to its county-service intersection — no recycling.
FAQ_EXTRA = {
("san-diego-county", "sell-my-house-fast"):
  ("Do you buy condos and townhomes here too?",
   "<p>Yes &mdash; and in this county that question matters, because HOA health is part of the price. We read the HOA documents, reserves and any pending special assessments or litigation before the offer, so the number already reflects them. A troubled HOA narrows your buyer pool badly; it doesn&rsquo;t remove us from it.</p>"),
("san-diego-county", "inherited-house"):
  ("The house is in a trust, not probate. Is that simpler?",
   "<p>Usually much simpler &mdash; a successor trustee can generally sell without the court&rsquo;s calendar, on the trust&rsquo;s own timeline. You&rsquo;ll want the trust document and a death certificate for title, and the sale itself works exactly like any other as-is purchase: one walkthrough, contents in place, your schedule.</p>"),
("san-diego-county", "stop-foreclosure"):
  ("What if I owe more than the house is worth?",
   "<p>Then the honest route is a short sale &mdash; your lender agreeing to accept less than the balance &mdash; and that&rsquo;s a conversation to have with the lender and a HUD-approved counsellor or an agent experienced in them, not primarily with a cash buyer. In equity-rich San Diego it&rsquo;s the rarer case, but when it&rsquo;s yours, we&rsquo;ll say so instead of wasting your clock.</p>"),
("san-diego-county", "sell-rental-property"):
  ("There&rsquo;s an occupied ADU on the property. Can you deal with that?",
   "<p>Yes &mdash; San Diego is the ADU capital of the state, and two tenancies on one parcel is a configuration we know well. Both tenancies transfer at close, each on its own terms, and the ADU&rsquo;s permit status gets read honestly into the price rather than discovered later.</p>"),
("riverside-county", "sell-my-house-fast"):
  ("My insurer non-renewed over wildfire risk. Does that affect the sale?",
   "<p>It affects financed buyers badly &mdash; no insurance, no loan &mdash; which is exactly why it doesn&rsquo;t affect us the same way. We buy for cash, arrange our own cover, and price the insurance reality of the location honestly. In the hills around the valley this has become one of the commonest reasons owners call.</p>"),
("riverside-county", "inherited-house"):
  ("Do I keep paying the HOA and Mello-Roos while the estate is open?",
   "<p>They keep accruing either way &mdash; HOA dues, special taxes and utilities are estate expenses, and letting them lapse invites liens and late penalties the estate pays eventually anyway. Budget for them in the estate accounting, and factor the carrying cost into how quickly the estate wants the house sold.</p>"),
("riverside-county", "stop-foreclosure"):
  ("My HOA is threatening its own foreclosure over unpaid dues. Is that real?",
   "<p>Real, and in this county&rsquo;s tract communities, common &mdash; California HOAs can foreclose on assessment liens separately from your mortgage. It runs on different rules and timelines than the bank&rsquo;s process. Bring the HOA letters to whatever professional you consult; in a sale, the arrears simply pay off through escrow like any other lien.</p>"),
("riverside-county", "sell-rental-property"):
  ("There&rsquo;s a property manager under contract. Do they have to sign off?",
   "<p>No &mdash; the management agreement is between you and them, and it doesn&rsquo;t give the manager a veto on your sale. Check your contract&rsquo;s termination clause for notice and any fee, keep them paid through close so records and keys transfer cleanly, and we&rsquo;ll coordinate the walkthrough with them if that&rsquo;s easier for the tenant.</p>"),
("san-bernardino-county", "sell-my-house-fast"):
  ("The house had a grow operation in it. Will anyone touch it?",
   "<p>We will, with eyes open. The county takes contamination and unpermitted electrical work seriously, and remediation orders follow the property &mdash; so the price reflects testing, cleanup and the electrical repair honestly. The rare cases we can&rsquo;t buy are the ones where title or health-order problems can&rsquo;t be cleared; we&rsquo;ll tell you which case you&rsquo;re in after the walkthrough, not after a contract.</p>"),
("san-bernardino-county", "inherited-house"):
  ("I&rsquo;m in Orange County and the house is in Victorville. How many trips is this?",
   "<p>Often none, sometimes one. Probate hearings for High Desert houses sit in Victorville, but attorneys handle most appearances and the court&rsquo;s portal handles the paper. On our side: the walkthrough is us, escrow signs by mobile notary wherever you are, and the house&rsquo;s keys, contents and condition stop being your problem at close.</p>"),
("san-bernardino-county", "stop-foreclosure"):
  ("I&rsquo;m behind on property taxes too. Is that a second foreclosure?",
   "<p>It&rsquo;s a second, slower clock &mdash; tax-defaulted property becomes subject to the county&rsquo;s power to sell after five years of delinquency, separate from your lender&rsquo;s process. The good news: tax arrears redeem through escrow in any sale, and five years is a far kinder timeline than 111 days. List both debts when you tally where you stand.</p>"),
("san-bernardino-county", "sell-rental-property"):
  ("It&rsquo;s rented by the room with nothing in writing. Can that even be sold?",
   "<p>Yes. Informal arrangements are still tenancies in California &mdash; month-to-month by operation of law &mdash; and they transfer like any other. We document what exists honestly (who pays what, since when), price around it, and handle the human side lawfully after close. It&rsquo;s a worse situation to keep than to sell.</p>"),
("kern-county", "sell-my-house-fast"):
  ("Half the houses here cool with swamp coolers. Do you mark that down?",
   "<p>We price it as the system it is: evaporative cooling is normal for Kern&rsquo;s climate and buyers here expect it. What moves the number isn&rsquo;t the cooler on the roof, it&rsquo;s the condition of what&rsquo;s under it &mdash; roof penetrations, duct state, and whether summer electrical load has been doing damage. That&rsquo;s a walkthrough question, not a penalty.</p>"),
("kern-county", "inherited-house"):
  ("The estate includes oil royalty payments tied to the land. What happens to those?",
   "<p>Usually they&rsquo;re severed rights the estate can keep or distribute separately from the house &mdash; selling the surface doesn&rsquo;t automatically sell the minerals, and Kern title reads this clearly. Tell your probate attorney they exist so the inventory captures them; on our side, the house sale simply proceeds around them.</p>"),
("kern-county", "stop-foreclosure"):
  ("My income is seasonal &mdash; oilfields, ag. Do lenders account for that?",
   "<p>Loss-mitigation departments can, if you ask formally &mdash; forbearance and modification programmes exist precisely for income interruption, and a HUD counsellor can help you present seasonal income properly. Start that conversation in writing, early. If the numbers still don&rsquo;t work, a controlled sale beats an auction &mdash; and we&rsquo;ll tell you honestly which side of that line your numbers sit.</p>"),
("kern-county", "sell-rental-property"):
  ("My tenants pay cash and there&rsquo;s no written lease. Deal-breaker?",
   "<p>No &mdash; a cash month-to-month tenancy is still a tenancy, and it transfers like any other. We&rsquo;ll document the terms that exist with a simple estoppel (who lives there, what they pay, since when), price the building on the real rent, and take over the relationship lawfully. No drama required, least of all for the tenant.</p>"),
}

M = {

# ═══════════════════════════════════ SAN DIEGO ═══════════════════════════════════

("san-diego-county", "sell-my-house-fast"): dict(
  h1="Sell a house as&#8209;is in San Diego County.",
  title="Sell Your House Fast in San Diego County | HARDT",
  desc="Sell as-is anywhere in San Diego County — El Cajon ranches, Chula Vista tract, coastal cottages. One walkthrough, one honest number, no repairs.",
  lede="This is our home county. A call in the morning is usually a walkthrough the same week &mdash; often the same day.",
  intro=(
    "<p>Most of the as-is houses we buy in San Diego County are East County "
    "houses: 1950s&ndash;70s ranches in El Cajon, Santee, La Mesa and Lemon Grove "
    "whose owners are staring down a roof, a repipe and a panel upgrade all at "
    "once. On a seventy-year-old house those aren&rsquo;t three surprises &mdash; they&rsquo;re "
    "the same surprise, and it arrives at inspection whoever the buyer is.</p>"
    "<p>We price that work as builders rather than negotiators. You see the "
    "finished value, the renovation budget and the margin &mdash; and if a "
    "contractor you trust says our repair number is inflated, we&rsquo;d genuinely "
    "rather hear it before closing than have you wonder after.</p>"),
  facts=("stock", "killers", "dtt"),
  narr_h="What as&#8209;is actually means here",
  narr=(
    "<p>San Diego&rsquo;s market punishes half-fixed houses. A partly permitted "
    "addition or a DIY kitchen doesn&rsquo;t add value on the open market &mdash; it adds "
    "questions, and financed buyers&rsquo; lenders ask them in writing. So when we "
    "say as-is, we mean it structurally: unpermitted garage conversion, "
    "original galvanised plumbing, a Federal Pacific panel an insurer just "
    "refused &mdash; all priced in, none of it yours to fix.</p>"
    "<p>The other thing being local buys you is speed without shortcuts. "
    "Because the drive is short, the walkthrough happens fast; because we "
    "renovate here constantly, the repair estimate doesn&rsquo;t need a week of "
    "sub quotes. Fourteen days from first call to close is typical when the "
    "title is clean &mdash; and this county&rsquo;s title records are the one place "
    "we&rsquo;ve had to slow down lately, since parcel-history searches moved "
    "back to in-person kiosks.</p>"),
  faq=[
    ("How fast can you actually close in San Diego County?",
     "<p>With clean title, about two weeks from first call &mdash; and the walkthrough usually happens within a day or two because this is home. Liens or probate add time, but that&rsquo;s the paperwork, not us.</p>"),
    ("The house has an unpermitted addition. Problem?",
     "<p>Common here, especially in East County. It changes the number &mdash; we price the cost of legalising or removing it &mdash; but it doesn&rsquo;t stop the sale. Bring whatever paperwork exists and we&rsquo;ll sort out the rest.</p>"),
    ("Do I pay transfer tax when I sell to you?",
     "<p>The county documentary transfer tax is $0.55 per $500 of price, and no San Diego County city we buy in adds its own on top. Who pays it is negotiable in the offer &mdash; and unlike commissions, it&rsquo;s the only percentage in the deal.</p>")],
),

("san-diego-county", "inherited-house"): dict(
  h1="An inherited house in San Diego County.",
  title="Sell an Inherited House in San Diego County | HARDT",
  desc="Probate runs through San Diego's Central Courthouse and takes months. We buy inherited houses as-is, contents included, on the court's timeline.",
  lede="The probate calendar downtown moves at its own pace. We work to the court&rsquo;s timeline, not against it &mdash; and the house can wait full of everything it holds.",
  intro=(
    "<p>Every San Diego County probate runs through one building: the Central "
    "Courthouse at 1100 Union Street. One venue for three-plus million people "
    "sets the tempo &mdash; petitions are examined before they&rsquo;re heard, examiners "
    "take calls half an hour a day, and hearing dates land weeks out. None of "
    "that is a problem for us. It&rsquo;s simply the schedule the sale lives on.</p>"
    "<p>What we actually do in the meantime is carry the house: it doesn&rsquo;t "
    "need to be emptied, cleaned, or shown. Take the photographs and the tools "
    "that matter, and leave the other forty years where they sit.</p>"),
  facts=("probate", "stock", "recorder"),
  narr_h="The East County estate house",
  narr=(
    "<p>The inherited house we see most in this county is specific: a "
    "1950s&ndash;60s ranch in El Cajon, La Mesa or Santee, owned outright for "
    "decades, original everything, deferred everything. Heirs get told to "
    "&ldquo;fix it up first&rdquo; &mdash; but a repipe, a rewire and a roof on a house you "
    "don&rsquo;t live in, managed from another city, mid-grief, is how estates "
    "burn a year and a renovation budget to net roughly what as-is money "
    "would have paid on day one. We&rsquo;ll show you both numbers and you can "
    "check our math with anyone.</p>"
    "<p>If the estate qualifies for the small-estate shortcuts or the house "
    "was held in a trust, the court may barely be involved and we can move "
    "on your schedule instead. That determination belongs to a probate "
    "attorney, not to a buyer &mdash; we&rsquo;ll work to whatever they say.</p>"),
  faq=[
    ("Where is probate actually handled here?",
     "<p>At the Central Courthouse, 1100 Union Street, downtown San Diego &mdash; probate for the whole county is heard there. Your attorney files electronically; hearings are typically set weeks out, so build the calendar around that.</p>"),
    ("Can you buy before the probate is finished?",
     "<p>Sometimes &mdash; it depends on the authority the court granted the representative and how title was held. With full independent authority, often yes; with limited authority, the sale may need court confirmation. Ask your probate attorney; we&rsquo;ll fit either path.</p>"),
    ("The house is full and I live out of state. Realistically, what do I do?",
     "<p>Realistically: nothing. We buy contents-in-place constantly &mdash; furniture, garage, paperwork, all of it. You take what matters by shipping box or by one trip, and the rest is our job, not yours.</p>")],
),

("san-diego-county", "stop-foreclosure"): dict(
  h1="Behind on payments in San Diego County.",
  title="Facing Foreclosure in San Diego County? | HARDT",
  desc="How California's foreclosure timeline plays out in San Diego County, what your options are at each stage, and straight answers with no pressure.",
  lede="The letters make it sound like next week. The statute says otherwise &mdash; and knowing where you actually stand is worth more than any offer.",
  intro=(
    "<p>A Notice of Default recorded against a San Diego County house starts "
    "the same statutory clock as everywhere in California &mdash; three months to "
    "reinstate before a sale can even be noticed, about 111 days minimum "
    "before an auction can happen, usually more. What&rsquo;s local is what the "
    "clock is worth: San Diego equity. Most people in default here still own "
    "real value, and every option below works better when you use the time "
    "rather than the last week of it.</p>"
    "<p>The options, plainly: reinstate if you can; ask the lender about a "
    "modification or forbearance; sell before the sale date and keep your "
    "equity; or talk to a HUD-approved counsellor about the rest. Selling to "
    "us is one branch of one option &mdash; and if listing would net you more and "
    "your timeline allows it, I&rsquo;ll say so on the first call.</p>"),
  facts=("recorder", "dtt", "stock"),
  narr_h="Why equity changes the calculus",
  narr=(
    "<p>In a county where even tired East County ranches carry substantial "
    "equity, letting a trustee sale happen is usually the worst financial "
    "outcome on the table &mdash; auction bidders price in their risk, and what "
    "they don&rsquo;t bid, you don&rsquo;t keep. A sale you control, at a price you saw "
    "the math on, closed before the auction date, preserves what the years "
    "of payments built.</p>"
    "<p>Two mechanical things worth knowing locally: the NOD and any Notice "
    "of Trustee&rsquo;s Sale are recorded documents, so confirming exactly what&rsquo;s "
    "been filed against your house takes one records check &mdash; and since "
    "parcel-number search moved off the county&rsquo;s website, that means a "
    "kiosk at a county office or a title contact who&rsquo;ll pull it. We do the "
    "second routinely, and knowing your true dates is free whether or not "
    "you ever talk to us again.</p>"),
  faq=[
    ("How much time do I really have?",
     "<p>Count from the recording date of the Notice of Default: three months before a sale can be noticed, then at least twenty more days before an auction &mdash; and the recorded documents, not the collection letters, are the truth of where you are. We can help you confirm what&rsquo;s actually on file.</p>"),
    ("Can I sell after a sale date is set?",
     "<p>Often, yes &mdash; up until the auction actually happens, a sale that pays the lender off in escrow stops the process. It gets tight and title has to move fast, which is one reason a cash buyer with a San Diego escrow team matters at that stage. Sooner is better; the last week is a bad plan.</p>"),
    ("Is talking to you a foreclosure-rescue service?",
     "<p>No. California regulates foreclosure consultants; we are not one, we charge nothing at any point, and we don&rsquo;t take fees to &ldquo;help.&rdquo; We buy houses as a principal. If buying yours makes sense we&rsquo;ll offer; if it doesn&rsquo;t, we&rsquo;ll tell you what we&rsquo;d do in your place &mdash; and a HUD-approved counsellor is free and on your side either way.</p>")],
  legal=True,
),

("san-diego-county", "sell-rental-property"): dict(
  h1="Done being a landlord in San Diego County.",
  title="Sell a Tenant-Occupied Rental in San Diego County | HARDT",
  desc="San Diego layers city tenant protections on state law. Selling with tenants in place sidesteps the hardest parts — no evictions, no vacancy, no repairs.",
  lede="Between state law and the city&rsquo;s own ordinance, the expensive path is emptying the building. So don&rsquo;t.",
  intro=(
    "<p>San Diego is the strictest rental market we buy in. Statewide "
    "just-cause rules cover most older rentals, and inside the city of San "
    "Diego the 2023 Tenant Protections Ordinance goes further &mdash; no-fault "
    "terminations come with relocation payments, typically two months&rsquo; rent, "
    "and the ordinance is enforced. The traditional advice &mdash; &ldquo;get the unit "
    "vacant, renovate, then list&rdquo; &mdash; now means months of carrying costs plus "
    "a relocation cheque before you&rsquo;ve earned a dollar.</p>"
    "<p>Selling occupied deletes that whole chapter. The tenancy transfers "
    "with the deed, the tenant&rsquo;s rights ride along undisturbed, and you&rsquo;re "
    "out at a number you saw the math on &mdash; without ever serving a notice.</p>"),
  facts=("stock", "dtt", "recorder"),
  narr_h="The maths of vacant-first, locally",
  narr=(
    "<p>Run the vacant-first plan against a real East County duplex: a "
    "no-fault termination with relocation assistance, a month or three of "
    "vacancy, a renovation on a 1960s building where the plumbing predates "
    "everyone involved, then commissions on the resale. It&rsquo;s common for "
    "that path to net less than an honest occupied price &mdash; before counting "
    "the risk that a termination is challenged, which in this city is a "
    "risk with teeth.</p>"
    "<p>We take the building as it stands: mid-lease or month-to-month, "
    "Section 8 with the housing authority paperwork, deposits prorated "
    "through escrow like any other credit. Your tenants keep their home; "
    "you keep your equity and your weekends.</p>"),
  faq=[
    ("Does the city&rsquo;s ordinance apply to my rental?",
     "<p>If the property is inside San Diego city limits, very likely &mdash; the 2023 ordinance covers most tenancies, with relocation payments on no-fault terminations. County-area and other-city rentals answer mainly to state law. Either way, selling with the tenant in place means the question never gets tested.</p>"),
    ("My tenant is behind on rent. Can I still sell?",
     "<p>Yes. Arrears, a payment plan, even an eviction already in motion &mdash; we&rsquo;ve bought through all of it. The situation gets priced honestly and handled after close by us, within the law, rather than by you under deadline.</p>"),
    ("Do I have to tell my tenant I&rsquo;m selling?",
     "<p>You have to respect notice rules for any entry &mdash; we schedule the single walkthrough legally and around their day. There&rsquo;s no requirement to market the sale to them, and because nobody is being displaced, the conversation is usually easier than landlords fear.</p>")],
),

# ═══════════════════════════════════ RIVERSIDE ═══════════════════════════════════

("riverside-county", "sell-my-house-fast"): dict(
  h1="Sell a house as&#8209;is in Riverside County.",
  title="Sell Your House Fast in Riverside County | HARDT",
  desc="Sell as-is in Temecula, Murrieta, Perris or Riverside. We price Mello-Roos, PACE liens and tract-stock repairs honestly — one walkthrough, one number.",
  lede="The southwest county&rsquo;s tract stock is young enough to look fine and old enough to need everything at once. We price what&rsquo;s actually there.",
  intro=(
    "<p>Riverside County as-is sales have a particular shape. The house is "
    "usually 1985&ndash;2010 tract &mdash; Temecula, Murrieta, Perris &mdash; and what&rsquo;s "
    "wrong isn&rsquo;t romantic old-house trouble, it&rsquo;s systems hitting end of "
    "life together: original HVAC, a twenty-year roof in year twenty-eight, "
    "early-90s plumbing. Cosmetically fine, mechanically due, and the open "
    "market prices that gap harshly once inspectors put it in writing.</p>"
    "<p>We&rsquo;d rather price it plainly at the start. You see finished value, "
    "the systems budget, the margin &mdash; and the offer doesn&rsquo;t shrink at "
    "week three, because there is no week three.</p>"),
  facts=("killers", "stock", "dtt"),
  narr_h="The two liens to find before anyone opens escrow",
  narr=(
    "<p>More Riverside County sales die late over tax-bill liens than "
    "anywhere else we work &mdash; and it&rsquo;s not the sellers&rsquo; fault. PACE/HERO "
    "financing was born in this county, so solar and efficiency assessments "
    "are everywhere; Mello-Roos rides on most of the newer tracts. Neither "
    "stops a sale. Both have to be found, priced, and paid or subordinated "
    "through escrow &mdash; and a buyer who discovers them in week four is a "
    "buyer who renegotiates or leaves.</p>"
    "<p>We pull the preliminary title report early and read the tax bill "
    "line by line, because we&rsquo;ve closed around both a hundred times. If "
    "your house is in the city of Riverside proper, we&rsquo;ll also flag the "
    "one local cost quirk: transfer tax there is double the county rate "
    "&mdash; worth knowing before you compare offers net-to-net.</p>"),
  faq=[
    ("There&rsquo;s a solar loan on the house. Can you still buy it?",
     "<p>Yes &mdash; this is the county where solar liens were invented, and we deal with them weekly. Leased panels, owned-but-financed, PACE assessments on the tax bill: each has a clean path through escrow. Bring whatever paperwork you have and we&rsquo;ll identify which one you&rsquo;ve got.</p>"),
    ("What&rsquo;s my Mello-Roos and does it kill my price?",
     "<p>It&rsquo;s on your property-tax bill as a special-district line, common across newer Temecula, Murrieta and French Valley tracts. It doesn&rsquo;t kill anything &mdash; it&rsquo;s a known monthly cost we and every informed buyer price in. Surprises kill deals; the assessment itself doesn&rsquo;t.</p>"),
    ("How fast can you close out here?",
     "<p>Around two weeks with clean title. I batch southwest-county trips, so tell me your timing &mdash; walkthroughs usually land within a few days, and the eSubmit-era county machinery records same-day through the title company.</p>")],
),

("riverside-county", "inherited-house"): dict(
  h1="An inherited house in Riverside County.",
  title="Sell an Inherited House in Riverside County | HARDT",
  desc="Riverside probate splits by region — Temecula cases go to Murrieta, not downtown. We buy inherited houses as-is, on the court's timeline.",
  lede="Which courthouse hears the estate depends on where the house sits &mdash; and for the southwest county, that&rsquo;s Murrieta, not a drive downtown.",
  intro=(
    "<p>Riverside County runs probate through regional venues: the Historic "
    "Courthouse downtown for the western county, the Southwest Justice "
    "Center in Murrieta for Temecula, Murrieta and the valley around them. "
    "For heirs, that geography is good news &mdash; a Temecula estate is handled "
    "twenty minutes away, filings go through the court&rsquo;s online portal, and "
    "out-of-area executors can keep the whole thing at arm&rsquo;s length.</p>"
    "<p>Our part is the house itself. Contents stay, maintenance stops "
    "being your problem at close, and if the court&rsquo;s calendar says three "
    "months, we&rsquo;re the buyer still standing there in three months.</p>"),
  facts=("probate", "stock", "dtt"),
  narr_h="Court confirmation, and the overbid that can help you",
  narr=(
    "<p>If the representative&rsquo;s authority is limited, a Riverside probate "
    "sale gets confirmed in court &mdash; and this county runs its overbid "
    "process on its own local form, with competing bidders invited to raise "
    "the price at the confirmation hearing. Sellers fear that step; it can "
    "actually work for the estate, since our offer sets a court-tested "
    "floor and any overbid only raises what the heirs receive. We stay in "
    "at our number and we don&rsquo;t flinch if someone outbids us honestly.</p>"
    "<p>One estate-specific cost note: inherited southwest-county houses "
    "often carry the same PACE assessments and Mello-Roos as everything "
    "else built there since the nineties. Those surface in the estate&rsquo;s "
    "title report, not as a crisis &mdash; just as line items the offer already "
    "accounts for.</p>"),
  faq=[
    ("Which court will the estate go through?",
     "<p>By region: southwest-county houses &mdash; Temecula, Murrieta, the valley &mdash; are heard at the Southwest Justice Center in Murrieta; western-county houses at the Historic Courthouse downtown. Your attorney files either way through the court&rsquo;s eSubmit portal.</p>"),
    ("What if the court has to confirm the sale?",
     "<p>Then the hearing includes the county&rsquo;s overbid procedure &mdash; open competitive bidding above our accepted offer, on the court&rsquo;s local form. It adds a few weeks and can only raise the estate&rsquo;s proceeds. We&rsquo;re comfortable with it and will walk you through what to expect.</p>"),
    ("Grandma&rsquo;s house has solar panels she financed. Whose problem is that now?",
     "<p>The estate&rsquo;s, technically &mdash; but practically, ours to solve in escrow. Financed panels and PACE assessments follow the property, get paid or subordinated at close, and are priced into the offer so there&rsquo;s no late surprise for the heirs.</p>")],
),

("riverside-county", "stop-foreclosure"): dict(
  h1="Behind on payments in Riverside County.",
  title="Facing Foreclosure in Riverside County? | HARDT",
  desc="California's foreclosure clock in Riverside County, why PACE liens make defaults here different, and every option on the table — stated plainly.",
  lede="Same statewide clock as everywhere &mdash; with one local twist: the other liens on the tax bill, and what they do to your real number.",
  intro=(
    "<p>The timeline itself is state law: a recorded Notice of Default, "
    "three months to reinstate, then at least twenty days&rsquo; notice before "
    "any auction &mdash; about 111 days minimum, usually more. Use the early "
    "part. Reinstatement, a lender modification, a counselled workout, or "
    "a controlled sale all work better with weeks in hand than days.</p>"
    "<p>What&rsquo;s distinctly Riverside about default is the second lien "
    "stack. This county pioneered PACE financing, and a default here often "
    "involves a mortgage <em>plus</em> a tax-bill assessment plus, in the newer "
    "tracts, Mello-Roos &mdash; which changes both your payoff math and what a "
    "rescue plan has to cover. Getting the full lien picture is step one, "
    "and it&rsquo;s free.</p>"),
  facts=("killers", "dtt", "recorder"),
  narr_h="Your equity math has more lines here",
  narr=(
    "<p>People in default usually know their mortgage balance and guess at "
    "the rest. In southwest Riverside the rest matters: a PACE assessment "
    "can be tens of thousands senior to everything, arrears accrue on the "
    "special taxes too, and an auction pays that stack before you see a "
    "dollar. A controlled sale prices the same stack transparently &mdash; we "
    "show the payoff lines one by one &mdash; and what&rsquo;s left is genuinely "
    "yours rather than what an auction happened to leave.</p>"
    "<p>And because the county recorder actively pursues even unrecorded "
    "transfers for tax, beware of anyone proposing clever title moves to "
    "&ldquo;buy time.&rdquo; The lawful options are the boring ones listed above. "
    "They&rsquo;re also the ones that actually preserve money.</p>"),
  faq=[
    ("What&rsquo;s actually recorded against my house?",
     "<p>The Notice of Default and any sale notice are public records with the county recorder, and your full lien picture &mdash; mortgage, PACE, special taxes &mdash; shows in a preliminary title report. We&rsquo;ll help you pull both so you&rsquo;re planning from facts. No charge, no obligation.</p>"),
    ("Can a sale still happen if there&rsquo;s no equity left after everything?",
     "<p>Sometimes &mdash; a short sale with lender approval &mdash; but that&rsquo;s a lender-and-counsellor conversation first, and we&rsquo;ll say so honestly rather than string you along. Where there is equity, which is common here, a pre-auction sale protects it.</p>"),
    ("Are you a foreclosure consultant?",
     "<p>No, and California law is strict about who is. We charge no fees, offer no rescue services, and buy property only as a principal. Free help exists: a HUD-approved housing counsellor can review every option with no stake in your answer &mdash; and we&rsquo;ll tell you the same thing on the phone.</p>")],
  legal=True,
),

("riverside-county", "sell-rental-property"): dict(
  h1="Done being a landlord in Riverside County.",
  title="Sell a Rental With Tenants in Riverside County | HARDT",
  desc="Sell a tenant-occupied Riverside County rental as-is — mid-lease, Section 8, or behind on rent. The tenancy transfers with the deed. No evictions.",
  lede="The rental you bought in 2005 did its job. Getting out shouldn&rsquo;t require getting anyone else out.",
  intro=(
    "<p>A lot of Riverside County rentals are accidental: the starter house "
    "kept after a move, the 2009 foreclosure-era buy that became someone&rsquo;s "
    "home for a decade. Now the owner is done &mdash; and discovers the exit the "
    "internet recommends means terminating a tenancy under state just-cause "
    "rules, floating a vacant tract house through a renovation, then paying "
    "commissions on the resale.</p>"
    "<p>The occupied sale is simpler in every dimension: the lease and the "
    "deposit transfer through escrow, rent prorates to the day of closing, "
    "and the tenant&rsquo;s next landlord is a company that fixes things. One "
    "walkthrough, scheduled inside the legal notice rules and around your "
    "tenant&rsquo;s shift pattern.</p>"),
  facts=("stock", "killers", "dtt"),
  narr_h="What we actually check on a tract rental",
  narr=(
    "<p>The southwest county&rsquo;s rental stock is mostly the same 1985&ndash;2010 "
    "tract as its owner-occupied stock, and it ages the same way: HVAC, "
    "roof, water heater, sometimes the early-90s plumbing. Long tenancies "
    "hide this &mdash; nobody calls about the roof until it leaks &mdash; so we "
    "assume systems-age by era rather than trusting a quick look, and the "
    "offer says so line by line. No post-inspection renegotiation, because "
    "the inspection thinking already happened.</p>"
    "<p>Two paper items to have handy: the lease (for the transfer) and "
    "the property-tax bill (because if there&rsquo;s Mello-Roos or a PACE "
    "assessment riding on it &mdash; and out here there often is &mdash; we price "
    "around it upfront). Section 8? The housing-authority relationship "
    "transfers; your tenant&rsquo;s voucher isn&rsquo;t disturbed.</p>"),
  faq=[
    ("My tenant&rsquo;s lease runs another 14 months. Do I wait?",
     "<p>No &mdash; the lease conveys with the property. We step into it exactly as written, terms and deposit intact, and the tenant&rsquo;s situation on the day after closing looks identical to the day before, minus the deferred maintenance.</p>"),
    ("Is my newer rental even covered by AB 1482?",
     "<p>Much of the southwest county&rsquo;s stock is young enough that the state law&rsquo;s fifteen-year rolling exemption matters &mdash; check the certificate-of-occupancy date rather than guessing. Either way it doesn&rsquo;t change our process: we buy occupied and nobody needs terminating.</p>"),
    ("The tenants stopped paying during COVID and never caught up. Now what?",
     "<p>We&rsquo;ve bought through exactly this. Arrears get disclosed and priced, any case in progress transfers to us to resolve lawfully, and you stop accruing the problem the day escrow closes. It&rsquo;s a worse story to carry than to sell.</p>")],
),

# ══════════════════════════════ SAN BERNARDINO ══════════════════════════════

("san-bernardino-county", "sell-my-house-fast"): dict(
  h1="Sell a house as&#8209;is in San Bernardino County.",
  title="Sell a House Fast in San Bernardino County | HARDT",
  desc="Sell as-is in San Bernardino, Fontana, Rancho Cucamonga, Redlands or Highland. Old-stock wiring, panels and plumbing priced honestly. One number.",
  lede="Half this county&rsquo;s housing tells its age at inspection &mdash; wiring, panels, plumbing. We price it like the builders we are and skip the theatre.",
  intro=(
    "<p>The as-is call from San Bernardino County usually starts the same "
    "way: the house is solid, but something an inspector will write in bold "
    "has surfaced. Aluminium branch wiring from the &rsquo;60s and &rsquo;70s. A "
    "Federal Pacific panel the insurer suddenly won&rsquo;t cover. Galvanised "
    "supply lines running rusty. In the older halves of San Bernardino, "
    "Redlands and Highland these aren&rsquo;t defects so much as the era &mdash; and "
    "financed buyers&rsquo; lenders and insurers have grown allergic to all "
    "three.</p>"
    "<p>We buy the era on purpose. The renovation plan already includes the "
    "rewire or the repipe, so the offer doesn&rsquo;t collapse when the "
    "inspection tells us what we already priced.</p>"),
  facts=("stock", "killers", "dtt"),
  narr_h="Valley floor and High Desert are different sales",
  narr=(
    "<p>Down the hill, the sale is straightforward: e-recording works "
    "same-day through the title company, city stock is on city services, "
    "and with clean title we close in about two weeks. Up the Cajon Pass "
    "it&rsquo;s a different transaction &mdash; wells, septic, and a county health "
    "department that wants a percolation test on file before septic "
    "permits move. Financed buyers routinely lose escrow weeks to well "
    "flow tests and septic certifications; cash exists to skip exactly "
    "that queue, and it&rsquo;s much of why we&rsquo;re useful to High Desert "
    "sellers.</p>"
    "<p>Either side of the pass, what you don&rsquo;t do is fix anything first. "
    "The number reflects the house as it stands &mdash; and the math behind it "
    "is on the table, not behind a curtain.</p>"),
  faq=[
    ("The insurance company just non-renewed over the electrical panel. Can you still buy?",
     "<p>Yes &mdash; Federal Pacific and Zinsco panels are a known quantity for us; the panel swap is in our renovation budget before we ever see yours. Your sale doesn&rsquo;t need the insurer&rsquo;s blessing; our purchase doesn&rsquo;t either.</p>"),
    ("My house is on a well and septic near Phelan. Does that slow you down?",
     "<p>Less than it slows anyone else. County health wants its paperwork &mdash; percolation records for septic work, and buyers typically want well tests &mdash; but as a cash buyer we&rsquo;re not waiting on a lender&rsquo;s checklist. We test for our own information and close on schedule.</p>"),
    ("What does closing actually cost me here?",
     "<p>Transfer tax is $0.55 per $500 with no city add-ons in the cities we buy in, escrow and title fees are negotiated in the offer, and there are no commissions because nobody is brokering anything. The offer states who pays what, in writing.</p>")],
),

("san-bernardino-county", "inherited-house"): dict(
  h1="An inherited house in San Bernardino County.",
  title="Inherited a House in San Bernardino County? | HARDT",
  desc="San Bernardino probate is heard in Fontana and Victorville — not downtown. We buy inherited houses as-is, contents included, on the court's clock.",
  lede="Probate here moved &mdash; Fontana and Victorville hear the county&rsquo;s estates now. The house, meanwhile, can wait exactly as it is.",
  intro=(
    "<p>First practical fact most San Bernardino County heirs learn: since "
    "early 2024, probate isn&rsquo;t heard at the downtown Justice Center. "
    "Decedents&rsquo; estates are filed and heard in Fontana &mdash; or Victorville "
    "for the High Desert &mdash; and the examiner&rsquo;s &ldquo;probate notes&rdquo; on your "
    "petition post to the court&rsquo;s portal two weeks before the hearing. "
    "Clear those notes early and the estate moves; ignore them and the "
    "hearing continues to a later date, which is how six months becomes "
    "ten.</p>"
    "<p>None of that requires the house to be touched. We buy estate "
    "houses full, tired, and exactly as the last decade left them.</p>"),
  facts=("probate", "stock", "killers"),
  narr_h="The estate house, valley and desert editions",
  narr=(
    "<p>The valley-floor estate house is the county&rsquo;s old stock in "
    "concentrate: a Redlands or San Bernardino bungalow owned since the "
    "&rsquo;70s, original wiring and plumbing, and forty years of contents. "
    "Heirs get quoted renovation numbers that assume a live-in owner&rsquo;s "
    "patience. We quote as-is and take the contents question off the "
    "table entirely.</p>"
    "<p>The High Desert estate house adds infrastructure: well, septic, "
    "maybe a parcel line nobody ever surveyed. Out-of-town heirs "
    "underestimate how much these complicate a financed sale &mdash; well "
    "tests, septic pump-and-certify, county health paperwork &mdash; and "
    "overestimate what the market pays for acreage. We&rsquo;ve bought both "
    "editions; the honest number comes with the reasoning attached.</p>"),
  faq=[
    ("Where does the estate get filed now?",
     "<p>Fontana District for most of the county, Victorville for the High Desert &mdash; downtown San Bernardino stopped hearing probate in February 2024. Your attorney will know; if you&rsquo;re doing it yourself, check the court&rsquo;s &ldquo;where probate cases are filed&rdquo; order before driving anywhere.</p>"),
    ("What are probate notes and why do they matter to selling?",
     "<p>They&rsquo;re the court examiner&rsquo;s published list of what&rsquo;s missing or defective in a filing, posted online about two weeks pre-hearing. Estates that clear their notes keep their dates; estates that don&rsquo;t get continued. Since our purchase rides the court&rsquo;s calendar, those notes are effectively the sale&rsquo;s schedule too.</p>"),
    ("The family house is in Phelan on a well. Will that sink the estate sale?",
     "<p>No &mdash; it narrows the buyer pool to people who understand wells and septic, which is a category we&rsquo;re squarely in. We price the infrastructure honestly, handle the county-health paperwork, and don&rsquo;t need a lender&rsquo;s comfort to close.</p>")],
),

("san-bernardino-county", "stop-foreclosure"): dict(
  h1="Behind on payments in San Bernardino County.",
  title="Facing Foreclosure in San Bernardino County? | HARDT",
  desc="The California foreclosure timeline as it plays out in San Bernardino County, your options at each stage, and honest answers without the pressure.",
  lede="The clock is state law. What you do with it &mdash; reinstate, negotiate, sell, or get counselled &mdash; is the part you still control.",
  intro=(
    "<p>From the day a Notice of Default records with the county, "
    "California gives you three months before a sale can even be noticed, "
    "and at least twenty more days before an auction &mdash; roughly 111 days "
    "minimum, longer in practice. San Bernardino&rsquo;s recorder runs same-day "
    "e-recording, so the documents in your mail are usually current; the "
    "dates on them, not the tone of the letters around them, are what "
    "matter.</p>"
    "<p>Every option stays on this table until late: reinstatement, a "
    "modification or forbearance from the lender, a HUD-counselled plan, "
    "or a sale you control before the auction controls it for you. We&rsquo;re "
    "the last of those, and only when it&rsquo;s genuinely your best number.</p>"),
  facts=("recorder", "stock", "dtt"),
  narr_h="Equity in an affordable county",
  narr=(
    "<p>San Bernardino has long been where Southern California&rsquo;s "
    "first-time buyers could actually buy &mdash; which means many defaults "
    "here sit on houses bought years ago with real appreciation behind "
    "them. That equity is precisely what an auction burns: bidders "
    "discount for unknowns, and the discount comes out of your side of "
    "the ledger. A controlled pre-auction sale converts the same equity "
    "at a price you examined, with the payoff lines shown.</p>"
    "<p>If the arithmetic is thinner &mdash; recent purchase, low equity &mdash; "
    "we&rsquo;ll say that plainly too, because a short sale or a counselled "
    "workout beats pretending. The conversation costs nothing and "
    "commits you to nothing; the recorded dates cost nothing to check, "
    "and we&rsquo;ll help you check them.</p>"),
  faq=[
    ("How do I find out exactly what&rsquo;s been recorded?",
     "<p>The NOD and any sale notice are public at the county recorder &mdash; the office e-records same-day, so the record is current. We&rsquo;ll pull what&rsquo;s filed against your address and read you the actual dates, free, whether or not we ever talk again.</p>"),
    ("The house needs work I can&rsquo;t afford. Does that close the sale option?",
     "<p>No &mdash; it just changes which buyers are real. This county&rsquo;s older stock in default often needs the classic trio (wiring, panel, plumbing), which financed buyers struggle with on a deadline. We price the work in and close on the calendar you&rsquo;re actually facing.</p>"),
    ("Someone offered to &ldquo;take over my payments.&rdquo; Should I?",
     "<p>Be very careful. Subject-to arrangements on a house in default are where sellers get hurt &mdash; and California law regulates equity purchases from owners in foreclosure for exactly that reason. Have any such offer read by an attorney or HUD counsellor first. Our approach is the boring one: a recorded sale, escrow, your payoff shown line by line.</p>")],
  legal=True,
),

("san-bernardino-county", "sell-rental-property"): dict(
  h1="Done being a landlord in San Bernardino County.",
  title="Sell a Rental in San Bernardino County | HARDT",
  desc="Sell a tenant-occupied San Bernardino County rental as-is — deferred maintenance, Section 8, arrears and all. The tenancy transfers. No evictions.",
  lede="A decade of deferred maintenance between tenancies is normal here. We price it plainly &mdash; you don&rsquo;t fix it, and nobody gets displaced.",
  intro=(
    "<p>The San Bernardino County rental we see most is a workhorse: "
    "bought affordably, rented continuously, maintained reactively. After "
    "ten or fifteen years the gap between rent-ready and market-ready has "
    "grown to a renovation &mdash; and the owner is being told to empty the "
    "house, spend the renovation, and list, all to reach buyers who&rsquo;ll "
    "then inspect the &rsquo;60s wiring anyway.</p>"
    "<p>Selling occupied skips the whole sequence. State just-cause law "
    "keeps termination genuinely costly; transferring the tenancy costs "
    "nothing. Lease, deposit and the housing-authority relationship (if "
    "it&rsquo;s a Section 8 tenancy) all move through escrow, and your tenant&rsquo;s "
    "Tuesday is undisturbed.</p>"),
  facts=("stock", "dtt", "recorder"),
  narr_h="Pricing the workhorse honestly",
  narr=(
    "<p>We assume era-typical systems rather than hoping: galvanised "
    "plumbing and aluminium-wiring-vintage electrics in the older valley "
    "stock, roofs by decade, panels by brand. Long tenancies mask "
    "condition &mdash; tenants report failures, not fatigue &mdash; so our number "
    "is built from what the era says is behind the walls, and we show "
    "that reasoning instead of discovering it dramatically after a "
    "contract is signed.</p>"
    "<p>Bring the lease and the last tax bill to the first call. "
    "Everything else &mdash; the walkthrough inside legal notice rules, the "
    "deposit proration, the arrears conversation if there is one &mdash; is "
    "process we&rsquo;ve run many times, and it lands gently on the person "
    "living there.</p>"),
  faq=[
    ("My rental is in rough shape and occupied. Do you need it vacant to assess it?",
     "<p>No. One walkthrough, legally noticed and scheduled around your tenant, is enough &mdash; and where access is genuinely difficult we can work from era, exterior and what you can tell us, with the assumptions written into the offer.</p>"),
    ("It&rsquo;s a Section 8 tenancy. Does that complicate the sale?",
     "<p>It changes the paperwork, not the outcome. The housing-authority contract moves with ownership, inspections continue on their cycle, and the voucher is untouched. We&rsquo;ve carried Section 8 tenancies through closing repeatedly &mdash; it&rsquo;s routine.</p>"),
    ("Can I sell if I&rsquo;ve already started an eviction?",
     "<p>Yes &mdash; disclose where the case stands and we&rsquo;ll price and plan around it. The matter transfers with the property and we resolve it lawfully after close. It&rsquo;s usually better for everyone than racing the courthouse.</p>")],
),

# ══════════════════════════════════ KERN ══════════════════════════════════

("kern-county", "sell-my-house-fast"): dict(
  h1="Sell a house as&#8209;is in Kern County.",
  title="Sell Your House Fast in Kern County, CA | HARDT",
  desc="Sell as-is in Bakersfield, Shafter, Wasco, Tehachapi or Ridgecrest. We've renovated here for years — honest numbers in a market where math is tight.",
  lede="We&rsquo;ve renovated more houses in Kern than anywhere else. The offers here come with a builder&rsquo;s local math, not a formula&rsquo;s.",
  intro=(
    "<p>Kern is where much of our renovation track record actually lives &mdash; "
    "Shenandoah Drive, Cale Court, Terrace Way, Huskey Drive. That matters "
    "to a seller for one reason: our repair numbers here aren&rsquo;t estimates "
    "from a spreadsheet, they&rsquo;re last quarter&rsquo;s invoices. When the margin "
    "between as-is and after-repair is as tight as Kern&rsquo;s, a buyer who&rsquo;s "
    "guessing either lowballs you to stay safe or renegotiates when the "
    "guess breaks. We don&rsquo;t need to do either.</p>"
    "<p>The stock we buy most is Bakersfield&rsquo;s 1950s&ndash;70s core &mdash; same "
    "mid-century systems story as coastal counties, at a price point where "
    "every repair dollar shows in the outcome.</p>"),
  facts=("stock", "killers", "recorder"),
  narr_h="Tight math, stated out loud",
  narr=(
    "<p>Here&rsquo;s the honest version of Kern economics: a renovation that "
    "pencils easily in Chula Vista can fail to pencil in Wasco, because "
    "the finished value ceiling is lower while the cost of a roof is not. "
    "That&rsquo;s why some Kern &ldquo;fixer&rdquo; listings sit for months &mdash; the math "
    "doesn&rsquo;t work at the asking price, and everyone who runs it walks. "
    "When we make an offer, the math that made it work is on the table: "
    "finished value from real local comps, work budget from our own subs, "
    "margin stated. If the numbers say the better move is listing it "
    "as-is with an agent instead, that&rsquo;s what I&rsquo;ll tell you.</p>"
    "<p>Mechanics note: Kern records at the counter and by mail &mdash; the "
    "title company handles closing day fine, but paperwork you record "
    "yourself takes weeks to come back, so we build that into any "
    "pre-sale title cleanup.</p>"),
  faq=[
    ("Why is your offer different from the we-buy-houses postcards I get?",
     "<p>Mostly because it comes with its arithmetic attached. We renovate in Kern constantly, so the repair budget is real, the comps are real, and the margin is stated &mdash; and we don&rsquo;t assign the contract to a stranger, so the name on the offer is the name at closing.</p>"),
    ("My house in Ridgecrest is a long way from anywhere. Do you actually come out?",
     "<p>Yes &mdash; I batch Kern trips and Ridgecrest is on the route. Tell me your timing; the walkthrough is me, in person, and usually lands within the week.</p>"),
    ("What&rsquo;s the transfer tax situation here?",
     "<p>$0.55 per $500 with no city add-ons &mdash; but Kern calculates it on the price or the unencumbered assessed value, whichever is greater, which is unusual and occasionally surprises below-market transfers. On a normal sale to us, the price governs and the offer states who pays it.</p>")],
),

("kern-county", "inherited-house"): dict(
  h1="An inherited house in Kern County.",
  title="Sell an Inherited House in Kern County, CA | HARDT",
  desc="Kern probate files at the Juvenile Justice Center in Bakersfield, and heirs often live hours away. We buy estate houses as-is, contents and all.",
  lede="Kern estates usually come with distance &mdash; heirs in San Diego or out of state, a house in Bakersfield, and a court system nobody knows.",
  intro=(
    "<p>Kern probate starts somewhere nobody guesses: the Juvenile Justice "
    "Center on College Avenue in Bakersfield &mdash; that&rsquo;s simply where the "
    "probate division sits. The court runs a dedicated examiner line and "
    "hears remote appearances in its probate department, which matters "
    "because the Kern executor who actually lives in Kern is the "
    "exception. Parents settled here for work decades ago; the heirs "
    "live everywhere else.</p>"
    "<p>That distance is the real burden we remove. The house doesn&rsquo;t "
    "need emptying, checking on, or a local cousin managing keys &mdash; we "
    "carry it as it stands, on the court&rsquo;s timeline, while you handle "
    "the estate from wherever you are.</p>"),
  facts=("probate", "recorder", "stock"),
  narr_h="Settling an estate from three hundred miles away",
  narr=(
    "<p>The recurring Kern estate: a paid-off ranch house in east or "
    "central Bakersfield, original systems, full of a life &mdash; and four "
    "heirs on three time zones. The listing route means someone flies in "
    "to empty it, someone manages a renovation by phone, and the house "
    "sits vacant (uninsured vacancies get expensive) while the market "
    "decides. The as-is route means one video call, one walkthrough we "
    "handle, and proceeds split by the estate&rsquo;s math rather than eaten "
    "by its logistics.</p>"
    "<p>Paper timing is the one local trap: affidavits and deeds the "
    "family records themselves come back from Kern&rsquo;s counter in weeks, "
    "not days. Anything title needs recorded, we route through the title "
    "company&rsquo;s channel instead &mdash; same county, professional lane, no "
    "lost month.</p>"),
  faq=[
    ("Nobody in the family lives in Kern anymore. How does the sale work practically?",
     "<p>Remotely, almost entirely. The court hears appearances remotely in its probate department, escrow signs by mobile notary wherever each heir lives, and the house itself is our problem from walkthrough onward. Most Kern estates we buy close without a single family trip.</p>"),
    ("The house has been empty for a year. Is that an issue?",
     "<p>It&rsquo;s a common one &mdash; vacancy is hard on houses and insurance. It doesn&rsquo;t change our interest; it usually strengthens the case for selling as-is soon rather than after another winter. We price what the vacancy has done honestly.</p>"),
    ("Is there oil or mineral rights weirdness on Kern titles?",
     "<p>Often, and it&rsquo;s usually fine: mineral rights were severed from the surface on much of the county long ago. It&rsquo;s a title-report line we know how to read, not a crisis &mdash; it rarely affects a residential sale, and we&rsquo;ll flag it plainly if your title carries anything unusual.</p>")],
),

("kern-county", "stop-foreclosure"): dict(
  h1="Behind on payments in Kern County.",
  title="Facing Foreclosure in Kern County, CA? | HARDT",
  desc="California's foreclosure timeline in Kern County, what the recorded notices actually mean, and every option stated plainly — with no pressure.",
  lede="Same California clock, smaller-town pressure. The recorded dates are the truth; the phone calls are just noise around them.",
  intro=(
    "<p>The statutory timeline doesn&rsquo;t change at the county line: a "
    "recorded Notice of Default opens three months to reinstate, a sale "
    "needs at least twenty days&rsquo; notice after that, and the practical "
    "minimum is around 111 days with most cases running longer. What "
    "changes in Kern is the surroundings: lower balances, thinner "
    "margins for error, and &mdash; in the smaller towns especially &mdash; a "
    "default that everyone on the street seems to know about before "
    "you&rsquo;ve decided anything.</p>"
    "<p>Decide from the record, not the neighbours. Reinstatement, "
    "lender workout, HUD-counselled plan, controlled sale &mdash; the full "
    "menu applies here, and the earlier weeks buy more than the later "
    "ones.</p>"),
  facts=("recorder", "stock", "dtt"),
  narr_h="Where the equity math lands here",
  narr=(
    "<p>Kern defaults split into two stories. Houses held for decades &mdash; "
    "common in Bakersfield&rsquo;s older core &mdash; often carry more equity than "
    "their owners assume, and that equity survives a controlled sale far "
    "better than an auction, where bidders discount hard for a market "
    "they know is unforgiving. Recent purchases carry less cushion, and "
    "for those the honest first stop is the lender and a HUD counsellor, "
    "not a buyer &mdash; we&rsquo;ll say exactly that when it&rsquo;s true.</p>"
    "<p>Confirming where you stand is mechanical: the NOD and any sale "
    "notice are recorded at Truxtun Avenue and we&rsquo;ll pull what&rsquo;s "
    "actually filed, free. One Kern-specific caution: in a county where "
    "recording your own paperwork takes weeks, last-minute title "
    "manoeuvres are even worse ideas than usual. The lawful, boring "
    "options are the ones that work.</p>"),
  faq=[
    ("Everyone from the courthouse steps list is calling me. Are you one of them?",
     "<p>We see the same public record everyone sees &mdash; that&rsquo;s how the system works &mdash; but we&rsquo;re not a call centre and there&rsquo;s no script. You&rsquo;d talk to me, once, and if what you need is a counsellor or your lender&rsquo;s workout department, that&rsquo;s the advice you&rsquo;ll get.</p>"),
    ("Can I sell with a sale date three weeks out?",
     "<p>It&rsquo;s tight but it&rsquo;s been done &mdash; cash, a motivated escrow, and clean-enough title are the requirements, and the payoff must reach the trustee before the auction. Call before it&rsquo;s three weeks if you possibly can; every extra week widens your options.</p>"),
    ("Will you charge me anything to figure out my options?",
     "<p>Nothing, ever &mdash; California heavily regulates charging homeowners in foreclosure for help, and we&rsquo;re not in that business. We buy houses as a principal. The options conversation is free, and a HUD-approved counsellor is a free, no-stake second opinion we&rsquo;ll actively point you to.</p>")],
  legal=True,
),

("kern-county", "sell-rental-property"): dict(
  h1="Done being a landlord in Kern County.",
  title="Sell a Rental With Tenants in Kern County | HARDT",
  desc="Sell a tenant-occupied Kern County rental as-is — Section 8, month-to-month, or long-vacant between tenants. The tenancy transfers at closing.",
  lede="Kern rentals earn steadily and age quietly. When you&rsquo;re done, the tenancy can transfer with the deed &mdash; voucher, deposit and all.",
  intro=(
    "<p>Kern&rsquo;s rental economics attracted a generation of landlords &mdash; "
    "prices low enough to buy in cash, rents steady, Section 8 demand "
    "constant. The same economics complicate the exit: the pool of local "
    "buyers for an occupied older rental is thin, financed investors are "
    "rate-shy, and the &ldquo;empty it and list&rdquo; route spends money a Kern "
    "resale price struggles to return.</p>"
    "<p>We&rsquo;re the buyer that pool is missing. The tenancy &mdash; lease terms, "
    "deposit, the housing-authority contract if there is one &mdash; transfers "
    "through escrow intact, the tenant keeps their home with a landlord "
    "who fixes things, and you exit at a number whose math you&rsquo;ve seen.</p>"),
  facts=("stock", "recorder", "dtt"),
  narr_h="Out-of-town owner, local building",
  narr=(
    "<p>A striking share of Kern rentals belong to owners who&rsquo;ve never "
    "lived in Kern &mdash; bought for the yield from LA or San Diego, managed "
    "by phone ever since. If that&rsquo;s you, the sale can stay remote: one "
    "noticed walkthrough that we handle with the tenant directly, "
    "documents by mobile notary, proceeds by wire. The management "
    "relationship, if there&rsquo;s a local property manager, winds down on "
    "your schedule rather than being needed for the sale.</p>"
    "<p>Condition-wise we assume Kern&rsquo;s eras honestly &mdash; 1950s&ndash;70s core "
    "stock means the mid-century systems bill sooner or later, and long "
    "tenancies mean later has usually arrived. It&rsquo;s in the number from "
    "the start, which is why the number doesn&rsquo;t move after the "
    "walkthrough.</p>"),
  faq=[
    ("My tenant has been there eleven years and pays under market. Does that tank the price?",
     "<p>It shapes it honestly rather than tanks it &mdash; we underwrite the actual rent, not a fantasy rent, and a long, stable tenancy is worth something real to a buyer who intends to keep the building running. What we won&rsquo;t do is price it assuming a displacement we have no intention of causing.</p>"),
    ("The housing authority inspection is due next month. Sell before or after?",
     "<p>Either works &mdash; the contract and inspection cycle transfer with ownership, and we&rsquo;ve taken buildings mid-cycle. If the inspection is likely to write up deferred items, selling before simply means those items are ours to cure, which is rather the point.</p>"),
    ("It&rsquo;s vacant between tenants and I don&rsquo;t want to re-let. Still interested?",
     "<p>Yes &mdash; a vacant Kern rental is carrying insurance and utilities against no income, which is its own clock. We can move at vacancy speed: walkthrough this week, close in about two.</p>")],
),
}
