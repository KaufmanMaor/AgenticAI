# Hallway (מסדרון): Founding Playbook

*The final output of three founding ideation rounds: Round 1 role views, Concept v2 plus stress tests, and Concept v3 plus sign-offs. Concept v3 is the base. Where they conflict, the founder's rulings on the sign-off fixes override it. Written Oct 13, 2026.*

*Conventions: **[A]** marks an assumption that has not been validated. **[LAWYER]** marks an item that needs Israeli counsel. ₪3.7 = $1. "T" is event day, Dec 22, 2026 (still to be confirmed).*

---

## 1. Founding thesis

**One-liner.** Hallway is the hiring layer for professional events. Companies that are hiring are visible, and candidates stay invisible until they knock. A knock leads to a 15-minute coffee intro with someone who does the job, held at the venue, and the next step is booked before either person leaves.

**Problem.** Two people sit in the same conference hall and can't reach each other.
- **The engineer.** Most attendees at a professional conference already have a job and are looking passively. They won't signal that they're "looking" in a room that holds their manager. Even LinkedIn won't promise to hide "Open to Work" from recruiters at the candidate's own employer.
- **The company.** It pays ₪20–80K for a booth [A, HR estimate]. In return it gets swag hunters and business cards, about 80% of whom are students, vendors or simply not relevant [A]. The engineers it wants never walk up to the booth, and nobody can show the CFO what the booth produced.

**Why now** (figures from the research report):
- **Applications are now noise.** LinkedIn gets about 11,000 applications a minute (+45%). Gartner predicts one in four candidate profiles will be fake by 2028, and 74% of organizations are moving back to in-person interviews. A registered badge at a professional conference marks a verified, pre-filtered candidate.
- **There's budget looking for a channel.** Cost per hire is $5,475 (non-exec) to $35,879 (exec) per SHRM; verify against the PDF before quoting. Agencies take 15–25% of salary, a LinkedIn Recruiter seat costs $9–15K a year, and conferences already sell lead retrieval at $350–599 per unit. That last one is the budget line we sit next to.
- **The gap is distribution, not technology.** Brella, b2match and Swapcard have recruiting modes, but only when the organizer pays and switches them on.
- **The audience is right.** About 75% of job-fair attendees are unemployed. Conference attendees are mostly employed and passive, which is who recruiters want. The "60% come for jobs" claim has no source: MPI found 52% attend to network. We'll measure the real number.
- **The mechanic is proven.** Hooked has run at more than 70 events with about 15K downloads. Density comes from the event, which solves the cold start that killed every "Tinder for jobs" (Jobr, Switch, Shapr, Workey).

