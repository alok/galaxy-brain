## Short answer

Don't put 95.1% in the paper as "test accuracy." You picked the best of about 200 configurations by looking at the test set, so 95.1% is the maximum of 200 noisy numbers. It is not an estimate of how the model will do on new data. The number itself is arithmetically correct. It is the wrong quantity for the headline.

The honest version gives reviewers one number too: select the configuration on a validation set, then report test accuracy once, for that single configuration. Confidence that the 95.1% headline is inflated: high. Confidence about how much: low to moderate, because it depends on your test-set size and on how correlated the configurations are.

## Why the number is inflated

Every configuration's test accuracy carries sampling noise. If the test set has n examples, the standard error of accuracy near 95% is about sqrt(0.95 × 0.05 / n). At n = 1,000 that is roughly 0.7 points. Even if all 200 configurations were equally good, the best of 200 noisy draws lands about 2.5 to 3 standard errors above the true mean. That is roughly 2 points of pure selection luck. Configurations are correlated, which shrinks the effective number of independent draws, so the real inflation is smaller than that, but it is not zero, and you cannot read its size off the 95.1 alone. Plug in your actual n.

The comparison is also lopsided. The baseline got no search. If the baseline had the same 200-configuration budget, with selection on validation, the gap could shrink or disappear.

## The cheapest check

Evaluate the top handful of configurations on data that played no role in choosing them. Ideally that is a fresh held-out set. If you have none, use the test set only to measure how stable the ranking is: bootstrap the test examples and see how often the 95.1 configuration is still the top one. If it is top only in a minority of resamples, the selection is mostly noise.

If the top configuration still scores about 95 on fresh data, the gain is real and the headline stands with a clean number. If it drops toward 93, you have measured the inflation directly, and that is the number to report.

## Options considered

- **Report 95.1% with a footnote saying it is the best of 200 on test.** Honest about the process, but the headline still names the wrong quantity, and most readers will take "test accuracy" at face value. Rejected as the headline.
- **Nested cross-validation.** An inner loop selects the configuration and an outer loop evaluates it, and you report the mean and spread across outer folds. This is the most rigorous option and gives a defensible single number with an uncertainty. It costs roughly the number of outer folds times the sweep cost. Worth it if the sweep is cheap. If not, use a single validation split.
- **A significance test against the baseline.** A paired test on the same examples can say whether the gap exceeds noise, but it does not repair the selection problem. A significant gap measured on a tuned-on-test number is still biased.

## What to write in the paper

"We searched 200 hyperparameter configurations using a validation split. The selected configuration reaches X% on the held-out test set, compared with Y% for the baseline under the same search budget." Fill X and Y from runs that were not used for selection. That gives reviewers the one headline they asked for without the test-set leak.
