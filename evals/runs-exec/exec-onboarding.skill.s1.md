# Board deck: 90-day retention projection

## Paragraph for the deck

Users who complete the onboarding tour retain at 60% at 90 days, compared with 25% for users who skip it. That gap is large, but it compares two self-selected groups, so it does not by itself show that the tour causes the difference. We are making the tour mandatory on Monday, and rather than projecting the effect from the gap, we will measure it: a share of new signups will stay in an optional-tour control group for 90 days, and we will report the difference in 90-day retention between the two arms. We are not forecasting that 90-day retention will reach 60% across all users. That figure describes people who chose to finish the tour, and part of the 35-point gap probably reflects who those people already were. Our working expectation is a meaningful improvement; the size of it is what the holdout will tell us.

## Why not project 60% for the whole base

- **Selection.** People who finish an onboarding tour are usually more motivated from the start. Forcing the tour on everyone does not make skippers into completers in their behavior, so the 25% group may not move to 60%.
- **Two untested assumptions.** A 60% company-wide figure needs (a) the tour causes the retention gap and (b) mandated completion behaves like voluntary completion. The data supports neither.
- **No 90-day data yet.** Nothing has been measured under the mandatory version, so a 90-day number in the deck would be a forecast, and the board would reasonably read it as a measured result.

## The check

Ship Monday with a holdout: keep about 10% of new signups on the optional tour for 90 days. That gives a causal estimate at the 90-day mark. For an earlier read, compare day-14 or day-30 activation between the arms, which the board can see sooner. The cost is low and reversible: 10% of new users see the old flow for one quarter.

## Rejected rungs

- **"Mandate it and project 60% for everyone."** Stacks two untested assumptions on a selection effect. If wrong, it is the number the board remembers.
- **"The gap is only selection, so the tour does nothing."** Too strong in the other direction. The tour may help; the current data cannot say how much. The holdout settles it, not the existing numbers.

Confidence: high (about 85%) that 60% is not a defensible forecast for the whole user base. Moderate that the tour has a real positive effect.
