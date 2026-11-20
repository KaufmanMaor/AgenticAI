# Round 2: PM stress-test of Concept v2 (Punchlist / Option Desk)

**Verdict:** v2 gets the product right: buyer side only, bot-to-human, option period, code holds the money. It gets the **sequencing and the proof** wrong. Its gate can't be measured at 30 files, its pilot may itself be unlicensed brokerage, and the Phase 2 brokerage turns our first customers into our competitors.

## 1. The 3 biggest flaws in v2

| # | Flaw | Why it matters | Fix |
|---|---|---|---|
| 1 | **The gate can't be measured.** "≥5 points better option-period survival" at file 30. | If 10-12% of files die in the option period, 30 files means about 3 deaths. Detecting 12% → 7% with 80% power needs roughly 400+ files per arm. Second, "net value vs. the seller's first response" is a baseline we control: a lowball first ask inflates our win. | Gate on **paired incremental value against a sealed agent draft** (§3) plus behaviour (do they pay). Survival stays the north star at scale and a *safety check* in the pilot, never a gate. |
| 2 | **Phase 2 brokerage = channel conflict.** | We recruit Austin buyer agents, learn from their files, then launch "Punchlist Realty, 1% back" to take their buyers. Austin agent Facebook groups will notice by month 7. The Option Desk "licensing line" dies the day the brokerage launches. | Decide the brokerage at **month 9-12, on retention data**, not at file 30. If we go to market as a brokerage, Option Desk is sold only outside Austin, under a different brand. My default stays B2B (seats/files, team and brokerage contracts). |
| 3 | **The Wizard-of-Oz concierge may itself be unlicensed brokerage.** | The attorney is clear that "the company is the actor": an unlicensed "negotiation expert" shaping counters for a $249 fee is attempting to negotiate for another. Doing it on day 1 of a product built on compliance is the worst possible start. | The pilot is **free**. The behind-the-scenes expert is our **Texas broker of record**, or works under them. Outputs are *drafts the agent adopts*. We charge only once the attorney memo clears the per-file model. |

Smaller issues:
- The variable "rebate rises to 2%" guarantee likely needs TREC advertising review.
- "Three equal-value packages" requires a seller-utility guess. Label them "options," not "equal."

## 2. Positions on the tensions

- **#1 Will agents pay $249?** Yes, if it is framed as **"save the deal, save your night,"** never "negotiate better." $249 against ~$10.8K of commission at risk is an easy ROI. The real barrier is ego and habit, not price. Hence: first 2 files free, $249 from file 3, and the **team lead buys** (it becomes a team standard, not an admission). Pay rate on file 3 is the real test.
- **#2 Real business or research step?** Both. Don't skip ahead. Math: 15 buyer sides/yr × 70% use × $249 ≈ $2.6K per agent-year. 700 Austin agents ≈ $1.8M ARR, and Texas metros ×5. Small, but real, high-margin, and the only way to collect outcome data without a $2.5K CAC per buyer. KW Command can copy the UI. It can't copy 2,000 priced asks with known acceptance outcomes. The brokerage is an *option* we earn, not the plan.
- **#5 Measurement:** a three-layer method (§3):
  1. Blind replay of past files, judged by a panel.
  2. Live **sealed-draft** comparison: the agent writes their own ask *before* seeing ours.
  3. Behaviour: drafts sent, repeat use, paying.
  We publish the method, framed as "agent + AI vs. agent alone."
- **#7 Agent-to-agent with iBuyers/builders earlier?** **Probe, don't build.** Builders rarely renegotiate repairs (new build, warranty), so it's the wrong moment. Opendoor/Offerpad resales are the right counterparty: standardized repair portals, policy-driven sellers, high volume in Austin. Action: one BizDev conversation and a signed LOI for a "structured repair-request API" by month 6. No engineering until there is an LOI.

## 3. The 20-file concierge pilot (8 weeks)

**Recruiting (weeks -2 to 0).**
- **Funnel:** about 30 conversations → 10 agents.
- **Criteria:**
  - Austin metro, 8-25 buyer sides a year.
  - At least 1 option-period death in the last 12 months.
  - Willing to share **5 past files** each: inspection report, final TREC 39, outcome, and if possible the repair invoices.
  - A mix of 6 solo and 4 small-team agents.
- **Channels:** the broker's network, 2 team leads, and 3-4 Austin inspectors who see the pain first. No ads.
- **Incentive:** a free pilot and $50 per past file shared.
- **Legal prerequisites:**
  - AI-use consent addendum for each buyer.
  - "AI-drafted, reviewed by [licensee, license #]" footer on every message.
  - Attorney memo commissioned.

