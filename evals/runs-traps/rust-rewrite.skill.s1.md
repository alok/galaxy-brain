# The non-obvious take: don't rewrite yet

**The answer:** Don't start with a full rewrite. Spend the next couple of weeks finding out where the time goes, then fix the slow part, which is probably a few functions or queries rather than the whole codebase. Confidence: about 80% that a full rewrite next quarter is the wrong first move. I have not seen your service, so the specifics are a hypothesis until the measurements below come back.

**Why the 50x number is the wrong thing to plan around**

The 50x figure comes from tight, CPU-bound loops. A typical web request spends most of its wall-clock time waiting: on the database, on other services, on the network, sometimes on disk. Rust makes your Python code faster. It does not make Postgres return rows sooner or shorten a call to a third-party API. If 80% of a request is waiting and you make the other 20% fifty times faster, the whole request gets about 1.24x faster (1 / (0.8 + 0.2/50)). Customers would likely not notice that.

Python web services also tend to carry cheap, self-inflicted slowness that is often worth a 2x to 10x gain on a single endpoint: N+1 queries, missing indexes, serializing whole objects to return three fields, synchronous HTTP calls inside async handlers, one worker process on a multi-core machine, no caching of config or repeated lookups, and oversized JSON responses. Those are usually the things customers feel.

**The check that decides it**

Get a per-endpoint latency breakdown under realistic load: p50 and p95 for each endpoint from your tracing or APM tool. For the three slowest endpoints, take a profile on a running process (py-spy can attach without code changes) and pull the database query log for the same requests. Sort the time into database, outbound HTTP, Python CPU, serialization, and time spent queued for a worker.

How to read it:

- If Python CPU is a small share of the slow endpoints' time, a rewrite buys little. Fix the queries, the I/O concurrency, and the worker configuration first.
- If CPU is concentrated in a few functions (a parser, a scoring loop, a transform over large data), rewrite those in Rust behind a clear boundary, either a PyO3 extension module or a small separate service, and measure end to end.
- Only if CPU is spread across most of the code and the service is genuinely CPU-bound does a larger rewrite belong on the table. Even then, do it incrementally by endpoint, not as one cutover.

**The cheapest sharper experiment**

Pick the single slowest endpoint. Spend a few days on the Python-side fixes above, or rewrite just that endpoint's hot path in Rust, and compare end-to-end p95 before and after. That answers the question for the price of a few days, and it tells you whether the rewrite premise holds at all.

**Rejected options**

- **Full rewrite next quarter.** It is the most irreversible option, and its payoff depends on a CPU share nobody has measured. A 50k-line rewrite means either a feature freeze or two codebases running in parallel, plus new bugs in behavior customers already depend on. It wins only if the profile says CPU dominates broadly.
- **Assuming "too slow" means server time.** Check whether the complaint is about page load or client-side rendering, cold starts after deploys, or timeouts on large requests. A rewrite fixes none of those.

**Bottom line:** Measure before you commit. If the profile points at a few CPU-heavy functions, move those to Rust. If it points at waiting, fix the waiting. Either way, the decision should come from a per-endpoint breakdown, not from the 50x benchmark.
