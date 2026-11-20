# Round 3: Tech sign-off (CTO)

**(a) SIGN-OFF WITH CONDITIONS.** The architecture is right: limits held in code, human sends, only the principals sign, deadline guardrails, a paired gate. But gate (a) has no defined way to put a dollar value on the agent's sealed draft, which is never sent. That has to be fixed before file 1.

**(b) Biggest remaining risk: gate (a) can't be computed honestly.** On a live file only our ask goes out, so the outcome of the sealed draft is never observed. v3 dropped my Round 2 condition that the simulated counterparty must first prove it can predict real seller responses. Without that, "≥$3K incremental" is a number we invent. A second problem: an agent writing a sealed ask at 9pm on day 3 may simply skip it.
- **Cheapest test (about 1 week, under $500, before any live file):**
  - Take 15 replay files where the real ask and the real seller response are both known.
  - Check whether the simulator and broker panel predict that response within ±25% of dollars in ≥60% of files.
  - Have 3 pilot agents time themselves writing a sealed ask. It must take ≤15 min.
- **If either check fails:** gate (a) becomes a panel-estimated value with κ ≥ 0.5, and we say so in the readout.

**(c) Inconsistencies in v3:**
1. **The process guarantee conflicts with the clock.** Ruling #5 promises an ask list in "4 business hours", but option periods run through nights and weekends. A report that arrives Friday at 9pm gets its ask list on Monday, which can be day 5 of 7. Use 4 clock hours, or tie the guarantee to "≥48h before the option deadline."
2. **The moat conflicts with the firewall.** Ruling #14 makes Austin priced-outcome data the moat. Ruling #1 firewalls any future brokerage from that data. Decide which asset the brokerage would actually use.
3. **The data rights don't reach the buyer.** "Every contract grants anonymized data rights" only binds the sponsoring broker. The inspection report and the buyer's preferences belong to the buyer's file, and the buyer has no contract with us. We need consent passed through the agent's client, or the moat has a hole in it.
4. **The plan is out of order.** The price book is built in weeks 0–2, but the 40-report gold set used to validate it only arrives with the replay files in weeks 2–5. The first live files would be priced on an unvalidated engine. Validate on the replay files first, and keep live asks gated by licensee review until targets are met.
5. **The gate math is tight.** 30 files from 10 agents means about 3 each in about 8 weeks, and gate (c) needs a paid third file. Recruit 12–15 agents, or the gate fails on volume, not on value.

**Verdict: Yes.** It's worth a founder's next 12 months, but only as a 13-week, roughly $50K bet that has to earn the other 9 months by passing gate (a). The $249 tool alone isn't venture-scale; the prize is the priced-outcome data and the brokerage it could unlock.
