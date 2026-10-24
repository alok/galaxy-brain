# Don't start the Rust rewrite yet. Find out where the time goes first.

**My answer (confidence: about 75%):** Don't commit to rewriting the whole service next quarter. Spend the first part of the quarter finding out where the latency actually is, then fix that. If the profile shows most of the time is Python CPU work in a few hot paths, rewrite only those paths in Rust and keep the rest in Python. If it doesn't, Rust won't help much.

**Why the 50x figure misleads here.** The 50x number usually comes from tight numeric loops. A web request is mostly other things: waiting on the database, waiting on other services, network round trips, serialization. Switching languages doesn't shorten those waits. If most of each request is spent waiting on I/O, a Rust rewrite might give a modest improvement after months of work.

**The check.** Take the two or three endpoints customers complain about most. For each, measure p50 and p95 latency and split it into time in database calls, time in outbound HTTP calls, and time in Python itself (a profiler or tracing spans will do this). Then load-test those endpoints at realistic concurrency. The prediction that separates the options: if database and network waits account for more than about 70% of the time on those endpoints, a Rust rewrite would speed them up by well under 2x, and the fix is in queries, indexes, caching, or call patterns. If Python CPU accounts for more than half, a Rust implementation of the hot functions is worth testing.

**Options that survive, roughly in the order I'd try them:**

- Fix the common causes first: N+1 queries, missing indexes, unbounded result sets, missing connection pooling, sequential calls that could run in parallel, and blocking calls inside async handlers. These account for most "too slow" complaints in Python web services and are usually cheap to fix.
- Cache or precompute read-heavy endpoints, if the data can tolerate some staleness.
- Move slow work out of the request. Return quickly and let a background job finish, with progress shown. Sometimes "too slow" means users wait for work they didn't need to wait for.
- If CPU really is the bottleneck, rewrite the hot functions in Rust behind a Python interface (PyO3 or similar), or test faster options on the hot path first, such as a faster JSON library or a different Python runtime.

**Rejected:**

- Rewriting all 50k lines in Rust next quarter. It assumes the bottleneck is Python CPU, which nobody has shown yet. It means months of work that must match existing behavior, usually with feature work slowed or frozen. It is also the hardest of these options to reverse.
- Treating "too slow" as a fixed engineering target. Ask customers which action they are waiting on. It may be one workflow, and it may be partly a UX problem.

**If the profile does show the service is CPU-bound everywhere,** a rewrite becomes a serious option, but do it incrementally. Move one endpoint at a time to Rust behind the same API, and keep a rollback path at every step. That keeps the cost of being wrong low.

**Bottom line:** The boring answer is right. Measure, fix the database and I/O patterns, and rewrite only the parts the profile shows are hot.
