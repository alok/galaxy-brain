**Don't ship on this result.** Either run the test to a pre-committed sample size, or ship only with a holdout that you read at a fixed later date. Confidence: about 85%.

The non-obvious part isn't "peeking is bad," which you already know. It's three things stacking up:

1. **The p-value is much weaker than it reads.** Checking daily and stopping at the first crossing is a sequential procedure with about six looks (days 1 through 6). If the true effect were zero, a rule like that declares a "winner" roughly 14 to 15% of the time, not 5%. A p of 0.04 reached this way is closer to a one-in-seven event than a one-in-twenty-five one. This is an estimate from standard repeated-testing inflation tables; a short simulation at your traffic levels would pin it down.

2. **The 4% is probably inflated.** Conditional on crossing the threshold early, the observed effect is biased upward. This is the winner's curse, and early stops on small samples are the worst case. Prior odds matter too: a checkout change producing a 4% lift is a large effect for that kind of change, and big early wins are the ones that most often shrink on replication. Also check whether the 4% is relative or absolute. A 4% relative lift on a 3% baseline is only 0.12 percentage points.

3. **Day 6 is a poor stopping point even without peeking.** Six days doesn't cover a full weekly cycle, so the weekday and weekend mix is off. Checkout tests also often show novelty effects that fade. Look at the daily running estimate. If the lift drifted down across days 1 to 6, that drift is your answer.

**The check that would move me:** apply a sequential method that you declare now (alpha spending, or always-valid p-values) to the same data. A p of 0.04 at day 6 probably won't clear it, because early looks face a stricter bar than 0.05. Applying the method only after seeing the result is itself a forking-path move, so treat it as a sanity check, not a rescue.

**Rejected alternatives:**

- **"Peeking doesn't matter for Bayesians, so ship."** In principle the posterior doesn't depend on the stopping rule, but it is only as good as the prior, and here the prior would be picked after seeing the result. That argument licenses exactly what you're trying to avoid.
- **"Just ship, it's reversible."** Reversibility is real, but you'd never learn the true effect, and checkout changes move things beyond conversion, such as order value, refunds and support volume, that six days won't show. This is acceptable only as a holdout-based rollout.
- **"Fix the experiment process."** Worth doing, but it doesn't answer whether to ship this change.

**What I'd do:** Pull the daily running lift and sample sizes, then pick one of two paths and write the stopping rule and analysis down before looking again.

- **Default:** Run to the sample size from a power calculation, keeping a 10% holdout, and decide then.
- **If the change is cheap to revert and the business accepts the risk:** Ship to 90% with a 10% holdout for at least two full weeks, and read the holdout at that point.
