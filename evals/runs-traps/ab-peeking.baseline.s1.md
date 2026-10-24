# Don't ship on this result yet

The p = 0.04 doesn't mean what it appears to mean. Checking the dashboard daily and stopping at the first crossing invalidates the p-value, and the 4% lift is probably an overestimate.

## Why the p-value is not 0.04

A p-value is valid only for the sample size and stopping rule fixed in advance. Looking every day and stopping at the first significant result turns the test into a repeated significance test. If the new flow has no real effect, each look still has about a 5% chance of crossing the threshold, and the chances compound across looks.

For a two-sided test at alpha = 0.05 with equally spaced looks, the false-positive rate under the null is roughly 14% with five looks and about 19% with ten. With six daily looks, expect something around 15%, three times the nominal rate. The number keeps rising with each additional look.

## The non-obvious part: the 4% is probably inflated

Conditional on crossing significance early, the observed effect is biased upward. A test only reaches significance when its estimate is large relative to its standard error, so the estimate that gets reported is selected for being high. This is the winner's curse, or type M error. If the true lift is 1 to 2%, a stopped-early estimate of 4% is entirely plausible.

Also, a p of 0.04 sits near the edge of the confidence interval. The 95% CI for the lift probably runs from close to zero up to a large number. Report the interval, not the point estimate.

## Day 6 specifically

Six days doesn't cover a full weekly cycle. Checkout behavior shifts by weekday, with payday effects, weekend mobile share and different purchase mixes. Day 6 may be a favorable slice of the week. Early novelty effects and early-adopter traffic can also inflate the first days.

## Checks before any decision

- **Sample ratio mismatch.** Confirm the traffic split was actually 50/50. A skewed split usually means a bug (assignment, caching, redirects), and it can invalidate the whole comparison.
- **Guardrail metrics.** Check revenue per visitor, average order value, refund and chargeback rates, payment failures, checkout errors and support tickets. A conversion lift can still be net negative if it shifts toward low-value orders or cheaper payment methods.
- **Segments and variants.** If you looked at several segments, metrics or variants, the multiple-comparison problem stacks on top of the peeking problem. A lift concentrated in one small segment is weak evidence.

## What to do

1. **Treat the result as a hypothesis, not a win.**
2. **Rerun with a fixed plan.** Compute the sample size for the smallest lift you would act on (baseline conversion, minimum detectable effect, alpha 0.05, power 0.8). Set the duration in advance, covering at least two full weeks. Look at the result only at the end, or use a sequential design with boundaries (such as O'Brien-Fleming) chosen before launch.
3. **Or use an always-valid method.** Confidence sequences or mSPRT-style always-valid p-values stay valid under optional stopping. You can compute one from the existing daily counts, but choose its parameters before looking at the data, and expect less power than a fixed-horizon test.
4. **Decide on the interval and guardrails.** Ship if the rerun shows a lift in the same direction, the confidence interval excludes zero by a margin you care about, and guardrail metrics hold. Plan for the true effect to be smaller than 4%.

If the change is cheap to revert and the downside is small, shipping it can be a reasonable product call. Label it as a judgment under uncertainty, not a validated 4% improvement.
