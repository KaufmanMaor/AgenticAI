# Round 2 — CTO stress-test of Concept v2

## 1. Three biggest flaws in v2

1. **Anonymized cards can be traced back to a real person.** Israel's dev scene is small. A card reading "Staff SRE, 7 yrs, Rust + eBPF" at DevOpsDays TLV points to about two people. A recruiter then screenshots it and sends it to a friend at the candidate's company. Our employer blocking never comes into play. *Fix:*
   - Cards use fixed categories only (role family, seniority band, 3 skills from a set list). No free text before reveal.
   - **k-anonymity gate:** a card shows only if at least 5 Open candidates at the event share its role and seniority band. Otherwise we broaden the categories or hide the card.
   - We watermark the screen with the viewer's name and limit how many cards a recruiter can view.
2. **The 72-hour pre-event window breaks the presence gate.** Profiles now exist *before* anyone has proven they're at the venue. People who registered and don't show up still use up pre-booked slots. And the organizer's email link can show the organizer who signed up. *Fix:*
   - Profiles stay **pending until the person checks in at the venue**. Recruiters see only an aggregate ("~N relevant people are coming").
   - A pre-booked slot is confirmed only after the candidate checks in at the venue, and released if they haven't checked in 30 minutes before it.
   - The organizer gets one generic link with no per-attendee tracking, and never receives the list of who signed up.
3. **Discretion leaks outside our database.**
   - WhatsApp previews on a locked phone ("Wix accepted your knock") can be read by the colleague in the next seat.
   - One-tap export into the company's applicant tracking system (Comeet/ATS) puts candidate data in the company's records forever, so the "deleted in 72 hours" promise quietly ends there.
   - *Fix:* message templates never name the company or the word "job" ("Hallway: update waiting"). Details show only inside the web app. ATS export is a separate, explicit consent step saying "this company now holds your data", and it's off by default.

## 2. The moat at 24 months, and a concrete "Verified Met-in-Person" credential

**Moat:** none of these is technical on its own; together they are what lasts.
- Exclusive organizer contracts (rev share plus multi-year terms).
- Recruiter workflow lock-in: their slots, notes and ATS sync across 15+ events a year.
- The only **consented dataset of which in-person intros led to hires**, which drives pricing and ROI reports.
- A **credential network** that candidates carry, with our name on it.

**The credential:**
- **Format:** a W3C Verifiable Credential 2.0 in a format that lets the holder reveal only some fields (SD-JWT VC). It's signed by Hallway as issuer, identified as `did:web:hallway.jobs`, with keys stored in a cloud key-management service (KMS). The organizer can optionally co-sign.
- **What it says:** holder is identity-verified; attended event E on date D; held N in-person intros with verified companies. Company names are fields the holder can reveal or keep hidden, so they can show "met 3 verified companies at Cyber Week" without saying which.
- **Who gets one:** both sides. Candidates get "met in person"; recruiters get a "verified interviewer" credential.
- **Why it's hard to fake:**
  - An intro is minted only if both phones scan each other's **one-time QR code**, signed by a key generated on the device for this session.
  - Each phone must also hold a valid **venue presence token** from the same event and the same 10-minute window.
  - Both identities are verified: the candidate through the organizer's badge list or LinkedIn sign-in, the recruiter through their work email domain and an account that has paid.
  - The signature can't be forged and a credential can't be self-issued.
  - We can revoke credentials through a W3C status list.
  - No blockchain.
- **Honest limit:** two colluding friends could fake an intro. We cap this by requiring the company to have paid and verified its domain, and by rate limits.

## 3. Knock/Open mechanics and the employer-blocking algorithm

**Knock (default):**
- The candidate taps Knock on a role card and picks how much to reveal: **L1** = the anonymized card, **L2** = adds name and LinkedIn.
- Each candidate gets **at most 5 open knocks per event**, so nobody can spray every company.
- The company either *Accepts and offers a slot* (the slot is held for 10 minutes) or does nothing.
- The candidate never sees a rejection. An unanswered knock fades to "no slot available" when the event ends.
- Knocking a company in your own blocked group requires an explicit override ("I know this is my employer's group").

**Open (opt-in):**
- A verified recruiter sends an *Invite* to an anonymized card that has passed the k-anonymity gate.
- The candidate accepts and picks L1 or L2. Identity is revealed only after that.
- Recruiters can send at most 15 invites per event.
- **Agency recruiters can't see Open mode in v1**: we can't know which companies they are recruiting for.

**Blocking algorithm:**
```
blocked(candidate) = expand(employers ∪ recent_ex(≤6mo, default ON) ∪ placements ∪ clients ∪ manual_list)
expand(c)          = all companies under ultimate_parent(c), plus aliases and domains
visible(cand, viewer) = viewer.company ∉ blocked(cand)
                        AND cand.employer_resolved   (resolution confidence ≥ 0.9, otherwise fail closed)
```