**Why us.** The code isn't the moat; Brella could copy the toggle within a quarter. What's hard to copy is organizer relationships, a trust brand with employed engineers, hiring-manager-led intros, and a consented dataset of which intros became hires. We build all four by hand at 3 events before writing production code. *[Founder: add your personal access to Israeli dev organizers and TA leaders. That is the real "why us," and it isn't in the files.]*

**How the idea evolved.**

| Version | What it was | What changed and why |
|---|---|---|
| **Original pitch** | "Hooked for job finding at conferences": everyone sees everyone with the opposite intent, an interview on the spot, a remote video booth | The research disproved "millions of conferences" and "60% come for jobs," and showed that "easy to build" means easy to copy. A visible seeker list exposes employed people |
| **v2** | Knock by default and Open by opt-in, a 15-minute Hallway Coffee, hiring-manager-led, pre-event matching, ₪3,500 pass, no dating language | Round 1: hiring is public and job seeking is risky. "Interview" scares people off. Recruiters buy booked meetings, not "who's here" |
| **v3** | Open mode deferred, blind invites added, presence becomes a status rather than a gate, one privacy promise, ₪2,000 founding price with a guarantee, the organizer sells to two pools | Round 2: cards could be re-identified, the 72h deletion contradicted the 14-day metric, sponsors are tool vendors rather than hirers, and buyers won't pay blind |
| **Final** | Rev share waived for the founding events, an honest P&L, a pro-rata guarantee, a gate of 35 or more, no candidate cards, a block scope we can actually build, "not this time" statuses, a fully manual pilot, hashed matching | The sign-offs found that ₪12–21K was really ₪10K gross, that the guarantee equaled the gate, that "cards" implied Open mode, that the block list relied on data that doesn't exist, and that "never sees a rejection" contradicted the 48h pledge |

---

## 2. The concept

### Candidate journey ("Yoni," backend engineer, 5 years, employed)
- **Before.** From Dec 1 the organizer's email links to the co-branded board (*"Hosted by DevOpsDays TLV · powered by Hallway"*), which lists companies, roles, the hiring manager in the room, and salary bands. Bands are visible only through the attendee link, never on a public page. Yoni joins a waitlist with phone, role family and seniority. At T-72h he fills in the 5-field knock card and his blocking inputs. A matchmaker confirms on WhatsApp: *"Your employer: [Company] and its group: blocked."* No company can see or browse him. If hashed matching shows he holds a ticket, his knocks open at T-24h. Otherwise they open when he checks in at the venue.
- **During.** He has 5 knocks. He knocks on a role and picks a slot. Only that company sees his card: no name, photo or employer. His name and LinkedIn are revealed after the company accepts. He may also get a blind invite and choose to knock back. Then a neutral WhatsApp ping, a 15-minute coffee at the corner, and a next step booked on the spot.
- **After.** Every knock ends as **accepted** or **"not this time."** If the company is silent for 48h, the status flips to "not this time" automatically and the company is flagged. At T+72h his data is deleted with a receipt unless he matched. For an accepted intro we keep who, when and the next step for 90 days, with consent. Export to a company's hiring system is a separate consent tap per company.

### Company journey (a scale-up platform team hiring 3 mid-level DevOps/SRE roles)
- **Before.** The company buys a ₪2,000 pass and posts at least 3 role cards with required salary bands. It names a team lead who accepts a 2-hour calendar block and signs the Hallway Coffee code. From T-14 it sees **totals only, for groups of 5 or more** (*"14 mid-level backend engineers (3–8 yrs) are coming"*). It sends blind invites, and slots arrive as .ics files.
- **During.** The hiring manager works a queue of accepted intros and logs 30 seconds after each one (next step: yes/no). Recruiters handle logistics.
- **After.** The company replies to every knock within 48h, gets ROI reports at T+14 and T+90, and is asked to rebuy at T+14.

### 2.1 Knock and blind invites
- **Knock** (candidate-initiated, the default and only mode in v1): 5 per candidate per event. A company can accept or stay silent. Silence becomes "not this time" after 48h.
- **Blind invite-to-knock.** A company writes one anonymous invite per role, for example *"Coffee at 11:30 with our platform lead: DevOps, 4–7 yrs, ₪32–40K."* It may offer **up to 10 invite slots per role**. The invite goes **automatically to the whole matching group** (role family × seniority band), and only if that group has **5 or more** people. It never goes to individually chosen profiles, because companies can't see profiles. The company learns who someone is only when that person knocks back.
- **No candidate cards in v1.** The rule of 5 applies only to (a) the totals companies see and (b) blind-invite targeting.

### 2.2 The Hallway Coffee intro
Fifteen minutes with someone who does the job, at a 3-table corner out of sight of the expo floor. It is structured (§7.1), it is **not an interview**, and it ends with a booked next step or an honest "not a fit." Coffee is on the company. The corner also hosts ordinary networking, so being seen there proves nothing. A company that can't send anyone can join by phone video from a quiet-room slot.

### 2.3 Privacy: the one promise
The privacy page carries one promise, and it is lawyer-reviewed before launch:

> **Nothing leaves the event unless you say yes to a specific company.**
> 1. Companies see only totals for groups of 5 or more people, never you.
> 2. Blind invites are sent to every profile in a matching group *before anyone has said yes*. A company that sends one learns nothing about who received it.
> 3. Your employer, its group, your recent ex-employers, your declared clients and anyone on your block list can never see you, even if they're sitting next to you.
> 4. The organizer never learns whether you joined. Ticket matching uses hashed contact details.
> 5. If you have no match, everything is deleted 72 hours after the event and you get a receipt. If you accept an intro, we keep who, when and the next step for 90 days, and only with your consent.

WhatsApp messages are neutral on the lock screen ("You have an update from Hallway"). Company names appear only after you open the chat.

### 2.4 Employer blocking (Employer Shield)
- **Blocked:** the employer's **company group**, from hand-curated lists, Wikidata parent/subsidiary links, an M&A feed and the Israeli companies registry (which lists legal entities, not groups); **recent ex-employers** (≤6 months, on by default); the candidate's **own declared clients** (freelancers and consultants); and a **personal block list**.
- **Never "the employer's clients."** That set is unbounded and would hide almost everyone.
- **Fail closed.** An unresolved employer means the candidate stays hidden and gets no invites until a matchmaker resolves it. A stealth employer gets a private record.
- **Red team before event 1:** resolve the groups of 60 real employers (past DevOpsDays and Reversim speakers plus our buyers). 5 engineers hunt for misses, and 5 recruiters try to re-identify colleagues from the totals and blind invites.

---

## 3. Positioning and brand

- **Name:** spoken brand **Hallway**, registered mark **Hallway Talent**, Hebrew sub-brand **מסדרון (Misderon)**. "Hallway track" is native dev-conference vocabulary. "Hallway" alone makes a weak trademark, but the risk of confusion in HR services is low. Known users of the name: an avatar startup in Missouri, Hallway Studios, and a Sydney agency.
- **Tagline:** *The hallway track, with intent.*
- **Product vocabulary:** Knock, Hallway Coffee, Employer Shield, Hallway Pass.
- **Category we own:** the hiring layer for professional events.

| Audience | Message |
|---|---|
| **Candidates** (employed, mid-level, wary of recruiters) | *"8 companies are hiring at DevOpsDays. See their roles and salary bands. They can't see you."* / *"Your employer is blocked automatically. Nothing is shared until you knock."* / *"No CV filter, no ATS black hole. 15 minutes with someone who does the job."* |
| **Heads of TA** | *"Your DevOpsDays booth, with coffees booked before you arrive."* / *"Eight coffees with mid-level engineers in your stack instead of 800 AI-generated applications."* / *"Verified people, real badges, zero fake candidates."* |
| **Hiring managers** | *"Two hours. Pre-booked slots. Engineers who chose you."* |
| **Organizers** | *"A new line on your sponsor form, with zero ops. Sponsors finally get booth ROI they can report, and hiring companies that don't sponsor become new customers through you."* |
| **Sponsors** | *"Own the Coffee corner, not the candidates."* We sell slots and placement, **never exclusivity and never data.** |

**Why we dropped "dating/Hooked."** To HR legal, "dating" signals harassment, unstructured interviews and discrimination risk. To employed engineers, it signals being exposed and judged. "Hooked for jobs" also risks a passing-off complaint. And Hooked's assets (QR entry, "who's here") are the cheap part; recruiter sales and the Employer Shield are the hard part. We keep the mechanics (event-scoped, density from the event, deletion) and drop the words "match," "swipe" and "date." The origin story is told once, in launch PR. With Hooked: one learning coffee with Noa Barazani about real QR scan rates, and no partnership.

---

## 4. Business model and economics

**Pricing**
- **Candidates:** always free.
- **Hallway Pass, founding price:** **₪2,000 per company per event** for the 3 founding events. List price later: ₪3,500 [A].
- What's included: at least 3 role cards, a hiring manager on site for 2 hours, blind invites, and a **5-held-intro guarantee paid as a pro-rata credit**. Each missing intro below 5 earns ₪400 of credit toward the next event.
- **Test:** ₪300 per extra held intro above 10.
- **Presenting Hiring Partner:** ₪20–30K, one per event. It includes the branded Coffee corner, first pick of slots, a stage mention and a logo in the attendee email.
- **Never sold:** exclusivity or data. Price quote if a sponsor insists on exclusivity: ₪60K [A]. If they won't pay it, we skip the event.
- **No success fee in year 1.** It invites attribution fights and placement-agency licensing risk.

**Event-1 P&L (concierge, organizer rev share waived)**

| ₪ | Floor: 5 companies | Target: 8 companies + Partner |
|---|---|---|
| Hallway Passes × ₪2,000 | 10,000 | 16,000 |
| Presenting Hiring Partner | 0 | 20,000–30,000 |
| Organizer rev share | 0 (waived) | 0 (waived) |
| 3 matchmakers × 2 days | −6,000 | −6,000 |
| Coffee corner (furniture, signage, coffee) | −3,000 | −3,000 |
| WhatsApp, forms, printing | −500 | −500 |
| **Contribution** | **+500** | **+26,500 to +36,500** |
| Founder sales time, ~3 weeks [A] | −6,000 | −6,000 |
| **After founder time** | **−5,500** | **+20,500 to +30,500** |

At the floor, event 1 is a **small loss**: ₪10K gross against ₪9.5K of on-site costs, so it goes negative once founder time or any shortfall credit is counted. With 8 companies and no Partner it makes +₪6.5K contribution, about break-even after founder time. With 8 companies and a Partner it is profitable. **Event 1 is a learning event.**

Credit exposure: at the gate of 35 held intros across 8 companies (an average of 4.4), an even spread would earn about ₪2,000 in credits. Credits push revenue into the next event. They aren't cash refunds.

**Unit value to the buyer:** ₪2,000 ÷ 5 guaranteed intros = at most ₪400 per held intro. HR's walk-away range is ₪200–400 per meeting, so the founding price sits at the top of that range.

**Year 1–3 path** (BizDev, gross bookings)

| | Year 1 | Year 2 [A] | Year 3 [A] |
|---|---|---|---|
| Events | 3 founding (concierge) + 5 on v1 = 8 | 25 (5 in the EU) | 60 |
| Passes | 3 × 6 × ₪2K + 5 × 6 × ₪3.5K [A: 6 per event] | 9 × ₪3.8K per event | 11 × ₪4K per event |
| Presenting Partners | 2 × ₪25K | 10 × ₪25K | 30 × ₪30K |
| Annual plans | 0 | 25 × ₪25K | 80 × ₪28K |
| White-label | 0 | 0 | ₪500K |
| **Total** | **~₪190K (~$52K)** | **~₪1.7M (~$460K)** | **~₪6.3M (~$1.7M)** |

Year 1 includes about ₪26K of organizer rev share at events 4–8, paid out of these bookings. Upside comes from the annual plan, expansion abroad (WeAreDevelopers, KubeCon EU), and white-label or acquisition by Brella, Swapcard or Bizzabo. **Scale beyond event 3 only if** at least 60% of companies intend to rebuy **and** at least 15 next steps are booked per event.

**Organizer deal terms**

| Term | Founding events 1–3 | From event 4 |
|---|---|---|
| Rev share | **Waived**, in exchange for co-branding and distribution | 25% of passes, 15% of the Presenting Partner fee (paid to the community fund at community events) |
| Organizer gives | Co-branding ("Hosted by … · powered by Hallway"), 1 newsletter slot plus the T-72h attendee email, the sponsor list for outreach, Coffee-corner space, a 20-second MC mention, a hashed ticket-holder list | The same, plus Hallway Pass as a line in sponsor tiers |
| We give | Staff, board, matching, privacy controls, post-event report | The same, plus co-marketing |
| Control | Organizer can veto any company and can choose sponsor-only mode | Same |
| Data | Aggregate stats only. No candidate data. The organizer can't see who joined | Same |
| Term | Per event, no exclusivity | 12-month right of first refusal on their series |

---

## 5. Go-to-market

### 5.1 Event #1 plan (DevOpsDays TLV, target Tue Dec 22, 2026, date still to be confirmed)
DevOpsDays is volunteer-run under the global devopsdays brand, so **get the organizer's yes this week.** If they refuse, fall back to **AI Dev TLV (~Dec 21, same gate date)** or **Reversim**. Reversim is ~Nov 30–Dec 1, which would pull its gate to about Nov 9 and is only workable with pre-orders already paid.

| Week | Companies | Candidates | Gate |
|---|---|---|---|
| Oct 13–26 | Organizer call, ₪2,000 pre-order link to 10 sponsors, 10 TA discovery calls (§10) | Fake-door page in the organizer newsletter and DevOps Israel groups | Organizer yes (this week); fake door ≥3–4%; ≥3 pre-orders paid by Oct 28 |
| Oct 27–Nov 8 | Close toward 8 companies + 1 Partner. Sign data-sharing agreements | Lawyer-reviewed privacy page; recruit 3 respected engineers to vouch | — |
| **W-6** Nov 9–15 | Cyber Week (Nov 9–12) as a sales trip to TA leads at their booths. Organizer MOU signed | Domains live; co-branded board skeleton | MOU signed |
| **W-5** Nov 16–22 | Collect role cards (≥3 per company, with bands). Each hiring manager accepts the 2h invite. Hire matchmakers | Build the concierge stack; dry-run hashed matching | — |
| **W-4** Nov 23–29 | **Go/no-go Fri Nov 27** | — | **≥5 prepaid (hard floor), target 8, each with ≥3 roles and a named HM. Otherwise refund and postpone** |
| **W-3** Nov 30–Dec 6 | Hiring-manager kit (guide, code, scorecard) | Organizer email #1, "Who's hiring at DevOpsDays," board plus waitlist. Advisors post on LinkedIn | — |
| **W-2** Dec 7–13 | 20-minute HM briefings plus signed code. Totals (≥5 only) shared | Email #2: "Board is live: 8 companies, 24 roles, salary bands" | — |
| **W-1** Dec 14–21 | Blind invites from T-48h (Dec 20). Slots as .ics | Read the T-3 gate Fri Dec 18 (Dec 19 is Shabbat). Profile form opens Sat night Dec 19. Knocks open Dec 21 for ticket holders. Email #3 + organizer WhatsApp channel | ≥60 pre-registrations (stretch: 90 [A]) |
| **Day** Dec 22 | "Hiring, ask me" lanyards; a live queue | QR on the back of the badge, table tents, MC mention at 10:30 | ≥35 held, 0 exposures |
| After | ROI report; rebuy ask on Jan 5 | "Not this time" by Dec 24; deletion plus receipts Dec 25 | T+14 Jan 5, T+90 Mar 22 |

### 5.2 The 15 target companies (BizDev Round 2)
**[A] = hiring status assumed; check their careers pages before reaching out.**

| # | Company | Type | Why |
|---|---|---|---|
| 1 | ScyllaDB | Dev-tool sponsor | Diamond sponsor at DevOpsDays TLV 2024, Israeli R&D |
| 2 | AWS Israel | Hyperscaler | Platinum sponsor in 2024; co-runs the DevOpsDays community event |
| 3 | Coralogix | Observability scale-up | Exhibited at DevOpsDays TLV 2025 |
| 4 | JFrog | DevOps vendor | Core audience overlap [A] |
| 5 | Wix | Large hirer | Strong engineering brand, hosts meetups [A] |
| 6 | monday.com | Large hirer | Hires at volume, sponsors dev conferences [A] |
| 7 | Nvidia Israel | Multinational R&D | Biggest tech hirer in Israel [A] |
| 8 | Wiz (Google) | Cyber/cloud | Hiring hard after the acquisition [A] |
| 9 | Check Point | Cyber | Cyber Week regular [A] |
| 10 | CyberArk (Palo Alto) | Cyber | Platform/SRE roles [A] |
| 11 | Cato Networks | Cyber scale-up | Infrastructure roles at volume [A] |
| 12 | Island | Cyber scale-up | Hiring fast, wants a strong employer brand [A] |
| 13 | AppsFlyer | Data/infra | Data engineering and SRE [A] |
| 14 | Riskified | Fintech | Platform roles, active in meetups [A] |
| 15 | Taboola | Ad-tech/infra | Large infrastructure team [A] |

For event 1, start with 1–4. The pre-order link goes to 10 DevOpsDays sponsors: these four plus LinearB, Couchbase and other 2024/25 sponsors. Next, 5–7 and 13–15, as non-sponsor hirers the organizer approves. Use the platform/SRE roles at 8–12 to fill gaps. We sell to two pools because most sponsors are tool vendors, not big hirers.

### 5.3 Organizer pitch email
> **Subject:** A hiring corner for DevOpsDays TLV, at no cost to you
>
> Hi [Name], we're piloting Hallway at Israeli dev conferences: a private "who's hiring here" board. Your attendees browse roles with salary bands and book a 15-minute coffee with the hiring manager, and their employer never sees them. We run everything on-site (a coffee corner and 3 staff), with no integration and no app to install. Your sponsors finally get booth ROI they can report, and hiring companies that don't sponsor become new paying customers through you. For our 3 founding events we take **no rev share**. We ask for co-branding ("Hosted by DevOpsDays TLV · powered by Hallway"), one newsletter slot and the T-72h attendee email. You can veto any company, and you'll never see which attendees joined, because ticket matching is hashed. If fewer than 5 companies prepay by Nov 27, we don't run it and it costs you nothing. Can we take 20 minutes this week? We also need to confirm Dec 22.

### 5.4 Company pitch
*"Coffees with mid-level engineers in your stack who chose you, salary aligned, at a conference you already attend. ₪2,000 founding price, 5 held intros guaranteed or pro-rata credit."* Main objections and answers:
- "Candidates are invisible." You get totals 14 days ahead, blind invites, and the guarantee.
- "My hiring manager can't give up a day." Two hours with pre-booked slots is enough.
- "You'll poach our people." The Employer Shield protects your staff too.

### 5.5 Stage script (MC, in Hebrew, 20 seconds, before the 10:30 break)
> "One thing before coffee. Eight companies in this room are hiring: DevOps, backend, AI. Their roles *and salary ranges* are on the Hallway board. Scan the QR on the back of your badge. They can't see you, and you decide who to talk to. Coffee's on them at the Hallway corner by the speaker lounge. And no, your manager can't see you there, even if they're sitting right next to you."

### 5.6 Sample WhatsApp messages (dedicated Hallway phone)
Lock-screen-safe first message:
> You have an update from Hallway. Reply **1** to see it.

After he replies 1:
> Hi Yoni. The platform team lead at [Company] accepted your knock. Coffee at the Hallway corner (Hall 2, behind the speaker lounge), 13:40–13:55.
> Reply 1 to confirm, 2 for another time, 3 to withdraw quietly.
> Nobody else knows you knocked, and your employer can't see you here.

---

## 6. Product and tech

### 6.1 Event-1 concierge tooling (no software built)
- **Tally form** (EU-hosted, GDPR DPA): first name, phone, the 5 knock-card fields, current employer, ex-employers from the last 6 months, declared clients, block list. **No CV, ID number, photo or LinkedIn URL** before an intro is accepted.
- **Locked-down Google Sheet** on a restricted Workspace drive: 2 named matchmakers with 2FA, downloads disabled, a filtered view without phone numbers, an incident log. **Totals are counted by hand and released only for groups of 5 or more.**
- **Dedicated WhatsApp Business phone**: one-to-one messages only, neutral templates. The **"Your employer: blocked"** confirmations and **deletion receipts** are sent by hand.
- **Human matchmakers** (2 before the event, 3 on the day): they resolve employer groups by hand (fail closed), broadcast blind invites to whole groups, and run a paper slot board. A recruiter gets a printed one-line summary only after both sides agree.
- **Hashed ticket matching**: the organizer sends salted hashes of ticket holders' emails and phones. We compare them to candidates' hashed inputs and return aggregate counts only.
- **T+72h purge** of the sheet and chats, with a deletion log. **Paperwork:** privacy notice, versioned consent, a lite DPIA, and a one-page data-sharing agreement per company.

**v1 software gets built only after the pilot shows signal** (gates in §8).

### 6.2 v1 scope: top 10 user stories
| # | Pri | Story |
|---|---|---|
| 1 | P0 | As a **candidate**, I browse the board (roles, salary bands, the hiring manager in the room) with no account and without being seen. |
| 2 | P0 | As a **candidate**, I'm automatically hidden from my employer's group, my recent ex-employers, my declared clients and my block list. I see "Your employer: blocked." If my employer is unresolved, I'm hidden from everyone. |
| 3 | P0 | As a **candidate**, I knock (5 per event) and pick a slot. Only that company sees my 5-field card. My identity is revealed only after it accepts. |
| 4 | P0 | As a **hiring manager or recruiter**, I post roles with a required salary band and slots, and see matching-attendee **totals only for groups of 5 or more**. |
| 5 | P0 | As a **hiring manager**, I send a blind invite (up to 10 slots per role). It goes automatically to the whole matching group of 5 or more, and I learn only who knocks back. |
| 6 | P0 | As a **candidate**, I build my card in 2 minutes. An LLM drafts the fields from my CV, which isn't stored, and I edit them. Nothing scores or ranks me. |
| 7 | P0 | As a **hiring manager**, I get a day queue with neutral WhatsApp reminders and the meeting point, and I log a 30-second note plus the next step before the candidate leaves. |
| 8 | P0 | As a **candidate**, I see accepted or "not this time" within 48h. Unmatched data is deleted at T+72h with a receipt, and I consent per company to keep or export. |
| 9 | P0 | As a **candidate holding a ticket**, my knocks open at T-24h through hashed matching, or when I check in at the venue. |
| 10 | P1 | As a **buyer**, I get an ROI report (T+14, T+90) and a CSV export with consent. Comeet comes later. |

### 6.3 Data model summary (Postgres, EU region; † = encrypted with the per-event key, crypto-shredded at T+72h)
- **Company graph:** `companies` (aliases, parent_id, kind employer/agency/stealth, source curated/Wikidata/M&A/registry), `company_domains`.
- **Events and people:** `events` (purge_at, key_ref), `attendee_hashes`, `presence` (pending / ticket_holder / checked_in), `users` (phone_hash), `recruiters` (domain-verified, is_agency).
- **Candidates:** `candidate_profiles†` (the 5 fields), `candidate_blocks` (source: group / ex_employer / declared_client / manual), `employer_resolution` (below the confidence threshold means hidden).
- **Matching:** `role_cards` (salary band NOT NULL, hm_user_id), `blind_invites` (group_key, slots ≤10, group_size ≥5), `knocks` (pending / accepted / not_this_time / withdrawn), `slots`, `intros` (outcome, next_step_at).
- **Governance:** `consents` (versioned, per purpose), `access_log`, `deletion_receipts`, `outcome_records` (expire at +90 days).

### 6.4 10-week build plan (2 full-stack engineers + a 0.5 designer; starts only after the Jan 5 readout, about Jan 10 – Mar 18, 2027)
| Wk | Deliverable |
|---|---|
| 1 | Schema, row-level security, WhatsApp code sign-in, events, venue check-in |
| 2 | Company-graph import (curated lists + Wikidata + M&A + registry) and resolution service; recruiter domain verification |
| 3 | Candidate onboarding (LLM drafts → user edits); consent records |
| 4 | Role cards (band required), board, Knock flow, 5-knock cap |
| 5 | **Blocking engine + group-of-5 gate for totals and invites, with adversarial tests (release gate)** |
| 6 | Blind invites to whole groups, slots, hashed ticket matching, neutral WhatsApp templates |
| 7 | Hiring-manager queue and notes, 48h "not this time" job |
| 8 | CSV export (explicit consent), ROI report |
| 9 | Crypto-shred purge, deletion receipts, audit log, pen test, DPIA sign-off |
| 10 | Dogfood at a meetup, fixes; first v1 event (event 4) |

Events 2 and 3 run as concierge while v1 is being built.

### 6.5 Moat
The code is not a moat. What lasts is organizer contracts (first refusal, multi-year), recruiter workflow lock-in across 15+ events a year, the only **consented dataset of in-person intros that became hires** (which drives pricing and ROI), and the "discreet one" brand. Later comes a "Verified Met-in-Person" credential (W3C VC / SD-JWT, issued by `did:web:hallway.jobs`, minted only when both phones scan each other at the venue).

### 6.6 Deferred
- **Open mode** waits for v1.1, and only with fixed-category cards, k≥5, watermarking, view caps and no agency recruiters.
- **Video booth** waits for year 2. Until then, phone video from a quiet room. The "Boomerang Booth" stunt only once we have hire stories.
- **Also deferred:** native Comeet, the story engine (manual until then: told by the employer, with consent, 90 days after a hire), success fees, the credential.
- **Never:** swiping, or AI that scores or ranks candidates (high-risk under the EU AI Act).

---

## 7. HR/TA playbook

### 7.1 Hallway Coffee: 15-minute guide for hiring managers
**Structure**
- **0–2 min, you:** your name and role, what the team builds, the role, the band, and that this is a conversation, not an interview.
- **2–8 min, them:** "What are you working on now?" "What's the most interesting problem you solved this year?" "What would make a move worth it?"
- **8–12 min, role probes:** 2 questions fixed per role, the same for everyone. Example: "How would you debug a latency spike in a service you don't own?"
- **12–15 min, logistics and next step:** notice period, work mode, salary expectation, and their questions.

**Allowed:** skills, experience, motivation, salary *expectations*, notice period, "Is hybrid 3 days in Herzliya workable?", "Are you authorized to work in Israel?", and clearance *only* if the role legally requires it.

**Forbidden:** age or graduation year; military unit or service history (if the candidate raises it, don't follow up); **reserve duty**, past or expected; pregnancy, children, family plans or marital status; religion or observance (state the schedule instead); where they live (ask about commute or work mode); health; their current employer's confidential details; any promise of an offer or a specific salary.

**Next-step script**
- Go: "I'd like you to meet [name] for a 45-minute technical conversation. Let's book it now: Tuesday 10:00 or Wednesday 16:00? You'll get a WhatsApp confirmation within the hour."
- Not a fit: "Honestly, this role needs [job-related requirement]. Can I keep your card for [other role], or would you prefer we delete it?"
- Never say "we'll be in touch" without a date. Reply to every knock within 48h.

**Logging (within 5 minutes, in the template):** role; a 1–4 score on the 3 predefined criteria, with one line of evidence each; decision (booked / hold / no) with a job-related reason. **Banned words:** "culture fit," "young," "energetic," appearance, accent, "overqualified." Write every note as if the candidate will read it, because under the privacy law they can.

Each hiring manager signs the one-page code and attends a 20-minute briefing before Dec 22. This is the HR sign-off condition.

### 7.2 The knock card: exactly 5 fields
| # | Field | Example (mid-level) |
|---|---|---|
| 1 | Target role + seniority | "Backend, mid-level, 5 yrs" |
| 2 | Top 3 skills, each with one proof line | "Kafka: 10M events/day pipeline" |
| 3 | What I'm looking for (≤140 characters) | "Owning a platform team's infra, less on-call firefighting" |
| 4 | Notice period + work mode/region | "60 days · hybrid, Tel Aviv area" |
| 5 | Salary expectation (gross monthly ₪) | Shown to the company only as "within / above your band" |

**Excluded:** name, photo, current employer, education, army unit, age. Name and LinkedIn are revealed only after the company accepts.

### 7.3 Legal minimums for the concierge pilot
- **Minimize.** Collect the 5 fields plus name, phone, email and blocking inputs. Never collect ID number, date of birth, photo, army unit, marital status or address.
- **Notice at collection** (Hebrew and English, one screen): purpose, recipients, that it's voluntary, retention period, and access/correction rights. Separate explicit consent per company, with no sharing by default.
- **Retention.** Unmatched data is deleted at T+72h. Outcome flags for accepted intros are kept with consent for 90 days. Each company signs a one-page agreement: hiring purpose only, no re-sharing, delete non-hired candidates within 6 months.
- **Fair hiring.** No filters on protected attributes, a mandatory guide, a signed code, an accessible corner.
- **[LAWYER]** Is job-seeking status "information of special sensitivity" under Amendment 13? Treat it as sensitive either way.
- **[LAWYER]** Who is the data controller: us, the organizer or the employer? Hashed matching hides who joined from the organizer, which points to us.
- **[LAWYER]** Does facilitating intros, even unpaid, require a placement-agency license under the Employment Service Law?
- **[LAWYER]** Database registration, DPO, and the 2017 Information Security Regulations. Also our liability if an employer discriminates during an intro.

---

## 8. Gates, metrics, kill criteria

**North star:** held intros with a next step booked within 14 days. **Guardrail:** zero candidates exposed to their own employer.

| When | Gate / metric | Pass | If it fails |
|---|---|---|---|
| This week (by Thu Oct 15; latest Sun Oct 18) | Organizer yes + Dec 22 confirmed | Yes in writing | Switch to AI Dev TLV (~Dec 21) or Reversim |
| Oct 25 | Fake-door landing page | ≥4% of recipients click "notify me," or ≥3% start a profile | 1–2%: rethink the candidate funnel before selling more |
| Oct 28 | Refundable ₪2,000 pre-orders (10 sponsors) | ≥3 paid within 14 days | Re-price or re-pitch; don't proceed on verbal yeses |
| Oct 26 | Discovery calls | 10 held; ≥1 named HM accepts a 2h invite within 48h | The HM-led model needs rework |
| Before Nov 27 | Block-list red team (60 employers) | 0 unfixed misses; 0 re-identifications | No event until it's fixed |
| **Fri Nov 27** | **Go/no-go** | **≥5 prepaid (hard floor), target 8, each ≥3 roles + named HM** | Refund and postpone |
| Fri Dec 18 (T-3) | Candidate pre-registrations | ≥60 (stretch 90 [A]) | Push organizer channels, extend invites |
| Dec 22 | Held intros / exposure | **≥35 held**; ≥40% with a next step booked at the venue; **0 exposures** | Any exposure is a P0 and stops the next event |
| Jan 5, 2027 (T+14) | Next steps; rebuy | ≥10 next steps; ≥3 companies prepay for the next event | Diagnose before event 2 |
| Mar 22, 2027 (T+90) | Hires | ≥1 attributable hire | Kill signal if 0 after 3 events |
| After event 3 | Kill / pivot | Rebuy ≥50%, median company ≥5 held intros, ≥1 hire | **Kill or pivot.** If knocks are under 10% of profiles while invites convert well, become invite-led |
| After event 3 | Scale | ≥60% rebuy intent and ≥15 next steps per event | Hold at concierge |

Also measured: the full funnel (board views → pre-registrations → profiles → knocks and invite-accepts → held → next step → hire), invite vs. knock conversion, recruiter minutes per held intro, 48h reply rate, employer-block catches and misses, and one anonymous question: "Did you come partly to explore opportunities?"

---

## 9. Risks register

| # | Risk | Owner | Mitigation test |
|---|---|---|---|
| 1 | Volunteer DevOpsDays organizers refuse or stall | BizDev | 20-minute call this week. No yes by Oct 18 → switch to AI Dev TLV or Reversim the same day |
| 2 | Employed engineers don't opt in to an unknown brand | Marketing | Fake door with an A/B test of 2 privacy lines; pass ≥3–4% |
| 3 | Companies won't prepay before they see candidates | BizDev | Refundable ₪2,000 pre-order to 10 sponsors; pass ≥3 paid in 14 days |
| 4 | Hiring managers don't show up (release, reserve duty) | HR/TA | Prepay is conditional on a *named* HM accepting the 2h invite within 48h; each company names a backup HM |
| 5 | Employer blocking misses a subsidiary, rebrand, stealth company or foreign parent | Tech | Red team on 60 real employers with 5 engineers; fail closed on anything unresolved |
| 6 | Re-identification through totals or blind invites in a small scene | Tech | 5 recruiters try to re-identify colleagues; groups smaller than 5 get no totals and no invites |
| 7 | Regulatory: sensitive data, controller role, placement-agency license | Founder + HR | Lawyer consult in the next 14 days; privacy page and DPIA signed before W-3 |
| 8 | Funnel too thin: 35 held from 60 profiles needs ~58% conversion | PM | Stretch target of 90 pre-registrations [A]; advertise a role family only if ≥2 companies hire for it; blind invites fill gaps |

---

## 10. The next 14 days (Tue Oct 13 – Mon Oct 26)

**Tue Oct 13 – Wed Oct 14**
- [ ] Email and call the DevOpsDays TLV organizers. Use the pitch in §5.3, confirm Dec 22, and ask for the newsletter slot, the sponsor list and the hashed attendee list. Open warm conversations with AI Dev TLV and Reversim in parallel.
- [ ] Send the **refundable ₪2,000 pre-order link** (Stripe/Morning payment link: "Founding pass, DevOpsDays TLV, fully refundable if we don't run") to 10 sponsors. **Pass: ≥3 paid by Oct 28.**
- [ ] Trademark search for "Hallway Talent" and "מסדרון" (Israeli registry plus a USPTO/EUIPO knockout). Check and buy hallway.jobs, hallwaytalent.com, hallway.co.il, misderon.co.il.
- [ ] Book the lawyer consult. Email Noa Barazani asking for one learning coffee.

**Thu Oct 15 – Sun Oct 18**
- [ ] **Organizer yes in writing by Thu Oct 15.** If there's no answer by Sun Oct 18, switch event #1.
- [ ] Build the **fake-door page**: "Companies hiring at DevOpsDays: browse privately," with the 5-line privacy text, 2 privacy-line variants and a "notify me" button (phone + role family + seniority). List **only companies with a pre-order or letter of intent.** Launch Sun Oct 18 in the organizer newsletter slot and the DevOps Israel FB/Telegram/WhatsApp groups.
- [ ] Start the **10 TA discovery calls** (Appendix A): 4 scale-ups that sponsor, 3 multinational R&D centers, 2 startups under 50 people, 1 agency. Don't pitch until question 9.

**Mon Oct 19 – Thu Oct 22**
- [ ] **Lawyer consult (2h):** Amendment 13 sensitivity, the data-controller question (given hashed matching), the placement-agency license, DPO/database registration, and the privacy page wording.
- [ ] **Block-list red team (1 day):** resolve groups for 60 real employers, then 5 engineers check for misses and 5 recruiters attempt re-identification. Log every miss and fix the curated list.
- [ ] Every discovery call ends with the prepay ask, **conditional on a named hiring manager accepting a 2-hour calendar invite for Dec 22 within 48h.** Count accepted invites, not verbal yeses. **Pass: ≥1.**
- [ ] **Learning coffee with Hooked's founder.** Ask about real QR scan rates, activation tactics that work, and whether they've seen deletion-receipt behavior. No partnership talk.

**Sun Oct 25 – Mon Oct 26**
- [ ] Read out the fake door (pass ≥3–4%), the pre-order count, HM invites accepted, red-team misses and the lawyer's answers.
- [ ] **Decision memo:** proceed to selling 8 companies + 1 Partner for Nov 27, or switch event, or rethink the candidate funnel.

---

## 11. Open questions still unresolved

1. **Is Dec 22 confirmed**, and will a volunteer-run, globally branded event accept a recruiting layer at all?
2. **[LAWYER]** Amendment 13 sensitivity, the controller role (the hashed design may make us controller, against PM's organizer-controller plan), and the placement-agency license.
3. **The gate sits below the guarantee.** At 8 companies, the sum of guarantees is 40 held intros while the gate is 35. Should the gate scale with the number of companies sold (for example, ≥4.5 × companies)?
4. **What "T-3: ≥60 profiles" means.** Profiles open only at T-72h, so we read the gate as pre-registrations, which v3 didn't specify. Confirm, or open profiles earlier.
5. **Funnel realism.** Does ~58% conversion from profile to held intro hold up, or is 90 pre-registrations the real floor?
6. **Blind invite mechanics.** We read "up to 10 per role" as 10 invite slots broadcast to the whole group, first come, first served. Is that enough reach, and does broadcasting to all of a group feel like spam?
7. **Events 2 and 3** (Q1 2027): which dev/AI events, which dates, and will organizers waive the rev share on the same terms?
8. **Will ≥60% of the ₪2,000 buyers accept ₪3,500 from event 4?** And does the ₪300 per extra intro test cannibalize the pass?
9. **Hiring managers on video.** Should we allow "on video inside the slot" (PM) when no one can come on site, or does that break the "someone who does the job, at the venue" promise?
10. **Salary bands.** How many target companies refuse to show them even inside the attendee-only board?

---

## Appendix A: Discovery interview questions (10 TA leaders)

**Who to interview:** 4 scale-ups that sponsor events, 3 multinational R&D centers, 2 startups under 50 people, 1 agency. Don't pitch until question 9.

1. Tell me about the last conference you attended as a company. What did it cost all-in, and what came out of it?
2. How do you report event ROI to your CFO today? What did you say last time?
3. Which 3 roles are hardest for you to fill right now, and why?
4. When did you last hire someone you first met in person? What happened?
5. What do you do with leads in the week after an event? Where do they end up?
6. Would your hiring managers give 2 hours at a conference? What would make them say no?
7. What would you need to see 14 days and 48 hours before an event to send someone?
8. Candidate-initiated knocks only versus anonymous blind invites to a matching group: how would each change your interest?
9. *(Show the concept.)* What's the price at which this is a no-brainer, the price where you'd need approval, and the price where you'd say no? Which budget line does it come from, and who signs?
10. What would worry your legal team or DPO? Do you have a policy on in-person screening?
11. Which ATS do you use, and is a CSV with consent good enough?
12. What would make you *not* renew after one event?
13. Would you commit to replying to every knock within 48h, including a "not this time"?
14. **The commitment ask:** "Would you prepay ₪2,000 for DevOpsDays TLV, with pro-rata credit if you get fewer than 5 held intros? It's conditional on [named hiring manager] accepting a 2-hour calendar invite for Dec 22 within 48 hours." Record yes, no, or "I need X," **and whether the invite was accepted.**

**Organizer call (20 minutes):** Can a recruiting layer run under the devopsdays brand? Is Dec 22 confirmed? Can we have a newsletter slot, the T-72h email, an MC mention and corner space? Which sponsors hire? Which companies would you veto? Can you share a hashed ticket-holder list?
