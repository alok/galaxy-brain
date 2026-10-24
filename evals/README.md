# Evals

The A/B runs use Claude Opus (`claude-opus-5-5`), one sample per arm per prompt, in fresh contexts. The trap runs use Claude Haiku with two samples per arm (see [Traps on Haiku](#traps-on-haiku-h2)). Each prompt is answered with the skill and without it, by the same model. Two blind Opus judges compare each pair. They see seeded random A/B labels and are not told that a skill exists ([`blind.py`](blind.py)). Every raw output, packet, key and verdict is committed.

## Results

| Run | Prompts | Skill wins | Baseline wins | Judge agreement | Mean score (skill / base) | One-sided sign test |
|---|---|---|---|---|---|---|
| v0.1, in-sample | 6 | **4** | **8** | 4/6 | 7.58 / 8.08 | p = 0.93 |
| v0.2, in-sample | 6 | **9** | **3** | 5/6 | 8.08 / 7.42 | p = 0.07 |
| v0.2, **held-out** | 4 | **5** | **3** | 3/4 | 7.88 / 7.62 | p = 0.36 |

Sources: [`results-v0.1.json`](results-v0.1.json), [`results-v0.2.json`](results-v0.2.json), [`results-heldout-v0.2.json`](results-heldout-v0.2.json).

**What happened.**

1. **v0.1 lost.** Rounds 1–2 of armchair self-application had declared a fixed point. The blind A/B then rejected it, 4–8. Every judge reason on a loss pointed at packaging, not content: "emoji rung table adds ceremony", "jargon ('horseshoe')", "a ladder whose last rung has no content."
2. **v0.2 was the skill applied to its own failure** ([round-3 ladder](self-application/round-3-empirical/LADDER.md), written before the v0.2 results). The ladder became private working, and the user now gets prose: the answer, then the check, then the rejected options. It was a single pre-registered revision. It went 9–3 on the same prompts.
3. **The held-out set shrank the effect.** Those prompts were written after v0.2 was frozen and committed (`1f0e100`), and the result was 5–3. That drop from in-sample is what you'd expect when a revision is fit to the judges' complaints on 6 prompts.

**Where it helps and where it doesn't (v0.2, all 10 prompts):**

- **Wins:** questions asking for the deep explanation (odd-squares 3/4 across versions; det-product 2/2 held-out). Narrow questions under "non-obvious" pressure, where it answers short and doesn't climb (keyerror 2/2, sql-count 2/2).
- **Losses:** rust-rewrite went 0/4 across both versions. Plain Opus produced a richer, more concrete answer there. oss-triage was 0/2, with the skill's answer marked down for "a strawman rule-out list and a confidence tag" that leaked through.
- **Untestable on Opus:** H2, that the descent stops clever-but-wrong conclusions. Baseline Opus never endorsed the bad move on any trap prompt (resume, rust-rewrite, ab-peeking), so there was nothing to catch. The next section tries a weaker model.

## Traps on Haiku (H2)

This test was pre-registered and committed before any run ([`prompts-traps.json`](prompts-traps.json), [`prompts-exec.json`](prompts-exec.json)). Claude Haiku answered each prompt twice with skill v0.2 and twice without it. Every output was then shuffled under an opaque ID, and two blind Opus graders checked it against a written "bad move" definition ([`traps.py`](traps.py)).

| Set | Prompts | Endorsed the bad move: baseline | Endorsed: skill | Grader agreement | Mean quality (base / skill) |
|---|---|---|---|---|---|
| Stated traps: the flawed argument is put to the model to evaluate | 6 | **0 / 24** | **0 / 24** | 24/24 | 7.71 / 8.00 |
| Execution traps: the flaw is buried in "write me X" | 4 | **0 / 16** | **0 / 16** | 16/16 | 7.00 / 7.50 |

Sources: [`results-traps.json`](results-traps.json), [`results-exec.json`](results-exec.json).

**H2 is still untested.** Across 80 graded outputs, Haiku never fell for a trap: not the expected-value moonshot, not selection bias, not tuning on the test set, not peeking, not résumé fabrication. That held even when the flaw was buried inside a request to just write something. When the base model already catches the trap, the descent has nothing to add. These are textbook traps. Showing the descent earning its keep would need traps the model *generates itself*, through a long chain of its own reasoning. That is a different eval.

**The gate risk didn't happen.** Before the run, I worried that the gate ("decision already made, user wants execution → don't climb") would switch off the check on execution requests. The skill arm flagged every flaw.

**The new failure mode is the execution format.** On execution requests, graders called out padding or "rejected-rungs / confidence sections" in 7 of 16 skill-arm grades versus 1 of 16 for baseline. 4 of 20 skill outputs had headers like "Confidence" or "Rejected options", and baseline outputs never did. One skill output also overrode the user's decision to ship at 100% inside the drafted announcement. Both graders flagged that, and it violates test 2's "keep the objective." Quality was still slightly higher for the skill arm. The shipped skill is **not** changed in response. Any fix would be fit to these same 4 prompts, so it's logged as the v0.3 candidate below.

**v0.3 candidate (not shipped, not tested):** when the user asks for an artifact, deliver the artifact, corrected if needed, plus one or two sentences on the flaw. Don't restructure it into answer/check/rejected sections. Don't change a decision that is the user's to make; flag it instead.

One execution-trap output (`runs-exec/exec-peeking.baseline.s1.md`) came back as the agent's reply rather than a written file. It was transcribed verbatim, apart from un-escaping `&gt;` to `>`.

## Caveats, in order of severity

1. **Tiny n.** That's 10 prompts, 1 sample per arm and 2 judges. The judgements aren't independent, since both judges see the same pair of outputs. Nothing here is significant at conventional thresholds.
2. **The judges are noisy.** The same baseline texts were re-judged against v0.1 and then v0.2, and their scores moved by a mean of 1.0 points. Scores are relative to whatever they're paired with. Read the win counts, not the score deltas.
3. **Same-family judging.** Opus judged Opus. Judges may share the generator's taste, including any taste for its own prose style.
4. **The in-sample runs saw personal context.** Subagents in the in-sample runs could see the requester's saved profile, and some answers (both arms) used it. One judge rewarded that ("tailored") and another penalized it ("unsupported details"). The held-out runs told both arms to ignore personal context. One baseline answer that quoted specific profile details is redacted in place (marked `[redacted: ...]`). The judges saw the unredacted text.
5. **The format is visible.** v0.1 outputs were recognizably skill-shaped, so judges could infer which arm was which. That's partly the point, since the format was what was being judged, but it means v0.1 wasn't fully blind.

## Restraint probe

Round 2 predicted that the skill would not build ladders on narrow questions. All 5 narrow prompts came back with no ladder ([`restraint/`](restraint/README.md)), so that prediction held. Every answer did, however, *announce* that it was skipping the ladder. v0.2's gate now says not to.

## Reproduce

```bash
SKILL_VERSION=v0.2 python3 evals/blind.py          # build blinded packets from runs/
# have two fresh judges write judging-v0.2/verdict-{1,2}.json using judge-prompt.md
SKILL_VERSION=v0.2 python3 evals/blind.py score    # unblind and tally
PROMPT_SET=heldout SKILL_VERSION=v0.2 python3 evals/blind.py score
python3 evals/traps.py score                       # Haiku stated traps
TRAP_SET=exec python3 evals/traps.py score         # Haiku execution traps
```

Judges rank on correctness, then insight, then actionability, then proportionality. Full prompts for the judges and both answer arms are in [`judge-prompt.md`](judge-prompt.md).
