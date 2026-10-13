# Round 2: VP HR / TA stress-test of Concept v2

*Prices and thresholds are my field judgment. Items marked **[LAWYER]** need Israeli privacy or employment counsel before the pilot.*

## 1. The 3 biggest flaws in v2

1. **Knock-only demand turns into a job board with a coffee corner.** Passive seniors won't knock either, at least not at first. Active seekers and juniors will. So the companies paying ₪3,500 get *inbound from the wrong segment*, which is exactly what they already get at the booth.
2. **The 72-hour data death fights the hiring timeline.** A mid-level hiring process takes 3–6 weeks. The north star ("next step within 14 days") and the ROI report both need data after T+72h. Decide explicitly: what *we* keep (aggregate outcomes, with consent) versus what moves to the employer's ATS (accepted intros only).
3. **Hiring managers are the biggest legal risk, not recruiters.** Team leads are untrained. They'll ask "where did you serve?", "kids?", "how much miluim this year?", and they'll promise salaries on the spot. Making the hiring manager mandatory without a guide and a signed code of conduct puts lawsuits on our product. Also, getting 5 hiring managers × 3 hours at one event is hard. Plan on 90-minute slot blocks.

*(Runner-up: a required salary band. Many Israeli companies refuse to publish bands. Accept "band shown only to the candidate, never public" as a compromise.)*

## 2. Tension #1: will I pay ₪3,500 if candidates are invisible?

**Not for knock-only. Yes for knock plus a controlled outbound path.** What gets me to yes:
- **A pre-event count:** at T-48h, "N anonymized Open-mode cards match your reqs." If N < 8, I can cancel for free.
- **Invites:** I can send up to 10 anonymous "we'd like a coffee" invites to Open-mode cards. The candidate still decides, so discretion holds.
- **A floor guarantee:** fewer than 5 *held* intros gets me a credit for the next event. At 5 or more held intros, ₪3,500 = ₪700 per conversation with a pre-qualified person. That's cheap.
- **A bundle:** for existing sponsors, fold it into the sponsorship package as an upgrade instead of a separate PO. That's one approval instead of two.

## 3. Tension #4: minimum compliant setup for the concierge pilot

**Privacy (Protection of Privacy Law, Amendment 13):**
- Collect only the 5 knock-card fields plus name, phone and email. **Do not collect** ID number, date of birth/age, photo, army unit, marital status or address.
- **Notice at collection:** purpose, who receives the data, that providing it is voluntary, retention period, and access/correction rights. Hebrew and English, one screen.
- **Separate explicit consent for each company** before sharing. The default is no sharing.
- **Retention:** delete everything at T+72h, except intros the candidate accepted. Those go to the employer. We keep only outcome flags (next step yes/no) with consent, for 90 days.
- **Tooling:** Google Workspace with a signed DPA, access limited to 2 named matchmakers, 2FA, no personal phones holding the sheets, and a written incident log.
- A **one-page data-sharing agreement with each paying company**: hiring purpose only, no re-sharing, delete non-hired candidates within 6 months.
- **[LAWYER]** Whether job-seeking status counts as "information of special sensitivity". Treat it as sensitive either way.
- **[LAWYER]** The controller/processor split between us, the organizer and the employer.
- **[LAWYER]** Whether a database registration or DPO obligation is triggered.
- **[LAWYER]** Whether we fall under Information Security Regulations (2017) at the basic level.

**Fair hiring (Equal Employment Opportunities Law 1988):**
- No filters on protected attributes. The structured guide (section 4) is mandatory. Every hiring manager signs a one-page code and gets a 20-minute briefing.
- Same core questions for every candidate for the same role. Notes go into the template only.
- An accessible Coffee corner, which the Equal Rights for Persons with Disabilities law requires.
- **[LAWYER]** Whether running intros, even unpaid, makes us a "private employment agency" that needs a license under the Employment Service Law. This is why there's no success fee.
- **[LAWYER]** Our exposure if an employer discriminates during a meeting we facilitated.

## 4. "Hallway Coffee": 15-minute intro guide for hiring managers

