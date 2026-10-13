# Round 1: PM View. From "Hooked for jobs" to a product

**My thesis in one line:** Hiring is public and something companies brag about. Job seeking is private and risky for the person doing it. So the product should make **companies visible and candidates invisible until they choose to show themselves.** The founder pictured a symmetric "see everyone with the opposite intent." That is the single design decision I would reverse. Everything else follows from it.

## 1. Segments and the "hair on fire" user

| Segment | Pain | Will pay? | Priority |
|---|---|---|---|
| **Talent lead at an Israeli scale-up (50–500 people) that is already sponsoring or exhibiting at the conference** | Pays ₪20–80K for a booth, gets swag-hunters and business cards. Can't turn the senior engineers walking past into pipeline. | Yes. Budget already exists in the event line. | **Primary** |
| Employed passive candidate (senior IC) | Curious about the market, but can't be seen looking | Never pays | The supply we must protect |
| Organizer | Wants sponsor ROI and renewals, plus a new revenue line | Takes a rev share | Distribution channel |

**Where I disagree with the research:** "a recruiter in Tel Aviv tech" is too broad. The hair-on-fire user is **the sponsor already in the room who can't prove ROI.** Choosing them solves half the liquidity problem: they are already there, with a booth budget and a renewal decision coming.

**Primary persona: "Dana", Head of Talent at a 200-person cyber scale-up.** 14 open roles, 6 senior. Sponsors 3 conferences a year. Her CFO asks "what did we get from the booth?" and she has no answer.

## 2. Core job to be done

- **Dana:** "When I'm at a conference I already paid for, help me have real conversations with the 10 relevant, qualified people in the room who would never answer my InMail. Then let me prove it to my CFO."
- **Candidate ("Yoni", senior backend engineer, employed):** "When I'm at a conference anyway, let me quietly see which companies here are hiring for my level and salary range. Let me talk to one over coffee, and make sure my boss never finds out."

The unit is **not "first interview on the spot"** but a **15-minute "coffee intro."** "Interview" raises the stakes, adds bias and legal exposure, and scares away passive talent. Real interviews happen after the event.

## 3. End-to-end journey

**Before (T-14 to T-0 days)**
- Organizer sells a Talent Pass on the sponsor order form (one bundled per sponsor package).
- Dana creates up to 5 role cards: title, seniority, **salary band (required)**, stack, slot windows.
- Organizer emails attendees: "23 companies are hiring at CyberWeek. Browse privately." Yoni builds a 2-minute web profile (LinkedIn or CV import, salary floor) with an **auto-built block list** (current employer and related companies).

**During**
- Yoni taps "I'm curious" on two role cards. **Dana sees nothing until he does.** Then she sees a one-line summary and accepts or declines (double opt-in, candidate moves first).
- On a match: a slot in the **"Coffee Corner"**, a discreet area away from the sponsor hall, with WhatsApp notifications.
- Dana works from a live queue of accepted intros, with a 30-second note per conversation.

**After (T+1 to T+60)**
- Yoni chooses: delete everything (Hooked-style) or keep a private "talent passport."
- Dana gets an **ROI report** (intros, next steps, hires, cost per conversation compared with agency fees). She renews based on it.
- Short outcome surveys at 14, 30 and 60 days for attribution.

## 4. MVP scope (after the concierge pilot)

**IN:** QR-opened web app, role cards with salary band, candidate-initiated double opt-in, automatic employer blocking, WhatsApp notifications, Coffee Corner slot booking, recruiter queue with notes, ROI report, manual organizer admin.

**Explicitly OUT:** swiping, AI scoring of candidates (what the pitch is against, and a legal minefield), native app, video booth, any public "seeker" badge or list, ATS integration (CSV is enough), in-product payments.

**Concierge first, as the research says, but with real money collected in advance from at least 3 sponsors.** A free pilot proves nothing about willingness to pay.

## 5. The "aha moment"

- **Recruiter:** *"By lunch I had 5 senior engineers who chose to come talk to me. Two agreed to onsites, and none of them were from the 'Open to Work' crowd."* The measurable version is 3 or more accepted intros in the first event day.
- **Candidate:** *"I saw 4 companies paying my salary range for my stack, and nobody knew I looked."* The aha comes **before** any meeting: the private browse with salary bands visible. This is why the salary band is required.

## 6. Metrics

**North star: qualified intros that turn into a next step within 14 days, per event.** It captures liquidity, quality and value to the payer in a single number.

Supporting: browse rate → "curious" rate → accept rate → show rate, plus **Talent Pass repurchase rate** (the real business metric).

Guardrails:
- **Discretion incidents = 0.** Any exposure to a candidate's own employer is a P0 and stops the next event.
- At least 70% of seekers see 1 or more relevant role cards.
- Recruiter ghosting under 10%.
- Organizer sponsor-NPS does not drop.

## 7. Liquidity: how to solve it

1. **Supply = sponsors who are already there.** Don't recruit recruiters. Convert exhibitors.
2. **A minimum threshold before launch.** Don't turn on hiring mode at an event with fewer than **8 hiring companies or 25 open roles.** An empty screen is worse than no product.
3. **Remote supply fills gaps:** a company not at the event buys a "remote card" for a 2-hour window. That's the cheap version of the booth idea.
4. **Liquidity is per niche, not per event:** one vertical (Israeli cyber and AI), so the same companies and candidates rotate across 8–10 events a year.
5. **Pre-event browsing** builds demand 2 weeks ahead, so the event day is for converting, not discovering.

## 8. Discretion UX: the principles

- Companies are public, candidates are dark, and the candidate always moves first. Recruiters never see a list.
- Automatic employer blocking from the email domain and a company graph.
- **No physical "seeking" signal:** no colored badges, and the Coffee Corner also hosts ordinary networking, which gives plausible deniability.
- A "panic button" pulls back all interest instantly. Data is deleted within 7 days unless the candidate opts in.

## 9. Two bold / contrarian ideas

1. **"Reverse Booth": companies pitch to candidates.** Each hiring company gets 5 minutes on a "Hiring Lightning Talks" stage. Watching is risk-free ("I just came to the talk"), so it's both top of funnel and discretion cover, and it's a sponsorship product organizers already know how to sell.
2. **Conference attendance as a verified signal ("living CV").** Sessions attended, workshops completed and talks given are signals **an AI can't fake** (see Gartner's fake-candidate trend). The moat isn't the matching app. It's a **cross-event, candidate-owned verified passport** that single-event, organizer-owned tools like Brella and Swapcard can't copy. That answers "easy to build = easy to copy."

(Bonus: shelve the "Speed InterviewDate" video booth for 18 months. It's a hardware and operations cost that solves a problem we don't have yet.)

## 10. Open questions for the other roles

1. **BizDev:** Will organizers allow a competitor of a paying sponsor to hire at the event, or do we need a "sponsors only" tier? And can we get 3 sponsors to **prepay** before the pilot?
2. **HR / Legal:** What is the minimum structure (consent text, retention, a standard question set) that keeps a 15-minute coffee intro outside the "interview" legal risk zone under Israel's Privacy Protection Law (Amendment 13) and anti-discrimination law?
3. **Marketing:** How do we make an employed senior engineer **trust** a brand-new brand with their job-search secret? Should it ship under the organizer's brand (white-label) or our own, and how does the Hooked association help or hurt? (A question for **Tech** that follows from this: can we reliably auto-detect "current employer plus related companies" from a LinkedIn or CV import?)
