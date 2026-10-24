# Round 2: galaxy-brain applied to its own SKILL.md

**Input:** round-1 `SKILL.md`, judged fresh (round-1 LADDER.md and round-0 files not read).

**Problem:** How should this SKILL.md change so that a model using it beats the same model with no skill? Better means it finds better framings when they exist, resists clever-but-wrong conclusions, and holds back on narrow questions. Constraints: the text is loaded on every use, so length costs something, and a human must be able to read it in two minutes.

## Gate

Climb. This is an open design question with no obvious answer, and the user asked for the procedure explicitly. Rung 1 ("change nothing") is a live candidate.

## Ladder

| Rung | Move | Claim | Distinguishing prediction | Verdict |
|---|---|---|---|---|
| 🧠 1 | obvious | Change nothing | On a blind A/B over three prompt sets (narrow, real reframe, seductive trap), the skill matches or beats no-skill on all three | **Survives** |
| ✨ 2 | zoom in | Test 6 contradicts "every rung above 1 must pass all six". It describes the top rung and says "say so" rather than kill. Reword it as a pass/fail test | None on verdicts. Partway up the ladder, a rung that restates rung 1 is already caught by the merge rule, so the outputs come out the same | Dies on 1: the text is inconsistent, but no verdict changes, so the fix is cosmetic |
| 🤯 3 | zoom in | "Output" reads as unconditional, so a gated narrow answer might still grow a table and a verdict block. Fix: retitle it "Output (when climbing)" | On narrow prompts, the rate of table or verdict-block output falls | Dies on 5 until there is evidence. The argument gets its force from my search for defects, not from any observed failure. The gate comes first, is bolded and says exactly what to output. The reverse argument is just as plausible. Revives if the experiment below finds the failure |
| 🌌 4 | invert | Survival is judged from the armchair by the model that wrote the rung, which favors the higher rung. Add a rule: if two rungs survive and the evidence that separates them is not in hand, take the lower one | More rung-1 and rung-2 verdicts on prompts where the clever rung cannot be checked | Dies on 3. The chain needs all of these: armchair survival over-favors high rungs (~0.6), tests 3 and 4 plus the confidence number fail to correct that (~0.4), and tie-breaking downward helps more than it suppresses real reframes (~0.5). Combined: ~12%. The rule also double-counts tests 3 and 4, and it would flip the worked example's correct rung-3 verdict |
| 🪐 5 | zoom out | 845 words is more than two minutes of reading. Cut toward ~500 | A shorter text uses less context, with no loss of behavior | Dies on 4. The prose is ~600 words, and the 161-word table gets skimmed, so it reads in about 2 minutes at 300 wpm. Reaching 500 words means cutting the worked example or the move glosses. Those carry the calibration, and losing them is a quiet regression that is hard to detect. Small trims are cosmetic |

Merged into rung 1: a **change the layer** reframe ("the text can't be improved by armchair critique; improve the eval harness"). It leads to the same SKILL.md action as rung 1, so it becomes rung 1's receipts and the experiment below. **Horseshoe:** the climb curved back to rung 1, and that is the answer.

## Descent notes

- **Clever-arguer, critique bias.** The task asks me to critique, which rewards finding changes. Rungs 2 and 3 are the shape that bias produces: a real textual nit that changes no observable behavior. Rung 2 is killed by the absence of any distinguishing prediction. Rung 3 is killed because its only support is the search incentive.
- **Clever-arguer, counter-bias.** "The skill is a fixed point of itself" is exactly the satisfying ending this skill rewards (test 6). Rung 1 does not rest on that elegance. It wins because each rival fails a specific test: 2 changes no verdict, 3 has no evidence, 4 has a weak chain and contradicts the worked example, 5 makes an unbounded cut for a constraint that is already met.
- **Self-reference caveat.** Rung 4's point applies to this verdict too. The same model judged its own text from the armchair. That is why confidence is 70% and not 90%, and why the experiment below is behavioral.

## Verdict

**FIXED POINT.** Rung 1, ~70%.

**Cheapest discriminating experiment (rung 1 vs. rung 3):** run the current skill on 5 narrow prompts with obvious answers, e.g. "time complexity of binary search?" or a one-character typo bug. If 1 or more of the 5 outputs contains a ladder table or a verdict block, rung 3 revives, and the fix is two words ("Output (when climbing)"). If none do, rung 1 stands. The fuller receipt for rung 1, not run here, is the blind three-set A/B in the rung-1 row.
