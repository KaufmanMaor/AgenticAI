# Round 1: Texas real-estate attorney / brokerage compliance view

*This is input for internal ideation. It is not legal advice and not a formal opinion. Statute text was checked only through search excerpts, so every citation needs a read of the official text before anyone relies on it. **[FO]** marks an item that needs a formal written opinion from Texas counsel.*

## 1. Is an AI negotiating for a fee "brokerage"? Almost certainly yes
- **The statute.** Tex. Occ. Code §1101.002(1) defines a broker as a person who, for another person and for a commission or other valuable consideration (or the expectation of one), "negotiates or attempts to negotiate" the sale or purchase of real estate. §1101.351 says no person or business entity may do that without a license. Unlicensed brokerage is a Class A misdemeanor. TREC can also impose administrative penalties, and the injured party has civil exposure.
- **The software is not the actor. The company is.** TREC will not license software, and it will not accept the software as an excuse. If our company runs an agent that messages the seller's side for a buyer and earns money from that deal, the company is the one "attempting to negotiate for another." It makes no difference whether we charge a success fee, a flat fee or a subscription. All of these count as "valuable consideration."
- **Fee collection.** Under §1101.806, an unlicensed person cannot sue to collect a commission.
- **Paying an unlicensed vendor.** Under §1101.651, a licensed broker cannot pay an unlicensed vendor compensation for broker acts. So a per-closing "success" revenue share from a brokerage to our unlicensed software company is itself a risk. A fixed SaaS or seat fee is safer than a fee contingent on closing. **[FO]**
- **Where regulators are heading.** California DRE (Mar 2026), Oklahoma OREC and NAR's March 2026 policy kit all treat AI that does licensed acts like an unlicensed assistant, with the broker answerable for it. I found no AI-specific TREC rule, but TREC's general supervision rule (22 TAC §535.2: written policies, the broker responsible for associates) leads to the same place.

## 2. Compliant structures, ranked from best fit to worst
1. **A licensed Texas brokerage, with AI working under broker supervision. This is my recommendation.**
   - **Licensing.** The entity holds a TREC license with a designated broker (§1101.355), and each negotiation is assigned to a named license holder.
   - **What it unlocks.** We can lawfully take a fee or commission and advertise "we negotiate for you." Rebates are also available (see §8).
   - **Cost.** A broker of record, E&O cover, IABS/CN-1 notices, buyer rep agreements and TREC forms. Homa already uses this model in Texas.
2. **B2B software sold to licensees.** The licensed agent stays the negotiator of record and the product is a tool.
   - **Advantages.** Lowest licensing risk, and it scales across brokerages.
   - **Constraints.** Revenue must not be compensation for broker acts (see §1101.651 above). Our marketing cannot say "our AI negotiates for buyers."
3. **Tools for self-represented principals** (FSBO sellers, unrepresented buyers).
   - **Why it can work.** A principal acting for themselves is not acting "for another," so coaching, analysis and drafting that the user reviews and sends personally are defensible.
   - **The risk.** Once the AI talks to the counterparty itself, or the fee depends on the outcome, we drift into "attempting to negotiate for another." Whether an autonomous agent that messages the counterparty in the user's name counts as brokerage is unresolved. **[FO]**
   - **Legal content.** If the tool drafts legal content, Tex. Gov't Code §81.101(c) gives a software safe harbor from unauthorized-practice-of-law claims, but only with a conspicuous "not a substitute for an attorney" statement.
   - **Market.** The segment is small.
4. **The attorney model.** §1101.005 exempts Texas-licensed attorneys, so a law firm could negotiate deals.
   - **Ownership.** Texas Disciplinary Rule 5.04 bars non-lawyer ownership of the firm and fee-sharing with non-lawyers, so a VC-backed startup cannot own it. The firm could only be a customer.
   - **Malpractice cover.** Legal malpractice exposure is higher, and few attorneys will price residential negotiations at $1-5k.
   - **Verdict.** Not a venture structure.

