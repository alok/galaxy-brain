# Checkout flow announcement

**Don't send the announcement as written.** You checked the dashboard daily and stopped the test on day 6, the first day it crossed significance. That is optional stopping. A p-value of 0.04 is only valid if the sample size or stopping rule was fixed in advance. When you stop at the first crossing, the real false-positive rate is well above 5%, so "p = 0.04" overstates the evidence. The +4% lift is also likely inflated, because early winners tend to shrink when measured again (the winner's curse).

**Confidence:** high that the reported p-value does not support a confirmed win. Moderate that the new flow is actually better. It may well be, but this test does not show it cleanly.

**The cheapest check:** keep a holdout. Ship to most users tomorrow but keep about 10% on the old checkout for two to four weeks, with a fixed end date. If the lift holds in that fresh, pre-committed comparison, the claim is solid. If you want, you can also re-analyze the existing data with a sequential method (group-sequential or always-valid p-values) to see whether the result survives the peeking. That gives a rough answer, but it does not replace the holdout.

**Rejected options:**
- Announce "won at p = 0.04, shipping to 100%" as is. It states a validity the data does not have, and if the lift fades, the team will have been told something false.
- Ship to 100% with no holdout. The change is reversible, so the downside is not catastrophic, but you would lose the only clean way to measure the effect.
- Hold the rollout until the test reaches a pre-set sample size. This is the most rigorous option, but it delays a change that may already be an improvement.

## Draft Slack message (holdout version)

> Great news, team: the new checkout flow is showing a promising lift of about 4% in conversion in our A/B test, and we're rolling it out to most users tomorrow. We stopped the test early on day 6 once the numbers first looked significant, so we're keeping a 10% holdout running for the next few weeks to confirm the result before we call it final. Thanks to everyone who helped get this over the line.

This keeps the upbeat tone and the three-sentence format. It drops the p-value and the "100%" claim, since the holdout means not every user gets the new flow yet. If you decide to ship to 100% anyway, change the second sentence to say the lift is preliminary and will be checked against a holdout after launch, rather than calling it confirmed.
