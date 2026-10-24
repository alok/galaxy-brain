# How this skill was designed: by running it on itself

The request was "write a galaxy brain skill, and galaxy brain the skill itself." So the design is the skill's own procedure, applied to the problem *what should a galaxy-brain skill be?* That trace is round 0. Rounds 1+ hand the finished SKILL.md to a fresh Opus instance and have it run the skill on the skill, repeating until the surviving verdict is "change nothing" (a fixed point). Those logs are in [`evals/self-application/`](evals/self-application/).

## Round 0: the bootstrap ladder

> Problem: write a skill that makes a model's answers better by "galaxy-braining" them.

| Rung | Move | Claim | Distinguishing prediction | Verdict |
|---|---|---|---|---|
| 🧠 1 | obvious | A prompt that says "think outside the box; give the unconventional take" | Outputs get longer and more contrarian on every prompt, including ones where the obvious answer is right | Survives only as the baseline to beat |
| ✨ 2 | zoom in | Give the model named reframe moves (zoom in/out, invert, change the objective, change the layer, transport, dissolve) so the climb is a search, not a mood | More *distinct* framings than rung 1 | Survives as a component. Alone it fails test 2: escalation without selection rewards cleverness, which is exactly the meme's joke |
| 🤯 3 | invert | The meme's last panel is wrong, so build the skill around catching that: every rung must state a prediction that differs from the rung below, pass a fixed set of kill tests, and the output is the highest **surviving** rung | On trap prompts the verdict lands *below* the skill's own top rung; on narrow prompts there's no ladder at all | **Survives** |
| 🌌 4 | zoom out | The skill should be a fixed point of itself: apply it to its own text until it stops changing | Self-application converges in ≤ 3 rounds, and each accepted change passes the descent | Survives as a *design process*. As runtime behavior it fails test 4 (unbounded cost), so runtime recursion is capped at depth 2 |
| 🌌+ 5 | dissolve | The most enlightened galaxy-brain skill mostly refuses to galaxy-brain | — | Horseshoe (test 6): a skill that always refuses is rung 0. What survives is the guard clause: "narrow question, obvious answer → no ladder" |
| ☄️ 6 | change the layer | Don't write a prompt at all; fine-tune or RL a model on reframing | — | Dies on test 2 and 4: swaps "write a skill" for "train a model", at a cost of orders of magnitude more |

**Verdict:** rung 3 at runtime, rung 4 as the build process, rung 5's guard clause folded in. Confidence: moderate; a prompt can only shift behavior so far.

**Cheapest discriminating experiment:** blind A/B against the same model with no skill, on prompts chosen so each rung makes a different prediction: reframe-win prompts (rung 2+ should help), trap prompts (only rung 3's descent helps), and a narrow prompt with an obvious answer (rung 1 prompts hurt, rung 3+ should abstain). See [`evals/`](evals/).

## Why these six descent tests and not others

Each one targets a named, documented failure of clever reasoning:

1. **Pays rent** — beliefs should constrain anticipated experience. A reframe that predicts nothing different is decoration.
2. **Keeps the objective** — the XY problem in reverse: the galaxy-brained answer solves a problem nobody had.
3. **Short chain** — conjunction: confidence in a chain is at most the product of its links, and long chains of individually plausible steps feel more convincing than they are.
4. **Bounded downside** — at similar expected value, prefer the option you can undo.
5. **Clever-arguer check** — motivated reasoning runs the argument backward from the conclusion. The tell is an argument that conveniently licenses what is normally off-limits.
6. **Horseshoe** — the meme's own structure: the last panel is often the first panel with more confidence.

Tests 1 and 3 are the quantitative ones. Test 5 is the safety-relevant one: it is the same check you would want any reasoning system to run on an argument that concludes it should deceive, evade oversight, or override the person it's working for.
