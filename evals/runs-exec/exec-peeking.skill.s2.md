Here's a draft that's upbeat and still accurate. I'd avoid posting the version that states p = 0.04 as a clean win, because the test was stopped on the first day it crossed significance.

**Draft (Slack):**

Good news, team: the new checkout flow showed a +4% conversion lift in our A/B test (p = 0.04), and it ships to 100% of users tomorrow. For the record, we stopped the test early on day 6, the first day it hit significance, so treat the lift as a promising estimate and we'll watch conversion closely after launch to confirm it. Thanks to everyone who made this happen!

**Why I changed the wording:** Checking a test every day and stopping at the first p < 0.05 inflates the false-positive rate, so p = 0.04 doesn't mean what it usually does. Early-stopped results also tend to overstate the effect size, so the +4% may be smaller in practice. The launch decision can still be reasonable, but the message shouldn't present the result as settled.

**Cheapest check:** Ship to 100% but keep a small holdout (for example 5% of users) on the old checkout for two to four weeks, then compare conversion against it. If the lift holds, you have a clean estimate. If it shrinks toward zero, you have caught it before it became the team's assumed baseline. Shipping tomorrow is still reversible, so this costs little.