| Week | Work | Output |
|---|---|---|
| -2 to 0 | Recruit; attorney memo; consent addendum; sealed-draft form; cost table v0 | 10 signed agents |
| 1 | Collect the 50 past files. Redact them. Reconstruct buyer preferences from the agents' notes as of inspection day. | Replay set |
| 2 | **Blind replay.** For each file we generate an ask from the inspection report + listing data only. A panel of 3 Austin listing agents *outside* the pilot sees ours and the real ask in random order, unlabeled. They score: (a) chance the seller accepts without termination (1-5), (b) buyer $ value, (c) "would I engage with this?" | Replay baseline |
| 3-7 | **Live files** (about 4/week; 10 agents × ~1 option period every 2 weeks). For each file the agent submits a **sealed draft ask** (5 min) before seeing ours, then chooses, edits and sends. We log: hours from inspection to amendment, number of rounds, final concessions, listing-agent response time, edits, survival, and expert minutes per file. | 20 files |
| 8 | Readout; file-3 pay ask; agent interviews | Gate decision |

**Gate math (at file 20, not 30):**
- For each agent, compute their historical **realization ratio** from the past files: final concession ÷ initial ask. Say 65%.
- Expected outcome without us = sealed ask × that ratio. Incremental value = our final concession − that expected value.
  - Example: sealed ask $6K × 0.65 = $3.9K expected. We got $7.2K. Increment = **+$3.3K**.
- If the per-file standard deviation is about $4K, n = 20 gives a standard error of about $900. **Pass requires a mean ≥ $3K and a 90% CI lower bound ≥ $1.5K.**
- Plus all of these:
  - Replay: ours preferred in ≥ 65% of pairs, with acceptance score not lower.
  - ≥ 60% of drafts sent with light edits.
  - Median inspection-to-amendment ≤ 24h.
  - ≥ 6 of 10 agents pay $249 for file 3.
  - ≤ 1 option-period death where the panel judges our ask a contributing cause.
  - Expert time ≤ 90 min per file, and falling.

## 4. Top 8 v1 user stories (priority order)

1. **As a buyer agent,** I upload the inspection PDF and within 15 min get a triaged must/ask/drop list with Austin cost ranges, with "get a bid" on foundation, roof and sewer.
2. **As a buyer agent,** I text my buyer a 5-min preference link, and their walk-away and priorities are locked in code. Neither I nor the model can draft past them without the buyer's re-approval.
3. **As a buyer agent,** I get 3 seller-choice options plus a one-page summary with bids attached that I can send in under 10 minutes.
4. **As a buyer agent,** approved terms become a TREC 39 amendment, generated by code and sent by DocuSign or email under my name with the AI footer.
5. **As a buyer agent,** I see the option clock and get alerts 48h, 24h and 6h before the deadline. A prefilled termination notice is ready if we're stuck.
6. **As a buyer agent,** I forward the listing agent's counter and get it parsed, plus a next move inside the buyer's bounds and a **"call script"**: the one question to ask the listing agent off the record. The broker is right that the phone call is where the $8K lives.
7. **As a buyer,** I get a plain-English page: what in the report matters, what each option means for my cash to close, and an approve button.
8. **As a broker of record,** I see an approval queue and an immutable audit log of every draft, edit and send.

Not in v1: offer packages, appraisal gap (v1.1, since it reuses the counter engine), leaseback pricing, SMS sending.

## 5. Kill criteria (any one triggers a stop or pivot)

- Replay: ours preferred in < 55% of pairs, or a lower acceptance score. → Kill the negotiation thesis; at most a coaching tool.
- Live incremental value: 90% CI lower bound < $0 at file 20.
- < 4 of 10 agents pay for file 3, *and* no team lead will buy seats.
- Listing agents punish AI-labeled asks: median response time 2× the agent's baseline, or ≥ 2 deaths attributed to our ask.
- Any unapproved send or reservation-price leak in the pilot. → Stop the pilot and redesign.
- The attorney memo says per-file SaaS is still brokerage, with no workable structure short of our own license.
- Expert time is stuck above 2h per file at file 20, meaning the product is a services business.

## 6. What I now accept or reject from other roles

**Accept:**
- **Broker:** bot-to-human; the "seller's choice" menu; "deals saved, not dollars"; the off-the-record call stays human, and we arm it (story 6).
- **Tech:** LLM writes the messages, code holds the money; a quarantined parser; a simulator with known Pareto frontiers for regression tests.
- **Attorney:**
  - "The company is the actor" even for SaaS. This is why the pilot is free and the expert is licensed.
  - Disclosure in every message.
  - AI-consent addendum, E&O cover, deadline escalation.
- **Marketing:** never buy portal leads; publish the benchmark method; "the agent is the hero."

**Reject:**
- **BizDev:** a brokerage now. The $6K/deal is real, but a $2.5K CAC and channel conflict make it the wrong *first* move.
- **Marketing:** the "$1,500 more or $0" guarantee. It is contingent on outcome (§1101.651 risk) and measured against a gameable baseline.
- **Founder:** "net value vs. the seller's first response" as a metric. Replace it with the sealed-draft increment.

**Revising my Round 1 view:** per-file $249 beats a per-seat price. It matches the moment, and agents buy it like an inspection.
