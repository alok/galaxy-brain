**The non-obvious take: "Rust is 50x faster" is true for a kind of work your service probably isn't doing much of. If so, the rewrite will cost several engineer-quarters and leave customer-visible latency about where it is. Or it will get faster for reasons that have nothing to do with Rust.**

## A concrete example first

Say a typical slow endpoint has a p95 of 900 ms. A trace of that request could look like this:

| Segment | Time |
|---|---|
| Waiting on Postgres (14 queries, 11 of them an N+1 loop) | 610 ms |
| Calling an internal or third-party HTTP API | 180 ms |
| Python CPU (ORM hydration, business logic, JSON serialization) | 90 ms |
| Framework and middleware overhead | 20 ms |

Rewrite that endpoint in Rust and make its CPU work 50x faster. The 110 ms of Python work shrinks to about 2 ms, so p95 goes from 900 ms to about 790 ms. That's a 12% gain, from a rewrite that probably takes over a year. If you instead fix the N+1 (one join or `selectinload`) and add one index, p95 lands around 350 ms. You could do that in an afternoon, in Python.

This is just Amdahl's law: a speedup only helps the fraction of time it applies to. In most CRUD-style web services, interpreter CPU time is a small fraction of request time.

## Things that are easy to miss

**1. The rewrite gives you the wrong lesson.** Rewrites usually do make things faster, because while rewriting you fix the queries, drop the N+1s, add caching and simplify the data flow. Then everyone credits Rust. Most of those gains were available in Python. The rewrite is a very expensive way to end up doing what a profiler would have told you.

**2. "Too slow" is a customer report, not a measurement.** Before deciding anything, find out:
- **Which endpoints or pages?** Slowness is usually concentrated in 3–5 routes, not spread across all 50k lines.
- **Latency or throughput?** If things are only slow under load, you may be hitting queueing. When workers are near 100% busy, waiting time grows very fast (Little's law plus utilization effects). Adding instances or workers costs money, not a quarter.
- **Median or tail?** A bad p99 tends to come from lock contention, connection-pool exhaustion, a blocking call inside an async event loop, or one heavy customer's data shape. A rewrite in another language tends to carry these problems over unchanged.
- **Backend at all?** Sometimes the perceived slowness is frontend waterfalls, oversized payloads, or missing pagination.

**3. A classic Python failure looks like "Python is slow" but isn't.** For example: a sync DB driver or `requests` call inside an `async def` handler. It blocks the event loop, so every concurrent request stalls behind it. Throughput falls off a cliff and you see huge latency spikes. Fixing it takes about one line. Rewriting in Rust also "fixes" it, which feeds the misattribution in point 1.

**4. Fifty thousand lines contain years of bug fixes no one wrote down.** The hard part of a rewrite isn't writing Rust. It's matching existing behavior: odd edge cases, implicit coercions, the date-handling bug a big customer now depends on. "Next quarter" is very unlikely for 50k lines of real business logic. Realistically, expect 2–4x that, with features frozen or built twice, and no customer-visible improvement until cutover.

**5. Is speed the real reason?** Sometimes the actual drivers are "the codebase is painful," "we want static types," or "the team wants to write Rust." Those can be legitimate. But judge them on their own terms, maintainability, correctness, hiring. Don't present them as a performance project, because the performance case will likely fail its own measurement.

## What I'd do instead (falsifiable version)

1. **Instrument.** Add OpenTelemetry tracing on the slow routes, and run `py-spy` in production for CPU flamegraphs. Turn on DB query logging with timings. Within a week you'll know where wall time goes, per endpoint.
2. **Pre-register a prediction.** Write down something like: "Fixing X should take endpoint Y's p95 from A to B." If you're wrong, you've learned something about the system.
3. **Pick the action based on what the measurement shows:**
   - **Mostly I/O or DB time**, the likely case: query fixes, indexes, batching, caching, connection pooling, a read replica. Rust doesn't help here.
   - **Concurrency pathology** (blocked event loop, pool starvation, too few workers): a config or architecture fix.
   - **Real CPU hotspots** (serialization, validation, a scoring or pricing loop, parsing): swap in Rust-backed libraries first. `orjson`, pydantic v2 (its core is Rust) and `polars` are all drop-ins. Then write targeted **PyO3** modules for whatever hot loops remain. That's Rust exactly where the 50x speedup actually applies, and nothing else changes.
   - **One subsystem that's fundamentally CPU-bound and well-bounded:** pull it out as a Rust service behind a stable interface (the strangler-fig approach). Use shadow traffic and compare outputs before cutover.
4. **Set a kill criterion for the full rewrite.** It's only justified if profiling shows Python CPU time is a large share of wall time on the hot paths, and the optimizations above have run out. Pick a threshold up front, e.g. more than 50% of time in interpreter CPU *after* the I/O fixes. Most 50k-line web services never meet that bar.

**Bottom line:** spend one or two weeks on measurement before committing a quarter or more to a rewrite. Then get cheap evidence: the data you'd need to justify a rewrite is the same data that usually shows you don't need one. If it shows you do, you'll know which 5% of the code to write in Rust.
