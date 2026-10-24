**Short version:** a triage contractor helps only if you also give them the authority to close things. Before you spend the money, check whether triage is what's burning your maintainers out. Often it isn't. (About 65% confident in this framing.)

**Why triage time probably isn't the problem.** Fifty issues a week at five to ten minutes each is roughly 4–8 hours a week, split between two people. That's real time, but it's rarely the part that burns people out. The usual causes are elsewhere:

- **The decisions.** "Is this a bug or intended?", "Will we ever support this?", "Do we take this PR?" A contractor can't make these calls. So triage tends to end with "needs maintainer input", and the same queue lands back on the same two people, now with labels on it.
- **The open-ended obligation.** A backlog that only grows feels like debt you never finish paying, however well it's sorted. Sorting doesn't make it smaller.
- **The social load.** Entitled or angry users, and being pinged constantly.

A contractor without decision rights also adds work at first. For the first month or two your maintainers will be answering the contractor's questions and checking their judgment. So expect things to get worse before they get better.

**What actually works:**

1. **Write a triage policy before hiring anyone.** For example: we close feature requests outside scope X. Issues with no reproduction get a request and auto-close after 14 days. Usage questions go to Discussions. We don't promise a response time. Writing this down is the valuable part. It turns maintainer judgment into rules someone else can apply. Then the contractor, a bot, or a volunteer can close issues without asking first. Without the policy, the contractor is just a router.
2. **Reduce inflow before you add capacity.** Require a reproduction in the issue template. Send questions to Discussions, since in many libraries a large share of "issues" are support requests. Use a bot to close issues marked needs-repro. Have maintainers triage once a week instead of continuously. All of this is cheap and easy to undo.
3. **Treat the issue count as data.** Fifty a week may mean a few root causes are generating most of them: a confusing API, a docs gap, a bad error message, a breaking change. Cluster your last 200 issues. If a handful of clusters account for 40% or more, one better error message or docs page beats a year of triage.

**The check (about two weeks, almost free):** have both maintainers log their issue-related time in four buckets: sorting/labeling/asking for repros, answering support questions, making decisions, and actually fixing things. At the same time, categorize your last 100 issues.

- If sorting plus support is most of the time, and questions or duplicates make up most of the issues, hire the contractor, with written close authority.
- If decisions and fixing dominate, a triager won't help much. Spend the money on a contractor who fixes bugs and handles the review work the maintainers dislike. Or use it to buy maintainers' time away from their day jobs.

**Options I'd rule out:**

- **Recruiting unpaid community triagers instead.** This moves the burnout onto volunteers and adds coordination work, which is the scarce thing.
- **"Just close everything and declare the project done."** That answers a different question unless you actually want to cut the project's scope. If you do, that's a legitimate choice and worth making on purpose.
- **Hiring on a one-off grant with no plan for renewal.** When the money runs out, the problem comes back, and users will by then expect fast responses.
