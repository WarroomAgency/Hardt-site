"""County research layer — the facts that make the county and matrix pages
defensible, with a source and a check date on every figure.

THE RULE (from CLAUDE.md, and it ends the project if broken): do not invent
numbers. Every entry here was read from the cited source on the date given.
Refresh quarterly: re-open each src URL, confirm the figure, update CHECKED.

Rendering happens in pages.py. This file is data only, so a quarterly
refresh is an edit here and a re-run, not a copy hunt across 34 pages.
"""

CHECKED = "August 2026"

# ── Statewide facts used on multiple pages ──────────────────────────────
# California non-judicial foreclosure clock (Civil Code §2924 et seq.):
#   NOD recorded → 3-month statutory period → Notice of Trustee's Sale may
#   be recorded (sale no earlier than 3 months + 20 days after the NOD).
#   Practical minimum ≈ 111 days; most take longer.
#   SB 1079 (Civ. Code §2924m, eff. 2021): after the auction, eligible
#   owner-occupant bidders and tenants get 15/45-day windows to match or
#   beat the winning bid on 1–4 unit properties.
# src: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=2924
# AB 1482 (Civ. Code §1946.2, eff. 2020): statewide just-cause and rent-cap
#   rules for most housing older than 15 years.
# src: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1946.2

FORECLOSURE_STATE = (
    "California foreclosures run on a statutory clock, not the lender's mood. "
    "A recorded Notice of Default opens a three-month period in which you can "
    "reinstate the loan. Only after that can a Notice of Trustee&rsquo;s Sale go up, "
    "with the auction itself no sooner than twenty days later: about 111 days "
    "minimum from NOD to sale, and usually longer in practice. Even after an "
    "auction, state law (SB&nbsp;1079) gives owner-occupant bidders and tenants a "
    "window to match the winning bid on houses of one to four units."
)

# ── Per-county research ─────────────────────────────────────────────────
# Each fact block: (heading, html) — html may contain <a> to the source.
# "sources" renders as a small footnote line on the page.

