# Rewriting a 50k-line Python service in Rust because it is "too slow"

**The non-obvious take:** the 50x figure is probably measuring the wrong thing. Customers feel end-to-end latency, and for most web services that latency is dominated by waiting: database round trips, calls to upstream APIs, network distance, large payloads, and queueing. A faster language only speeds up the slice that is CPU time spent executing your code. So the real question is not "Python or Rust?" but "what share of a slow request is our code running on the CPU, and which code is it?"

## Why 50x will probably not show up

- **Amdahl's law.** If 85% of a slow request is spent waiting on Postgres and upstream services, infinitely fast handler code saves at most 15%. Rewriting in Rust while keeping the same queries and call pattern leaves that 85% untouched.
- **Microbenchmarks overstate it.** Python-to-Rust gaps of 10x to 100x come from tight numeric loops. Real handlers spend much of their CPU in the framework, JSON encoding and decoding, ORM object construction, and logging. Rust makes those faster too, but rarely by 50x unless the design changes as well.
- **The architecture comes along.** A rewrite often preserves serial external calls, N+1 queries, and chatty service boundaries. You then reproduce the same latency in a faster language.

## Cheaper causes to check first

- N+1 queries and missing indexes. Count queries per request, not just query time.
- Serial calls to external services that could run concurrently.
- Connection pools that are too small, or a new DB or HTTP connection created per request.
- Too few worker processes, or blocking code inside an async framework. A single slow synchronous call stalls every other request on that event loop, which shows up as bad p99 under load.
- Large responses: whole objects returned, no pagination, no compression.
- Work on the request path that could be cached, precomputed, or moved to a background queue.
- Cold starts, if the service scales to zero.
- Distance: a single region serving far-away customers adds tens to hundreds of milliseconds per round trip.
- Frontend weight: bundle size and the number of requests per page. Customers experience this as "slow" even when the API is fine.
- Debug-level logging or tracing in hot paths.

Python-side moves that often give real gains: upgrade to a recent CPython (interpreter speed has improved meaningfully since 3.11), use a faster serializer such as orjson or msgspec, add workers, cache at the right layer, and move one CPU-heavy function into a native extension (Rust via PyO3 and maturin, Cython, or NumPy where it fits). For pure-Python CPU-bound code without C-extension dependencies, PyPy is another option to measure.

## Rewrite-specific risks

- **Parity.** 50k lines carry years of bug fixes and edge-case behavior. A rewrite must reproduce all of it, and the gap is where customer-facing regressions come from.
- **Timeline.** One quarter is very likely too short for a full rewrite of a service this size while feature work continues. A common result is a half-migrated dual system that stays in production far longer than planned.
- **Velocity.** Engineers spend weeks learning ownership, async, and the Rust ecosystem, and hiring pool breadth shrinks.
- **No customer benefit until cutover.** The cutover is the riskiest moment, and it is the only point where customers would notice the change.

## If you still want Rust

Use a strangler approach. Pick the single endpoint or function with the largest measured CPU share, implement it in Rust behind the same interface (a PyO3 extension or a small separate service), and measure end-to-end p50, p95, and p99 under production-like load. Expand only where the numbers move.

## A falsifiable experiment before deciding

1. **Define the metric customers mean.** For example, p95 latency of the top five endpoints by traffic, or page load time. Take a baseline over a representative week.
2. **Trace slow requests.** Use OpenTelemetry, py-spy, or a sampling profiler. For each sampled request, record total time, DB time, external call time, CPU time in your code, and serialization time. This is the most important step.
3. **Predict and test the language hypothesis.** Example prediction: "If our own CPU time is at least 50% of p95 on the top endpoint, a Rust version of its hotspot will cut that p95 by at least 30%. If CPU share is below that, changing language will not fix the complaint." Build a prototype of that hotspot and measure end to end.
4. **Predict and test the cheap fixes.** Example prediction: "Fixing the top three query and I/O issues will cut p95 by X%." Apply them and measure.
5. **Decide on end-to-end deltas**, not microbenchmarks.

Outcomes:

- If profiling shows mostly waiting, the rewrite is not worth it. Fix the I/O and architecture issues.
- If a few hot functions dominate CPU, moving those to Rust is a reasonable targeted change.
- A full rewrite only makes sense when the architecture is sound and the language is genuinely the binding constraint. For a typical web service, that is rare.

If you can share a trace or profile of a slow request, or the top endpoints by p95, I can help work out which of these branches you are in.
