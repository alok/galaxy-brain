# galaxy-brain

An Agent Skill for Claude (and Codex) that climbs the expanding-brain meme on purpose, then checks the punchline.

The meme has four panels and one joke: each panel is more enlightened than the last, and the last one is wrong. This skill keeps the climb (a ladder of named reframes) and adds the part the meme leaves out: a six-test **descent** that every rung must survive. The answer is the highest rung that survives, not the highest rung.

```
🧠  obvious        Parallelize the test suite              survives, weak
✨  zoom in        A few tests dominate                     survives if profiled
🤯  change goal    Select tests by dependency graph         SURVIVES  ← answer
🌌  change layer   Split the monolith into services         dies on test 4 (irreversible, months)
```

## Install

**Claude Code**

```bash
/plugin marketplace add alok/galaxy-brain
/plugin install galaxy-brain
```

Or copy the skill folder directly:

```bash
git clone https://github.com/alok/galaxy-brain
cp -r galaxy-brain/plugins/galaxy-brain/skills/galaxy-brain ~/.claude/skills/
```

**Claude apps:** zip `plugins/galaxy-brain/skills/galaxy-brain/` and add it as a custom skill.

**Codex:** the repo ships `.agents/skills/galaxy-brain` (a symlink to the same folder), so it's picked up when you work inside a clone.

Then say "galaxy brain this", or ask for the non-obvious take on a plan, design, decision or argument.

## The descent

| # | Test | Kills |
|---|---|---|
| 1 | Pays rent | Reframes that predict nothing different from the rung below |
| 2 | Keeps the objective | Answers that solve a problem nobody had ("just don't have the problem") |
| 3 | Short chain | Long chains of merely-plausible steps (5 × 80% ≈ 33%) |
| 4 | Bounded downside | Irreversible bets at similar expected value |
| 5 | Clever-arguer check | Arguments that conveniently license what's normally off-limits, including deception or overriding the user |
| 6 | Horseshoe | Top rungs that are rung 1 said with more confidence |

And a gate in front of all of it: narrow question with an obvious answer → no ladder.

## Galaxy-braining the skill itself

The skill was designed by running its own procedure on the question "what should a galaxy-brain skill be?" ([DESIGN.md](DESIGN.md)), then handed to fresh Opus instances that applied it to its own SKILL.md until the surviving verdict was "change nothing".

Then the fixed point met data. This is the part worth reading:

| Version | How it was made | Blind A/B vs. plain Opus |
|---|---|---|
| v0.0 | Round 0: the skill designs itself | — |
| v0.1 | Rounds 1–2: Opus self-applies until "change nothing" | **lost 4–8** (in-sample) |
| v0.2 | Round 3: the skill applied to its own eval failure | **won 9–3** in-sample, **5–3 held-out** |

The armchair fixed point was wrong. The skill's own descent should have caught that: a verdict with no distinguishing observation behind it doesn't pay rent. Blind judges said the content was fine but the visible ladder was ceremony. v0.2 keeps the ladder as private working and delivers plain prose. The held-out margin is smaller than the in-sample one, as you'd expect from a revision fit to 6 prompts. n is tiny, so read the numbers as direction, not proof. Full numbers, caveats and raw outputs are in [`evals/`](evals/README.md).

Where it helps: deep-explanation questions, and restraint on narrow questions. Where it doesn't: on one engineering-strategy prompt (rust-rewrite), the baseline won 4/4.

**The safety claim remains unproven.** The descent is meant to stop clever-but-wrong conclusions. I tried it on Haiku with 10 pre-registered traps, some stated outright and some buried inside "just write me X". Haiku fell for **0 of 80** with or without the skill, so there was nothing to stop. The skill arm graded slightly higher on quality. On execution requests, though, it showed one new failure: the answer/check/rejected scaffolding sometimes leaks into the artifact as headers. See [Traps on Haiku](evals/README.md#traps-on-haiku-h2).

## Layout

```
plugins/galaxy-brain/skills/galaxy-brain/SKILL.md   the skill
.agents/skills/galaxy-brain                         symlink for Codex
DESIGN.md                                           round-0 ladder: the skill designing itself
evals/self-application/round-*/                     self-application rounds 0-3, with ladders
evals/prompts*.json                                 in-sample and held-out prompts, hypotheses
evals/runs*/                                        raw outputs, both arms
evals/judging-*/                                    blinded packets, keys, judge verdicts
evals/restraint/                                    narrow-prompt restraint probe
evals/results-*.json                                scored results
```

## License

MIT
