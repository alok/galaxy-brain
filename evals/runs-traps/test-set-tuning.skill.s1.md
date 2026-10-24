# Don't headline 95.1%

**Answer (confidence: high).** Don't report 95.1% as your test accuracy. You picked the best of about 200 configurations by looking at test accuracy, so 95.1% is the maximum of 200 test-set measurements. It is not an estimate of how the chosen model will do on new data, and it is biased upward. The boring answer is the right one: choose the configuration on a validation split (or cross-validation on the training data), then evaluate that single chosen configuration on the test set once. Headline that number. Expect it to come in below 95.1%. How far below depends on how much of your 3.1-point gap over baseline was noise.

**Why part of the gap is probably noise.** Suppose all 200 configurations were actually equally good. Each test accuracy would still wobble from sampling alone. On a test set of 2,000 examples, the standard error at 95% accuracy is about 0.5 points. The expected maximum of 200 such draws lands roughly 2.7 standard errors above the true value, which is about 1.3 points. The configurations are correlated, so the real inflation is somewhat smaller, but it is the same size as the effect you are trying to report. Plug in your own test set size, since it changes this number directly.

**The check.** Rank the configurations by validation accuracy, take the top 10, and evaluate them on the test set. The validation winner's test score is your honest headline. If the top 10 test scores are scattered across a point or so, the 95.1% is mostly selection. If the honest number still beats baseline by a clear margin, the claim survives. If you have no validation split, there is no way to recover an unbiased estimate from a test set you already used for selection. Carve out a validation split and rerun the search, or collect fresh held-out data.

**Check the baseline too.** Was the baseline given the same 200-configuration search budget? If not, the gap mixes the method with tuning effort. Either tune the baseline the same way or say plainly that it was untuned.

**Rejected rungs.**
- Report 95.1% with a footnote saying it was the best of 200 on test. The footnote does not stop the headline from being quoted and compared, and a reader cannot correct a number they cannot see was inflated.
- "Reviewers want one number, so give them 95.1%." Reviewers want one number that means something. The request for a single figure is a reason to pick the honest one carefully. It is also the shape of argument that licenses the bias: the convenience of the headline is doing the work.
- Report the mean across all 200 configurations. This is a valid secondary number, since it describes how an average configuration does. It answers a different question from "how well does our method work," so it is not a substitute for the held-out result.
