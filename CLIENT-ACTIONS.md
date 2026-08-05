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

**4. DBA + Blair.** DONE on the filing: "HARDT" is filed. Two tails
remain. First, the publication run: California requires the FBN to be
published in an approved newspaper in San Diego County once a week for
four consecutive weeks, starting within 30 days of filing, then an
affidavit of publication filed with the County Clerk — the DBA is not
legally complete until that affidavit lands, and it expires in five
years (calendar the renewal). And Blair
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

**6. The three stories on /how-weve-helped/.** The new page tells three
real situations from your intake, names withheld: the foreclosure save
(Robert), the Huskey Drive close (Eli's deal), and Graphic Street
(Chuck). Three things needed from you:
   - Read each telling and correct anything that isn't exactly how it
     went. Nothing publishes wrong on my watch, including stories.
   - Ask Robert, Eli and Chuck whether they're comfortable being named.
     Named stories resonate harder; the page works either way.
   - Optional but powerful: a 60-second phone video at any of the five
     projects, you talking through what the house needed. No script, no
     polish. That becomes the strongest thing on the page.

**7. Competitor gut-check (10 minutes).** Open these five and tell me:
which one feels closest to what you want HARDT to be, the one thing any
of them does that you wish we had, and anything you'd never want us to
do. homehelpersgroup.com · sellersnewday.com · cenvalrei.com ·
gghomes.com · newwestern.com. Also: your intake listed "Central Valley
Home Buyers" and "Best Home Offer" — I couldn't confidently find those
two; send links if they're different from the above. My own read is in
COMPETITOR-NOTES.md in the repo.

**8. Reviews are the one gap that compounds.** Home Helpers Group has
~205 Google reviews in Kern; we have one, on the old Fluid profile.
When you ask Chuck, Robert and Eli about the stories (item 6), ask each
for a Google review in the same conversation. Three real, specific
reviews beats zero, and the GBP rename preserves them.

**9. Loose ends from your intake, quick answers needed:**
   - Does the peter@hardtrealestate.com mailbox actually exist yet? The
     site publishes it; if it isn't live, leads are bouncing silently.
   - Mailers/ads may carry different phone numbers per your intake note.
     Fine offline, but the (707) 489-6236 number must be the only one
     that ever appears online, anywhere, or the citations fracture.
   - Your intake said DBA "Hardt or Hardt Properties"; Michael says
     plain "HARDT". Confirm the final SOS/county filing wording so the
     site, GBP and legal line all match it exactly.
   - Frances and the frances@ mailbox: you wanted to talk this one
     through — also affects the "team" framing now live on About.
   - LinkedIn / BiggerPockets profiles: yes or no, and who runs them.
   - You listed partners (SoCal Title, Placer, Kiavi, NREIG, Winans).
     A partners strip on the site is a real trust signal, but only with
     their OK — want me to draft the ask?
   - Security note: your intake document contains live passwords
     (Namecheap, BiggerPockets). Rotate both; intake docs get shared.


**10. Team section details (About page).** Frances is now on the About
page as "Frances — Operations" with a placeholder card. Needed to finish
it: her full name as she wants it published, her preferred title, a
yes/no on the two-line description we drafted ("Keeps the paperwork,
scheduling and escrow moving on every purchase"), and both headshots.
Text the two headshot files over and they go straight into the new
photos-in/ slots (team-peter, team-frances). The dark-studio shots work
as stopgaps; front-of-project shots replace them whenever they're taken.


**11. Watermarked project photos (quick win, needs one phone call).**
Thank you for the Drive folder: your headshots, Frances's headshot, and
the Graphic Street set are live on the site already, including a
before/after slider of the garage and driveway that came out great.

The Shenandoah, Cale, Terrace and Huskey *after* photos I can't use yet.
They're the MLS listing sets and every frame has "LCA CINEMA" and "GEMLS"
burned into the bottom corners. Putting another company's watermark on
your own site looks wrong, and the licence on MLS listing photos normally
stays with the photographer rather than the seller, so I won't crop them
out or use them as-is.

You paid for those shoots, so ask LCA Cinema for the un-watermarked
originals with permission to use them on hardtrealestate.com. That's
usually a five-minute email. The moment they land, three more project
cards and a real hero photo go live.
