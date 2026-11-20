# Round 2: RE attorney / compliance stress-test of Concept v2

*This is internal ideation input, not legal advice and not a formal opinion. **[FO]** marks a point that needs a written opinion from Texas counsel. **[U]** marks a point I recalled from memory and did not verify this round.*

## 1. The three biggest flaws in v2
1. **The concierge, and the Option Desk "buyer preference interview," put our staff in the principal's ear.**
   - In v2, our people and our tool talk to the buyer directly about walk-away points and what to ask for. That is advice to a principal on negotiation.
   - TREC's unlicensed-assistant guidance does not let unlicensed staff negotiate or give opinions to principals.
   - The fix is to make every buyer-facing touch the licensee's: run under their brand, through their account, with their review. Our staff never counsel the buyer and never contact the listing agent.
2. **The Phase 2 "guarantee" competes with the credits we win, inside the same lender cap.**
   - Lenders cap interested-party contributions (IPC):
     - Fannie/Freddie: 3% at more than 90% LTV, 6% at 75-90%, 9% below 75%.
     - FHA: 6%.
     - VA: 4% concessions.
   - Fannie and FHA list the real estate agent/broker as an interested party, so our rebate likely counts toward the cap **[U, confirm with lender compliance]**.
   - For a 5%-down buyer, a $9K inspection credit plus a 2% rebate can exceed 3%. The excess is lost, or it forces a price restructure.
   - So the guarantee can pay out exactly when it cannot legally reach the buyer.
3. **Selling a tool to agents and then competing with them as a brokerage creates a confidentiality and conflict problem.**
   - Option Desk files contain the agents' clients' confidential information. The licensee owes that client confidentiality.
   - If that data later trains or targets Punchlist Realty, the licensee has a breach, and we have deceptive-trade-practices (DTPA) and tortious-interference exposure.
   - A free consumer "Ask List" tool used by buyers who already have an agent invites claims that we are interfering with another broker's exclusive client (§1101.652, negotiating directly with a represented party, and inducing a party to break a contract).
   - Even the shared "Punchlist" name blurs vendor and brokerage, and TREC advertising rules (22 TAC §535.154-.155) require the broker's licensed or assumed name in every brokerage ad.

## 2. The $249 flat per-file fee and §1101.651
- **Paid by the agent or team: acceptable, with conditions** (moderate-low risk, [FO]). §1101.651 bars paying an unlicensed person for acts that require a license. It does not bar paying for support services. Brokers routinely pay unlicensed transaction coordinators per file. Four conditions keep it there:
  - The fee is billed when the file opens, not when the deal closes.
  - It is the same whether or not the deal closes or how much is won.
  - It is billed to the sponsoring broker or team, not to the buyer.
  - Our deliverable is drafts for the licensee, never communications to principals.
- What changes the answer:
  - Any refund or price tied to outcome or closing.
  - Our staff contacting either party.
  - Marketing that says "we negotiate."
- **If the agent passes it to the buyer:** allowed only as the licensee's own disclosed fee.
  - It must appear in the buyer representation agreement's compensation terms (§1101.563 requires those terms in writing) and on the Closing Disclosure.
  - Check loan-program limits on fees a borrower may pay. VA buyer-broker fee rules have shifted since 2024 **[U]**.
  - We must **never invoice the buyer**. A buyer paying us for negotiation support is a principal compensating an unlicensed negotiator, which is brokerage.
  - Ban line items that name us, such as a "Punchlist negotiation fee."
- **First 20 files free:** this reduces the §1101.651 risk on the fee, but it does not cure the conduct question. §1101.002 also covers acting "with the expectation of receiving" compensation, and a free pilot followed by a paid product supplies that expectation.
  - So "free" protects us only if we are not doing broker acts in the first place.
  - Document that the pilot is a product test for the licensee and that we have no interest in any transaction.

