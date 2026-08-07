# Lead routing: website form → RESimpli

The chain, end to end:

```
hardtrealestate.com/contact/  (Netlify Form: "hardt-lead")
        │  POST, spam-filtered by Netlify
        ▼
Netlify outgoing webhook
        │  JSON
        ▼
Zapier  →  Catch Hook  →  split contact  →  RESimpli: Create Lead
                                         └→  SMS to Peter
```

RESimpli publishes no REST API, so their Zapier app is the supported
route. Everything below is done in a browser; nothing here touches the
site's code.

**This path needs no mailbox.** The webhook carries the lead, so it works
before `peter@hardtrealestate.com` exists. Read the safety-net note at
the bottom before relying on that.

---

## What the form actually sends

Form name: **`hardt-lead`**. Five visible fields, exactly these names:

| Field name (use verbatim in Zapier) | Example |
|---|---|
| `Property address` | 1425 Oak St, El Cajon |
| `Situation` | I inherited it / it's in probate |
| `Name` | Robert Alvarez |
| `Phone or email` | 619-555-0134 **or** rob@example.com |
| `Notes` | optional free text |

A sixth field, `company`, is the honeypot. It is invisible to people and
only bots fill it. Netlify quarantines those before the webhook fires, so
nothing on the Zapier side needs to check it.

Netlify posts JSON shaped like this. In Zapier the fields appear as
`data__Property address`, `data__Name`, and so on:

```json
{
  "form_name": "hardt-lead",
  "created_at": "2026-08-07T18:22:04.000Z",
  "data": {
    "Property address": "1425 Oak St, El Cajon",
    "Situation": "I inherited it / it's in probate",
    "Name": "Robert Alvarez",
    "Phone or email": "619-555-0134",
    "Notes": "",
    "referrer": "https://hardtrealestate.com/inherited-house/"
  }
}
```

---

## Step 1 — Confirm Netlify is capturing the form

Netlify detects forms at deploy time, so this should already be true.

1. Netlify → the HARDT site → **Forms**
2. You should see a form named **hardt-lead**
3. Submit a real test through <https://hardtrealestate.com/contact/> and
   confirm it appears

If the form is not listed, nothing downstream can work. Stop and fix that
first: it means a deploy did not include the form markup.

## Step 2 — Get the RESimpli API token

RESimpli → app icon, top right → **API Token** → copy to clipboard.
Zapier asks for this once when you connect the account.

## Step 3 — Build the Zap

**Trigger:** Webhooks by Zapier → **Catch Hook** → Continue → copy the
custom webhook URL it gives you. Leave the tab open.

**Action 1 — split the contact field.** The form deliberately asks for
"phone or email" as one question, because that is one less decision for
somebody filling this in at 11pm. RESimpli wants them separate, so add a
**Code by Zapier → Run JavaScript** step. Input data: `contact` =
`data__Phone or email`.

```js
const raw = (inputData.contact || '').trim();
const isEmail = raw.includes('@');
const digits = raw.replace(/\D/g, '');
return [{
  email: isEmail ? raw : '',
  // 10 digits, or 11 starting with 1, normalised for the CRM
  phone: isEmail ? '' : (digits.length === 11 && digits.startsWith('1')
                          ? digits.slice(1) : digits)
}];
```

**Action 2 — RESimpli → Create Lead.** Connect with the API token, then
map:

| RESimpli field | Maps from |
|---|---|
| First / last name | `data__Name` (split with a Formatter step if RESimpli wants them separate) |
| Phone | Code step → `phone` |
| Email | Code step → `email` |
| Property address | `data__Property address` |
| Notes / description | `data__Situation` + `data__Notes` + `data__referrer` |
| **Lead source** | `website` |
| **Campaign** | `website` |

Lead source and campaign are Peter's explicit ask from the intake. Set
them as static text, not mapped fields, so every website lead is tagged
identically and the reporting stays clean.

Put the referrer in the notes. It tells you which page the lead was
reading when they decided to call, which is the single most useful thing
for knowing what the site is doing.

**Action 3 — text Peter.** Add either Zapier's built-in SMS action or
Twilio, to **(619) 558-0369**, with something like:

```
New HARDT lead: {{data__Name}} — {{data__Property address}}
{{data__Situation}}
Contact: {{data__Phone or email}}
```

Check RESimpli's own notification settings first. If it already texts on
new leads, skip this and let the CRM do it rather than running two
sources of alerts.

## Step 4 — Point Netlify at the Zap

Netlify → the site → **Forms** → **Form notifications** → Add
notification → **Outgoing webhook**

- Event: *New form submission*
- URL: the Catch Hook URL from Step 3
- Form: **hardt-lead** (not "any form")

## Step 5 — Test the whole chain

Submit a real enquiry through the live contact page with recognisable
test data. Then check, in order:

1. Netlify → Forms → the submission is listed
2. Zapier → Zap History → the run succeeded
3. RESimpli → the lead exists, with source and campaign both `website`
4. The text arrived

Test twice: once with a phone number and once with an email address, so
you prove the Code step routes both correctly. Delete the test leads
afterwards.

---

## Things that will bite

**No mailbox means one delivery path.** Skipping email is fine for
launch, but it leaves the webhook as the only way a lead reaches anyone.
If the Zap turns off, hits its task limit, or errors, submissions sit in
Netlify and nobody is told. **Add a second notification** — Netlify →
Forms → Form notifications → Email notification — pointed at any inbox
that already works, even a personal Gmail. It costs nothing and it is the
difference between a delayed lead and a lost one. Swap it for the branded
address when that exists.

**Netlify form notifications are off by default.** Nothing is sent until
Step 4 is done, and there is no warning. Submissions accumulate silently.

**Address arrives as one line.** The form asks for street and city only,
because that is the lowest-friction question. If RESimpli wants city,
state and postcode in separate fields, add a Formatter step or let the
single string go into the street field and tidy it in the CRM.

**Spam never reaches the Zap.** Netlify's honeypot and filtering hold it
back, so Zapier tasks are not burned on bots. If a real submission ever
goes missing, check the spam list in Netlify before assuming the Zap
broke.

**Zapier task budget.** The intake estimates ~50 leads a month. Each lead
is 3 tasks here (catch, code, create) plus 1 if Zapier sends the SMS, so
roughly 150–200 tasks a month. Comfortably inside a Starter plan; worth
knowing before volume grows.
