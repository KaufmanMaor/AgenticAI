# Round 1 — Tech lens (CTO / founding engineer)

**Bottom line:** We can build a negotiation agent that beats a typical human on a multi-issue Texas repair amendment today. The hard part is not getting the model to negotiate well. The hard part is making sure it **cannot** give away the principal's money, leak private information, or bind anyone without consent. The evidence is clear: every LLM seller whose floor was written into its prompt conceded past that floor (NeurIPS 2026), and limits enforced in code never broke. So the LLM writes the messages and nothing else. A deterministic engine decides what to offer, and a human signs anything that binds. V1 is one-sided (buyer side), runs under a licensed Texas broker, and covers one moment: the option-period repair/credit amendment. Agent-to-agent comes later, as a protocol, not as the starting point.

## 1. Agent architecture: "LLM writes the messages, code holds the money"
1. **Preference elicitation (about 10 min, voice or chat).** The LLM interviews the principal, but the output is a **structured utility spec**, not notes. It records:
   - a weight and a curve for each issue
   - a hard **walk-away**, set by the principal and confirmed twice
   - one **conjoint-style trade-off quiz** ("$3k credit or roof repaired by seller?", "close 10 days later for $2k?")

   The principal signs off on the spec. It is versioned and immutable for that deal.
2. **Utility model over issues:** price, repairs (item by item, done by the seller or credited), closing-cost credit / rate buy-down, closing date, seller leaseback (days, rent), option fee and option-period extension, earnest money, appliances. Each issue gets a piecewise-linear utility, plus hard constraints:
   - the lender's cap on seller credits
   - leaseback ≤ 90 days on the TREC temporary lease
   - licensed-contractor requirement for some repairs
3. **Planner / strategy engine (deterministic plus search).** It keeps a Bayesian estimate of the counterparty's priorities, built from their concessions. It generates candidate packages, scores them with our utility, and picks the next move using a concession schedule: warm in tone, but with reciprocity enforced. That is the MIT finding, "warmth alone is not enough."
4. **Policy gate (code, not prompt).** Every outbound offer is checked against the walk-away and the constraints. Anything outside them is rejected before any text is generated. **The reservation values live only here.** The LLM never sees them, not even as a range.
5. **Language layer (LLM).** It turns the chosen move into an email or text in the persona's voice. The prompt contains only the move, public deal facts and the counterparty's last message after it has been sanitized (see section 5).
6. **Human approval gate.** Nothing binding goes out without a tap from the principal **and** a review by the supervising licensee. "Binding" here means a signed amendment, a counter-offer, or any message that states an acceptance. The agent can send *non-binding exploratory* messages within limits the principal has pre-approved ("we're open to a credit instead of repairs") on its own. Default mode in v1: **every outbound message is approved by a human.** We loosen that once the eval data justifies it.

## 2. Channel to the counterparty
- **Reality: the other side is a human listing agent about 95% of the time.** So v1 is **email and SMS from the licensed buyer agent's own identity**. Email goes through the Gmail/Microsoft Graph API; SMS goes through Twilio with A2P 10DLC registration. It's disclosed as AI-assisted in the signature, which TREC's AI guidance and consumer sentiment (65% want AI disclosed) both point toward. No bot impersonating a person. The listing agent never needs to install anything.
- **Agent-to-agent comes second.** We'll define a small **structured offer protocol** (JSON term sheet, signed, versioned, with explicit "binding: false/true" flags) and carry it over **Google's A2A protocol** as the transport, with an MCP tool interface for brokerages' own agents. We publish it openly. If listing-side tools adopt it, negotiations drop from days to minutes. If they don't, we've lost nothing.
- **One rule:** the counterparty's natural language is always **untrusted input**, never instructions, on every channel.

## 3. Forms and e-sign
- Texas licensees must use TREC-promulgated forms, so we **fill forms; we don't draft contracts**. Targets:
  - the Amendment (39-x), including repairs, credits and the closing date
  - Notice of Buyer's Termination
  - Seller's Temporary Residential Lease (for leaseback)
  - counter terms on the One to Four Family contract (20-x)
