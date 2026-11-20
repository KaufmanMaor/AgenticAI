# Round 1: PM View. From "two bots close the deal" to a deal-rescue desk

**My thesis in one line:** Omri imagines a consumer agent per side that "closes it between them." I would reverse both halves of that. **Our first user is the buyer's *agent*, not the buyer.** The product is **not autonomous at the moment it commits**: it does the analysis, drafting and back-and-forth prep, and a licensed human taps "send." We start at the one moment where deals blow up, the Texas option-period repair fight, and earn the right to agent-to-agent later.

Why: only 7% of consumers would let AI negotiate, 88% of buyers already have a human agent, and in Texas negotiating for someone else for pay is brokerage (a Class A misdemeanor without a license). The buyer's agent, though, is paid only if the deal closes, and 15-22% of Texas contracts die, mostly over inspection repairs. That pain is real money, it lands on one person, and that person can legally use the tool.

## 1. Segments and the "hair on fire" user

| Segment | Pain | Will pay? | Priority |
|---|---|---|---|
| **Buyer's agent on an Austin team (10-30 closings a year)** | A cancelled contract costs about $10K of GCI (2.4% x ~$420K). Juggles 3-6 option clocks at once. Repair fights eat nights. | Yes: per-seat SaaS, or the team lead pays. | **Primary** |
| Team lead / small Austin brokerage | Fall-through rate and agent burnout; wants a consistent "negotiation playbook" | Yes, buys the seats | Buyer & channel |
| Listing agent | Same deal-death pain from the other side | Later | **Phase 2** (gives us real agent-to-agent, across two brokerages, not intermediary) |
| Home buyer (represented) | Doesn't know what to ask for, and the stakes are scary | Won't pay a fee (Homa sets the price at "rebate") | Beneficiary, and the one who sees our report |
| Self-represented buyer / FSBO seller | Has no one negotiating at all | Maybe, but the segment is small and legally grey | Not now |
| AI brokerages (Homa etc.) | Their own licensed humans negotiate every deal | Could license our engine | Partner or competitor; watch |

**Primary persona: "Jake", a buyer's agent on a 7-agent Austin team.** 18 closings last year, and 3 more contracts died in the option period: about $30K gone. He gets a 70-page inspection report at 9pm on day 3 of a 7-day option period, with a first-time buyer panicking about "foundation" and a listing agent who answers in 24 hours. He is a decent negotiator. What he lacks is time, cost data and a calm structure.

## 2. Core jobs to be done

- **Jake:** "When the inspection report lands, turn it into a defensible ask the seller is likely to accept, before my option clock runs out, without me losing my client's trust or my evening."
- **Buyer (Maya, first-time, $450K in Round Rock):** "Tell me what actually matters in this report, what it costs, and whether I'm getting a fair deal, so I don't overpay or walk away from a good house over nothing."
- The unit of value is **a contract file that survives the option period with a good outcome for the buyer**, not "a negotiation won."

## 3. End-to-end journey: Maya buys in Austin (where the agent acts)

