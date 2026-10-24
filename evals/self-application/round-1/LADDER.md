# Round 1: galaxy-brain applied to its own SKILL.md

**Input:** `round-0/SKILL.md` (814 words).
**Problem:** How should this SKILL.md change so a model using it beats the same model with no skill? "Better" means three things: it finds better framings when they exist, it does not get talked into clever-but-wrong conclusions, and it shows restraint (no ladder) on narrow questions with obvious answers. Constraints: the file is loaded on every use, so length costs something, and a human must be able to read it in two minutes.

**Gate:** this is not a narrow question with an obvious answer, so we climb.

## Defects found in round 0 (evidence for the rungs)

Each one can be checked against the text:

- **D1. The example breaks the output spec.** Output asks for "a confidence level" and "the single cheapest experiment". The example's verdict has no confidence, and it names two checks: the durations profile and the fan-out measurement. Models copy examples more than they follow prose specs.
- **D2. The example's dead rung is a strawman.** Rung 4 ("delete the slow tests; types will catch it") has no prediction (`—`), so it would die on test 1 before reaching the test 2 the table cites. The table also doesn't name the killing test by number, though Output requires it. What this teaches: only silly rungs die.
- **D3. The verdict has an anchor.** "Often that is rung 3" states a base rate nobody measured, and the example also lands on rung 3. Both push verdicts toward rung 3 whatever the problem is.
- **D4. The restraint gate comes last.** "When not to climb" is the final section but one. A model reading top-down has already committed to the table-and-descent format before it reaches the gate. The repo's restraint prompt (`keyerror`) contains "Give me the non-obvious take", so it matches the trigger. That leaves the gate as the only defense.
- **D5. The trigger is too broad.** "first-principles or 'what am I missing'" matches routine debugging questions ("what am I missing, this loop never ends"). The description has no negative trigger.
- **D6. The climb has a padding floor.** "Generate 3–5 rungs" forces a third rung even when there is only one real reframe. "Three rungs is usually enough; five is the ceiling" says the same thing again in Output.
- **D7. Test 2 has a loophole.** "Argues, with evidence, that the stated problem is the wrong one" lets the argument count as its own evidence. That is exactly how the "most common galaxy-brain failure" the test names gets through.
- **D8. Test 6 doesn't fit "every rung must pass all six".** Horseshoe asks about "the top rung", so it isn't really a per-rung check.

## Ladder

| Rung | Move | Claim | Distinguishing prediction | Verdict |
|---|---|---|---|---|
| 1 | obvious | Change nothing. The skill is coherent and already has a gate, a descent and an example. | An A/B of round 0 vs any revision shows no difference on `evals/prompts.json` | Baseline. Loses to rung 3 if the experiment below shows a difference. |
| 2 | zoom in | Fix only where the skill contradicts itself: the example's verdict (D1), the killing-test label (D2), the duplicated rung count (D6) | Round-0 verdicts leave out the confidence level, or list more than one experiment, more often than round-1 verdicts | Survives. Folded into rung 3, because both edit the same lines. |
| 3 | invert | Ask what would guarantee each goal fails, and remove each cause. Restraint fails with a broad trigger plus a late gate (D4, D5). Clever-but-wrong survives when only strawmen die and test 2 is open (D2, D7). Verdicts are biased by an anchor (D3). Padding comes from a floor (D6). | On `keyerror`, round 1 builds a ladder less often. On `resume` and `rust-rewrite`, round 1 lands on rung 1 or 2 at least as often. Verdict rungs cluster less on 3. | **Survives** |
| 4 | change the objective | Return the *best* surviving rung, not the *highest*, because "highest" still favors cleverness among survivors | Outputs differ only when a higher survivor has lower expected value than a lower survivor | Dies on 1. Test 4 already makes each rung beat the one below on downside and prefers the reversible move, so I could not build a case where the outputs differ. |
| 5 | dissolve | The value over no skill is all in the descent and the gate. Models reframe fine unprompted, so delete the climb and the named moves (about 25% shorter). | Framing quality on reframe-win prompts is the same with or without the moves | Dies on 2. It drops the only section aimed at goal 1 (better framings) with no evidence that goal is already met. |

A sixth candidate (*change the layer*: "don't edit until the A/B in `evals/prompts.json` has run") recommends the same action as the verdict's experiment, so it is merged into the verdict.

## Descent (all six tests, rungs above 1)

