# The 95.1% is not a clean test accuracy

The non-obvious problem is not the 200 runs. It is that you chose the configuration by looking at test-set accuracy. Once you pick the maximum over test scores, the number you report is a validation score that happens to be computed on the test set. It is biased upward, and the size of the bias depends on how many configurations you tried and how noisy the estimate is, not on whether the chosen configuration is any good.

## Noise alone can produce this number

Assume a test set of n = 1,000 examples (substitute your own n). At roughly 93% accuracy, the sampling standard error is sqrt(0.93 × 0.07 / 1000), about 0.8 points.

Now suppose every configuration has the same true accuracy of 93%, so hyperparameters do nothing. The maximum of 200 independent noisy estimates is about the mean plus 2.7 standard errors, which is roughly 93 + 2.2 = 95.2%. Your 95.1% is what pure noise would produce. Real configurations are correlated, so the exact figure will differ, but the order of magnitude holds.

## The comparison is also lopsided

- The method received about 200 configurations of tuning. The 92.0% baseline presumably received one or none. Part of the 3.1-point gap may measure search effort, not the method.
- The gap looks large, but it compares a selected maximum against an unselected number. That is not a like-for-like difference.

## What to report instead

1. **Best option, if the data allows:** a fresh held-out set that was never used for selection. Pick the configuration on validation data, then evaluate that one configuration once on the untouched test set and report that number.
2. **If the test set is all you have:** nested cross-validation. The outer loop estimates the performance of the whole procedure ("tune 200 configurations, then pick the best"). Report the outer-fold mean and spread.
3. **If you must keep this test set:** label the number honestly, as "best of 200 configurations, selected on this test set, optimistic." Also report the distribution across all 200 configurations (median, and the fraction that beat the baseline) so readers can see how much of the result is selection.
4. **Give uncertainty with any headline number.** At n = 1,000, the 95% interval around 95.1% is roughly ±1.3 points. For the comparison with the baseline, use a paired test on the same examples (for example McNemar's test) rather than comparing two independent point estimates.

## A quick diagnostic

Look at the spread of test accuracy across all 200 configurations. If most of them fall within about a point of each other, the hyperparameters barely matter, and the gap over the baseline is more likely an artifact of search than a property of the method. If the spread is wide, your headline is one draw from a lottery.

## On the reviewers

A reviewer who asks how the configuration was chosen will find the answer quickly. A paper that reports "95.1% test accuracy" after selecting on the test set is exposed to that question. A lower number from a procedure that never touched the test set is defensible, and it is the one that answers what the paper claims.
