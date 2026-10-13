# Round 1 — Tech lens (CTO / founding engineer)

**Bottom line:** The founder is right that it's light to build. The product won't break on code. It breaks on trust (discretion) and on getting recruiters into the room. So the architecture should mostly serve those two things: privacy is designed in from the start, and the distribution path is through organizers. The real engineering work is the privacy model, the notification loop and integrations. Swiping is not the hard part.

## 1. App vs. "no app": PWA via QR, no contest
- Asking people to install an app at a venue costs us most of the funnel. Venue Wi-Fi is bad, people won't take 90 seconds for an app store, and an installed job-search app on your phone is a discretion leak in itself. Use a **QR → mobile web app (PWA)**. It opens in under 3s and needs no account wall.
- **Catch:** iOS web push only works after "Add to Home Screen", and nobody does that at a conference. So the notification channel is **WhatsApp (Meta Cloud API) with SMS fallback**. Israelis live on WhatsApp anyway. Sign-in is a phone OTP over WhatsApp.
- Native comes later, and only for **recruiters**, who use it across many events. Even then I'd wrap the same codebase with Capacitor rather than build a second app.

## 2. MVP architecture and cost
- **Stack:** Next.js (TypeScript) PWA on Vercel, plus Supabase (Postgres, Auth, Realtime, Storage) in the **EU (Frankfurt)** region. Israel has EU adequacy status and EU data residency makes GDPR straightforward. Background jobs run on Inngest or Supabase cron. WhatsApp goes through Meta Cloud API or Twilio. The LLM is a hosted API with a zero-retention setting.
- **Cost:** about **$150–400/month** in infrastructure before scale. Marginal cost per event (500 attendees, around 3k messages, 300 CV parses) is roughly **$50–150**. The cost driver is people, not cloud.

## 3. The 2-minute profile, and AI that structures but never judges
- **LinkedIn import is mostly a myth.** "Sign in with LinkedIn" (OIDC) returns only name, email and photo. Work history needs partner API access we won't get, and scraping breaks their terms of service. Use LinkedIn sign-in **only to verify identity**.
- **The flow:** (1) pick an intent. (2) Upload a CV, or a LinkedIn "Save to PDF" export. An LLM extracts five fields: role family, seniority, top skills, location/remote, and **current employer**. (3) The user confirms or edits chips; never auto-submit. (4) Optional 30-second voice or text pitch. The LLM tidies the transcript, the user approves, and the audio is not kept.
- **How we avoid becoming the "AI filter":** AI writes *on behalf of* the candidate and never *about* them. There is no scoring, no ranking and no auto-rejection. Recruiters see **every** candidate who passes their hard filters (role, seniority, location), in neutral order (recently active / available now). This is also a legal requirement in disguise: ranking candidates is **"high-risk AI" under the EU AI Act (Annex III)**. Staying out of that category is a feature we can market.

## 4. Matching and presence
- **Hard filters only:** intent (opposite side) + role family + seniority band (±1) + location/remote compatibility + "available now / today". It's a deterministic SQL query, so every match can be explained.
- **Recruiter-led queue, not a swipe.** The recruiter opens 15-minute slots. Matched seekers get a WhatsApp message: "Company X (anonymous until you accept) wants 10 min at Table 4, 14:30?"
- **Proving someone is actually at the venue**, from strongest to weakest:
  - (a) A **rotating QR code** (time-based token, refreshed every 60s) on screens at the venue. A photo of the QR shared in a WhatsApp group goes stale within a minute.
  - (b) Matching the attendee against the organizer's registration list, or scanning their badge.
  - (c) Geofencing. It's unreliable indoors and creepy, so it is **not in v1**.
- Presence expires at the end of the event.

## 5. Privacy and security architecture
- **Visibility is asymmetric.** Seekers are invisible to everyone except verified recruiters. Seekers never see other seekers. Recruiters and companies are public, since hiring isn't a secret.
- **Verifying recruiters:** OTP to their work email domain, plus manual approval in the MVP. Without this, anyone can pose as a "recruiter" and browse who is job hunting.
- **Hiding seekers from their employer:** a seeker is automatically hidden from every recruiter whose verified domain belongs to their declared current employer. That includes a maintained parent/subsidiary map (Wix ↔ Wix-owned brands, etc.). The seeker can add more companies to a personal blocklist. The default fails closed: if we can't resolve the employer, we hide.
- **Double opt-in reveal:** the recruiter first sees an anonymous card (role, seniority, skills, pitch) with no name, photo or employer. Identity is revealed only after the seeker accepts.
- **Data is temporary:** all data belongs to one event and is encrypted with a **per-event key**. At T+72h we delete the key ("crypto-shredding"), so even the backups become unreadable. The only data that survives is a match where *both* sides chose "keep in touch", and that is stored as an explicit consent record.
- **Compliance:**
  - We need explicit, granular consent, separate for each purpose: matching, export to an ATS, and a later opt-in to future events.
  - Under Israel's Privacy Protection Law **Amendment 13 (in force since Aug 2025)**, we should treat "looking for a job" as highly sensitive. That means:
    - a database-defining document
    - appointing a privacy officer early
    - logging access to the data
  - We need a GDPR data processing agreement (DPA) with organizers.
  - We need a data protection impact assessment (DPIA) before the first pilot.
