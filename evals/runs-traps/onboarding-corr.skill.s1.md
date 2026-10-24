**Don't bank the 60%. Treat Monday as a test, not a forecast.** Mandatory onboarding may well help people who skip today, but the 60% projection is very likely too high. Confidence: about 80% that the projection overstates the effect; moderate that the true effect is positive.

**Why the gap isn't the effect.** The 60% vs. 25% split compares people who chose to finish an optional tour with people who chose not to. Those who finish are already more motivated and more likely to stick around, so they would retain better with or without the tour. Making the tour mandatory changes the gate, not the people. The skippers who get forced through are, by definition, the ones least inclined to engage, so the realistic lift is some fraction of the gap, not all of it.

**The arithmetic.** "About 60%" is the overall rate you get only if every signup retains like today's completers. Only the skip share moves. Suppose skippers are 40% of signups (an illustration; use your real number). Today's overall 90-day retention is 0.6 × 60% + 0.4 × 25% = 46%. If the gate lifts skippers to 35%, overall becomes 50%. You reach 60% only if skippers reach 60% too, which is the same selection assumption again.

**Ways Monday's numbers could look better without the product being better:**
- **Click-through completion.** Forced users tap through the tour. Completion rises, but the content isn't absorbed, and the retention lift may not follow.
- **Denominator.** If 90-day retention is computed among users who finished onboarding, the gate quietly removes the people who would have churned at it. Measure retention per signup, not per completer.
- **Gate churn.** The users most annoyed by being forced leave before signup finishes. That shows up as funnel drop, which often gets attributed to something else.

**The check.** Ship the gate to a random share of new signups (half, or a 20% holdout) and compare 90-day retention by assignment, not by completion, with per-signup denominators. That is an intent-to-treat comparison. A 90-day readout takes three months, so pre-register a day-7 or day-14 activation metric as an early signal. Before Monday, you can run a cheaper pre-check on past users: match skippers and completers on signup source, day-0 activity and plan, then see how much of the 35-point gap survives the match.

**The rival this check can settle.** The main competitor is that the tour mostly sorts users who would have retained anyway. If the holdout shows the gap closing to near zero, mandatory onboarding is a funnel cost with no retention gain.

**Rejected alternatives:**
- *Ship the mandatory gate to everyone and project the completer rate onto all signups.* This assumes the tour causes the gap and that forcing it reproduces the completers' behavior. That is a chain of about five assumptions, each only partly likely, so the joint confidence is low.
- *Move the first-value moment earlier in the product instead of changing the tour.* This is the fallback if the holdout shows the tour's effect is small. It is a bigger product change than Monday's question needs, so I'd hold it until the data says the tour isn't doing the work.
