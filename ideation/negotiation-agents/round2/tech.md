# Round 2 — Tech lens (CTO): stress-testing Concept v2

**Bottom line:** v2 is the right product: buyer-only, bot-to-human, the option period, limits held in code, no signing credentials. I'd build it. But three of its load-bearing pieces are weaker than they look:
- the file-30 gate can't be measured as written;
- the repair-cost engine is treated as a single bullet even though it's both the product and the main liability;
- the deadline clock depends on a contract date we never take in.

Fix those three and the plan holds.

## 1. The 3 biggest flaws in v2
1. **The gate is statistically blind.** Say about 15% of contracts terminate in the option period. Then 30 files hold about 4–5 terminations, and the 95% CI on survival is roughly ±13 points. A "≥5-point survival gain" can't be detected below about 700 files per arm. The $3K net-value gate also has a problem: it's measured "vs. the seller's first response", which a high opening anchor games. **Fix:** make the gate a *paired* comparison against the agent's own pre-committed draft (section 4). Report survival descriptively only.
2. **The repair-cost engine is under-specified but carries the value and the liability.** Every package, every "equal-value" claim and every Moffatt-style "you told me $4K" rests on our number. v2 names no data source, accuracy target or validation plan. Without them, the three packages just look precise without being right. **Fix:** section 3. Every number is a range with a source tag, and the licensee confirms it.
3. **The option clock has no reliable input, and approval is a single point of failure.** The deadline is 5:00 p.m. local time on the last day, counted from the Effective Date. That comes from the executed TREC 20-x contract, which v2 never ingests. Separately, a licensee who doesn't tap "approve" at 3 p.m. on day 7 is a missed deadline whatever our alerts say. **Fix:**
   - Parse the contract, and make the licensee **confirm the computed deadline at intake** (a hard block until they do).
   - Name a backup approver for each file.
   - At T−6h, escalate to a phone call, not just SMS.
   - Pre-draft a **Notice of Termination** for the buyer to sign, so walking away is always one signature away.

## 2. Concierge tooling (2 weeks, under $5K)
| Step | Manual (a human) | Scripted (we write it) |
|---|---|---|
| Intake | Agent forwards contract + inspection PDF to desk@; we call the buyer for the 5-min interview | Watcher puts files in a per-file folder; Claude (vision, structured output, no tools) extracts items and the Effective Date / option days to JSON |
| Pricing | Expert sanity-checks; we phone 1–2 Austin contractors for top items | Lookup in a Google Sheet price book (item code × Austin range × source); specialist items auto-flagged as "get a bid" |
| Packages | Negotiation expert picks the final 2–3 | Spreadsheet utility model scores the options and enforces walk-away and lender credit caps |
| Paperwork | Licensee reviews and sends from their own email; buyer signs | Fill the TREC 39 PDF field by field (pypdf), diff it against the last version, send via the agent's DocuSign |
| Clock | Licensee confirms the deadline | Google Calendar + Twilio SMS/voice at 48h, 24h and 6h; a backup approver gets paged |
| Log | Expert codes the outcome | Airtable row per message, decision and outcome. This is the seed of the eval dataset |

**Budget:**

