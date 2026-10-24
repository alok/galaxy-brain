# Mandatory onboarding: why the 60% projection is probably wrong

The 35-point gap between completers and skippers mostly reflects who chooses to finish an optional tour, not what the tour does. Making the tour mandatory changes who is in the cohort and how skippers behave, so 60% is the completers' rate, not a forecast for everyone.

## 1. The gap is mostly selection

People who finish an optional tour tend to be more motivated, more curious, and more likely to arrive with a concrete job to do. They are also more likely to be on the device, plan, or account type where the product works best. Those traits predict 90-day retention whether or not the tour exists.

The skippers you would force through are not a random sample of skippers. Some of them are the users least likely to stick around under any circumstances. A mandatory tour changes their first session, but not necessarily their intent.

## 2. The projection assumes the causal effect equals the correlation, for everyone

"About 60%" implies that every current skipper ends up with completer-level retention after a mandatory tour. That requires the tour to cause the entire gap and to work equally well on people who chose to skip. Neither is likely.

Illustrative arithmetic, assuming 40% of users complete today:

- Today: 0.4 x 60% + 0.6 x 25% = 39% overall.
- If the tour gives skippers a real but modest lift to 33%, with completers unchanged at 60%: 0.4 x 60 + 0.6 x 33 = about 44% overall.
- Overall reaches 60% only if skippers jump all the way to 60%.

A plausible outcome sits in the low-to-mid 40s. Treat any number near 60 as a warning sign.

## 3. Cohort composition can raise the metric for the wrong reason

If mandatory onboarding adds friction at signup, some low-intent users who would have signed up and churned will now leave before an account exists. Retention is measured on signed-up cohorts, so removing the weakest users from the denominator raises the percentage without improving anyone's experience. The change can look like a win on retention while losing signups, revenue, and top-of-funnel volume.

Check signup volume and signup-to-activation conversion by cohort alongside retention. Compare absolute retained users, not just the percentage.

## 4. Some skippers are not new users

Skippers include people who already know the product: invited teammates, returning users, and people who came from docs or a colleague. A forced tour is pure friction for them, may raise their churn risk, and can read as condescending. This group is unlikely to be in the "should double" bucket.

## 5. Check when completion happens

If many tour completions happen on day 20 or 30, the tour may be a symptom of already being engaged rather than a cause. Look at completion timing relative to signup and to the first key action. Completion after value is a marker of retention, not evidence for it.

## 6. Monday cannot validate a 90-day outcome

No 90-day retention data will exist by Monday. The 60% figure is a forecast with no supporting data behind it, and it should not go into the plan as a target.

## What I would do instead

- **Randomize.** Hold out a slice of new signups (10 to 20%) on the current optional flow and ship mandatory to the rest. Compare 90-day retention, with signup volume and day-7 activation as early signals. This is the only clean way to measure the causal effect.
- **If you cannot randomize,** look for a natural experiment in history: a period when the tour was broken, the skip button moved, or a past A/B test touched onboarding. You can also model retention using pre-signup covariates (channel, device, role, referral source) to estimate the gap among users with similar profiles.
- **Pre-register the prediction.** Write down an expected range (for example, 40 to 48%) and what would count as failure, so the result cannot be reinterpreted after the fact.
- **Set guardrails now:** signup conversion, onboarding-related support tickets, and early drop-off or uninstall rates. Friction costs show up within days, while retention effects take months.

## Bottom line

The correlation is real, but it is not evidence that the tour causes the gap. A mandatory tour will likely help some skippers and hurt others. The net effect is probably a modest lift in overall retention, not a doubling. Ship only with a holdout, and do not commit to 60%.
