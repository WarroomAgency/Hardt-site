# Client actions — what we need from Peter, and the ops setup

Two halves: the email to send Peter (paste-ready, Michael's voice), and
the ops setup that's on us (Netlify + RESimpli), written as steps.

---

## The email to Peter

**Subject: HARDT site — 5 quick things that unblock the rest**

Peter —

Site's in great shape: 40 pages live-ready, county pages built out with
the local research layer (recorder, probate court, transfer tax per
county — all sourced), and real photography in the hero and county pages.
Five things are blocking the last mile, and four of them are five-minute
answers:

**1. The real numbers.** Your intake had a few that don't line up —
"2 years operating" vs. a 2021 start, "5+ homes bought" vs. "12 families
helped", "3 counties worked" vs. projects in two. Until we lock these,
the site runs on the four claims we can defend: Since 2021, four
counties, ~14 days, no assignments. Send me the real figures and I'll
work the strongest ones in.

**2. LA County — in or out?** You ticked it as a service area and
Lancaster is on your project list, but the site currently covers four
counties. If LA is in, I build a fifth county hub + four more pages.
One word answer is fine: in or out.

**3. Hours.** One answer said Mon–Sat 8–6, another said 7 days. The site
and the schema currently say Mon–Sat 8–6. Whatever you pick, the Google
Business Profile has to match it exactly — tell me which is true.

**4. DBA + Blair.** The "HARDT Real Estate" DBA still needs filing (San
Diego County Clerk, $54, then the newspaper publication run). And Blair
should look at two things before we go loud: the /stop-foreclosure/
page and the footer line about buying as a principal. Both are written
conservatively but he should bless them. GBP work is parked until the
DBA exists.

**5. Photos — the fun one.** You said you have before/during/after of
all five projects plus your headshot. Those fill the six most important
slots on the site, they're free, and they're already in your phone.
Text them to me as-is; the pipeline handles cropping. Especially want:
before + after of the same house from the same spot, and one finished
exterior of each project.

That's it. #1 and #5 are the ones that make the biggest visible
difference.

— Michael

---

## Ops setup (on us, not Peter)

### Netlify form notifications — do this right after next deploy
Off by default; submissions pile up silently until it's flipped.

1. Netlify → the HARDT site → **Forms** → verify `hardt-lead` is detected
2. **Site configuration → Forms → Form notifications → Add notification**
3. Email notification → Peter's email (and cc hello@warroomagency.com)
4. Send a test submission through /contact/ and confirm it arrives,
   and that the honeypot (`company`) stays empty in real submissions

### Peter's lead flow: text-on-lead + RESimpli record
RESimpli has no native web-form capture, so it needs a hop:

1. **Path A (Zapier):** Netlify Forms trigger → new `hardt-lead`
   submission → two actions:
   - SMS to Peter's (707) 489-6236 (Zapier SMS or Twilio)
   - RESimpli "create lead" — set **lead source: website**,
     **campaign: website**
2. **Path B (webhook):** Netlify outgoing webhook on form submission →
   small worker → RESimpli API. Cleaner long-term, more setup today.
3. Whichever path: field mapping is address → property address,
   situation → notes, name/phone → contact. Test with a fake lead
   end-to-end before telling Peter it's live.

### GBP (parked until DBA files)
Reminders from the handoff, so they don't get lost: rename the existing
Fluid Developments LLC profile (don't create new), hide the address
(service-area business), no keywords in the name field, category tested
against what actually ranks (not "Real estate agency"), and **Kern gets
no map presence** — website only.