| Item | Cost |
|---|---|
| Claude API | ~$300 |
| Twilio | ~$100 |
| Airtable / Google | ~$150 |
| Contractor desk-estimate panel (3 trades × $50/report × 20) | $3,000 |
| Broker-reviewer stipend | $1,000 |
| **Total** | **≈ $4.5K** (founders' time not counted) |

## 3. Repair-cost engine (Austin)
- **Sources, in order of trust:**
  1. Paid contractor desk estimates from a panel of 3–5 Austin trades: roof, HVAC, plumbing, electrical, foundation.
  2. Our own outcome data: credits accepted per item in final amendments. This one is biased toward compromise, so we use it for *negotiation* priors, not cost.
  3. Licensed cost data: RSMeans / Craftsman National Repair & Remodeling Estimator, with Austin area modifiers.
  4. City of Austin open-data building permits, for declared valuations of roof, HVAC and foundation jobs. Noisy, but local.
  5. Angi/HomeAdvisor cost guides, as a sanity bound only.
  6. Option: license from inspection-to-estimate vendors (Repair Pricer, Inspectify). Check their terms and whether they compete with us.
- **Output per item:** P25–P75 range, mid-point, source tag and confidence. Specialist and structural items never get a number in v1.
- **Accuracy targets, all release gates:**
  - ≥70% of priced items have the contractor quote inside our P25–P75 band.
  - Report-level total within ±20% of the summed contractor estimates (MAPE ≤ 20%).
  - **≥98% recall on safety and structural flags.** A missed foundation item is the worst failure.
  - Zero items priced that aren't in the report.
- **Validation:**
  - A held-out set of 40 Austin reports, where the panel prices the top 10 items blind.
  - We track calibration by trade and price tier every month, and re-fit the price book quarterly.
  - Every live file where a real bid arrives becomes a new test point.

## 4. Tension #5: measuring "incremental value"
- **Pre-commitment (the key trick):** on each live concierge file, the agent writes *their own* ask and plan **before** seeing ours, and we freeze it. That gives a paired counterfactual on the same house, buyer and seller.
- **Blind replay (historical, n≈50 files from 2–3 teams):**
  - Inputs are only what was knowable at inspection time: report, contract, listing data and the buyer interview notes the agent kept.
  - We generate our ask and packages.
  - 3 Texas brokers rate *pairs* (ours vs. the real one), with order randomized and formatting normalized. They score likely seller acceptance, buyer value, and "would you send this?"
  - Inter-rater agreement must be κ ≥ 0.5, or the panel's verdict doesn't count.
- **Simulated counterparty:**
  - We build listing-agent and seller personas from several model vendors, each with a seller utility (days on market, already bought elsewhere, cash need).
  - **We calibrate on the real file:** fit the persona so it reproduces the seller's *actual* response to the *actual* ask, then replay our ask against it.
  - **We validate the simulator first:** on held-out files it must predict the real response within ±25% of dollars in ≥60% of cases. If it can't, the simulator is used for red-teaming only, never for claims.
- **Statistics at n=30 (paired):**
  - The primary metric is the per-file difference in buyer net value, ours vs. the agent's frozen plan. We score it with the simulator plus a panel estimate, normalized to % of the inspection total.
  - Assume SD of the difference ≈ $4–6K. Detecting a $3K mean (d ≈ 0.5–0.75) then gives about 75–95% power (paired t-test, α=0.05).
  - Robustness: Wilcoxon signed-rank test, and a bootstrap 95% CI.
  - We pre-register the metric, the exclusions and the analysis before file 1.
  - Secondary measures: share of drafts sent with ≤ light edits, and the licensee's hours per file.
  - Survival is reported with a Wilson CI, labelled "directional".
  - **The gate passes if** the CI lower bound is > $0 and the point estimate is ≥ $3K. A second required condition: ≥70% of drafts are sent with light edits.

## 5. Threat model
| Threat | Vector | Impact | Controls | Test |
|---|---|---|---|---|
| Prompt injection | Hidden/white text or metadata in an inspection PDF; "ignore instructions" in a listing-agent email | Wrong asks, leaked data, rogue sends | Quarantined model with no tools or secrets and schema-only output; render PDF → image → OCR so hidden text is dropped; planner never sees raw text; human approves every send | Injection corpus of 300+ samples in CI; zero schema escapes allowed |
| Leakage | LLM restates walk-away or private facts ("relocating", "pre-approved to $X") | ZOPA collapses; fiduciary breach | Limits only in the policy engine, never in context; DLP blocks numbers within ±5% of limits; tagged private facts plus canary tokens; frontier model only | Red-team "persuade the bot to reveal its max" runs; target 0 leaks / 1,000 |
| Missed deadline | Wrong Effective Date parse, time-zone mistake, approver offline | Buyer loses termination right: malpractice | Deadline confirmed by the licensee at intake; 5 p.m. local time; 48/24/6h alerts plus a call; backup approver; Notice of Termination pre-drafted; clock runs on Temporal with idempotent timers | Property tests on date math; fault-injection drills (approver silent) |
| Hallucinated defect | Vision LLM invents or inflates an item, or misses one | Credibility with the listing agent; liability (Moffatt) | Every item cites page and quote from the report; items without a citation are dropped; recall checks on safety/structural; licensee checks the list | 40-report gold set; 0 uncited items; ≥98% structural recall |
| Form error | Wrong TREC 39 field or amount | Binding wrong terms | Code-only field mapping; a unit test per field; diff view; principal e-signs | Golden-PDF tests on every release |

## 6. v1 build plan (12 weeks, 3 engineers)
| Wk | Deliverable |
|---|---|
| 1 | Deal data model; Temporal workflows; per-tenant KMS; hash-chained audit log; eval harness loaded with concierge files |
| 2 | Contract intake (Effective Date, option days, fee) → deadline engine + licensee confirm step |
| 3 | Option clock: SMS/voice/email escalation, backup approver, Notice of Termination draft |
| 4 | Inspection parser v1 (Spectora, HomeGauge, TREC REI 7-x), quarantined, citation-required |
| 5 | Repair-cost engine v1 (price book + panel data, ranges, specialist flags); 40-report gold-set eval |
| 6 | Buyer interview → utility spec; policy gate (walk-away, lender credit caps, leaseback ≤ 90 days) |
| 7 | Package generator (2–3 options); TREC 39 field mapper + golden tests; DocuSign |
| 8 | Counter reader (quarantined) → next-move planner; licensee approval queue (mobile web) |
| 9 | Language layer + DLP + canaries; send via licensee's Gmail/Graph and Twilio |
| 10 | Red-team sprint: injection and leakage corpus; simulator v1 calibrated on replay files |
| 11 | Blind replay on 50 files + shadow mode on 5 live concierge files |
| 12 | External pentest; fixes; launch to 10 agents with incident runbook |

## 7. What I now accept / reject
**Accept:**
- buyer-only representation
- bot-to-human under a named licensee, with AI disclosure
- the option-period wedge
- limits in code and no signing credentials
- zero-miss deadline guardrails
- concierge before the build
- a flat $249 fee with no closing link
- year-2 protocol with institutional sellers; but I'll make our internal term sheet that protocol's schema from day 1

**Reject or modify:**
- **Survival as a gate metric:** use the paired value test in section 4.
- **"vs. the seller's first response" as the baseline:** use the agent's frozen plan instead.
- **"Isolated parser (prompt-injection safe)":** call it *injection-resistant*. Nothing is safe, and we test every release.
- **Three packages on every counter:** send 2–3 options in *one* message and generate the TREC 39 only after the seller chooses. Three draft amendments confuse listing agents.
- **"Build after the concierge":** no. The eval harness, price book and clock start in week 1 of the concierge, because they're needed either way.