RESEARCH = {

"san-diego-county": dict(
    recorder=dict(
        h="Recording a deed",
        html=("The county Assessor/Recorder/County Clerk records deeds at five "
              "offices around the county, and title companies e-record the same "
              "day in a normal escrow. One wrinkle worth knowing: since December "
              "2024, state law (AB&nbsp;1785) removed parcel-number search from the "
              "county&rsquo;s online records index. Looking up a property&rsquo;s recorded "
              "history by APN now means a records kiosk at a county office."),
        src="https://www.sdarcc.gov/content/arcc/home/divisions/recorder-clerk/recording.html",
        srcname="SD Assessor/Recorder/County Clerk"),
    dtt=dict(
        h="Transfer tax",
        html=("Documentary transfer tax is $0.55 per $500 of price ($550 on a "
              "$500,000 house), and none of the cities we buy in add a city tax "
              "on top. A county proposal to raise the rate was dropped in "
              "January 2026, so the number above is current."),
        src="https://www.sdarcc.gov/content/arcc/home/divisions/recorder-clerk/recording.html",
        srcname="SD Recorder; county news, Jan 2026"),
    probate=dict(
        h="Probate here",
        html=("Probate for the whole county is heard downtown at the Central "
              "Courthouse, 1100 Union Street. Attorneys have been required to "
              "e-file since April 2021; the probate examiners who review every "
              "filing take calls for one half-hour window a day (10&ndash;10:30am), "
              "which tells you most of what you need to know about the "
              "calendar. Plan in months, not weeks."),
        src="https://www.sdcourt.ca.gov/sdcourt/probate2",
        srcname="Superior Court of California, County of San Diego"),
    stock=dict(
        h="The housing stock",
        html=("Three markets wearing one county&rsquo;s name. East County (El Cajon, "
              "La Mesa, Santee, Lemon Grove) is dominated by 1950s&ndash;70s "
              "single-storey ranches, which is the era of galvanised supply "
              "lines, undersized panels and additions that never saw a permit. "
              "Chula Vista splits in two: older stock west of the 805, and "
              "1990s&ndash;2000s master-planned tract to the east, where Mello-Roos "
              "special-tax districts ride on the tax bill. Near the coast, "
              "anything inside the coastal zone can need a Coastal Development "
              "Permit before it changes shape, which is one reason small old "
              "coastal cottages sell to people with patience."),
        src=None, srcname=None),
    killers=dict(
        h="What kills deals here",
        html=("Unpermitted additions and garage conversions surface at "
              "inspection constantly, East County especially. Mello-Roos in "
              "eastern Chula Vista changes a buyer&rsquo;s monthly cost and gets "
              "missed by out-of-area buyers. And ADU potential cuts the other "
              "way: a lot that can legally hold a second unit is worth more "
              "than the house on it suggests, and we price that in rather than "
              "hoping you don&rsquo;t know."),
        src=None, srcname=None),
),

"riverside-county": dict(
    recorder=dict(
        h="Recording a deed",
        html=("The Assessor&ndash;County Clerk&ndash;Recorder records countywide, with "
              "offices including Riverside and Temecula, and e-recording "
              "through title companies is routine. The office also actively "
              "pursues transfer tax on <em>unrecorded</em> changes of ownership "
              "(entity transfers included), so &ldquo;we just won&rsquo;t record it&rdquo; is not "
              "a strategy here."),
        src="https://www.rivcoacr.org/documentary-transfer-tax-exemption",
        srcname="Riverside County ACR"),
    dtt=dict(
        h="Transfer tax",
        html=("Countywide the rate is $0.55 per $500. Inside the city of "
              "Riverside it doubles to $1.10 per $500: the county&rsquo;s own "
              "information sheet prints it in bold. Temecula, Murrieta and "
              "Perris charge no city add-on. On a $500,000 sale that&rsquo;s $550 "
              "in Temecula and $1,100 in the city of Riverside, which is worth knowing "
              "before you compare net sheets."),
        src="https://www.rivcoacr.org/media/Forms/Recorder/Recorder_Forms/documentary-transfer-tax-information-sheet---acr195_ada.pdf",
        srcname="ACR form 195"),
    probate=dict(
        h="Probate here",
        html=("Where your case is heard depends on where you live: the "
              "Historic Courthouse at 4050 Main Street downtown serves the "
              "western county, and the Southwest Justice Center in Murrieta "
              "serves Temecula, Murrieta and the surrounding valley, which spares "
              "a Temecula estate the drive downtown. Filings go through the court&rsquo;s eSubmit portal, and "
              "court-supervised sales use the county&rsquo;s own overbid form "
              "(RI-PR008) at the confirmation hearing."),
        src="https://www.riverside.courts.ca.gov/divisions/probate",
        srcname="Superior Court of California, County of Riverside"),
    stock=dict(
        h="The housing stock",
        html=("Southwest Riverside is overwhelmingly 1985&ndash;2010 tract housing: "
              "big, newish, and built fast during two booms. What ages first "
              "isn&rsquo;t structure, it&rsquo;s systems and stucco: original HVAC at end "
              "of life, polybutylene-era plumbing in the early stock, and "
              "twenty-year roofs on thirty-year houses. The city of Riverside "
              "is a different animal, full of genuinely old neighbourhoods like the "
              "Wood Streets, where the work is knob-and-tube-era wiring and "
              "foundations, not cosmetics."),
        src=None, srcname=None),
    killers=dict(
        h="What kills deals here",
        html=("Two liens ride on tax bills here more than anywhere else we "
              "work. Mello-Roos special taxes are standard in the newer "
              "Temecula, Murrieta and French Valley tracts. And PACE/HERO "
              "solar and efficiency loans were <em>invented</em> here: the HERO "
              "programme launched with the Western Riverside Council of "
              "Governments in 2011, so a striking share of local houses carry "
              "an assessment that must be paid or formally subordinated before "
              "title transfers. Both are findable in a preliminary title "
              "report, and both are exactly the sort of late surprise that "
              "collapses a sale with an unprepared buyer."),
        src="https://en.wikipedia.org/wiki/HERO_Program",
        srcname="WRCOG / HERO programme history"),
),

"san-bernardino-county": dict(
    recorder=dict(
        h="Recording a deed",
        html=("The Assessor&ndash;Recorder&ndash;Clerk records at the Hall of Records in "
              "San Bernardino, publishes a fee calculator, and supports "
              "same-day e-recording through authorised submitters, which in "
              "an ordinary escrow means the deed records the day of closing. "
              "Budget for the state&rsquo;s $75-per-document Building Homes and Jobs "
              "Act fee on non-sale recordings; it surprises people doing "
              "family transfers."),
        src="https://arc.sbcounty.gov/document-recording/",
        srcname="SB County Assessor-Recorder-Clerk"),
    dtt=dict(
        h="Transfer tax",
        html=("Documentary transfer tax is the standard $0.55 per $500 of "
              "price, and none of the cities we buy in (San Bernardino, "
              "Fontana, Rancho Cucamonga, Redlands, Highland) levy a city "
              "tax on top."),
        src="https://arc.sbcounty.gov/document-recording/",
        srcname="SB County Assessor-Recorder-Clerk"),
    probate=dict(
        h="Probate here",
        html=("Since February 2024, probate isn&rsquo;t heard in downtown San "
              "Bernardino at all: decedents&rsquo; estates are filed and heard at "
              "the Fontana and Victorville districts. Probate notes, the "
              "examiner&rsquo;s to-fix list for your petition, post to the court&rsquo;s "
              "online portal two weeks before the hearing, and clearing them "
              "before the date is the difference between one hearing and "
              "three."),
        src="https://sanbernardino.courts.ca.gov/divisions/probate",
        srcname="Superior Court of California, County of San Bernardino"),
    stock=dict(
        h="The housing stock",
        html=("The valley floor tells its age in decades: prewar and postwar "
              "bungalows in central San Bernardino and older Redlands, "
              "1960s&ndash;70s ranches through Highland and the mid-city, and "
              "1980s-onward tract across Fontana and Rancho Cucamonga. The "
              "older half is where inspection findings cluster: galvanised "
              "supply lines, aluminium branch wiring from the late &rsquo;60s and "
              "&rsquo;70s, and Federal Pacific panels that insurers increasingly "
              "refuse outright."),
        src=None, srcname=None),
    killers=dict(
        h="What kills deals here",
        html=("In the High Desert (Phelan, Pi&ntilde;on Hills, the unincorporated "
              "fringe), water and waste are private: wells, septic tanks, and "
              "a county health department that wants a percolation test on "
              "file before a septic permit moves. Financed buyers routinely "
              "lose weeks to well tests and septic certifications, which is "
              "why cash matters more up there than down the hill. On the "
              "valley floor it&rsquo;s the older-stock trio above (plumbing, "
              "wiring, panels) that resets buyers&rsquo; numbers at inspection."),
        src="https://www.sbcounty.gov/uploads/dph/Documents/2018/09/All-inclusive-Septic-FAQ-9.10.18-1.pdf",
        srcname="SB County Environmental Health septic FAQ"),
),

"kern-county": dict(
    recorder=dict(
        h="Recording a deed",
        html=("Kern still does recording the old way: at the counter, 1530 "
              "Truxtun Avenue in Bakersfield, weekdays 8am&ndash;3pm, by check or "
              "money order, no cards. The county&rsquo;s own published timelines "
              "say originals come back in three to four weeks for walk-ins "
              "and four to six by mail. Title companies handle this in a "
              "normal escrow, but if you&rsquo;re clearing paperwork yourself (an "
              "affidavit of death, a quitclaim), build those weeks into the "
              "plan."),
        src="https://www.kerncounty.com/government/departments/assessor-recorder/records/document-recording",
        srcname="Kern County Assessor-Recorder"),
    dtt=dict(
        h="Transfer tax",
        html=("The rate is the standard $0.55 per $500, but Kern computes it "
              "on the purchase price <em>or the unencumbered assessed value, "
              "whichever is greater</em>: the county&rsquo;s recording page says so in "
              "as many words. On a below-market family transfer that "
              "distinction changes the bill. No city add-ons in Bakersfield "
              "or the towns we buy in."),
        src="https://www.kerncounty.com/government/departments/assessor-recorder/records/document-recording",
        srcname="Kern County Assessor-Recorder"),
    probate=dict(
        h="Probate here",
        html=("Kern files probate somewhere nobody guesses: the Juvenile "
              "Justice Center at 2100 College Avenue in Bakersfield; call "
              "(661)&nbsp;610-6000, option 5. The court runs a dedicated probate "
              "examiner line and hears remote appearances in department J1, "
              "which matters if the executor lives in San Diego or out of "
              "state, as they often do for Kern estates."),
        src="https://www.kern.courts.ca.gov/divisions/probate",
        srcname="Superior Court of California, County of Kern"),
    stock=dict(
        h="The housing stock",
        html=("Bakersfield&rsquo;s core (central, east, Oleander, La Cresta) is "
              "1950s&ndash;70s ranch stock, with the same mid-century plumbing and "
              "panel issues as East San Diego County at half the price point. "
              "The northwest and southwest are newer tract. In the smaller "
              "towns (Shafter, Wasco, Tehachapi, Ridgecrest), age and "
              "condition vary street by street, and comps are thin enough "
              "that pricing takes local eyes rather than a formula."),
        src=None, srcname=None),
    killers=dict(
        h="What kills deals here",
        html=("Water and what&rsquo;s under the ground. Rural and ag-adjacent "
              "parcels run on wells in a groundwater basin the state lists as "
              "critically overdrafted under SGMA, so well condition and "
              "recorded water arrangements get real scrutiny. Mineral rights "
              "are severed from the surface on much of the county: usually "
              "harmless, occasionally a title condition a lender balks at. "
              "And because prices are lower, renovation arithmetic is "
              "unforgiving: work that pencils in Chula Vista can fail to "
              "pencil in Wasco, which is why some &ldquo;fixer&rdquo; listings sit."),
        src="https://sgma.water.ca.gov/basinmod/basindashboard",
        srcname="DWR SGMA basin prioritisation"),
),
}