## 3. Wizard-of-Oz concierge: does the human expert need a license?
- **If the expert talks to the buyer or the listing agent, or the licensee rubber-stamps the expert's moves, then yes.** In substance the expert is "attempting to negotiate for another," and the brokerage-for-compensation risk sits on us.
- **If the expert is pure back office (drafts reviewed by the licensee, no party contact, the licensee decides), the risk is lower, but it is grey.** Negotiation strategy is not clerical work. [FO]
- **A sales-agent license is not the cure.** A sales agent may act only through their own sponsoring broker, and the pilot agents sit at other brokerages.
- **Cleanest option:** the concierge expert is a **Texas-licensed broker** (ideally the broker co-founder). That broker signs a written consulting agreement with each pilot agent's **sponsoring broker** (broker-to-broker is permitted) and stays back office.
- **Also required:**
  - The buyer consents to vendor access to confidential information.
  - An NDA binds everyone on our side.
  - Nobody tells users it's "AI" when a human did the work.

## 4. Liability allocation, ToS clauses, E&O, and repair-cost ranges
- **Who is exposed for what:**

| Party | Exposure |
|---|---|
| Licensee | Owns every sent statement and the deadline calendar (§1101.803 broker responsibility; TREC 20-18 option period ends 5 p.m. local time). |
| Inspector | Owns the report. Their contracts typically cap liability at the inspection fee. |
| Us | The buyer can still reach us in tort as a foreseeable relier on our estimates: negligent misrepresentation under *McCamish v. F.E. Appling* (Tex. 1999), plus a product-negligence theory if the deadline clock miscomputes. *Moffatt v. Air Canada* (2024 BCCRT 149) means "the AI said it" is no defense. |

- **Agent/broker ToS clauses:**
  - The contracting party is the **sponsoring broker**, and the agent joins it.
  - The licensee retains professional judgment and must review every output.
  - The tool is not an inspection, appraisal, legal advice or contractor bid.
  - The deadline clock is a reminder aid; the licensee's calendar governs.
  - The broker obtains client consent to vendor processing.
  - We make no use of client data beyond the file and no training, and we expressly will not use it for any brokerage affiliate.
  - Liability is capped at 12 months of fees, with consequential damages excluded. Carve-outs: data breach, gross negligence, and our failure to follow the configured walk-away limits.
  - Mutual indemnities: ours for system defects, theirs for content they edit or send.
  - A DTPA waiver is unlikely to hold against small agents. Under §17.42 it needs legal counsel and specific conspicuous form, so price that risk.
  - Never market "zero missed deadlines." That turns a guardrail into a warranty.
- **E&O:**
  - **Us:** tech E&O/professional liability plus cyber, $1-2M to start.
  - **Agents:** get the carrier to confirm in writing that their real-estate E&O has no AI or technology exclusion.
  - **Phase 2:** if the designated broker owns less than 10% of the entity, Texas requires the business entity to carry at least $1M E&O (§1101.355) **[U, verify]**. That is likely in a VC-owned structure.
- **Repair-cost ranges are probably not an "opinion of value."** They are cost-to-cure estimates for components, not an appraisal (ch. 1103) or a broker price opinion of the property.
  - **Do not interpret beyond the report.** Restating a defect's severity beyond what the report says drifts toward inspection opinion under ch. 1102, which licenses inspections for compensation.
  - **Who owns the price advice.** Converting repairs into an "equal-value price reduction" is price advice the licensee must own.
  - **Labeling.** Label each range with its source and date, mark it "for negotiation, not a bid," and keep "get a bid" on specialist items.
  - **Presentation.** Never send a range to the counterparty as fact. Attach real bids where you have them.