- **Integrations, in order:**
  1. **DocuSign eSignature API.** Universal, and good for envelope status webhooks.
  2. **Lone Wolf (zipForm / Transactions).** That's where TAR/TREC forms actually live for most Texas agents. This is a partnership, not a public API.
  3. **dotloop** (Zillow).

  Until 2 and 3 exist, we generate a flattened PDF of the official TREC form and send it through DocuSign.
- **Mapping from agreed terms to form fields is deterministic code with unit tests per field.** The LLM never writes text that goes into a field. A diff view shows the principal exactly what changed against the last signed version.

## 4. Inspection parsing and repair pricing
- **Input:** inspector PDFs (Spectora, HomeGauge; Texas uses TREC's REI 7-x report format), plus photos. **Pipeline:**
  1. Vision-LLM extraction into an item list: system, severity, "deficient" checkbox, safety flag, location.
  2. Normalize to a repair taxonomy of about 150 codes.
  3. Price each item as a **range** (P25 to P75) from Austin cost tables. We seed them from RSMeans-style data and contractor quotes, then refine with our own outcome data.
  4. Flag items that need a specialist, such as foundation, roof, HVAC or electrical panel. Those come with "get a bid" instead of a number.
- **Output:** a ranked request list: must-fix for safety or lender requirements, then high-value items, then items to drop as goodwill. Each item is priced both as "seller repairs" and "credit", which feeds the utility model directly. **The license holder reviews every estimate.** We never present a number as a contractor quote.
- Inspection PDFs are also an **injection surface**: hidden text, or white-on-white "ignore previous instructions". They go through the same quarantined parser as counterparty mail.

## 5. Security and fairness
- **Prompt injection:** we use a **dual-LLM / CaMeL-style split.** A *quarantined* model reads counterparty emails and PDFs and may output **only a typed schema**: offer terms, questions, sentiment, claimed facts. It has no tools and no access to secrets. The *privileged* planner never sees raw counterparty text. Claims like "my seller has three other offers" are stored as *unverified assertions* with a discount on them, so they never act as facts. This also blunts the Magentic first-proposal and urgency manipulations.
- **Information leakage:**
  - The language model never holds reservation values (section 1).
  - An outbound **DLP filter** blocks any number within ±5% of the walk-away. It also catches private facts we've tagged, such as "relocating for job" or "pre-approved to $X", and planted **canary tokens**. A hit blocks the message and pages a human.
  - Small models leak early, so the language layer uses a frontier model only.
- **Collusion and "both sides use us":** in v1 we serve only the buyer side, which removes the problem. If we later serve both sides of one deal, the deal must follow TREC intermediary rules, with written consent from both parties. Technically that means:
  - Separate tenants and separate KMS keys per side, with no shared memory or retrieval.
  - Our operators can't see across sides (break-glass access only, audited).
  - No live cross-side learning, and no "close-rate" objective anywhere: each agent optimizes **its own principal's utility only**.
  - **Symmetry is pinned and disclosed:** same model, same reasoning budget, same strategy version, recorded in a signed deal manifest both parties can audit.

  That is our answer to Project Deal's finding that "the stronger model wins and the loser doesn't notice." In our product, nobody can buy a stronger agent within the same deal.
- **Audit:** an append-only, hash-chained log of every message, every planner decision and every approval. It's our defence in the Moffatt-style "the bot said it" case and with TREC.

## 6. Evaluation harness (built before the product)
- **Simulator:** synthetic Austin deals, each with a property, an inspection report, and seller and buyer utilities we generate ourselves. That gives us *ground-truth Pareto frontiers*. Counterparty personas include a stubborn seller, a lazy listing agent, an anchoring bully and a "three other offers" bluffer, played by several models from different vendors.
- **Metrics:**
  - deal rate
  - share of surplus captured and distance to the Pareto frontier
  - **limit breaches (must be 0, release-blocking)**
  - leakage rate, number of turns, a tone score
  - how the principal rates the outcome against what an expert human negotiator would have done
- **Red team:** a continuously growing corpus of injection attempts covering email, PDFs, fake "broker authorization", emotional pressure and long-con persuasion, plus our own agent against itself with a stronger opponent. Every incident in production becomes a regression test.
- **Human benchmark:** 30 to 50 role-played amendments against real Texas listing agents (paid $100/hr) before the first live deal.

## 7. MVP build plan and cost
| Phase | Scope | Time | Team |
|---|---|---|---|
| **0. Concierge** | Partner broker. We parse inspections and draft requests and messages with Claude plus a spreadsheet utility model; a human sends everything. 10 live deals | 3–4 wks | 1 eng + licensed partner |
| **1. Copilot v1** | Elicitation, utility and planner engine, policy gate, quarantined parser, DLP, inspection pricer, email/SMS, DocuSign + TREC PDF fill, approval app, audit log, eval harness | 12 wks | 3 eng (backend/ML, full-stack, security-minded infra) + 0.5 design |
| **2. Scale** | Lone Wolf/dotloop, offer-stage negotiation, seller-side product, A2A protocol, constraints from lender integrations | +6 mo | 5–6 eng |
- **Stack:** TypeScript/Python, Postgres, Temporal for long-running deal workflows that span days, Claude via API with zero data retention, AWS KMS per tenant, SOC 2 Type I by month 9.
- **Unit cost:** about $10–40 in LLM and tool spend per negotiated deal (eval runs cost more than production). Infrastructure is about $1–2k/month before scale. The real cost is the eval harness and the licensed humans in the loop.

## 8. Moat
- **Code: none.** Any brokerage can bolt an LLM onto email in a quarter.
- **Data on accepted outcomes: yes, and it's the only real moat.** What matters is not the transcripts. It's **priced outcomes**: for each item, market and property type, what was asked, what was accepted, whether as a credit or a repair, and at what ratio. Over time we also learn **how each listing agent responds** to a request. Nobody records this today; it's buried in PDFs on dotloop. It compounds per market, so we need to own Austin densely before going wide.
- **Second moat: the eval and red-team corpus** and our record of zero limit breaches. That's what lets a broker of record, an E&O insurer or TREC trust us. Trust is the product.

## 9. Two bold technical ideas
1. **The MESO engine** (Multiple Equivalent Simultaneous Offers). Every counter goes out as **three packages of equal value to our principal**, for example "$9k credit", "repair roof + $3k credit + close 7 days later", or "$6k price cut + 21-day leaseback". The listing agent's choice reveals the seller's priorities, which the planner learns from. Each package is pre-rendered as a ready-to-sign TREC amendment. This is the founder's "if you bring me this I'll bring you that" turned into an algorithm, and it delivers win-win *with teeth*.
2. **A sealed "deal room" in a confidential-compute enclave** for when both sides use us. Both principals' utility specs go into an attested TEE (AWS Nitro Enclaves or similar). A mechanism computes a Pareto-efficient, roughly Nash-bargaining split, and each side sees **only the proposed package**, never the other side's inputs. Remote attestation proves to both parties and to TREC that we can't peek or steer. This is the only technical design I believe can make "both sides on one platform" both fair and legal. It also skips language-based haggling, so the "stronger model wins" problem goes away.

## Open questions for the other roles
- **PM:** Is the first user the *buyer* (consumer app plus a partner broker) or the *buyer's agent* (copilot that saves them hours per deal)? That changes the elicitation UX and who taps "approve". I lean toward the agent copilot.
- **Marketing:** Do we disclose "AI-negotiated" to the listing side as a selling point ("faster, documented, no drama") or keep it low-key? What is the proof metric: dollars saved per amendment, or deals saved from termination?
- **BizDev:** Can we get Lone Wolf/zipForm or dotloop partner access within 6 months? Which Austin brokerage gives us 50 deals per quarter for outcome data? Is there an E&O insurer willing to underwrite an AI-assisted negotiation?
- **Texas Broker:** Can a supervising licensee approve AI-drafted messages in a batch, or must each be individually reviewed? How do listing agents react today to a structured, three-option repair counter?
- **RE Attorney:** Does our software "negotiate" under TRELA §1101 if a licensee approves every message? Who is liable for a mispriced repair estimate? Under UETA §14, can a "binding: false" protocol flag reliably keep exploratory agent messages from forming a contract? Would the enclave deal room satisfy the intermediary rules?
