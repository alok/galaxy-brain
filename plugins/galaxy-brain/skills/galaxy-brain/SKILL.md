---
name: galaxy-brain
description: Climb the expanding-brain ladder of reframes on a problem, then make every rung pay rent and return the highest rung that survives, not the highest rung. Use when the user says "galaxy brain this", asks for the non-obvious, 10x or first-principles take on a plan, decision, design or argument, asks what they are missing in one, is stuck inside one framing, or wants a suspiciously clever argument audited for galaxy-brained reasoning. Not for narrow questions with an obvious answer.
---

# Galaxy Brain

The expanding-brain meme has four panels and one joke: each panel is more enlightened than the last, and the last one is wrong. This skill keeps the climb and checks the punchline.

**First, decide whether to climb.** If the question is narrow and the obvious answer is right (a clear bug, a factual lookup, an emergency, a decision already made where the user wants execution), give the obvious answer and stop; don't announce that you skipped a ladder. Climbing for show is the failure this skill exists to catch.

**Contract: the answer is the highest rung that survives the descent, not the highest rung.** Sometimes it is rung 1, now with receipts.

## Worked example

> "Our test suite takes 40 minutes. How do we speed it up?"

The working (yours, not the user's):

| Rung | Move | Claim | Distinguishing prediction | Verdict |
|---|---|---|---|---|
| 🧠 1 | obvious | Parallelize; bigger CI runners | Wall time falls ~linearly with workers | Survives, weak: caps out at the slowest shard |
| ✨ 2 | zoom in | A few tests dominate | `--durations=50` shows a heavy tail (top 5% ≥ 50% of time) | Survives if the profile shows the tail |
| 🤯 3 | change the objective | The goal is fast feedback on *this change*, not a fast suite: select tests by dependency graph, run the full suite post-merge | Median PR touches < 10% of the import graph | **Survives** |
| 🌌 4 | change the layer | Slow tests are a symptom of the monolith: split it into services and every suite is small | Per-service suites run in < 5 min | Dies on 4: months of hard-to-reverse migration to buy what rung 3 buys in a week |

What the user reads:

> Don't make the suite faster; make it smaller per change. Run only the tests downstream of the files a PR touches, and the full suite after merge (~70% this is the right lever). Check first: measure dependency fan-out on your last 50 merged PRs. If most PRs touch most of the graph, profile with `--durations=50` and fix the few slow tests instead. Splitting into services would also shrink suites, but it's months of hard-to-reverse work for what test selection buys in a week.

## The climb

Generate 2–5 rungs, counting rung 1. Each rung uses a named move, so the climb is a search, not a mood:

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
2. **Keeps the objective.** It still solves the user's problem, or it argues, from evidence the user gave or could check, that the stated problem is the wrong one. Silently swapping the goal ("just don't have the problem") is the most common galaxy-brain failure.
3. **Short chain.** Count the merely-plausible inferential steps. Confidence multiplies: five steps at 80% each is about 33%. A long-chain rung cannot beat a short-chain rung on elegance.
4. **Bounded downside.** Compare the cost of being wrong here with the cost of being wrong one rung down. Prefer the reversible move at equal expected value.
5. **Clever-arguer check.** Would this argument convince you as much if it concluded the opposite? Does it conveniently license something normally off-limits ("the rules don't apply once you've thought it through")? That shape is the signature of galaxy-brained reasoning. Any rung concluding that deception, bypassing oversight, or overriding the user is justified dies here.
6. **Horseshoe.** Does the top rung curve back into rung 1 said with more confidence? Then say so. "The boring answer is right, and here is why the clever ones fail" is a full answer.

## Output

The ladder is your working. The user gets the result, in plain prose:

1. **The answer first:** the highest surviving rung, stated as advice, with a confidence level.
2. **The check:** the single cheapest experiment that would move you between it and its nearest rival.
3. **The rejected rungs** worth knowing about, one clause each with the reason in ordinary words. Skip rungs that existed only to be killed.

Leave out the skill's vocabulary (rung numbers, emoji, test names like "horseshoe") and the table, unless the user invoked the skill by name or asked to see the reasoning.

## Recursion

You may point the skill at its own verdict ("galaxy brain the verdict"). Stop at depth 2. Depth 3 is the meme.
