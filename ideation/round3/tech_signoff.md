# CTO sign-off — Concept v3

**(a) SIGN-OFF, with conditions.** DevOpsDays TLV is 10 weeks out and the go/no-go gate is in 7, so v1 can't ship in time. The pilot must run as a manual concierge. Three v3 features assume software (counts only for groups of 5 or more, the live "employer blocked" view, deletion receipts), and each needs a manual version for event 1.

**(b) Biggest risk: employer blocking misses a match.** A subsidiary, a rebranded company, a stealth startup or a foreign parent slips through. That breaks the zero-exposure guardrail and the brand with it. **Cheapest test (1 day, ₪0):**
- Resolve the company groups for 60 real employers of past DevOpsDays/Reversim speakers, plus our target buyers.
- Have 5 engineers check for misses.
- Ask 5 recruiters to try to re-identify colleagues from the group counts and blind invites.

**(c) Inconsistencies:**
1. Ruling 9 says "the employer's clients". It should be the *candidate's* clients (freelancer or consultant placements). An employer's clients are unbounded, so blocking them would hide almost everyone.
2. The Israeli companies registry has no group structure. Group mapping needs hand-curated lists, Wikidata and an M&A feed.
3. Ruling 4 refers to "cards", but Open mode is deferred, so v1 has none. The rule of 5 should apply to the totals and to who receives blind invites.
4. Blind invites (Ruling 3) can't go to individually chosen "matching profiles" while profiles are hidden. They must go to a whole group of 5 or more.
5. "Ticket holders 24h before" means matching against the organizer's attendee list. That must use hashed contact details.
6. Confirm the Dec 22 date.