**Company graph data sources:**
- Israel's Registrar of Companies (data.gov.il) for legal entities.
- Wikidata parent/subsidiary links (P749 and P355).
- OpenCorporates.
- Israeli startup databases (IVC, Finder) and an M&A news feed, refreshed 48 hours before each event.
- The candidate's work email domain, checked by one-time code. This is optional but makes resolution reliable.
- Manual curation of the **top 300 Israeli tech employers and their group companies** (for example, Wix-owned brands, and Intel ↔ Mobileye).
- Recruiters are tied to a company only through their verified work email domain.

**Edge cases:**
- **Freelancer:** employer = self. We prompt "clients in the last 12 months" and block those by default.
- **Consultant / outsourced (body-shop):** block both the consultancy and the client company where they sit day to day.
- **Stealth startup:** we create a private company record from the work email domain. With no domain, Open mode is off and Knock only is allowed.
- **Just left (within 6 months):** the former employer is blocked by default; the candidate can turn this off. **Signed elsewhere but not started:** also block the future employer.
- **Unresolved employer, or "rather not say":** Open mode is disabled and the candidate is told why. Knock still works.

## 4. Tooling for the hand-run pilot (low privacy risk)

- **Tally** form (EU-hosted, GDPR DPA). It collects only first name, phone, role family, seniority band, current employer (used only for blocking) and companies to avoid. **No CV and no LinkedIn URL.**
- The data lives in a **Google Sheet on a restricted Google Workspace shared drive**:
  - only 2 named matchmakers have access, with 2FA
  - downloads are disabled
  - viewers see a filtered view without phone numbers
- **WhatsApp Business app on a dedicated phone.** One-to-one messages only, never groups, using neutral templates.
- Recruiters get a candidate's one-line summary **only after both sides agree**, read aloud or on a printed card. Nothing is sent electronically.
- Slots are managed on a paper board at the Coffee corner.
- **Deletion at T+72h:** the sheet is purged, a deletion log is kept, and the WhatsApp chats are wiped.
- Paperwork: a privacy notice, consent with a version number, a lite data protection impact assessment (DPIA), and 2 hours of lawyer review on the Amendment 13 obligations.

## 5. v1 data model (Postgres; rows marked † are encrypted with the per-event key)

- **Company graph:**
  - `companies(id, name, aliases[], parent_id, kind[employer|agency|stealth], verified)`
  - `company_domains(domain, company_id)`
- **Events and presence:**
  - `events(id, organizer_id, starts_at, ends_at, purge_at, key_ref)`
  - `presence(event_id, user_id, first_seen, token_window)`
- **People:**
  - `users(id, phone_hash, idp_sub, created_at)`
  - `recruiters(user_id, company_id, email_domain_verified_at, is_agency)`
- **Candidate side:**
  - `candidate_profiles†(event_id, user_id, role_family, band, skills[], pitch, mode[knock|open], status[pending|live])`
  - `candidate_blocks(profile_id, company_id, source[employer|ex|client|manual])`
- **Matching and meetings:**
  - `role_cards(event_id, company_id, title, band, salary_min, salary_max NOT NULL, hm_user_id)`
  - `intro_requests(id, event_id, from_side, profile_id, role_card_id, reveal_level, status, expires_at)`
  - `slots(id, role_card_id, starts_at, intro_request_id)`
  - `intros(id, slot_id, cand_scan_at, rec_scan_at, outcome, next_step_at)`
- **Governance and credentials:**
  - `consents(user_id, purpose, version, granted_at, revoked_at)`
  - `access_log(viewer_id, profile_id, action, at)`
  - `credentials(id, intro_id, holder_id, status_index, issued_at)`

## 6. 10-week sprint plan (2 full-stack engineers + 0.5 designer)

| Wk | Deliverable |
|---|---|
| 1 | Schema, row-level security, WhatsApp code sign-in, events, rotating venue QR / presence tokens |
| 2 | Company graph import and resolution service, recruiter domain verification |
| 3 | Candidate onboarding: CV → LLM drafts the 5 fields → user edits; consent records |
| 4 | Role cards (salary band required), "who's hiring" board, Knock flow |
| 5 | **Blocking engine plus the k-anonymity gate, with adversarial tests** (release gate) |
| 6 | Slots, pre-event pending mode, neutral WhatsApp templates |
| 7 | Recruiter live queue and notes, organizer console |
| 8 | Comeet API + CSV export (explicit consent), ROI report, credential issuance |
| 9 | Crypto-shred purge job, audit log, external penetration test, DPIA sign-off |
| 10 | Dogfood at a meetup (load test, fixes), launch event |
