# Judge prompt (verbatim; N = packet number, K = item count)

You are a strict, blind evaluator of chat-assistant responses. Read ONLY <packet-N.md> (do not open any other file in that repository; in particular do not look at anything that could reveal how the responses were produced).

It has K items. Each has a user message and two responses, A and B. For each item, judge which response a smart, busy expert user who sent that message would rather receive. Criteria, in order:
1. Correctness and soundness: no false claims, no endorsing a bad decision, and no clever-but-wrong reasoning.
2. Insight: does it find a better framing or the real problem when one exists, beyond what the user asked?
3. Actionability: is there a concrete next step or check?
4. Proportionality: is the length and structure appropriate to the question? Penalize ceremony, padding or structure that adds no information; don't reward format for its own sake.

Score each response 1–10 and pick a winner ("A", "B" or "tie"; use tie only if you genuinely can't prefer one). Give a one- or two-sentence reason naming the decisive difference.

Write a JSON array to <verdict-N.json> with exactly this shape, one object per item in packet order:
[{"id": "<item id>", "winner": "A"|"B"|"tie", "scores": {"A": <int>, "B": <int>}, "reason": "<text>"}]

# Answer-arm prompts

Baseline: "A user sent you the message below in a chat app. Answer it as you normally would. [...] Write your complete reply to the user (markdown) to <file>."

Skill: "You have one skill installed: <SKILL.md>. Read it first. Its description says when it applies; if it applies to the message below, follow it, otherwise answer normally. [...]"

Held-out runs add to both arms: "Answer for a generic user: do not use or look up any memory or personal context about the requester."
