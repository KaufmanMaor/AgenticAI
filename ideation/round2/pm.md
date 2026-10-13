# Round 2: PM stress-test of Concept v2 ("Hallway")

v2 is much better than the pitch: asymmetric visibility, coffee intros instead of interviews, hiring managers in the room, and the gates. But three parts of it contradict each other, and they need fixing before the pilot.

## 1. The three biggest flaws

**Flaw 1: "Ephemeral and presence-gated" contradicts "pre-event matching" and "ROI reporting."**
- A rotating venue QR can't gate profiles that open 72 hours *before* the event.
- Data that "dies at T+72h" can't support the north star, which counts next steps within 14 days. It also can't support the ROI report or "Hired in the Hallway" stories.

As written, v2 can't measure its own north star. The fix:
- Presence becomes a **status** ("here now"), not an entry gate. Eligibility comes from matching against the organizer's registration list.
- Deletion applies to **everything that was never matched**.
- Matched intros keep a minimal **outcome record** that the candidate consented to: company, date, next step, hired yes or no. No CV.

**Flaw 2: The recruiter value promise depends on the mode most candidates won't choose.**
- The founder says "N relevant people are coming, pre-book slots" is what makes a recruiter buy.
- But Knock mode is the default and candidates are invisible in it. Only Open-mode users (an opt-in minority of employed people) could be pre-booked.
- So the sales pitch rests on the smallest group of candidates. Section 2 fixes this.

**Flaw 3: The gates are set for scale, not for learning.**
- Requiring "≥5 prepaid companies at ₪3,500, each bringing a hiring manager" for event #1, with no case study yet, sets the risk of not even getting to launch higher than the risk of the product failing.
- HR (₪3–5K, or ₪200–400 per meeting) and Marketing (₪1,500–2,500, refundable) both priced lower for a reason.
- Separately, sponsor "24h early access" means nothing in a Knock-default world. Early access to what?

## 2. Open tensions

**#1: Will companies pay if candidates are invisible?** Yes, if we sell **guaranteed conversations, not visibility.** Four mechanics:

1. **Aggregate demand signal.** Before the event, each role card shows "23 registered attendees match this role," built from *all* profiles in both modes. A count only appears when there are at least 5 matches, so no one can be singled out. This is what Dana shows her CFO before buying.
2. **Blind invite-to-knock.** The recruiter sends one invite per role ("Team lead from X, coffee at 11:30, DevOps 4–7 yrs, ₪38–45K"). We deliver it to matching attendees in both modes. The recruiter learns only who accepts. That gives recruiters outbound reach with zero exposure for candidates. It's the core B2B feature.
3. **Meeting guarantee.** The pass includes at least 5 held intros, or a pro-rated credit toward the next event. What we sell is held conversations, not access.
4. **Sponsor perk becomes placement, not data.** Sponsors get pinned role cards and the first invite wave 24 hours earlier, never early access to candidate profiles.

Open mode moves to v1.1, and in the concierge pilot we only ask "would you turn this on?" to measure appetite.

**#2: Are 5 prepaid companies realistic, and what does that mean for candidates?** Five is realistic at a dev conference of 1,000–1,500 people *at a founding price, sold by the organizer, mostly to its existing sponsors*. Typical events have 15–30 sponsors, and many sponsor in order to hire. ₪3,500 becomes realistic from event 3, once we have a case study. Five companies is a thin board, so on the candidate side:

- **Coverage rule:** we only advertise a role family (DevOps, backend, data, etc.) if at least 2 companies are hiring for it, so a candidate has a choice.
- **Role family is the first question** in onboarding. If nothing matches, we say so honestly: "No SRE roles today. We'll tell you when there are." The candidate never sees an empty board.
- **Make the board feel alive:** hiring-manager office hours, plus remote slots to fill gaps in coverage.
- **Target 8 companies.** Five is the floor, not the goal.

## 3. Concierge pilot: event #1 runbook

Recommended event: DevOpsDays TLV (Dec 22), which has a tight niche of scarce skills.