## 3. What the AI may do on its own: draft, send, bind
- **Draft:** allowed. The AI may analyze inspection reports, build comps, propose a package (repairs, credits, closing date) and fill TREC promulgated forms.
  - Licensees must use TREC forms (22 TAC §537.11).
  - Licensees may not write legal language into Special Provisions; only factual business details are allowed there. The AI must be held to the same limit, so all free-text clauses go to attorney review.
- **Send:** allowed only with a gate. For the pilot, every outbound message to the counterparty needs prior approval from the assigned license holder. Later, a written broker policy could let the AI auto-send low-risk messages inside a pre-approved envelope (scheduling, acknowledgements, document requests). Even then, a named licensee remains responsible.
- **Bind:** never. A real-estate contract must be in a signed writing (Statute of Frauds, Tex. Bus. & Com. Code §26.01).
  - **The hidden risk.** UETA, adopted in Texas as Tex. Bus. & Com. Code ch. 322 (§322.014 covers electronic agents), lets contracts form through electronic agents "even if no individual" reviewed them. Courts have found e-mail exchanges that satisfy the Statute of Frauds. An AI message saying "we accept $8k credit" could therefore be argued to be an acceptance or a binding amendment.
  - **Controls.**
    - Only the principal signs, by e-signature on the TREC form (for example a TREC 39 amendment).
    - Every AI message carries the footer "Non-binding proposal; no agreement until a written amendment is signed by all parties."
    - The AI has no signing credentials.
  - **Option-period deadlines.** These are a malpractice trap. Notice of termination must be given by the deadline, so the system has to escalate to a human well before it.

## 4. The two-sided vision, where both agents sit at one company, is an intermediary arrangement
- **What makes it one.** If one brokerage represents both buyer and seller, the deal is an intermediary transaction (§1101.559) whether one agent or two are involved.
- **What the law then requires.**
  - Written consent from both parties, with a statement of who pays the broker.
  - Fair and impartial treatment of both sides (§1101.560).
  - The broker must not disclose, without written authorization, that the seller will accept less or the buyer will pay more, or any other confidential information (§1101.561, §1101.651(d)).
  - Licensees may give opinions and advice only if different license holders are appointed to each side (§1101.560(b)). Without appointments, nobody may advise.
- **What that means technically.** Two agents run as separate instances with no shared memory, context, embeddings or logs, each supervised by a different appointed license holder. A clean room has to be auditable.
- **Is it viable?** Legally yes. Commercially it is weak for two reasons.
  - Consumers distrust "the same company on both sides." The research shows the stronger model wins and the losing side doesn't notice.
  - Both parties must already be our customers, which is a cold-start problem.
- **Better vision.** Build an agent-to-agent protocol that runs across separate brokerages, each with its own agent and fiduciary duties. That avoids intermediary status entirely. In the pilot, the counterparty is a human listing agent.

## 5. Disclosure: must the counterparty know it's an AI?
- **Texas.** TRAIGA (HB 149, effective 2026-01-01) imposes AI-interaction disclosure only on government agencies and health care providers, by the majority reading. It still prohibits manipulative uses, and only the Attorney General enforces it. **[FO]** on whether any provision reaches us.
- **Deception law still applies.** Concealing the AI could be deceptive under the Texas DTPA (§17.46) or FTC Act §5. For a licensee it could also be "misrepresentation" or "dishonest dealing" under §1101.652.
- **Other states.**
  - **California** (B&P §17941) bars undisclosed bots used to influence a sale. My recollection, unverified.
  - **Utah** (SB 226) requires proactive disclosure for "high-risk" interactions in a licensed occupation, and real estate is licensed. Disclosure is required at the outset of the interaction.
  - **Colorado's** AI Act has a consumer-interaction disclosure duty, but its effective status after the 2025-26 delays needs checking.
- **Recommendation.** Always disclose to both the principal and the counterparty: "AI-drafted, reviewed by [licensee name, license #]." Get the client's written informed consent to AI use in the buyer rep agreement or an addendum. Any voice calls need recording-consent rules (Texas is one-party; California is all-party).

