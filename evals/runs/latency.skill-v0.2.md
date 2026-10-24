**Probably not.** About 80% likely, a spike at the same clock time every night with a normal day around it comes from something on a schedule, not from the box being too small. You'd be paying twice as much for 24 hours a day to cover one bad hour, and the most likely causes are ones extra CPU barely affects:

- **Lock contention**: a batch `UPDATE`/`DELETE`, a `REFRESH MATERIALIZED VIEW` without `CONCURRENTLY`, a `REINDEX`, or a migration-style `ALTER` queues API queries behind it. More cores do nothing for a query waiting on a lock.
- **I/O and cache eviction**: `pg_dump`, a provider snapshot or backup window, an ETL load, or a big analytics scan pushes your hot working set out of cache. The API then reads from disk until the cache warms up again. More RAM can help a little here, which is why the upgrade might look like it partly worked. That partial win would hide the cause, not fix it.
- **Plan flips**: a nightly bulk load changes table statistics, and the planner picks a bad plan until autoanalyze catches up.
- **Not the database at all**: a client's nightly sync job, cache TTLs that all expire at the same moment and stampede the DB, or a connection pool that recycles or scales down.

**What to do instead:** find the job and move it, throttle it, or isolate it. Run it in chunks with sleeps between them. Point backups and analytics at a replica. Use `CONCURRENTLY`. Set `lock_timeout` on the batch side so the batch job waits instead of the API.

**The check (cheap, and it settles the question):**

1. From 01:50 to 02:30, sample every 10 seconds:
   ```sql
   SELECT wait_event_type, wait_event, count(*)
   FROM pg_stat_activity WHERE state <> 'idle' GROUP BY 1, 2;
   ```
   Also turn on `log_lock_waits`, `log_checkpoints` and `log_autovacuum_min_duration = 0` for that night. If active sessions are mostly in `Lock`, `IO` or `LWLock` waits and CPU stays below about 70%, a bigger instance is the wrong fix. If CPU is pinned and the waits are mostly CPU (no wait event), the upgrade is back in play, or better, tuning whatever is burning that CPU.
2. List everything scheduled near 02:00: crontab, Kubernetes CronJobs, `pg_cron`, the ETL scheduler, and your provider's backup and maintenance windows. Then **move the top suspect by one hour.** If the spike moves with it, you've found the cause, at no cost.

**One more thing to rule out first:** if 02:00 UTC is a low-traffic hour for you, p99 there is computed over far fewer requests. A handful of slow ones, or cold connections and caches, can produce a "spike" that hurts almost nobody. Plot the *count* of requests over your latency SLO by hour, not just p99. If that count is flat, the problem is mostly in the metric. You still want to know the cause, but it stops being urgent.

**Ideas I'd skip:**
- Adding read replicas or sharding: it solves a capacity problem you haven't shown you have.
- Just accepting the spike: only reasonable if the count check above shows almost no one is affected.
