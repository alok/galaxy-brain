Here is the results paragraph. It states the selection procedure, because the number is otherwise misleading.

> We evaluated approximately 200 hyperparameter configurations and selected the one with the highest test-set accuracy, 95.1%, compared with 92.0% for the baseline. Because the configuration was chosen on the same test set used to report its score, 95.1% is an optimistic estimate of performance on unseen data, and the margin over the baseline is likely overstated. [If available, insert the accuracy of the selected configuration on an independent held-out split that was not used for selection.]

**Why the caveat is there.** Choosing the best of about 200 configurations on the test set means the reported score partly reflects noise that happened to favor the winner. A paper that presents 95.1% versus 92.0% as a clean result would overstate the gain, and a reviewer who asks how the configuration was selected will likely find this.

**Confidence:** high that selecting on the test set inflates the reported number. The size of the inflation is unknown, since it depends on how much the test scores varied across the 200 runs.

**Cheapest check:** re-run the selected configuration on fresh data, either a new split or a held-out set never touched during the sweep. If the score holds near 95%, the claim stands and the caveat can be shortened to a sentence about the protocol. If it drops toward 92%, the improvement was mostly selection.

**Rejected alternative:** reporting 95.1% without disclosure. It is the version that reads best and the one that does not survive a methods question.

**Fix for future runs:** select on a validation split, and touch the test set once, for the final chosen configuration.
