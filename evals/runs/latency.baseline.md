Probably not, at least not yet. A spike that shows up at the same clock time every night almost always comes from something scheduled. Too little hardware for your traffic would look different. Doubling CPU and RAM is a 24/7 cost aimed at a problem that lasts about 20 minutes a day. It may not touch the cause at all. If it does help, it will probably help by accident, and then you've lost the clue that would have told you what's actually wrong.

## Why the bigger instance is the wrong first move

The spike is tied to the clock, not to load. If you were short on capacity, p99 would follow request volume (daytime peaks, Monday mornings, launches). One that fires at exactly 02:00 UTC points to cron, a backup window, a maintenance window or a batch job. The usual suspects are below, along with whether more CPU and RAM would help:

| Likely cause | What it looks like | Does 2x CPU/RAM help? |
|---|---|---|
| **Backup or snapshot** (RDS backup window, `pg_dump`, EBS snapshot) | Storage latency and IO waits rise, CPU stays fairly normal | Mostly no. The limit is storage throughput and IOPS. On RDS a bigger instance class gets more EBS bandwidth, so it might help a little by accident |
| **Lock pileup** (`REFRESH MATERIALIZED VIEW` without `CONCURRENTLY`, a nightly `ALTER`/`REINDEX`/`TRUNCATE`, or a migration waiting behind a long query while everything else waits behind it) | Many sessions show `wait_event_type = Lock`, CPU is *idle* | **No, not at all.** You can't buy your way out of a queue |
| **Batch job / ETL / report query** doing big scans or bulk deletes | CPU and IO rise, and the cache gets flushed | Partly. A bigger cache also hides how bad the job's access pattern is |
| **Cache eviction afterward**: the batch job pushes your hot data out of `shared_buffers` and the OS page cache | p99 stays high *after* the job finishes and recovers slowly as the cache warms | Partly. More RAM keeps more of the hot set, but it's a band-aid |
| **Connection pool exhaustion**: the batch job shares the API's pool or `max_connections` | The API waits on the pool, and DB-side query time looks fine | No |
| **Not the database at all**: cache keys with a daily TTL all expiring at once, log rotation, cert renewal, GC on app hosts | DB metrics are flat while API p99 spikes | No |

Notice the row where CPU is idle. Lock contention is the most common cause I'd expect here, and it's also the one where a bigger instance does nothing.

## A free test you can run soon

DST ends in Europe on **25 Oct** and in the US on **1 Nov**. Watch where the spike lands over the next two weeks:

- **It stays at 02:00 UTC:** something scheduled in UTC (cloud backup or maintenance windows, UTC cron).
- **It moves by an hour:** a job scheduled in some local time zone, or real traffic. Note that 02:00 UTC is 7pm Pacific / 10pm Eastern right now, so check request volume at that hour before assuming nothing is going on.

## What to actually do before Friday's 02:00

1. **Record the wait events.** From 01:45 to 02:30, take a snapshot every 10s:
   ```sql
   SELECT now(), pid, state, wait_event_type, wait_event,
          pg_blocking_pids(pid) AS blocked_by,
          now() - xact_start AS xact_age, left(query, 200)
   FROM pg_stat_activity WHERE state <> 'idle';
   ```
   On RDS you can get the same breakdown from Performance Insights' "DB load by wait". The mix of wait types answers most of the question:
   - **Lock:** contention, so find the blocker.
   - **IO / DataFileRead:** storage or cache.
   - **CPU:** the only case where more CPU is even a candidate.
   - **Client / nothing:** the problem is on the app side.
2. **Turn on the cheap logging:** `log_lock_waits = on`, `log_checkpoints = on`, `log_autovacuum_min_duration = 0`, `log_min_duration_statement = 500ms`.
3. **Take `pg_stat_statements` deltas** for 01:50–02:30 versus a quiet window. The top movers by total time and by `shared_blks_read` will name the job.
4. **List everything scheduled near 02:00:** the RDS/Cloud SQL backup and maintenance windows, crontabs on every host, k8s CronJobs, Airflow/dbt schedules, and any analyst's scheduled queries.
5. **Check whether p99 is high on every endpoint or just a few.** If only a few, see which tables they touch, which narrows the cause quickly.

## Typical fixes once you know the cause

All of these cost less than doubling the instance:

- Take backups from a replica, or move the backup window to your actual quietest hour.
- Use `REFRESH MATERIALIZED VIEW CONCURRENTLY`. Set `lock_timeout` on any DDL so a blocked `ALTER` fails instead of queueing everyone behind it.
- Break bulk deletes and updates into small batches with sleeps between them. Point read-heavy batch work at a replica.
- Give batch jobs their own connection pool and their own `statement_timeout`.
- Add jitter to daily cache TTLs.

## When the upgrade *is* right

Upgrade if the wait events show genuine CPU saturation from work you can't reschedule or move to a replica, or if your daytime headroom is already thin and 02:00 is just the first place it shows. Even then, find the cause first. Otherwise you're paying monthly to blur the clue, and the same job will cause a spike again once it grows into the new headroom.
