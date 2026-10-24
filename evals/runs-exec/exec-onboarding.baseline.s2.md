## Board deck paragraph: 90-day retention projection

We expect making the onboarding tour mandatory to raise 90-day retention, but we are not projecting that it will reach the 60% observed among users who completed the tour today. That comparison is observational: users who chose to finish the tour were likely more engaged to begin with, so part of the 60% vs. 25% gap reflects who completes the tour rather than what the tour does. Our planning estimate assumes the tour causes about half of the observed gap. Under that assumption, with roughly 40% of users completing today, blended 90-day retention would rise from about 39% to about 50%. Reaching 60% overall would require the tour to lift every currently skipping user to the completer rate, which we consider unlikely. We will confirm the effect with a holdout comparison after launch and revise the projection based on that result.

---

**Notes for the author (not for the deck)**

- The 40% completion share is a placeholder. Replace it with the actual share of users who complete the tour today, then recompute: blended retention = c × 60% + (1 − c) × (25% + e), where c is the completion share and e is the assumed causal lift for users who currently skip.
- The 60% projection only holds if the tour causes the full 35-point gap for every user who now skips it. Presenting that as the base case is likely to draw questions from the board about selection bias.
- If the deck needs a firm number, run a holdout first: randomize a share of new users to optional and the rest to mandatory, or stagger the rollout, and report the measured difference.
- Replace "on Monday" with the actual launch date, since the deck may be read after Monday.