| When | Step |
|---|---|
| T-6w | Organizer agreement: organizer is the data controller and we are the processor. Short DPIA (data protection impact assessment) with a privacy lawyer, consent text per purpose, a named privacy owner, and a deletion protocol. |
| T-5w → T-2w | The organizer sells 5–8 companies a **₪2,000 founding pass**: up to 3 roles each, a required salary band, a hiring manager on site for at least 3 hours, and a guarantee of 5 held intros (otherwise credit). |
| T-2w | Board page (Notion/Carrd), Tally form, Airtable, one WhatsApp Business number, 2 matchmakers. |
| T-72h | Organizer email: "8 companies are hiring here. Browse privately." Profile form has 5 fields: role family, seniority, stack, current employer, block list. CV is optional. Then a "curious" tick per role. |
| T-72h → T-12h | **Manual employer check, fail-closed**: if the employer is unclear, the profile goes to no one. We send anonymized cards *only* for knocked roles and send the blind invites. Accepted intros get a slot and an .ics file. |
| Day | Coffee corner with 3 tables, out of sight of the expo floor. MC mention at 10:30. QR on table tents. Live knocks go through WhatsApp. After each intro: a 30-second recruiter form (next step booked yes/no) and a 2-question pulse for the candidate. |
| T+72h | Delete unmatched data and keep a deletion log. Send a reminder for the 48-hour follow-up promise to companies. |
| T+14 / T+90 | Survey both sides about next steps, then hires. Ask for a re-buy for event #2 at T+14. |

**What we measure:**
- **The funnel:** registered attendees → board visits → profiles → knocks → accepted → held → next step booked at the venue → next step held by T+14 → hires by T+90.
- **Who comes:** seniority mix compared with the roles on offer; share of Knock vs. "would use Open."
- **Effort and quality:** recruiter minutes per held intro; employer-block catches, and any misses.
- **Repeat signals:** candidate "would use again"; company prepay for the next event.
- **One anonymous question for every candidate:** "Did you come partly to explore opportunities?" This replaces the made-up "60%".

**Success bar for event #1:**
- At least 40 profiles, at least 70% of which see 1 or more relevant role
- At least 25 held intros (5 or more per company)
- At least 40% of held intros with a next step booked at the venue
- At least 3 companies prepay for event #2
- 0 exposure incidents

**Kill or pivot, judged after 3 events:**
- Held intros average fewer than 15 per event, *or*
- fewer than 2 companies re-buy per event, *or*
- 0 hires we can attribute by T+90 across all three events, *or*
- any exposure of a candidate to their employer that we can't fully contain.

**Pivot signal:** if knocks are under 10% of profiles while invites convert well, candidates prefer being asked. In that case we lean into invite-led matching.

## 4. v1 PRD skeleton: top 10 user stories, prioritized

| # | Pri | Story |
|---|---|---|
| 1 | P0 | As a **candidate**, I can browse the event's hiring board (role, salary band, hiring manager in the room) with no account and without being seen. |
| 2 | P0 | As a **candidate**, I'm automatically hidden from my current employer, its group companies and its agencies, and I can add my own blocks. If my employer can't be resolved, I'm hidden from everyone. |
| 3 | P0 | As a **candidate**, I knock on one role and pick a slot. Only that company sees my anonymized card, and my identity is revealed only after it accepts. |
| 4 | P0 | As a **recruiter or hiring manager**, I post roles with a required salary band and slot windows, and I see the k-anonymous count of matching attendees. |
| 5 | P0 | As a **recruiter**, I send a blind invite-to-knock to matching attendees and see only who accepted. |
| 6 | P0 | As a **hiring manager**, I get a day queue with WhatsApp reminders and the meeting point. |
| 7 | P0 | As a **candidate**, I create a profile in 2 minutes from my CV with AI-drafted fields that I edit. The AI never scores me. |
| 8 | P0 | As a **recruiter**, after each intro I log a structured 30-second note and book the next step before the candidate leaves. |
| 9 | P0 | As a **candidate**, I control my data: unmatched data is deleted at T+72h, I consent per company to keep or export, and I get a status update if the company goes silent for 48 hours. |
| 10 | P1 | As a **company buyer**, I get an ROI report (intros, next steps, T+14 and T+90 outcomes) and a CSV export, with Comeet later. |

**Deferred to v1.1+:** Open mode, rotating-QR presence, the organizer console (we run admin ourselves), native Comeet integration, the story engine, and video slots.

## 5. Where I still disagree with the founder

1. **Rotating QR as a gate is solving the wrong problem.** Fake attendees aren't the risk; an empty board is. Use the registration list, and keep the QR as the check-in for "here now."
2. **Don't market "everything dies in 72 hours."** We have to keep outcome records. The honest promise that earns trust is: **"No one sees you unless you knock."**
3. **Open mode and the story engine don't belong in v1.** Open mode is our biggest privacy risk and still unproven. The story engine is marketing work, not product.
4. **Pricing:** fixing ₪3,500 per event before any data is a guess. Test a hybrid in the pilot: **₪2,000 base including 5 intros, plus ₪300 per additional held intro.** That matches the budget logic HR described and makes the guarantee self-funding.
5. **Hiring manager rule:** keep it, but allow "on site for 3 hours *or* joining by video within the 15-minute slot." Otherwise we lose the supply we need.
