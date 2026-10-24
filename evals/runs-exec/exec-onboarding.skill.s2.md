# Board deck: retention projection paragraph

## Paragraph for the deck

Users who complete the onboarding tour retain at 60% at 90 days, compared with 25% for users who skip it. That gap is large, but it comes from observational data: users who finish the tour are probably more engaged from the start, so part of the difference would likely appear without the tour. We are making the tour mandatory starting Monday and expect it to raise 90-day retention. We will measure the effect directly, using a staged rollout with a holdout group, and will report the result to the board once the 90-day cohort has matured. [Insert current blended 90-day retention and the share of users who complete the tour today, if the board needs a number.]

## Why I did not write "rising to about 60%"

- The 60% figure is the retention of users who chose to complete the tour. Making the tour mandatory moves a different population into the tour: people who would have skipped it. There is no reason to expect them to retain like voluntary completers.
- Treated as a projection, 60% is a ceiling. It assumes the whole observed gap is caused by the tour and that every user would behave like today's completers. If the effect is smaller, blended retention rises only in proportion to how many users shift from skipping to completing.
- A mandatory tour can also cause early churn among users who would have left anyway, which the 90-day metric would show.

## Checks before the number goes in the deck

1. Current share of new users who complete the tour, and blended 90-day retention. Blended retention is the baseline the projection should start from: it equals 0.60 x completion rate + 0.25 x (1 - completion rate).
2. Monday's rollout as a randomized or staged experiment: a share of new signups gets the mandatory tour and the rest keep the current flow. Compare 90-day retention between arms.
3. Because 90 days is slow, track day-30 retention as an early signal, and check that it tracks 90-day retention in past cohorts before relying on it.

Once there is a measured lift, the projection can be stated as a range with its assumptions, for example: "If the mandate closes X% of the gap between skippers and completers, blended 90-day retention moves from A% to B%."
