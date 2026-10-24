We conducted a hyperparameter search over approximately 200 configurations and selected the configuration with the highest test-set accuracy. The selected configuration achieved 95.1% test accuracy, compared with 92.0% for the baseline. Because selection used the test set, the reported 95.1% is optimistically biased relative to performance on unseen data, so the 3.1-point gap should be interpreted with that caveat. An unbiased estimate would require selecting configurations on a separate validation split and evaluating the chosen configuration once on the test set.

---

Notes for the authors (not part of the paragraph):

- The bias comes from choosing the best of about 200 configurations by test accuracy. The more configurations searched, the larger the expected optimism, and the 3.1-point gap may shrink under a clean protocol.
- If you can rerun, the cleanest fix is a validation split for the search, with a single final test evaluation of the chosen configuration. The paragraph above then becomes a plain results statement.
- If you cannot rerun, keep the disclosure sentence. Also state whether the baseline received a comparable search budget, since an untuned baseline versus a 200-configuration search is a second source of advantage.
