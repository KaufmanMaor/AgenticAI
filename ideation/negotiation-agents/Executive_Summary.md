# Option Desk: Executive Summary

*Idea source: Omri Bitan ("AI agents that negotiate real-estate deals for you"). Research plus 3 rounds with PM, Marketing, BizDev, CTO, an Austin broker and a Texas RE attorney. US only. Nov 2026.*

## Bottom line: YES, but not the original version
All six roles signed off (with conditions): worth a founder's next 12 months as a **16-week, ~$50–150K kill-or-continue bet**.

**The original idea doesn't survive.** In it, each side has an AI agent and the two close the deal between them. It fails for four reasons:
- In Texas, negotiating for someone else for a fee is **licensed brokerage**. Doing it unlicensed is a criminal misdemeanor.
- If both agents sit under one company, the deal becomes a Texas "intermediary" transaction. That requires written consent from both sides and walls between them.
- **The stronger model wins**, and the losing side doesn't notice (Anthropic's Project Deal).
- The counterparty is a human listing agent, not a bot.

## The refined idea: Option Desk
A back office for **Texas buyer agents**, focused on the moment deals die: **the option period after the home inspection**.
- **What the agent gets:** upload the inspection report and get back the same evening:
  - a priced repair-ask list;
  - one recommended ask plus 1–2 alternatives;
  - a call script;
  - a ready TREC 39 amendment (the standard Texas repair amendment form);
  - a deadline clock.
- **Who does what:** the AI drafts, the licensed agent sends under their own name (labeled AI-assisted), and only the principals sign. The buyer's walk-away limits are enforced in code, never in the prompt.
- **Structure:** a Texas broker as co-founder, a licensed company serving brokers business-to-business, and **$249 per file**, flat and never tied to closing.
- **Omri's agent-to-agent vision** survives as a later protocol across brokerages, probed first with iBuyers (Opendoor/Offerpad) for a letter of intent by month 6.

## Market
| | Figure |
|---|---|
| US existing-home sales | ~4.06M/yr (2024–25, a 30-year low) + ~0.65M new homes |
| Median price | ~$414K |
| Buyer-agent commission | ~2.4% (post-NAR settlement) |
| **US buyer-side commissions (TAM)** | **~$45B/yr** |
| Texas buyer-side commissions | ~$2.7B/yr (335K sales) |
| Austin buyer-side commissions | ~$280M/yr (~27K closings) |
| Contracts cancelled | ~15% US, 17–22% in Texas metros, mostly over inspection/repair disputes |
| Sales with seller concessions | ~46% (Austin: $5–15K typical) |
| Buyers represented by an agent | ~88%, which is why we sell to agents, not consumers |
| Commission lost by an agent per dead deal | ~$10.8K |

**Option Desk's addressable volume** (inspection/option-period negotiations):

| Market | Files/yr | Revenue at 100% ($249/file) | Realistic share | ARR |
|---|---|---|---|---|
| Austin | ~21K | ~$5M | ~15–35% | **~$0.8–1.8M** |
| Texas | ~250K | ~$62M | 10–20% | **~$6–12M** |
| US (state-by-state rework) | ~3.2M | ~$800M | ~5% | **~$40M** |

## Revenue potential
- **Core product (per-file SaaS):** ~$2.6K per agent per year, ~85% gross margin. Austin reaches about $1–2M ARR. Texas-wide reaches $6–12M ARR by about years 3–4. A US rollout is roughly a $40M ARR ceiling. **That is a good business, but not venture-scale on its own.**
- **The venture case needs the expansion path:**
  - appraisal-gap and listing-side files;
  - enterprise licenses ($5–15K per brokerage office);
  - a priced-outcome data product for iBuyers, lenders and insurers;
  - a month-12 decision between **(A)** our own AI-first buyer brokerage (~$6K net per deal, ~59% gross margin, ~$1.6M revenue at 1% of Austin, separate metro and brand) and **(B)** the iBuyer agent-to-agent protocol.
- **Capital:** a $0.75–1M pre-seed now, then a $3–4M seed after the gate. Comparable seed rounds: Indigo $8M, Homa $3–5M.

## Competition
- **Homa:** a licensed AI buyer brokerage. Launched in Austin and Texas in June 2026 and rebates about 2% of the price to the buyer.
- **Indigo:** an AI offer platform.
- **Final Offer:** live counteroffers, sold through Keller Williams in Texas.
- **Pactum:** proves autonomous negotiation works in business-to-business purchasing.
- **Zillow, Compass, KW:** have AI products, but Zillow says negotiation stays with humans.
- **The gap:** **no one owns AI-run repair and option-period negotiation.** The risk is that an incumbent copies the feature. **The moat** is data on which asks get accepted, at what price, by which kind of listing agent.

## The test (16 weeks)
1. **Weeks 0–3:**
   - sign the broker co-founder;
   - get a ~$3K attorney memo on the legal structure;
   - build an Austin contractor price book;
   - check our simulator against 15 past files.
2. **Weeks 2–5:** pre-sell a **refundable 3-file pack at $399** to 15–20 Austin agents. **Fewer than 4 buyers → stop.**
3. **Weeks 4–15:** 30 live files, handled by hand under the licensed broker.
4. **Week 16 gate:**
   - ≥ $3K average value per file above the agent's own track record;
   - ≥ 60% of agents buy again;
   - ≥ 70% of drafts are sent with light edits;
   - deal fall-through does not rise.

**Biggest risk:** agents may like the drafts but not route live, high-stress files to us, or not pay repeatedly, since an option period comes about once a month per agent.
