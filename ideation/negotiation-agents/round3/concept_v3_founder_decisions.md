# Concept v3: Founder decisions after Round 2

*The team stress-tested v2. These are my rulings. Every open tension is closed or turned into a gate. US only, Texas first.*

## The concept in one paragraph
**Option Desk** is a back office for Texas buyer agents, run under a license, for the moment deals die: the option period after inspection. Within 4 hours of receiving the inspection report, it returns a priced, prioritized ask list, a recommended ask plus 1–2 alternatives, a ready TREC 39 amendment once the seller picks, a call script for the "one more phone call", and a deadline clock that will not let the option expire. The AI drafts, the agent sends under their own name (labeled AI-assisted), and only the principals sign. Omri's "agents negotiating with agents" becomes the long-term protocol, tested first with institutional sellers (iBuyers), not between two consumers.

## Rulings

| # | Tension | Ruling | Driven by |
|---|---|---|---|
| 1 | Brokerage now vs. tool first | **Option Desk is the company for the first 12 months.** The consumer brokerage (Punchlist Realty) is **deferred**. It is decided at month 9–12 on retention data, and if launched it goes **in a different metro, under a separate brand, with a data firewall**, because we won't compete with our own customers. | PM, Broker, Marketing |
| 2 | License | **A Texas broker joins as co-founder and designated broker from month 0** (10–15% equity, compliance veto). The company holds a TREC brokerage license from day 1, for compliance, not retail: the concierge is run **broker-to-broker** by a licensee, and every buyer-facing touch runs under the agent's license. | Attorney, BizDev |
| 3 | Price | List **$249 per file**. Pilot: **first 2 files free per agent, then $149**. A 10-file team pack is $1,990. **Fixed, billed to the sponsoring broker, never to the buyer, never tied to closing** (§1101.651). | Broker, BizDev, Attorney |
| 4 | Framing | "**Your negotiation transaction coordinator**": save the deal, save your night. White-label to the agent. Never "negotiate better than you." | Broker, Marketing |
| 5 | Guarantee | **Dropped.** No guarantee on money, which pays us to nitpick, collides with lender caps and can't be advertised. **We guarantee process: ask list in 4 business hours or the file is free.** We never market "zero missed deadlines." | PM, Broker, Attorney |
| 6 | Packages | **One recommended ask + 1–2 alternatives in one message.** The TREC 39 is drafted only after the seller picks. | Broker, Tech |
| 7 | Disclosure | Every outbound message: *"Prepared with AI-assisted drafting (Option Desk). Reviewed and sent by [Name], TREC #[x]. Non-binding proposal; no agreement until a written amendment is signed by all parties."* | Marketing, Attorney |
| 8 | Gate (file 30) | Baseline = **the agent's own sealed draft ask**, written before seeing ours. **Pass all of:** (a) mean incremental net value ≥ $3K with 95% CI lower bound > $0 (paired); (b) ≥ 70% of our drafts sent with light edits; (c) ≥ 60% of pilot agents pay for a further file; (d) blind replay panel of 3 brokers prefers ours ≥ 65%. Option-period survival is **reported, not gated** (n is too small). | PM, Tech |
| 9 | Cost engine | Price book built with a **paid panel of Austin contractors** (~$3K). Targets: ≥ 70% of priced items inside the contractor range; ≥ 98% recall on structural/safety items; every item cites its report page. Foundation, roof and sewer get "get a bid." | Tech, Broker |
| 10 | Deadline | The licensee **confirms the Effective Date at intake**, plus a named backup approver and a **pre-drafted Notice of Termination**, with escalation at 48h, 24h and 6h. | Tech, Attorney |
| 11 | Safety | Walk-away limits stay out of the model's context. PDFs are rendered to images and OCR'd before parsing, with an outbound leak filter and canaries. We call it "injection-resistant, tested every release," never "safe." | Tech |
| 12 | Liability | Agent ToS: we are a drafting tool. The licensee approves and is negotiator of record, and repair ranges are "estimates, not inspections or valuations." We buy tech E&O plus the brokerage E&O. We accept that DTPA/McCamish exposure can reach us directly, which is why we have the review gates. | Attorney |
| 13 | Consumer tool | **The free consumer "Inspection → Ask List" tool is dropped** (it risks interfering with another broker's client). It is replaced by a **"send to your agent" invite**. | Attorney, BizDev |
| 14 | Moat | **Priced-outcome data** (which asks get accepted, at what price, by which listing-agent type). Every contract grants us anonymized data rights. The protocol is a vision, not a moat. | BizDev, Tech |
| 15 | Agent-to-agent | **A probe, not a build:** pitch Opendoor/Offerpad (and Lennar) on fewer option-period cancellations, aiming for **one signed LOI by month 6**. No engineering until then. | PM, BizDev |
| 16 | Money | **Pre-seed $0.75–1M** now, then a $3–4M seed after the gate. | BizDev |

## Plan
- **Weeks 0–2:** co-founder broker signed, TREC entity filed, attorney memo (~$3K) on the flat fee, concierge and disclosure. Contractor panel and price book. Concierge stack (~$4.5K): Claude extraction, Sheet price book, pypdf TREC 39, DocuSign, Twilio clock, Airtable log.
- **Weeks 2–5:** recruit 10 Austin solo or small-team buyer agents ("Bring us a dead deal" blind replay as the hook).
- **Weeks 4–12:** 30 live files (concierge). The test harness, price book and clock are built in parallel from week 1.
- **Week 12–13:** gate readout. Pass → 12-week v1 build (3 engineers) and seed raise. Fail → kill or pivot (see below).

## Kill criteria
- Gate (a) fails: no measurable value over the agent's own plan.
- Fewer than 6 of 10 agents pay for a further file.
- A TREC complaint, a missed option deadline caused by us, or a reservation-price leak in the pilot.
- An attorney memo saying the B2B flat fee is not workable.
