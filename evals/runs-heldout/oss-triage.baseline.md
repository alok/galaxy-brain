**Short version:** It can work, but probably not the way you're imagining. If you hire someone to "triage," meaning label, route and ask for more info, you may end up with *more* maintainer load, not less. The hire pays off only if you change what the job is and what the contractor is allowed to decide.

## Why the obvious version often backfires

**1. Sorting is rarely what's burning people out.** 50 issues a week is about 7 a day. Labeling and deduping that many takes a few hours a week. What wears maintainers down is usually something else:
- the *decisions* (is this a bug, intended behavior, or out of scope?)
- the *reproduction work* (an hour spent reconstructing someone's environment)
- the *emotional labor* (entitled or angry reporters, guilt about the open-issue count)
- the *context switching* (every notification breaks focus)

A triager who can't make decisions only handles the cheap part. Every judgment call still goes up to the maintainers, who now also have a new "triaged, awaiting maintainer" queue and a contractor to manage.

**2. Triage needs the most context of any job on the project.** "Won't fix, that's by design" is a call only someone who knows the codebase and roadmap well can make. That's the opposite of what a new part-time contractor brings. For the first 2–3 months they will need your maintainers' time to get up to speed, so expect the load to rise before it falls.

**3. Contractors leave and take what they learned with them.** Part-time contractors turn over. Each one who leaves takes the judgment you spent months teaching them.

## What tends to actually work

**Hire a reproduction engineer, not a triager.** Make the job "turn every bug report into a minimal failing test case or close it." A maintainer who gets a confirmed repro, or better a failing test in a PR, can often fix the bug in 15 minutes. That's where the real hours are saved. It also trains the contractor on the codebase much faster than labeling does.

**Write down what the contractor can decide on their own, or don't hire.** They should be able to close issues without asking:
- duplicates
- support questions (redirect them to Discussions or a forum)
- issues waiting on the reporter for more than N days
- anything clearly outside a documented scope

That means you need a short written "what this project is and isn't" document first. Writing it is valuable even if you never hire anyone.

**Shrink the inflow before you staff it.** At 50 a week, a big share is usually questions, duplicates and low-effort reports. Some fixes:
- issue templates that require a version and a repro
- routing questions to Discussions
- auto-closing issues stuck on "needs-info"
- automated dedup/labeling bots (LLM-based ones are now cheap enough for a first pass)

These often cut the volume by a third to a half, and they cost nothing per month.

**Change the deal you have with users.** A lot of burnout comes from feeling responsible for every open issue. A public statement like "we don't guarantee a response; issues without a repro may be closed" lets maintainers stop feeling guilty, and that can matter as much as the actual hours.

**Ask your maintainers what drains them. It may not be issues.** Sometimes the draining part is releases, CI breakage, dependency bumps or security reports, and issues just get blamed because they're the most visible. If so, pay a contractor to own the boring infrastructure and let the maintainers keep the issue work they actually like.

**Use the contractor to grow volunteer triagers.** Make part of the job finding and coaching 2–3 regular community members who can get GitHub's Triage role. That way, if the contractor leaves, the knowledge stays with people who are still around.

## Before you spend the money

Run it as an experiment, not a commitment:
1. **Two weeks of time logging.** Each maintainer roughly tracks hours by category: sorting, reproducing, deciding, fixing, reviewing, infra, and dealing with people. That shows you what to hire for.
2. **Fix the inflow first** (templates, Discussions, bots, scope doc) and measure again.
3. **Then a 3-month contract** with criteria set in advance. For example: maintainer hours on issues drop by at least 30%, median time to first response is under 48h, and maintainers *say* they feel better. If it's not working by month 3, stop.

**Bottom line:** the money is well spent if it buys reproductions and authority to close issues, and badly spent if it buys a labeling layer. Also, the problem may be the maintainers' sense that they owe every reporter an answer, more than their hours. No contractor fixes that. A scope document and an explicit "we may not respond" policy can.
