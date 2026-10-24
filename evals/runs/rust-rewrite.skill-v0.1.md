The non-obvious take: the 50x figure is real, but it only speeds up the part of each request where Python is actually running code. In a typical web service that part is small. Amdahl's law sets the limit. If a fraction *f* of a slow request's wall time is Python CPU, a 50x faster language gives you at most:

| *f* (Python CPU share) | Best-case speedup from the rewrite |
|---|---|
| 0.2 | 1.24x |
| 0.5 | 1.96x |
| 0.9 | 8.5x |

Most CRUD-style services sit nearer 0.2 than 0.9, because the time goes to waiting on the database, the network and other services. Those waits take the same time in Rust.

## The ladder

| Rung | Move | Claim | Distinguishing prediction | Verdict |
|---|---|---|---|---|
| 🧠 1 | obvious | Rewrite all 50k lines in Rust next quarter | Traces show Python CPU at ≥ 70% of wall time, spread evenly across the codebase | **Dies on bounded downside.** A quarter or more with no improvement customers can see, plus bugs from matching the old behavior. At typical *f* the payoff is about 1.2–2x. Rewrite estimates also slip. |
| ✨ 2 | zoom in | A few endpoints and a few causes (N+1 queries, missing indexes, calls made one after another that could run in parallel, an unbounded serializer) carry most of the latency | For the 3–5 flows customers complain about, tracing shows > 60% of wall time in DB or network calls, concentrated in a handful of call sites | **Survives** if the trace shows that concentration. This is the usual result. |
| 🤯 3 | change the objective | The goal is "the flows customers complain about feel fast", which is not the same as "the service is fast". Some fixes don't touch backend speed at all: move a slow export to an async job, paginate, cache a dashboard, remove a frontend request waterfall | Complaints cluster on ≤ 3 named workflows, and some of that time is spent outside the backend | **Survives.** It's cheap to check: pull the actual complaint tickets and match each one to an endpoint. |
| 🌌 4 | transport (queueing theory) | "Slow" may be queueing, not compute. Near saturation, wait time grows like ρ/(1−ρ). Sync workers stuck on I/O (e.g. gunicorn sync workers or a small thread pool) then show huge p99s even when each request's own work is fast | p99 tracks load and time of day. Traces show time spent waiting for a worker before the handler starts | **Survives conditionally.** If it holds, the fix is worker count, async I/O or connection pooling, and it takes days. A Rust rewrite would only help here by accident, through higher throughput per box. |
| 🪐 5 | change the layer | If a real CPU hotspot exists (parsing, pricing math, serialization of large payloads), move only that code into Rust with PyO3/maturin, or swap in libraries that already are Rust (orjson, pydantic v2, polars) | A profile (py-spy) shows one or a few functions taking a large share of CPU on the slow paths | **Survives conditionally.** You get the Rust speedup where it counts, at maybe 1–3% of the rewrite's cost, and you can reverse it one function at a time. |

Clever-arguer check on rung 1: "Rust is 50x faster, so rewrite" would argue just as well for rewriting in C++, Go or Zig, whatever the service's bottleneck is. An argument that doesn't depend on any measurement of your service hasn't used any information about your service.

## Verdict

Rungs 2+3, combined into one move, about 80% confident that the right fix is not a full rewrite: find the flows customers are actually complaining about and measure where their time goes. Rungs 4 and 5 are the likely follow-ups, depending on what the measurement shows.

**Cheapest experiment that settles it (about one week):** add OpenTelemetry tracing to the 3–5 complained-about endpoints, and run py-spy on production for a day. For each flow, compute *f*, the Python CPU share of wall time, and the queue-wait share.

- **Low *f* (< 0.4):** the rewrite is ruled out. Fix the queries, the calls made in sequence, or the worker model (rungs 2–4).
- **High queue-wait share:** this is a capacity or concurrency problem (rung 4).
- **High *f*, concentrated in a few functions:** use PyO3 for those functions (rung 5).
- **High *f*, spread evenly across the whole codebase:** only then is a rewrite a serious option. Even then, do it piece by piece behind the existing API (a strangler-fig migration), not as a one-quarter big bang. Price it against simply adding more machines.

The rewrite plan is ahead of the evidence, not wrong in principle. A week of measurement either confirms it or saves you a quarter.
