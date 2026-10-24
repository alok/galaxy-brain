**Don't ship mandatory onboarding on Monday as a retention fix. The 60% projection is a comparison between two self-selected groups, not a forecast of what a mandatory tour would do.** Confidence: about 80% that the projection is wrong. About 60% that the tour helps at all in its current form, which is why it is worth testing rather than dismissing.

**Why the gap isn't the effect**

- **Who finishes an optional tour is not random.** People who finish it tend to be more motivated and more likely to have a concrete task. People who skip include experienced users, people who came in through a referral or team invite with an existing workflow, and people who wanted one thing and left. Forcing skippers through the tour does not make them into the people who finished it.
- **A gate changes who counts as "completed."** Some people who would have left at the gate will now click through it without absorbing anything. They join the completed group with a weaker retention profile than today's completers, so the 60% is likely to fall.
- **The comparison leaves out everyone who never reached the tour.** A mandatory gate can cost signups before any retention question arises. A 60% vs 25% comparison among people who got through the door says nothing about the ones who bounced at it.
- **The projection assumes the causal effect is real and complete.** If the tour has no causal effect, retention stays at today's blended rate. If it has the full effect the gap suggests, overall retention approaches 60% only in the best case, and anything less lands between. "About 60%" is a ceiling under your own assumption, not a forecast.

**Timing.** A 90-day retention number cannot be observed for anyone who signs up after Monday until late January 2027. You would be committing to a projection you cannot check for three months.

**The check.** Randomize new signups, starting now, between the mandatory tour and the current flow. Measure 90-day retention on an intention-to-treat basis, meaning all assigned users, not just completers. Also measure signup-to-activation at the gate, since that cost is invisible in the retention number. Ship mandatory to everyone only if the retention lift has a confidence interval that excludes zero and is large enough to justify whatever the gate costs in signups. For a faster early read, use an activation metric such as first meaningful action within 7 days. That is a proxy, not a substitute for the 90-day result.

**If you must ship Monday,** roll it out to 50% behind a flag. That gives you the holdout and a clean way to reverse.

**Rejected rungs**

- *Mandatory tour for everyone now:* treats a selection gap as a causal effect, and turns the gate into a churn risk for users who skip for good reasons.
- *Hard-gate only new users who skip:* same causal assumption and the same problem, applied to a narrower group.
- *Tour completion as the target metric:* completion is a proxy for activation, and forcing it inflates the number without showing that users got value.
- *Shorter tour that ends at the first real action:* the most promising alternative, but it is still an untested gate. It belongs in the experiment as a variant, not as a conclusion.

The boring answer is right here: test the tour before you mandate it.
