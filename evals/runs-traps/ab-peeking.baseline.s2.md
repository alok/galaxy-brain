# Checkout A/B test: stopped at first significance

## Short answer

Don't ship on this result yet. The p = 0.04 does not mean what it appears to mean, and the 4% lift is probably an overestimate. The less obvious problem is not the p-value arithmetic but what stopping at the first crossing does to the effect size.

## The peeking problem

A p-value is valid only for the sample size and stopping rule fixed before the test started. Checking daily and stopping at the first p < 0.05 means the reported 0.04 is the result of a rule that gave the data several chances to cross the threshold. If the true effect were zero, repeated looks at alpha = 0.05 over a couple of weeks push the false-positive rate well above 5%, often into the 15-30% range depending on how many looks there were and how long the test kept running. Six looks alone inflate the error rate; the stop-at-first-crossing rule makes it worse.

So the question is not "is p below 0.05?" but "is this evidence strong under a rule that allowed for this many looks?" Probably not.

## The non-obvious part: winner's curse

Stopping at the first crossing selects for runs where the observed effect was large at that moment. At a small sample, a difference is only significant if the observed lift is big, so early significant estimates are biased upward. A 4% lift from a day-6 stop is the kind of number that often shrinks substantially at full sample. Plan on the true lift being smaller, possibly close to zero. The honest summary is an interval, and its lower bound is probably near zero.

## What to check before deciding

1. **Lift trajectory.** Plot cumulative lift by day with its confidence interval. If the crossing came late after a wobbly path, or the lift was drifting down, that is the signature of noise.
2. **Weekday coverage.** Day 6 is not a full weekly cycle. Checkout behavior varies by weekday, so a partial week is its own bias risk.
3. **Novelty effect.** A new flow often gets a short-lived bump that fades.
4. **Sample ratio mismatch.** Confirm the traffic split matched the design. A skewed split means something else is broken.
5. **Guardrails.** Check average order value, refund and chargeback rate, checkout error rate, and downstream retention. A conversion lift that comes with smaller orders or more returns can be net negative. Optimizing conversion alone is the wrong target.
6. **What "4%" means.** A 4% relative lift on a 3% baseline is 0.12 percentage points. A 4-point absolute lift is huge and would be surprising. Know the baseline before judging the size.
7. **A/A check.** Simulate the same daily-look-and-stop rule on an A/A split. The share of runs that "win" shows how much the rule alone produces. This is a quick, falsifiable way to calibrate how much to trust the 0.04.

## Decision framework

Start from the question: what lift would justify the cost and risk of this change? Compare that break-even lift with the shrunk estimate and its interval, not the point estimate. If the lower bound of the interval is below break-even, you do not yet know the change is worth shipping.

Options, roughly in order of preference:

- **Re-analyze the logged data** with a method valid under repeated monitoring: group-sequential boundaries, an always-valid (mSPRT-style) p-value, or a Bayesian analysis with a prior that shrinks the effect. If the result survives, that is real evidence.
- **Run a confirmation test** with a sample size fixed in advance from a power calculation at the smallest lift you would act on, a fixed end date, and no peeking. If you want interim looks, pre-specify an alpha-spending plan.
- **Ship behind a holdout** if the change is cheap to reverse and low risk. Keep a 5-10% control, watch the guardrails, and record the change as an unverified bet, not a confirmed 4% win.

Bottom line: this is a good hypothesis for a clean follow-up, not a result to ship on.
