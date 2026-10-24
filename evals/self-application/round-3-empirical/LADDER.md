# Round 3: galaxy-brain applied to its own eval result

Rounds 1–2 were armchair self-critique, and round 2 declared a fixed point. Then the blind A/B came back (see `evals/results-v0.1.json`): **the skill lost 4–8** against the same model with no skill. Two independent blind Opus judges preferred the baseline on slack, rust-rewrite and resume (both judges), split on latency and keyerror, and preferred the skill only on odd-squares (both judges).

The judges' stated reasons cluster tightly: "emoji rung table adds ceremony", "jargon ('horseshoe')", "a ladder whose last rung has no content", "same reasoning in plain prose is cleaner". Content was rated comparable or better; packaging lost.

So this round asks the skill about its own failure. **Written before the v0.2 results came in.**

| Rung | Move | Claim | Distinguishing prediction | Verdict |
|---|---|---|---|---|
| 🧠 1 | obvious | The skill doesn't help Opus; delete it | v0.2 still loses by a similar margin | Survives as the null; the experiment decides |
| ✨ 2 | zoom in | The losses are format, not content: judges penalize the visible table, emoji and skill jargon. Keep the procedure, but make the ladder private working and deliver prose: answer first, the check, rejected options in one clause each | v0.2 closes most of the gap on slack/rust/resume, and keeps the odd-squares win | **Survives.** Every judge reason on a loss names packaging |
| 🤯 3 | change the objective | The skill should only fire when the user invokes it by name; on "non-obvious take" prompts, plain Opus is already good | The trigger description gets narrower; nothing else changes | Dies on 1 for this experiment: the eval prompts all say "non-obvious take", so it predicts the same outcomes as rung 1. Kept as a fallback if rung 2 fails |
| 🌌 4 | invert | Trap prompts can't be won: Opus already refuses the bad move, so the descent has nothing to catch, and H2 was never testable on this model | On trap prompts, v0.2 ties at best | Survives as a note: H2 needs a weaker model or subtler traps |

**Change (v0.1 → v0.2):** the Output section now delivers prose, not the table. The worked example shows both the working and what the user reads. The gate no longer announces "no ladder needed". Word count goes from 845 to 967.

**Pre-registered:** one revision only. Both v0.1 and v0.2 numbers get reported whichever wins. Same 6 prompts, same baseline outputs, same judge prompt, same seeds. Overfitting risk: 6 prompts is tiny, and this revision was fit to the judges' complaints on them.