# ── Tenant-rules notes for the sell-rental-property matrix pages ────────
TENANT = {
"san-diego-county": (
    "Layered rules. Statewide just-cause and rent-cap law (AB&nbsp;1482) applies "
    "to most older rentals, and the city of San Diego adds its own Tenant "
    "Protections Ordinance (June 2023) with relocation payments "
    "(typically two months&rsquo; rent) on no-fault terminations. Selling with the tenant in "
    "place sidesteps the no-fault question entirely, which is a large part of "
    "why landlords here call us."),
"riverside-county": (
    "State law is the layer that matters: AB&nbsp;1482 just-cause and rent-cap "
    "rules for most rentals older than fifteen years. The newer southwest-"
    "county stock is often young enough to sit outside AB&nbsp;1482, so check the "
    "certificate of occupancy date before assuming either way. We buy with "
    "tenants in place, so no termination is needed to sell."),
"san-bernardino-county": (
    "State rules (AB&nbsp;1482) are the operative layer for most of the county&rsquo;s "
    "older rental stock. The practical issue we see isn&rsquo;t the law. It&rsquo;s "
    "condition: rentals here often carry a decade of deferred maintenance, "
    "and we price that plainly instead of asking you to fix it between "
    "tenancies."),
"kern-county": (
    "State law (AB&nbsp;1482) is the framework; Bakersfield doesn&rsquo;t add a city "
    "ordinance on top of it. Kern rentals are frequently Section 8, and that&rsquo;s "
    "fine: the housing authority relationship transfers with ownership, and "
    "we&rsquo;ve carried tenancies through closing without disturbing anyone&rsquo;s "
    "voucher."),
}

def sources_line(county_slug, keys=("recorder", "dtt", "probate", "killers")):
    """Small-print sources footnote for a county's fact set."""
    r = RESEARCH[county_slug]
    seen, parts = set(), []
    for k in keys:
        s = r.get(k, {})
        if s.get("src") and s["src"] not in seen:
            seen.add(s["src"])
            parts.append(f'<a href="{s["src"]}" rel="noopener">{s["srcname"]}</a>')
    if not parts:
        return ""
    return ('<p class="small" style="margin-top:30px;max-width:78ch">Sources: '
            + " &middot; ".join(parts)
            + f'. Figures checked {CHECKED}; we re-verify quarterly.</p>')
