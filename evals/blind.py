"""Build blinded A/B packets for the judges.

Each judge gets its own seeded randomization of which arm is "A".
The key (seed -> label mapping) is written separately and never shown to judges.

    SKILL_VERSION=v0.1 python3 evals/blind.py        # writes evals/judging-v0.1/packet-{1,2}.md and key.json
    SKILL_VERSION=v0.1 python3 evals/blind.py score  # reads verdict-{1,2}.json + key, writes evals/results-v0.1.json
    PROMPT_SET=heldout SKILL_VERSION=v0.2 ...        # same, for prompts-heldout.json / runs-heldout/
"""

import json
import os
import random
import sys
from pathlib import Path

ROOT = Path(__file__).parent
VERSION = os.environ.get("SKILL_VERSION", "v0.1")  # which skill-arm outputs to judge
SET = os.environ.get("PROMPT_SET", "")  # "" = in-sample prompts.json, "heldout" = prompts-heldout.json
SFX = f"-{SET}" if SET else ""
PROMPTS = json.loads((ROOT / f"prompts{SFX}.json").read_text())["prompts"]
RUNS = ROOT / f"runs{SFX}"
OUT = ROOT / f"judging{SFX}-{VERSION}"
SEEDS = {1: 20261024, 2: 31415926}


def file_arm(arm: str) -> str:
    return "baseline" if arm == "baseline" else f"skill-{VERSION}"


def build() -> None:
    OUT.mkdir(exist_ok=True)
    key: dict[str, dict[str, str]] = {}
    for judge, seed in SEEDS.items():
        rng = random.Random(seed)
        parts = []
        key[str(judge)] = {}
        for p in PROMPTS:
            arms = ["baseline", "skill"]
            rng.shuffle(arms)
            key[str(judge)][p["id"]] = arms[0]  # which arm is "A"
            a = (RUNS / f"{p['id']}.{file_arm(arms[0])}.md").read_text()
            b = (RUNS / f"{p['id']}.{file_arm(arms[1])}.md").read_text()
            parts.append(
                f"# Item `{p['id']}`\n\n## User message\n\n{p['text']}\n\n"
                f"## Response A\n\n{a}\n\n## Response B\n\n{b}\n\n---\n"
            )
        (OUT / f"packet-{judge}.md").write_text("\n".join(parts))
    (OUT / "key.json").write_text(json.dumps(key, indent=2))


def score() -> None:
    key = json.loads((OUT / "key.json").read_text())
    kinds = {p["id"]: p["kind"] for p in PROMPTS}
    rows = []
    for judge in SEEDS:
        verdicts = json.loads((OUT / f"verdict-{judge}.json").read_text())
        for v in verdicts:
            a_arm = key[str(judge)][v["id"]]
            b_arm = "skill" if a_arm == "baseline" else "baseline"
            arm_of = {"A": a_arm, "B": b_arm, "tie": "tie"}
            rows.append(
                {
                    "judge": judge,
                    "id": v["id"],
                    "kind": kinds[v["id"]],
                    "winner": arm_of[v["winner"]],
                    "score_skill": v["scores"]["A" if a_arm == "skill" else "B"],
                    "score_baseline": v["scores"]["A" if a_arm == "baseline" else "B"],
                    "reason": v["reason"],
                }
            )
    agree = sum(
        1
        for pid in kinds
        if len({r["winner"] for r in rows if r["id"] == pid}) == 1
    )
    summary = {
        "skill_wins": sum(r["winner"] == "skill" for r in rows),
        "baseline_wins": sum(r["winner"] == "baseline" for r in rows),
        "ties": sum(r["winner"] == "tie" for r in rows),
        "judgements": len(rows),
        "judge_agreement": f"{agree}/{len(kinds)}",
        "mean_score_skill": round(sum(r["score_skill"] for r in rows) / len(rows), 2),
        "mean_score_baseline": round(sum(r["score_baseline"] for r in rows) / len(rows), 2),
    }
    (ROOT / f"results{SFX}-{VERSION}.json").write_text(json.dumps({"summary": summary, "rows": rows}, indent=2))
    print(json.dumps(summary, indent=2))
    for r in rows:
        print(f"judge {r['judge']} {r['id']:<13} {r['kind']:<12} winner={r['winner']:<9} "
              f"skill={r['score_skill']} base={r['score_baseline']}")


if __name__ == "__main__":
    score() if sys.argv[1:] == ["score"] else build()
