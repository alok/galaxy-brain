# The 60% vs 25% gap mostly reflects who people are, not what the tour does

The non-obvious point is that the comparison you're using to forecast the effect is the one least able to measure it. People who finish an onboarding tour differ from people who skip it before the tour has any effect: they tend to be more motivated, more curious, and more likely to have a use case that fits the product. Those same traits predict whether someone is still around at day 90. So the 35-point gap is some mix of causal effect and selection, and selection probably accounts for most of it.

Mandating the tour changes what the skippers do, not what they intend. They will click through or sit through it, but their underlying fit with the product stays the same. Their 90-day retention will move toward that of people with similar intent who happened to skip, not toward the 60% of voluntary completers. Projecting 60% assumes the tour is what causes the trait that drives retention. There is no evidence for that.

Illustrative arithmetic, with made-up numbers: suppose half of users complete the tour today. Overall retention is 0.5 x 60 + 0.5 x 25 = 42.5%. If mandatory onboarding adds a generous 5 points to the skippers' retention (to 30%), the blended figure becomes about 45%, a lift of roughly 2.5 points. The 60% projection is what you get only if the entire gap is causal and fully transfers to forced users. That is the one scenario you can rule out cheaply.

Other things that can go wrong:

- **Friction at the front.** Mandatory gates lose people who would have stayed but won't sit through a tour. That shows up first as lower activation and signup completion, and it can offset any retention gain.
- **Completion stops meaning anything.** Once the tour is forced, "completed" means "did not close the window." The completed group's retention gets diluted with users who wouldn't have engaged anyway, so completion rate is no longer a useful signal.
- **Metric definition.** Check how 90-day retention is defined and when tour completion is logged. If completion is recorded only for users who came back, the 60% is conditioned on survival and inflated by construction.
- **The tour may not deliver the thing that matters.** If the retention effect comes from a specific early action (connecting data, creating a first project), a tour may not produce that action. Prompting the action inline could be the real intervention.

How to find out, before Monday if possible or shortly after:

- **Randomize.** Assign a random 10-20% of new signups to mandatory tour versus current behavior. Analyze by assignment (intention to treat), not by completion. Retention among assigned users is the number the launch projection should be built on.
- **Pre-register the prediction.** Write down the expected lift before the test runs. If the honest guess is 0 to 3 points, a result of 8 points is worth investigating, and a result of 0 is a finding about the tour, not a failed launch.
- **Look for a natural experiment in existing data.** Any past period when the tour was forced, prior A/B tests on tour prompts, or users who skipped because of a bug or a skip-button rollout will give cleaner comparisons than the completer/skipper split.
- **Watch activation and signup conversion alongside retention.** Those will move first and are the early warning for the friction problem.

Bottom line: don't project 60%. The defensible claim today is that completers retain better, which you already knew. Whether mandating the tour causes retention to rise is an empirical question a holdout can answer in a few weeks. My expectation is a small single-digit lift on overall retention, possibly partly offset by friction. If Monday is fixed, ship it behind a flag with a holdout so the launch teaches you something, and don't report 60% as the outcome.
