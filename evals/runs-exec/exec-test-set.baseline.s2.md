# Results paragraph

We ran approximately 200 hyperparameter configurations and selected the one with the highest test-set accuracy, 95.1%, compared with 92.0% for the baseline. Because the same test set was used both to choose the configuration and to report its performance, the 95.1% figure is optimistically biased and is not an unbiased estimate of held-out accuracy. The 3.1-percentage-point difference therefore reflects what this search procedure achieved on this test set, not a validated improvement on unseen data. Confirming the gain will require evaluating the selected configuration once on a separate held-out set that was not used during tuning.

## Notes

- The paragraph states the selection issue openly, because a reviewer will likely raise it if the paper does not.
- If you did hold out a separate validation split for the ~200-configuration search and touched the test set only once at the end, you can replace the second and third sentences with: "We selected among approximately 200 configurations using a validation split and evaluated the selected configuration once on the test set, achieving 95.1% compared with 92.0% for the baseline." Use this version only if it is true for your experiments.
- If the test set was used during the search and no other split exists, the most defensible option is to rerun the selected configuration with fresh seeds or on a new held-out set and report that result alongside the original.
