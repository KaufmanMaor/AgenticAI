# Round 2: Head of BizDev stress-tests Concept v2

**Bottom line:** I accept doing the tool first. I reject getting the license only after the tool proves out. We should start the Texas broker-of-record and entity license in month 0, alongside the Option Desk concierge, so the file-30 gate decides which line to scale rather than whether we may start the brokerage at all. Doing both in parallel saves about 4 months and about $300K on the way to the first $250K of revenue. It also removes a licensing risk that v2 creates in its own concierge phase. All numbers are my assumptions unless noted, on the same base as Round 1: a $430K Austin home, a 2.4% buyer side ($10.3K), and ~21K Austin option-period negotiations a year.

## 1. The three biggest flaws in v2

1. **The free inspection tool can't feed Punchlist Realty.** Whoever uploads an inspection report is already under contract, and 88% of them already have an agent, who is named on a TREC buyer agreement. That buyer can't switch to our brokerage mid-deal. So the tool's leads only pay off for A on that person's *next* purchase, years away, or from the ~10% who are unrepresented. **Fix:** make the tool feed B instead. The buyer sees the priced ask list, then a "Send this to your agent" button that invites the agent onto Option Desk. That gives buyer-led agent acquisition at close to $0 CAC. A needs its own pre-search channels: relocation, builders, and first-time-buyer content.
2. **The concierge as written is a §1101.651 risk.** A "human negotiation expert" who drafts the counters behind the scenes, paid through a $249 fee, looks like an unlicensed person being paid for broker acts. **Fix:** the expert must hold a Texas license under our own broker of record, or the concierge files must be free. That alone is a reason to license in month 0, not month 6.
3. **Phase 1 creates a channel conflict, and the gate measures the wrong thing for Phase 2.** The Austin buyer agents who pay us and train our models in Phase 1 then face Punchlist Realty as a competitor in Phase 2. They will notice, and they will churn and talk. Meanwhile the gate (≥$3K, or +5 points of survival, against a "blind replay" that won't convince anyone) tests whether the *tool* creates value. It says nothing about whether *A* can win buyers away from Homa at a CAC under $1.5K, and that is the risk that actually decides A. **Fix:** (a) hold Phase 1 sales to teams outside our Phase 2 buyer channels, tell design partners upfront that we plan a brokerage, and give them a referral split on any of their buyers we serve; (b) add the commercial gates in §3.

## 2. Tension #2: go straight to the brokerage or not (path to the first $250K of revenue)

| | **Path 1: v2 (B first, license after the gate)** | **Path 2: license now, run both lines (my call)** | **Path 3: B only** |
|---|---|---|---|
| Months 0-2 | Recruit 10 agents; concierge files 1-10 free | Same, plus broker-of-record co-founder, TREC entity license, E&O with an AI endorsement, ABoR/MLS (~$25-35K one-off) | Same as Path 1 |
| Months 2-5 | Files 11-30 at $249; 12-week build starts | Concierge also runs on our own buyer clients (relocation/builder pilots), so buyer agreements start signing in month 2 | Build |
| Gate | Month ~5 | Month ~5. Picks which line to scale | Month ~5 |
| First A closing | Month ~9-10 (license setup plus a 60-90 day contract cycle) | **Month ~5** | Never |
| $250K reached via | ~42 A closings at $6K net, plus B fees | ~35 A closings plus ~120 B files | **~1,000 files** at $249, about 5% of every Austin option period |
| **Time to $250K** | **~15-16 months** | **~11-12 months** | ~20 months (needs ~150 active agents) |
| **Burn to $250K** | **~$1.3M** | **~$1.0M** | ~$1.8M |
| Downside if the gate fails | ~$0.4M lost, clean pivot | ~$0.45M lost, plus a license we can wind down cheaply | n/a |

Burn assumes a ~$85-110K/month team (2 founders, 3 engineers from month 3, a licensed negotiator, part-time legal) and A's CAC at $2.5K. **The concierge itself is cheap:** 20 files × (~6 expert hours at $100 + $40 inference + $100 to source a repair bid) ≈ **$15K direct**, or ~$25K with recruiting and the attorney's opinion memo. Its real cost is the **5 months of calendar time** it consumes if the license waits behind it. Path 2 costs only ~$50K more if we're wrong, and it gets us to the first $250K **4 months sooner and ~$300K cheaper** if we're right.

## 3. Phase 1 pilot economics

- **Is $249 right? Yes, as the list price.** The broker accepts $150-300 per file. The value to the agent: +5 points of survival × ~$10.8K of GCI at stake ≈ $540, plus 4-6 hours saved (~$400), so ~$900 per file. $249 is ~28% of that, which is fine.
- **Are files 1-20 free? Only 1-10.** Files 1-10 are free design-partner files, which also removes the §1101.651 issue during the concierge. Files 11-30 are a **$149 founding price**, refunded if no amendment gets sent. Charging is the only real test of Tension #1. Then $249 list price, or a **team pack of 10 files for $1,990** sold to the team lead (the person who feels fall-throughs across the team).
- **Per-file margin:** concierge ≈ -$600 (human-heavy, which is fine as research spend). After the build: $249 - $40 inference - ~$40 for 30 minutes of human QA ≈ **$170 (68%)**.
- **Commercial gates to add at file 30:** ≥60% of design partners pay for their third file; listing agents engage (reply within 24h) with ≥70% of AI-assisted counters; and for A, ≥100 waitlisted buyers from relocation or builder channels at ≤$1.5K expected CAC.

## 4. Tension #7: an agent-to-agent pilot with iBuyers and builders

- **Is it real?** Half of it is. **Builders aren't API-ready, and new homes have no option-period repair fight.** There the negotiation is incentive allocation (rate buydown vs. price cut vs. upgrades vs. closing costs), which suits three-package offers. **iBuyers are the true agent-to-agent fit:** they're institutional, repeat sellers with algorithmic pricing and standard concession policies, which is the Pactum/Walmart pattern. But their Austin resale volume is small (unverified, likely a few hundred homes a year), and they gain nothing from an API that helps buyers extract more.
- **The pitch is about holding cost, not concessions:** "Every cancelled resale costs you ~30-45 days of carry (~$2.5-4K at $430K) plus relisting. We send structured, priced asks that already fit your concession policy, as machine-readable terms. Your engine answers in hours, not days. You pay nothing. We measure the change in your option-period fall-through."
- **Who:** the **Opendoor** brokerage and Key Agent product team (it already has a Texas brokerage); **Offerpad** (HENRY's AI inspection estimates make it the natural counterpart for repair pricing); **Lennar** through its LenX venture and innovation arm (doubles as a strategic investor); **Taylor Morrison** (an online-reservation buying flow, so the most digital-ready); **Perry Homes and D.R. Horton** Austin divisions for spec-inventory incentives.
- **Sequencing:** open conversations in **month 3**, aim for an LOI or design-partner letter by **month 6** (a big fundraising asset), run the pilot as **structured-email-to-their-team** in months 6-12, and move to a real API in year 2. It deserves an earlier *slot*, not earlier *engineering*.

## 5. The fundraising angle

**What a seed investor must believe:**
1. AI-prepared option-period negotiation **saves deals measurably** (≥5 points of survival, or ≥$3K per file). We prove this in 30 files.
2. A licensed AI-first brokerage can **acquire buyers at ≤$1.5K before they search**, through relocation and builder channels, and win against Homa's 2% rebate on outcome, not on price.
3. **TREC forms are statewide**, so Austin replicates to DFW, Houston and San Antonio with no form rework (Texas buyer-side commissions are ~$2.7B a year).
4. **Priced outcome data compounds** into a pricing index and a listing-agent response graph that rebate shops don't have.

**Comparables:** Homa (~$3-5M seed, Quiet Capital, live in Austin with a 2% rebate), **Indigo ($8M seed, "AI offer negotiation")**, Ridley ($6.4M, Fifth Wall), HouseWhisper (~$10M seed), Breezy ($10M pre-seed), and Pactum (>$100M raised, which is proof that autonomous negotiation commands a premium). **The raise:** a ~$750K-1M pre-seed now (concierge, license, first 20 closings), then a **$3-4M seed after the gate**. Targets: Fifth Wall, MetaProp, Moderne Ventures, Zigg Capital, Navitas, Quiet Capital, and LenX as a strategic. **The story: "the deal-rescue layer for Texas real estate, with a brokerage on top."**

## 6. Tension #6: the moat at 24 months (ranked honestly)

1. **Priced outcome data.** For each finding: what was asked, what was accepted, credit vs. repair, and the ratio, broken down by listing agent and listing brokerage. At ~1,000 files plus ~200 closings a year (~5% of Austin option periods), it's enough for a defensible local index. **It's only a moat if we own it:** every Option Desk contract must grant us rights to anonymized outcome data.
2. **Trust credentials:** our own license, an AI-endorsed E&O policy, a record of zero limit breaches, and published "Negotiation Replays." Slow to copy, and it's what lets brokerages, insurers and iBuyers sign with us.
3. **Channel lock-in:** inspector co-branding (flat RESPA-safe fees) and team packs.
4. **The protocol:** worth **nothing at 24 months** unless an iBuyer joins. It's a year-3 option, not a moat.

Homa, KW Command or Compass can copy the *feature* in a quarter. What they can't copy quickly is a year of Austin outcome data from both lines. That is the strongest argument for B, and I'm adding it to my Round 1 case.

## 7. What I now accept and reject

- **Accept:** representing the buyer only; bot-to-human under a named licensee; the option-period wedge; limits enforced in code; "deals saved" as the north star (it matches how agents are paid, which makes B easier to sell); a fixed per-file fee; B as a real line, not just research, because it's our low-CAC data engine.
- **Accept, revised from my Round 1:** the free inspection tool feeds **B, not A**. And the "1% + guarantee" offer launches only once partner channels bring CAC to ≤$1.5K.
- **Reject:** licensing only after the gate (do it in month 0); a concierge run by an unlicensed expert charging $249; selling Option Desk to Austin teams without disclosing the brokerage plan; a gate with no commercial criteria; engineering the iBuyer API before month 9.