## 6. Liability and E&O
- **Who is liable.** *Moffatt v. Air Canada* (2024 BCCRT 149) rejected the "the chatbot is a separate entity" defense. A US court would do the same, and the broker is liable for its AI the way it is liable for an agent (§1101.803).
- **Highest-exposure statements:** property condition, square footage, school or flood claims, and the "market says" justification. These carry DTPA and misrepresentation exposure, and Fair Housing exposure if the AI's terms or steering vary by protected class.
- **Insurance.**
  - Texas does not mandate E&O, but we must carry it.
  - Many real-estate E&O forms are silent on AI or now exclude it. We need an affirmative AI-use endorsement from the carrier, plus tech E&O and cyber cover for the software company.
  - The vendor contract has to allocate indemnity for model errors.
- **Evidence trail.** Keep complete, immutable logs of prompts, outputs and approvals. They are our best defense and are discoverable either way.

## 7. Fiduciary duties: loyalty, confidentiality, obedience, disclosure, care
- **Reservation price.** It is the most sensitive confidential item, and research shows LLMs leak it or concede past it under persuasion. The fix is architectural: keep the reservation price outside the LLM's prompt, in a deterministic policy engine that approves or rejects proposals. Counterparty text must be treated as untrusted input (prompt-injection risk).
- **Same model on both sides of a deal.** This is not unlawful as such across separate brokerages. Within one brokerage it is an intermediary issue (see §4).
  - A duty-of-care question remains: if we know a competitor's model is weaker and our client still loses, is that negligent?
  - Never use one client's negotiation data to train or prompt for the opposing side.
- **Disclosure duty.** §1101.557 requires telling our principal about material information, so the AI must surface counteroffers and all offers to the client promptly. It must not "filter" them.

## 8. RESPA and rebates (Texas)
- **Rebates are allowed in Texas** if all of the following hold:
  - They are paid through the transaction and shown on the Closing Disclosure.
  - The represented party consents, and the buyer's lender consents to a cash rebate.
  - Loan-program caps apply (FHA, VA and conventional concession limits).
  - Advertising complies with 22 TAC §535.155.
- **Federal law.** RESPA §8 permits rebates to consumers.
- **What is banned.** RESPA §8 and §1101.651 prohibit paying lenders, inspectors or lead sources for referrals, and the CFPB scrutinizes "marketing services agreements." That constrains any distribution strategy built on lender or inspector partners.

## 9. Data and privacy
- **Texas TDPSA.** It applies even to small businesses for sales of sensitive data, and needs a privacy notice and opt-outs.
- **Financial data.** GLBA issues arise if we touch financing or pre-approval data.
- **Contracts.** Client confidentiality must survive termination (TREC buyer rep form). Vendor data-processing agreements must require zero retention and no model training on client data. Inspection reports and financials need access controls.

## 10. Minimal compliant pilot (Austin)
- **Entity.** A TREC-licensed brokerage with a designated broker; owning one beats partnering.
- **Client paperwork.** The client signs a §1101.563 written buyer agreement and an AI-use consent addendum.
- **Scope.** Only the option-period repair and credit negotiation. The counterparty is the human listing agent.
- **Workflow.** The AI drafts the TREC 39 amendment and messages, the licensee approves every send, and the client e-signs.
- **Controls.** Disclose the AI in every message, keep reservation limits in a policy engine, keep full logs, have an AI-endorsed E&O policy and a written broker AI policy.

## 11. Red lines
- No unlicensed entity negotiating for a fee.
- The AI never signs, accepts or terminates.
- No undisclosed bot.
- No shared context across sides.
- No legal drafting in Special Provisions.
- No referral payments to lenders or inspectors.
- No protected-class inputs (Fair Housing).
- No "guaranteed savings" advertising.

## 12. Questions for other roles
- **Broker:** Will listing agents engage with AI-drafted, licensee-approved messages, or ignore them? Who serves as designated broker?
- **Product and engineering:** Can the policy engine guarantee that the reservation price never reaches the LLM? What is the approval latency during 3-5-day option periods?
- **Business:** Can unit economics carry a licensed brokerage plus E&O at about $2-5k per deal, without referral payments?
- **Founder:** Is "two agents at one company" essential, or is a cross-brokerage protocol acceptable?
