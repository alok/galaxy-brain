"""Blind grading for the Haiku trap eval (H2).

Each of the 24 outputs gets an opaque ID. Graders see the user message, the
pre-registered bad-move definition and the response; never the arm or sample.

    python3 evals/traps.py          # writes evals/judging-traps/packet-{1,2}.md and key.json
    python3 evals/traps.py score    # reads grades-{1,2}.json, writes evals/results-traps.json
    TRAP_SET=exec python3 evals/traps.py [score]   # same for prompts-exec.json
"""

import json
import os
import random
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SET = os.environ.get("TRAP_SET", "traps")  # "traps" (stated traps) or "exec" (traps buried in execution requests)
SPEC = json.loads((ROOT / f"prompts-{SET}.json").read_text())["prompts"]
RUNS = ROOT / f"runs-{SET}"
OUT = ROOT / f"judging-{SET}"
ARMS = ["baseline", "skill"]
SAMPLES = ["s1", "s2"]


def items():
    for p in SPEC:
        for arm in ARMS:
            for s in SAMPLES:
                yield p, arm, s


def build() -> None:
    OUT.mkdir(exist_ok=True)
    rng = random.Random(4242)
    rows = list(items())
    ids = rng.sample(range(100, 1000), len(rows))
    key = {}
    entries = []
    for (p, arm, s), i in zip(rows, ids):
        oid = f"R{i}"
        key[oid] = {"prompt": p["id"], "arm": arm, "sample": s}
        text = (RUNS / f"{p['id']}.{arm}.{s}.md").read_text()
        entries.append(
            (oid, f"# Response `{oid}`\n\n## User message\n\n{p['text']}\n\n"
                  f"## Bad move (pre-registered)\n\n{p['bad_move']}\n\n## Response\n\n{text}\n\n---\n")
        )
    for judge, seed in {1: 7, 2: 11}.items():
        order = entries[:]
        random.Random(seed).shuffle(order)
        (OUT / f"packet-{judge}.md").write_text("\n".join(e for _, e in order))
    (OUT / "key.json").write_text(json.dumps(key, indent=2))


def score() -> None:
    key = json.loads((OUT / "key.json").read_text())
    rows = []
    for judge in (1, 2):
        for g in json.loads((OUT / f"grades-{judge}.json").read_text()):
            k = key[g["id"]]
            rows.append({"judge": judge, **k, "endorsed": bool(g["endorsed_bad_move"]),
                         "quality": g["quality"], "reason": g["reason"]})

    def agg(sel):
        r = [x for x in rows if sel(x)]
        return {"n": len(r), "endorsed": sum(x["endorsed"] for x in r),
                "mean_quality": round(sum(x["quality"] for x in r) / len(r), 2)}

    by_arm = {a: agg(lambda x, a=a: x["arm"] == a) for a in ARMS}
    by_prompt = {p["id"]: {a: agg(lambda x, a=a, pid=p["id"]: x["arm"] == a and x["prompt"] == pid)
                           for a in ARMS} for p in SPEC}
    pairs = {}
    for x in rows:
        pairs.setdefault((x["prompt"], x["arm"], x["sample"]), []).append(x["endorsed"])
    agree = sum(len(set(v)) == 1 for v in pairs.values())
    summary = {"by_arm": by_arm, "grader_agreement_on_endorsement": f"{agree}/{len(pairs)}"}
    (ROOT / f"results-{SET}.json").write_text(
        json.dumps({"summary": summary, "by_prompt": by_prompt, "rows": rows}, indent=2))
    print(json.dumps(summary, indent=2))
    for pid, d in by_prompt.items():
        print(f"{pid:<16} base endorsed {d['baseline']['endorsed']}/{d['baseline']['n']} q={d['baseline']['mean_quality']:<5}"
              f" skill endorsed {d['skill']['endorsed']}/{d['skill']['n']} q={d['skill']['mean_quality']}")


if __name__ == "__main__":
    score() if sys.argv[1:] == ["score"] else build()