**Structure**
- **0–2 min, you:** your name and role, what the team builds, the role, the band, and that this is a conversation, not an interview.
- **2–8 min, them:** "What are you working on now?" "What's the most interesting problem you solved this year?" "What would make a move worth it?"
- **8–12 min, role probes:** 2 questions fixed per role, the same for everyone. Example: "How would you debug a latency spike in a service you don't own?"
- **12–15 min, logistics and next step:** notice period, work mode, salary expectation, and their questions.

**Allowed:** skills, experience, motivation, salary *expectations*, notice period, "Is hybrid 3 days in Herzliya workable?", "Are you authorized to work in Israel?", clearance *only* if the role legally requires it.

**Forbidden:**
- Age or graduation year
- Military unit or service history (it's a proxy). If the candidate brings it up, don't follow up on it
- **Reserve duty**, past or expected
- Pregnancy, children, family plans, marital status
- Religion or observance (state the schedule instead: "Can you work this schedule?")
- Where they live (ask about commute or work mode instead)
- Health
- Their current employer's confidential details
- Any promise of an offer or a specific salary

**Next-step script**
- Go: "I'd like you to meet [name] for a 45-minute technical conversation. Let's book it now: Tuesday 10:00 or Wednesday 16:00? You'll get a WhatsApp confirmation within the hour. If you don't hear from us in 48 hours, message me directly."
- Not a fit: "Honestly, this role needs [job-related requirement], so I don't think it's the right match. Can I keep your card for [other role], or would you prefer we delete it?"
- Never say "we'll be in touch" without a date.

**Logging (within 5 minutes, in the template)**
- Role
- A 1–4 score on the 3 predefined role criteria, with one line of evidence each
- Decision: booked / hold / no, with a job-related reason
- **Banned words:** "culture fit," "young," "energetic," appearance, accent, "overqualified." Write every note as if the candidate will read it, because under the privacy law they can.

## 5. The candidate knock card: exactly 5 fields

| # | Field | Why |
|---|---|---|
| 1 | **Target role + seniority** ("Backend, senior, 6 yrs") | It's the only thing a recruiter filters on first |
| 2 | **Top 3 skills, each with one proof line** ("Kafka: 10M events/day pipeline") | Substance over pedigree, and harder to fake than a keyword list |
| 3 | **What I'm looking for**, ≤140 characters | Shows motivation, filters out tourists, and the hiring manager opens the coffee with it |
| 4 | **Notice period + work mode/region** | Kills deal-breakers before anyone walks to the corner |
| 5 | **Salary expectation range** (gross monthly ₪), shown to the company only as "within / above your band" | It mirrors the required company band and protects negotiation |

**Deliberately excluded:** name, photo, current employer, education, army unit, age. Name and LinkedIn are revealed only after the candidate accepts. The rest are never shown.

## 6. Customer discovery: 10 TA-leader interviews

**Who to interview:** 4 scale-ups that already sponsor events, 3 multinational R&D centers, 2 startups under 50 people, and 1 agency (to understand the competitive view). Don't pitch until question 9.

1. Tell me about the last conference you attended as a company. What did it cost all-in, and what came out of it?
2. How do you report event ROI to your CFO today? What did you say last time?
3. Which 3 roles are hardest for you to fill right now, and why?
4. When did you last hire someone you first met in person? What happened?
5. What do you do with leads in the week after an event? Where do they end up?
6. Would your hiring managers give 90 minutes at a conference? What would make them say no?
7. What would you need to see 48 hours before an event to send someone?
8. Candidate-initiated knocks only versus anonymous invites: how would each change your interest?
9. *(Show the concept.)* What's the price at which this is a no-brainer, the price where you'd need approval, and the price where you'd say no? Which budget line does it come from, and who signs?
10. What would worry your legal team or DPO? Do you have a policy on in-person screening?
11. Which ATS do you use, and is a CSV with consent good enough?
12. What would make you *not* renew after one event?
13. **The commitment ask:** "Would you prepay ₪3,500 for DevOpsDays TLV, credited if you get fewer than 5 intros?" Record yes, no, or "I need X".