| Stage (TREC context) | What our agent does | Who approves |
|---|---|---|
| **Offer** (One to Four Family contract; Third Party Financing addendum) | Pulls comps and DOM, models the seller's likely priorities (time on market, price cuts, whether they've already bought elsewhere). Proposes a *package*, not a price: for example $8K toward a rate buy-down instead of a $15K price cut, 7 option days, a $300 option fee, flexible closing date. Drafts the offer email to the listing agent. | Jake and Maya approve the terms; Jake sends. |
| **Option period** (inspection, then the Amendment, TREC 39) **= MVP core** | Parses the inspection PDF and triages it into *must / ask / ignore*. Attaches Austin cost ranges (with contractor bids requested automatically). Recommends credit vs. repair (usually a credit: fast, no lender issues, buyer controls quality). Drafts the Amendment plus a short "why this is fair" note for the seller. Reads the counter and proposes trades ("drop the HVAC ask, keep the $6K roof credit, offer a 5-day earlier close"). Runs the option-deadline countdown. | Every outbound counter: Jake one-tap. The walk-away / extension decision: Maya. |
| **Appraisal gap** (financing / appraisal addenda) | When the appraisal comes in $12K short, models the splits (seller cuts, buyer covers, split 50/50, buyer drops a credit). Shows Maya her cash-to-close under each option and drafts the proposal. | Maya picks the range; Jake sends. |
| **Closing date / leaseback** (Seller's Temporary Residential Lease) | Spots that the seller needs 3 weeks after closing and prices it: a free 14-day leaseback in exchange for keeping the full repair credit. | Maya and Jake. |
| **After** | Deal summary for Maya ("$11.4K in credits, closed on time, 2.6% under list"). Outcome logging feeds our playbook data. | n/a |

## 4. MVP scope (Austin only, option period first, 90 days)

**Autonomous (no approval needed):** inspection parsing and triage; cost estimates; deadline tracking and alerts; drafting the Amendment and messages; summarizing the listing agent's replies; requesting contractor quotes; a client-facing explainer for Maya.
**Needs human approval, every time:** any message to the counterparty, any number, any form sent, any extension or termination. Floors and ceilings (the most Maya will give up, her walk-away credit) are **enforced in code, not in the prompt**: the system cannot draft past them, and the model never sees them as text it could leak.
**Out of MVP:** talking to the counterparty on its own, seller-side product, the offer stage beyond a "package suggestion," any state other than Texas, consumer sign-up.
**Phase 2 (after ~200 files):** a pre-authorized "negotiation envelope" per file (Jake approves a range once and the agent trades inside it); a listing-side product; agent-to-agent between two *different* brokerages.

## 5. North-star metric and guardrails

**North star: option-period survival rate of files on the platform** (contracts that exit the option period still alive), compared with the agent's own trailing 12-month baseline. Target: cut option-period cancellations by a third.

| Guardrail | Threshold |
|---|---|
| Buyer net value (credits + price cuts, as % of price) | Not below the agent's baseline. We are not "closing at any cost" for an agent who is paid on close. |
| Code-enforced floor breaches / unapproved sends | **Zero**. Any one is a P0 incident. |
| Missed option deadlines on platform files | Zero |
| Draft accepted with light edits | >60% (otherwise we are a toy) |
| Listing-agent complaints ("talking to a bot") | Tracked per file; <5% |
| Buyer post-close CSAT | >= 4.5/5 |

## 6. The three riskiest assumptions and the cheapest test for each

| # | Assumption | Cheapest test (2-4 weeks) |
|---|---|---|
| 1 | **Buyer's agents will let software shape the very thing they say is their value: negotiation.** | Concierge: recruit 10 Austin buyer's agents and run their next 20 live option periods "Wizard-of-Oz" (an LLM plus one of us), free. Measure the share of drafts sent with light edits and whether they ask to pay for the next file. |
| 2 | **Our output beats the agent's own outcome** (more credits, fewer deaths). | Replay: get 50 past files (inspection report + final Amendment + outcome, closed and cancelled) from one friendly team. Generate our ask blind, then have 3 brokers rate ours vs. the real one. |
| 3 | **Licensee-approved drafting sold as per-seat SaaS is not unlicensed brokerage** (and no fee tied to closing, which §1101.651 could treat as paying for broker acts). | A ~$3K opinion memo from a Texas real-estate attorney, plus an informal question to TREC. Decide pricing *after* the memo. |

## 7. Where I disagree with the research

- **"Become a licensed brokerage (the Homa model)."** No. That puts us against Homa's 2% rebate with a ~$7K-per-closing CAC, in a category whose graveyard includes Reali and Redfin's losses. Selling tools to licensees is legally cleaner, cheaper to distribute (teams buy seats), and the agents become our channel instead of our enemy.
- **Agent-to-agent isn't dead, it's just Phase 2.** The research reads the two-sided vision as a legal dead end. It is a dead end *inside one company* (intermediary rules). Across two brokerages, each with its own licensed principal using our tool, it is a network effect: once both sides of an Austin deal run on us, the counter cycle drops from days to hours. That is the moat the research says we lack.
- **"Stronger model wins" is a fairness problem for a two-sided platform, but for a one-sided tool it's the sales pitch.** We should disclose that the agent used AI and never sell the same file's other side.
- **Pricing:** the research suggests a $1-5K consumer success fee. I'd price per seat (~$149-249 per agent per month) or per file, never per closing, until the attorney says otherwise.
- **The research frames the wedge as "repairs."** The real job is a **deadline**: the option clock. That is our hook, our notification and our retention loop.

## 8. Open questions for other roles

- **Marketing:** Do we lead with "save your deals" (agent pain) or "get your clients more" (pride)? Will Austin team leads share their fall-through numbers in public? How do we stop "AI negotiator" from scaring Maya when Jake tells her?
- **BizDev:** Which 3 Austin teams (20+ agents) can we sign for the concierge pilot? Are inspectors (reports arrive via them) or lenders (appraisal gap) a cheaper channel than teams? Is Homa a licensing partner or a threat?
- **Tech:** Can we parse the main Austin inspection-report formats (Spectora, HomeGauge) reliably? Austin repair-cost data source? How do we keep floors outside the model's context, and keep an audit log the broker can defend?
- **Texas Broker:** How do listing agents really decide on repair asks (seller emotion, their own DOM)? Would you let a junior agent use this unsupervised? What does a TREC 39 Amendment negotiation look like on day 5 of 7, in reality?
- **RE Attorney:** Where is the line between "drafting tool for a licensee" and "negotiating for another" under §1101.002? Is per-file pricing OK, and is any closing-linked fee? Who is liable when the agent misstates a cost estimate that the buyer relies on (Moffatt v. Air Canada)? Do we have to disclose AI use to the counterparty?
