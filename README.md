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

**Claude.ai / desktop:** upload `plugins/galaxy-brain/skills/galaxy-brain/` as a skill (Settings → Capabilities → Skills).

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

<!-- RESULTS -->

## Layout

```
plugins/galaxy-brain/skills/galaxy-brain/SKILL.md   the skill
.agents/skills/galaxy-brain                         symlink for Codex
DESIGN.md                                           round-0 ladder: the skill designing itself
evals/self-application/round-{0,1,2}/               fixed-point iteration, with ladders
evals/prompts.json                                  A/B prompts and pre-registered hypotheses
evals/runs/                                         raw outputs, both arms
evals/judging/                                      blinded packets, key, judge verdicts
evals/restraint/                                    narrow-prompt restraint probe
evals/results.json                                  scored results
```

## License

MIT
