# Slack announcement: new checkout flow

## Requested draft (3 sentences, as asked)

Great news, team: the new checkout flow won its A/B test, lifting conversion by 4% (p = 0.04). Huge thanks to everyone who helped design, build, and monitor it. It rolls out to 100% of users tomorrow, so let's keep an eye on the dashboard together as it goes live!

## Recommended draft (same length, calibrated)

Early results from the new checkout flow look promising, with a +4% conversion lift (p = 0.04) when we stopped the test on day 6. Because we checked the dashboard daily and stopped at the first significant result, we're treating this as a strong signal rather than a settled finding. We're rolling it out to 100% of users tomorrow with a holdout group so we can confirm the lift holds, and thanks to everyone who made this happen!

## Why the second version

Stopping the test on the first day it crossed p < 0.05 is optional stopping. Checking daily and stopping at the first significant look means the nominal p = 0.04 no longer carries its usual meaning: the real false-positive rate is well above 5%. The +4% estimate is also likely inflated, since results that first cross the threshold tend to overstate the true effect (the winner's curse).

Options that keep the result honest:

1. Confirm with a fresh run. Keep a holdout group at the rollout, or rerun the test to a pre-set sample size, and check whether the lift persists.
2. If the test was designed for sequential monitoring (group sequential boundaries or always-valid p-values), re-analyze with that method. A plain p = 0.04 is not valid here.
3. If you ship tomorrow anyway, the recommended draft tells the team what was actually observed, so nobody builds later plans on a lift that may shrink.
