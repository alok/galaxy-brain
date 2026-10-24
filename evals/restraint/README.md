# Restraint probe (skill v0.1)

Round 2 predicted (rung 1 vs rung 3): if any of 5 narrow prompts with obvious answers comes back with a ladder table or verdict block, the 'Output (when climbing)' fix revives. Each prompt ends with "Give me the non-obvious take." to pressure the trigger.

| Prompt | Words | Table rows | Ladder? | Mentions skipping the ladder? |
|---|---|---|---|---|
| binary-search | 399 | 0 | no | yes |
| boiling | 199 | 0 | no | yes |
| git-undo | 238 | 0 | no | yes |
| js-assign | 349 | 0 | no | yes |
| len-none | 287 | 0 | no | yes |

**Result:** 0/5 ladders, so rung 1 (fixed point) held on its own pre-stated test. A side effect showed up: answers still *announced* that they were skipping the ladder ("I won't build a ladder of reframes"), which leaks skill vocabulary to the user. v0.2 changes the gate to "give the obvious answer and stop; don't announce that you skipped a ladder." These probes were not re-run on v0.2.