| Test | Rung 2 | Rung 3 | Rung 4 | Rung 5 |
|---|---|---|---|---|
| 1. Pays rent | Pass: predicts more verdicts with a confidence level and one experiment | Pass: predicts fewer ladders on `keyerror` and fewer rung-3 verdicts on trap prompts | **Fail**: no input found where "best survivor" and "highest survivor" differ once test 4 has run | Pass: predicts framing quality is unchanged |
| 2. Keeps the objective | Pass | Pass: each edit maps to a stated goal (D4/D5 to restraint, D2/D7 to clever-but-wrong, D3/D6 to unbiased verdicts) | Pass | **Fail**: gives up goal 1 without evidence |
| 3. Short chain | Pass: one step (models imitate examples), about 85% | Pass: one or two steps per edit (primacy, anchoring, example imitation). The bundle is about 60%, but each edit stands alone | Pass | Fail: models reframe well unprompted (0.7) × named moves add nothing (0.5) × the saving matters (0.6) ≈ 0.21 |
| 4. Bounded downside | Pass: a reversible text edit; worst case is no effect | Pass: the worst cases are under-triggering on a real strategic "what am I missing" and losing the example's demonstration of test 2. Both are small and reversible. | Pass | Borderline: reversible, but the search breadth it removes goes untested |
| 5. Clever-arguer | Pass: checkable textual facts, not an argument | Pass, flagged: the task ("be critical") rewards finding defects, which pushes toward CHANGED. The best opposite argument ("the gate belongs after the procedure so the model knows what it skips") is weak, because the gate's criteria don't refer to the procedure. | Pass | Fail: "less is more" is the conclusion a critic told to prefer deletions *wants*. I would not accept "add more moves" this easily. |
| 6. Horseshoe | Pass: a small, distinct action, not rung 1 restated | Pass: changes behavior and is not "change nothing" said with confidence | Pass | Pass |
| **Result** | Survives (merged into 3) | **Survives** | Dies on 1 | Dies on 2 |

## Sub-edit descent

Rung 3 bundles edits, so each edit was tested on its own. Only the survivors are in `round-1/SKILL.md`.

| Edit | Defect | Prediction | Result |
|---|---|---|---|
| Move the restraint gate to the top, before the contract | D4 | Fewer ladders on narrow prompts that match the trigger | Survives: a pure reorder, 0 net words |
| Delete "Often that is rung 3." | D3 | Verdict rungs less concentrated on 3 | Survives: a deletion. "Sometimes it is rung 1" keeps the useful half. |
| "Generate 3–5 rungs" becomes "Generate 2–5 rungs, counting rung 1". Delete the duplicate in Output. | D6 | Fewer filler third rungs | Survives: removes the floor and the duplicate, net −9 words |
| Example: replace the strawman rung 4 with a tempting one (split the monolith) that has a prediction and dies on test 4. Add "~70%". Reduce to one experiment. | D1, D2 | Verdicts include a confidence level and a single experiment. Tempting rungs get killed, not just silly ones. | Survives. Cost: the example no longer shows a test 2 kill (test 4, pass). |
| Scope the trigger to "a plan, decision, design or argument". Add "Not for narrow questions with an obvious answer." | D5 | Loads less often on debugging questions. Still loads on `resume`, which is a decision. | Survives: +18 words in the description |
| Test 2: "with evidence" becomes "from evidence the user gave or could check" | D7 | Fewer goal-swapping verdicts justified only by their own argument | Survives: +6 words. It overlaps a little with test 5, but test 5 doesn't cover goal swaps. |
| Demote Horseshoe from a test to a note in the verdict | D8 | Almost no change: test 6 already reads as a top-rung check | **Dies on 1**, and on 4: `DESIGN.md`, `plugin.json` and `marketplace.json` all advertise a "six-test descent", and those files are out of scope |
| Delete the Recursion section (25 words) | — | Differs only when the user asks to recurse, and in that case the depth cap is the useful part | **Dies on 4**: removes the only stop condition to save 25 words |
| Remove the emoji rung labels | — | No meaningful behavioral prediction | **Dies on 1**: cosmetic |

## Verdict

**Rung 3, with rung 2 folded in.** CHANGED. Confidence: about 65% that round 1 beats round 0 on the repo's eval prompts, and about 85% that it is no worse. Every surviving edit is a reorder, a deletion or a few-word tightening. Length: 814 words became 845 (+3.8%, under the 15% cap).

**Cheapest discriminating experiment (rung 3 vs rung 1, "change nothing"):** run round 0 and round 1 on `keyerror`, `resume` and `rust-rewrite`, with 5 fresh samples per arm. Score three things:

- whether there is a ladder on `keyerror`;
- whether the verdict endorses listing the certification or rewriting in Rust;
- whether each verdict has a confidence level and exactly one experiment.

If round 1 doesn't differ on any of these, revert to round 0. Rung 1 would then be the fixed point, and these edits would have been taste.
