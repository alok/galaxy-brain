**Don't rewrite next quarter. Spend one week finding out where a slow request actually spends its time.** I'd put about 80% on the bottleneck not being Python execution. If that's right, a Rust rewrite costs a quarter and fixes very little.

Here's the arithmetic. Take a 2-second request that customers complain about. Suppose a typical breakdown: 1.6 s waiting on Postgres and other services, 0.4 s running Python. Make the Python part 50x faster and 0.4 s drops to 8 ms, so the request goes from 2.0 s to about 1.61 s. That's roughly 20% faster for a quarter of work. Fixing one N+1 query or adding one missing index on the same request could plausibly bring it to 300 ms in an afternoon. This is Amdahl's law: a rewrite can only speed up the share of time spent in Python CPU, and in most web services that share is small. The ~50x figure also comes from tight CPU-bound loops. A web service already spends much of its CPU time in C (DB drivers, JSON libraries, the framework's hot paths), so the real ratio for your code is lower.

The other half of the non-obvious take: "too slow" is what customers feel, not a property of the whole service. Complaints are almost always about a handful of endpoints and their worst-case latency (p95/p99), not the median across 50k lines. So the target is those few requests, not the codebase.

**The check (about a week):**
1. List the 3–5 screens or endpoints customers actually complain about.
2. For each, pull p95 traces from your APM or OpenTelemetry, and split wall time into DB, external calls, and Python CPU. Run `py-spy` against production to get a flame graph of the CPU part.
3. Also confirm the time is server-side at all. If server time is 300 ms of a 4-second page load, the problem is the frontend or the network, and no backend language change will help.

**What the result tells you:**
- **Python CPU under ~30% of slow-request time:** a rewrite can't beat a ~30% improvement even if Rust were infinitely fast. Fix queries, add indexes, cache, and move heavy work into background jobs. This is the outcome I expect.
- **CPU dominates but sits in a few functions** (pricing, serialization, some numeric kernel): rewrite only those functions in Rust with PyO3/maturin. You get the speedup where it matters and keep the other ~95% of the code.
- **CPU dominates and is spread evenly across the codebase:** then there's a real case for Rust. Even so, migrate one service or route at a time behind the existing API (strangler-fig style), not as a single big rewrite.

**Why the full rewrite loses even when Rust is the right language:** 50k lines of Python in one quarter is optimistic. You'd freeze features for that time, and you'd have to rediscover years of bug fixes hidden in the existing code to reach behavior parity. If it ships late or with regressions, you can't easily back out. The targeted options above cost days and can be reversed. The profile is cheap and tells you which situation you're in, so get it before committing the quarter.
