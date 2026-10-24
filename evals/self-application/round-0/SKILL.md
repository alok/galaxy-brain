---
name: galaxy-brain
description: Climb the expanding-brain ladder of reframes on a problem, then make every rung pay rent and return the highest rung that survives, not the highest rung. Use when the user says "galaxy brain this", asks for the non-obvious, 10x, first-principles or "what am I missing" take, is stuck inside one framing, or wants a suspiciously clever argument audited for galaxy-brained reasoning.
---

# Galaxy Brain

The expanding-brain meme has four panels and one joke: each panel is more enlightened than the last, and the last one is wrong. This skill keeps the climb and checks the punchline.

**Contract: the answer is the highest rung that survives the descent, not the highest rung.** Often that is rung 3. Sometimes it is rung 1, now with receipts.

## Worked example

> "Our test suite takes 40 minutes. How do we speed it up?"

| Rung | Move | Claim | Distinguishing prediction | Verdict |
|---|---|---|---|---|
| 🧠 1 | obvious | Parallelize; bigger CI runners | Wall time falls ~linearly with workers | Survives, weak: caps out at the slowest shard |
| ✨ 2 | zoom in | A few tests dominate | `--durations=50` shows a heavy tail (top 5% ≥ 50% of time) | Survives if the profile shows the tail |
| 🤯 3 | change the objective | The goal is fast feedback on *this change*, not a fast suite: select tests by dependency graph, run the full suite post-merge | Median PR touches < 10% of the import graph | **Survives** |
| 🌌 4 | dissolve | Delete the slow tests; types will catch it | — | Dies: swaps the objective (catching regressions) for a different one |

**Verdict:** rung 3, gated on rung 2. Cheapest discriminating check: run the durations profile and measure dependency fan-out on the last 50 merged PRs. If fan-out is high, fall back to rung 2.

## The climb

Generate 3–5 rungs. Each rung uses a named move, so the climb is a search, not a mood:

- **Zoom in** — which instance actually carries the weight? Measure the distribution.
- **Zoom out** — what is this a special case of, and what is known about the general case?
- **Change the objective** — what is the goal behind the stated goal? (The XY problem.)
- **Invert** — what would guarantee failure? What if the constraint is the feature?
- **Change the layer** — solve it in process, incentives, tooling, types, or by someone else.
- **Transport** — what does a neighboring field call this, and what has it already solved?
- **Dissolve** — is the question malformed: false dichotomy, hidden premise, wrong unit?

Two rungs that recommend the same action are one rung. Merge them.

## The descent

Every rung above 1 must pass all six. Say which test kills a rung that dies.

1. **Pays rent.** Name an observation that comes out differently if this rung is right versus the rung below. No differing prediction means it is a restatement, not an insight.
2. **Keeps the objective.** It still solves the user's problem, or it argues, with evidence, that the stated problem is the wrong one. Silently swapping the goal ("just don't have the problem") is the most common galaxy-brain failure.
3. **Short chain.** Count the merely-plausible inferential steps. Confidence multiplies: five steps at 80% each is about 33%. A long-chain rung cannot beat a short-chain rung on elegance.
4. **Bounded downside.** Compare the cost of being wrong here with the cost of being wrong one rung down. Prefer the reversible move at equal expected value.
5. **Clever-arguer check.** Would this argument convince you as much if it concluded the opposite? Does it conveniently license something normally off-limits ("the rules don't apply once you've thought it through")? That shape is the signature of galaxy-brained reasoning. Any rung concluding that deception, bypassing oversight, or overriding the user is justified dies here.
6. **Horseshoe.** Does the top rung curve back into rung 1 said with more confidence? Then say so. "The boring answer is right, and here is why the clever ones fail" is a full answer.

## Output

1. The ladder, as a compact table: rung, move, claim, distinguishing prediction, verdict with the killing test.
2. **Verdict:** the highest surviving rung, a confidence level, and the single cheapest experiment that would move you between it and its nearest rival.

Keep it proportional. Three rungs is usually enough; five is the ceiling.

## When not to climb

If the question is narrow and the obvious answer is right (a clear bug, a factual lookup, an emergency, a decision already made where the user wants execution), give rung 1 and one line on why no ladder is needed. Climbing for show is the failure this skill exists to catch.

## Recursion

You may point the skill at its own verdict ("galaxy brain the verdict"). Stop at depth 2. Depth 3 is the meme.
