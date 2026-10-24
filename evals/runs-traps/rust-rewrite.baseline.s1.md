# Rewriting a 50k-line Python service in Rust because customers say it is "too slow"

## The short version

Don't start the rewrite on the strength of "Rust is about 50x faster." That number comes from tight CPU loops. A web service spends most of its time waiting: on the database, caches, upstream HTTP calls, and the network to the customer. Changing the language only speeds up the CPU part. Before committing a quarter to a rewrite, find out where the time goes.

## Why "50x" is the wrong number

- Microbenchmarks of CPU-bound code (parsing, numeric loops) can show 10 to 100x differences. A typical request handler is mostly I/O.
- Amdahl's law applies. If 85% of request latency is waiting on I/O, making the Python CPU work 10x faster saves about 14% of latency (0.85 + 0.15/10 = 0.865, so 1/0.865 is roughly 1.16x).
- End-to-end gains from a language swap are often 1.5 to 3x, and only when the rewrite keeps the same query and call patterns.

## The "too slow" probably has a non-language cause

These are common, and most are cheap to test:

- **N+1 queries or lazy ORM loads.** 200 queries at 1 ms each is 200 ms in any language. A Rust rewrite that preserves the access pattern keeps all 200 queries.
- **Missing indexes, unbounded result sets, no pagination**, or serializing whole object graphs when the client needs three fields.
- **Sequential third-party calls** in the request path that could run concurrently or be moved off the path.
- **Connection pool exhaustion.** Requests queue waiting for a DB connection. This looks like slow code but is not CPU.
- **Too few workers**, or sync workers handling I/O-bound traffic.
- **Blocking calls inside async code.** A synchronous DB or HTTP call on the event loop stalls every other request. This is a common Python-specific trap, and fixing it needs no Rust.
- **No caching** for read-mostly data, or cache stampedes.
- **Work done inside the request** that could be a background job.
- **Geography and payloads.** App and database in different regions, uncompressed responses, large payloads, or a frontend making many sequential calls.

## Measure before deciding

1. **Pin down what "too slow" means.** Which endpoints or actions, which customers, what percentile, and what target. Ask customers for specific examples.
2. **Put p50, p95 and p99 per endpoint on a dashboard**, and compare them against a stated target.
3. **Break slow requests into components** with tracing (OpenTelemetry or an APM tool): DB time, external HTTP time, Python CPU time, and queue wait.
4. **Profile under realistic load** with a sampling profiler such as py-spy, which attaches to a live process.
5. **Count queries per request.**

A rule of thumb for the decision: if a hot endpoint spends most of its time (say, more than 60 to 70%) in Python code you wrote, the language matters for that endpoint. If not, a rewrite will not fix it.

## What a 50k-line rewrite actually costs

- **Parity is the hard part, not translation.** 50k lines encode years of edge cases, bug fixes and undocumented behavior. Customers will notice when they change.
- **Calendar.** A rewrite of this size usually takes a team many quarters, plus a period of running old and new systems side by side. One quarter is unlikely to finish and ship it safely.
- **Risk is front-loaded.** Months pass before customers see any improvement, and feature work slows or freezes.
- **Team.** Rust's learning curve, hiring, compile times, and a different operational toolchain.
- **Ecosystem gaps.** Some Python libraries (data, ML, certain vendor SDKs) have no good Rust equivalent, so you may end up calling Python anyway.
- **You may ship the same slowness.** Same database, same queries, same architecture, now in a faster language.

## Cheaper options that keep Python

- Fix the top three measured bottlenecks. These usually account for most of the available win.
- Remove blocking calls from async paths, or add workers for I/O-bound concurrency.
- Faster serialization (orjson, msgspec) and Pydantic v2, whose validation core is written in Rust.
- Caching at the right layer, proper connection pooling, and a pooler such as PgBouncer.
- Move slow work to a queue.
- Upgrade Python. Recent versions are measurably faster, so benchmark your service on them.
- **Rust for one hot function.** If profiling shows one CPU-bound loop, extract it with PyO3 and maturin, or use Cython or numba. This gets Rust's benefit where it is needed without a rewrite.
- **Strangler pattern.** Put one endpoint behind a gateway, served by a Rust service, and measure the real end-to-end gain before deciding whether to continue.

## A plan for the quarter

1. **Weeks 1 to 2:** Instrument the service, set the latency target, and collect specific slow examples from customers.
2. **Weeks 2 to 6:** Fix the top bottlenecks in Python and re-measure after each change.
3. **Around week 6:** If CPU-bound hot paths remain, prototype the single worst endpoint in Rust under production-like load. Measure the actual end-to-end difference, not the microbenchmark.
4. **Decide with criteria written down in advance.** For example: "A Rust version is justified for endpoint X if it cuts p95 by at least 2x and X accounts for at least Y% of CPU or customer complaints." Expand only where the prototype clears that bar.

## When a rewrite is the right call

- Profiles show most time spent in your own Python code, not waiting.
- Compute cost is high and CPU-bound, so the fleet bill is a real driver.
- The team already knows Rust, or has committed the time to learn it.
- You have a strong test suite, or can shadow production traffic and diff old and new outputs.
- You have a specific requirement, such as very high concurrency with tight tail latency, that Python cannot meet even after tuning.

## Bottom line

A full rewrite is probably the wrong first move. Measure where the time goes, fix the I/O and query problems, and isolate CPU-bound hot paths for Rust only if the profile supports it. Treat "50x" as a result for a loop, not a prediction for your service.

Caveat: I don't know this service's architecture, traffic, or profile. The thresholds above are rules of thumb to test against your own data.