## 5. Exact wording
- **Counterparty footer** (every email and SMS, sent from the licensee's account):
  > "Prepared with AI-assisted drafting tools; reviewed and sent by [Agent Name], [Brokerage Name], TREC Lic. #[___], who represents the Buyer. This is a non-binding proposal for discussion only. No agreement, amendment, waiver or acceptance exists unless a written TREC amendment is signed by all parties. Repair figures are estimates for negotiation purposes, not contractor bids, inspections or appraisals."
- **Rule for licensees:** never type "accepted" or "agreed" in a message. Conduct can override a footer (UETA ch. 322).
- **Buyer consent addendum** (attached to the buyer representation agreement):
  > "Broker uses software tools, including artificial intelligence, provided by [Vendor], to analyze inspection reports, estimate repair costs, and draft proposed communications. A licensed agent reviews every communication before it is sent, and only you sign agreements. Broker will share your confidential information, including your priorities and limits, with [Vendor] solely to provide these services; [Vendor] may not use it to train models, for any other client, or for any affiliated brokerage. You may opt out at any time."
- **On every buyer-facing estimate:**
  > "Estimate range from [source], [date]. Not a bid or inspection; obtain a licensed contractor bid for [item]."

## 6. Phase 2: "1% back plus guarantee," and the intermediary issue
- **The rebate itself:** a rebate to the buyer we represent is legal in Texas.
  - It must be in writing, paid through closing and shown on the Closing Disclosure, with lender consent.
  - A fixed formula for an outcome-adjusted amount is fine **if it is defined objectively in the buyer agreement**. Define "Negotiated Value" as credits plus price reduction in the executed amendment (seller repairs at a pre-agreed value), measured against the executed contract.
  - Say plainly that it pays only at closing.
  - Disclose that the guarantee gives the broker a financial interest in the form of the outcome. That interest can tilt us toward credits over repairs, or toward pushing harder than the client's "save the deal" goal.
- **Advertising** (22 TAC §535.155): include the broker name; say "1% of purchase price, paid at closing, subject to lender approval and loan-program limits"; avoid "guaranteed savings." Recommended copy: "If your option-period amendment wins under $3,000, your rebate increases to 2%. Terms apply."
- **The IPC fix:**
  - Underwrite the IPC headroom before the option period.
  - Where the cap binds, pay the guarantee as a pre-agreed fee reduction or post-closing service credit only if lender compliance clears it [FO plus lender].
  - Otherwise offer the guarantee only to buyers with headroom.
  - A promise to adjust our own fee is likely not insurance, but confirm **[U]**.
- **Builder or iBuyer clients:**
  - If Punchlist Realty ever represents, or takes non-commission compensation from, a builder or iBuyer that sells to our buyer, that is an intermediary arrangement (§1101.559) or dual compensation (§1101.652 requires full disclosure and consent from all parties).
  - That means written intermediary consent in both agreements, appointed licensees per side, and §1101.561 confidentiality enforced as separate data stores.
  - Builder-affiliated lenders trigger RESPA affiliated-business disclosures.
  - Software-only deals with iBuyers across separate brokerages avoid intermediary status, but the relationship still has to be disclosed to our buyer.

## 7. Minimal Phase 1 compliance checklist
1. Texas RE counsel opinion memo (about $3-5K) on the vendor structure and fee, plus an informal TREC inquiry. TREC won't bind itself.
2. Contract with each **sponsoring broker** (ToS + DPA). The broker adopts the tool in its §535.2 written policies.
3. Buyer AI/vendor consent addendum on every file.
4. Every send comes from the licensee's own account after review. Our staff have zero contact with principals or the counterparty.
5. The concierge expert is a licensed broker under the broker-to-broker agreement.
6. The TREC 39 is filled from structured terms. No Special Provisions text.
7. Footer and estimate labels as in §5.
8. A deadline engine tested on the 5 p.m. local cutoff, with escalation alerts.
9. Logs retained for at least 4 years and exportable to the broker **[U on period]**.
10. A Texas Data Privacy and Security Act (TDPSA) privacy notice, zero-retention LLM terms, encryption, and a deletion schedule.
11. Tech E&O and cyber for us; written AI-coverage confirmation from each agent's carrier.
12. No payments to inspectors or lenders. TREC inspector rules separately limit inspectors' compensation arrangements.
13. Marketing review: no "AI negotiates" or "zero missed deadlines" claims. Outbound text marketing to agents must check Texas SB 140 telemarketing registration **[U]**.
14. Fair Housing: no protected-class or proxy inputs.

## 8. What I now accept and what I reject
- **Accept:**
  - Buyer side only.
  - Bot-to-human.
  - The option-period wedge.
  - The AI drafts, a human sends, and only the principal signs.
  - Walk-away limits in code.
  - A fixed per-file fee billed to brokers.
  - A protocol across separate brokerages.
  - The brokerage sequenced after the gate.
- **Reject or modify:**
  - An unlicensed concierge expert.
  - Option Desk interviewing buyers directly. It should run as the licensee's form.
  - Billing buyers.
  - Using vendor-side client data for Punchlist Realty.
  - The guarantee before IPC underwriting is solved.
  - One shared brand for the vendor and the brokerage.
  - A free consumer tool marketed to buyers who already have an agent.
