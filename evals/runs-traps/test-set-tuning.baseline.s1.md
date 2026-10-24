# Reporting 95.1% from a 200-configuration sweep

The non-obvious problem is not that 95.1% is miscalculated. It answers a different question than the paper will claim. You picked the maximum of about 200 noisy measurements on the test set. That is "the best of 200 settings, chosen by looking at the test set," not "how well this method generalizes." Once the test set has been used to choose the configuration, it is no longer a held-out test set.

## How big the selection effect can be

Assume a test set of N = 1,000 (substitute your real size). At accuracy near 0.95, the standard error of a single measurement is sqrt(0.95 × 0.05 / 1000), about 0.7 points.

If all 200 configurations had the same true accuracy, the expected maximum of 200 independent noisy measurements sits about 2.7 standard errors above the mean, roughly +1.9 points. That alone could account for most of your 3.1-point gap over the 92.0% baseline.

The configurations are not independent, so the real inflation is smaller. But it is not negligible, and you cannot size it without looking at the rest of the sweep. With a smaller test set the effect is larger: at N = 500 the standard error is about 1 point and the inflation approaches 2.7 points.

## Two other things the headline hides

1. **Unequal tuning budgets.** If 200 configurations were tried for your method and the baseline got one run or a default setting, the comparison favors you by construction. Give the baseline the same search budget or say explicitly that it was not tuned.
2. **Seed noise.** One training run per configuration means the 95.1% may partly be seed luck. Check seed variance for both the winner and the baseline.

## What to do instead, cheapest first

1. **Look at the distribution, not the max.** Report the median and top-10 across the 200 configurations. If the median is around 93 and only a few reach 95, say so. If most configurations cluster near 95, the result is robust and the maximum matters much less.
2. **Re-run the top few configurations with fresh seeds.** This is the regression-to-the-mean test. Take the top five by test accuracy, run five new seeds each, and report mean and standard deviation. If the winner falls back toward the pack, the 95.1% was selection.
3. **Compare to the baseline on a paired basis.** Use the same seeds and the same test examples. Run McNemar's test on per-example correctness, or bootstrap a confidence interval on the difference.
4. **For future work, separate the roles.** Select on a validation split (or k-fold cross-validation on training data) and touch the test set once, for the final number.

## A headline that survives review

> Selecting among 200 configurations on a validation split, the chosen configuration reaches 9X.X% ± Y.Y (mean ± s.d. over 5 seeds) on held-out test, versus 92.0% ± Z.Z for the baseline (paired difference +A.A points, 95% CI [lo, hi]).

If the test set was already used for selection, you cannot call the test number held out. Your options are a fresh test set, or re-running the protocol with a validation split. If neither is possible, report the 95.1% as "best of sweep, test-selected" and put the re-run estimate in the headline.

Reviewers who want one number usually accept a single held-out number with its selection procedure stated. What they reject is a maximum over a sweep presented as a generalization result, especially after they find the sweep in the appendix.