- **Security basics:**
  - row-level security in Postgres
  - audit logs of every time a recruiter views a profile, shown to the seeker ("3 recruiters viewed you")
  - rate limits against recruiters scraping profiles

## 6. Integrations
- **ATS:** use **Merge.dev** (a unified API covering Greenhouse, Lever, Workday and others) instead of building N connectors. Build a **native Comeet** connector, since Comeet is the Israeli default and the beachhead depends on it. The output is "push candidate + interview notes into the job pipeline", done only with the seeker's consent. Until that exists, a CSV export works in v1.
- **Event platforms:** Swapcard and Bizzabo have APIs, Brella and Cvent have partner APIs. We import the attendee list (for presence) and embed a deep link into their app. Strategically, we should **be a plugin inside their apps, not a competitor.**
- **Calendar:** Google/Microsoft OAuth for recruiters. Seekers get an .ics file via WhatsApp. Don't build a scheduler; slots live inside our queue.

## 7. Remote video booth: buy the video, build the experience
- **Never build WebRTC.** Use **Daily** (or Whereby Embedded). It's roughly $0.004 per participant-minute, which comes to about $0.15 per 15-minute interview. It handles room tokens, recording off by default, and a browser-only remote recruiter.
- **Hardware per booth:** an iPad or small PC locked in kiosk mode, a USB conference camera, a directional mic, a ring light, and a semi-enclosed pod for privacy. About $1.5–3k per booth, or rent the pod from the venue. Use wired Ethernet or a 5G router and never rely on venue Wi-Fi.
- This belongs in **v2, as an upsell** to companies that didn't send anyone to the event. It's not core.

## 8. Where a real moat could come from
- **The code: no moat.** Brella can copy the toggle in a quarter.
- **Data: weak, and on purpose**, because data is deleted after each event. The only data asset we can keep is **consented outcome data**: which in-person meetings led to hires. That proves ROI to recruiters, and nobody else measures it.
- **Workflow lock-in** is stronger: recruiters plan their conference calendar, their slots and their ATS sync inside our tool across 20 events a year.
- **Distribution network:** organizer contracts plus a recruiter subscription that works across many events. This is the real moat, and it's a business moat, not a technical one.
- **Trust brand:** being "the discreet one" is hard for a general event app to credibly copy.

## 9. Build plan

| Phase | Scope | Time | People |
|---|---|---|---|
| **Concierge MVP** | QR → Tally form, Airtable, matching by hand, WhatsApp Business, one interview corner, a privacy checklist. Under $300 per event | 1–2 weeks of setup | 1 engineer part-time + 2 ops people at the event |
| **v1** | PWA, CV parsing, anonymous cards + double opt-in, employer hiding, rotating-QR presence, recruiter queue, WhatsApp notifications, organizer console, CSV export, crypto-shredding | 8–10 weeks | 2 full-stack engineers + 0.5 designer (+ privacy lawyer for about 2 weeks) |
| **v2** | Comeet + Merge ATS, Swapcard/Bizzabo integrations, recruiter subscription across events, video booth, outcomes analytics, white-label SDK | +4–5 months | 3–4 engineers + 1 product manager |

## 10. Two bold technical ideas
1. **A "Proof-of-Presence" credential.**
   - After each in-person interview, both sides get a signed, verifiable credential (W3C Verifiable Credential): "met in person at CyberTech 2026, identity verified".
   - Gartner expects 1 in 4 candidate profiles to be fake by 2028, so a portable credential that proves a real human showed up becomes valuable.
   - It's also the one asset that survives deletion of our database, and it carries our brand with it.
2. **An "Interview scribe, not judge".**
   - The recruiter dictates 20 seconds after each meeting. The LLM turns it into a structured scorecard (the recruiter's own criteria, the recruiter's words) and pushes it to the ATS.
   - This takes AI out of the candidate gate and puts it into recruiter productivity. It's the workflow hook that makes recruiters log in at every event.

## Open questions for the other roles
1. **Business / CEO:** Will organizers sell this as a paid add-on for recruiters, or see it as a threat to sponsors whose staff get poached? That decides whether we sell a white-label plugin or a standalone app.
2. **Product / UX:** Will an employed attendee mark themselves "open" if we guarantee employer hiding? What's the *one sentence* on the QR landing page that earns that trust in 5 seconds?
3. **Legal / Ops:** Can we run the first pilot under organizer-controller / us-processor roles, and what is the minimum Amendment 13 setup (database registration, privacy officer, DPIA) we need *before* touching real candidate data?
