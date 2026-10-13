# Round 2: PM stress-test of Concept v2 ("Hallway")

v2 is much better than the pitch, but three parts of it contradict each other, and they need fixing before the pilot.

## 1. The three biggest flaws

1. **"Ephemeral and presence-gated" contradicts pre-event matching and the north star.**
   - A rotating venue QR can't gate profiles that open at T-72h.
   - Data that dies at T+72h can't measure next steps at T+14, the ROI report, or hires.
   - **Fix:** presence becomes a *status*, not a gate; eligibility comes from the organizer's registration list. We delete everything unmatched. For matched intros we keep a minimal, consented outcome record: company, date, next step, hired yes/no.
2. **The recruiter value promise depends on the mode most candidates won't choose.** "N relevant people are coming, pre-book slots" only works for Open-mode users, and that's a small opt-in group of employed people. The sales pitch rests on the smallest group of candidates.
3. **The gates are set for scale, not for learning.**
   - Five companies prepaying ₪3,500 each, each with a hiring manager, before any case study exists, makes it more likely we never get to launch than that the product fails.
   - Sponsor "24h early access" means nothing when the default is Knock mode. Early access to what?

## 2. Open tensions

**#1: Will companies pay if candidates are invisible?** Yes, if we sell **guaranteed conversations, not visibility**:

- **Aggregate demand signal:** each role card shows "23 registered attendees match," counted across both modes. A count only appears at k≥5, so no one can be singled out. This is what a buyer shows the CFO.
- **Blind invite-to-knock:** the hiring manager sends one invite per role (e.g. "coffee at 11:30, DevOps 4–7 yrs, ₪38–45K"). It goes to matching attendees, and the company learns only who accepts. That's outbound reach with zero exposure, and it's the core B2B feature.
- **Meeting guarantee:** the pass includes 5 held intros, or a pro-rated credit.
- **The sponsor perk is placement, not data:** pinned role cards and the first invite wave, never early access to candidate profiles.
- **Open mode moves to v1.1.** In the pilot we only ask "would you turn this on?"

**#2: Are 5 prepaid companies realistic?**
- At a 1,000–1,500-person dev conference it's realistic *at a founding price, sold by the organizer to its existing sponsors* (often 15–30, many of whom sponsor to hire). ₪3,500 only becomes realistic from event 3.
- Five companies make a thin board, so on the candidate side:
  - **Coverage rule:** we advertise a role family only if at least 2 companies hire for it.
  - **Role family is the first onboarding question.** If nothing matches, we say "no SRE roles today, we'll ping you" and never show an empty board.
  - Hiring-manager office hours and remote slots fill the gaps.
- **Target 8 companies.** Five is the floor.

## 3. Concierge pilot runbook (event #1: DevOpsDays TLV, Dec 22)

| When | Step |
|---|---|
| T-6w | Agreement: organizer is the data controller, we are the processor. Short DPIA (data protection impact assessment) with a privacy lawyer, consent text per purpose, a named privacy owner, and a deletion protocol. |
| T-5→2w | The organizer sells 5–8 **₪2,000 founding passes**: up to 3 roles each, a required salary band, a hiring manager on site for at least 3 hours, and the 5-intro guarantee. |
| T-2w | Board page, Tally form, Airtable, a WhatsApp Business number, 2 matchmakers. |
| T-72h | Organizer email: "8 companies hiring. Browse privately." The form asks 5 fields (role family, seniority, stack, employer, block list) plus a per-role "curious" tick. CV is optional. |
| T-72h→T-12h | **Manual employer check, fail-closed.** We send anonymized cards only for knocked roles, plus the blind invites. Slots go out as .ics files. |
| Day | Coffee corner with 3 tables, out of sight of the expo floor. MC mention at 10:30. QR on table tents. After each intro, a 30-second recruiter form (next step booked yes/no) and a 2-question candidate pulse. |
| T+72h | Delete unmatched data and log the deletion. Nudge companies on the 48-hour follow-up. |
| T+14 / T+90 | Surveys on next steps and hires. Ask for a re-buy for event #2 at T+14. |

**What we measure:**
- The full funnel: registered → board views → profiles → knocks/invite-accepts → accepted → held → next step booked at the venue → next step held by T+14 → hired by T+90.
- How invites convert compared with knocks.
- Seniority mix compared with the roles on offer.
- Recruiter minutes per held intro.
- Employer-block catches and misses.
- One anonymous question: "Did you come partly to explore opportunities?" This replaces the made-up "60%."

**Event #1 succeeds if:**
- At least 40 profiles, at least 70% of which see a relevant role
- At least 25 held intros
- At least 40% of held intros have a next step booked at the venue
- At least 3 companies prepay for event #2
- 0 exposure incidents

**Kill after 3 events if any of these happens:**
- fewer than 15 held intros per event on average
- fewer than 2 companies re-buy per event
- 0 hires we can attribute by T+90
- any exposure we can't contain

**Pivot signal:** if knocks are under 10% of profiles while invites convert well, we become invite-led.

## 4. v1 PRD skeleton: top 10 user stories

| # | Pri | Story |
|---|---|---|
| 1 | P0 | As a **candidate**, I browse the hiring board (role, salary band, hiring manager in the room) with no account and without being seen. |
| 2 | P0 | As a **candidate**, I'm auto-hidden from my employer, its group and its agencies, I can add blocks, and if my employer is unresolved I'm hidden from everyone. |
| 3 | P0 | As a **candidate**, I knock on a role and pick a slot. Only that company sees my anonymous card, and my identity is revealed only after it accepts. |
| 4 | P0 | As a **hiring manager or recruiter**, I post roles with a required salary band and slots, and see a k-anonymous count of matching attendees. |
| 5 | P0 | As a **hiring manager or recruiter**, I send a blind invite-to-knock and see only who accepted. |
| 6 | P0 | As a **hiring manager**, I get a day queue with WhatsApp reminders and the meeting point. |
| 7 | P0 | As a **candidate**, I build a profile from my CV in 2 minutes with AI-drafted fields that I edit. Nothing scores me. |
| 8 | P0 | As a **recruiter**, I log a structured 30-second note and book the next step before the candidate leaves. |
| 9 | P0 | As a **candidate**, unmatched data is deleted at T+72h, I consent per company to keep or export, and I get a status update if the company is silent for 48 hours. |
| 10 | P1 | As a **buyer**, I get an ROI report (T+14 and T+90 outcomes) and a CSV export; Comeet comes later. |

**Deferred:** Open mode, rotating-QR presence, the organizer console, the native Comeet connector, the story engine, video slots.

## 5. Where I still disagree with the founder

1. **A rotating-QR gate guards against the wrong risk.** Fake attendees aren't the problem; an empty board is. Gate on the registration list, and use the QR as the "here now" check-in.
2. **Don't market "everything dies in 72h."** We have to keep outcome records. The honest promise is: **"No one sees you unless you knock."**
3. **Open mode and the story engine don't belong in v1.** Open mode is the biggest privacy risk and still unproven. The story engine is marketing work.
4. **Fixing ₪3,500 before we have data is a guess.** Test **₪2,000 including 5 intros, plus ₪300 per extra held intro**. That matches HR's per-meeting logic and makes the guarantee self-funding.
5. **Keep the hiring-manager rule, but allow "on site for 3 hours *or* on video inside the slot."** Otherwise we lose the supply we need.
