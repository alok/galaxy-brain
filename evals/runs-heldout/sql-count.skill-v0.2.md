The query is the boring one, and it's correct:

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
ORDER BY order_count DESC;
```

The non-obvious part is the meaning, not the syntax. This query gives the right answer to "rows per customer_id" and can still be wrong about "orders per customer" in three common ways:

**1. Customers with zero orders are missing.** `GROUP BY` only produces groups that exist. If you need every customer, including those with 0, start from the customers table:

```sql
SELECT c.customer_id, COUNT(o.customer_id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id;
```

Use `COUNT(o.customer_id)` here, not `COUNT(*)`. `COUNT(*)` counts the NULL-padded row from the LEFT JOIN, so every zero-order customer would show 1.

**2. NULL `customer_id` becomes its own group.** Guest checkouts or broken imports all land in one `NULL` row, which can quietly be your "biggest customer." Filter it out with `WHERE customer_id IS NOT NULL` or label it, but decide on purpose.

**3. A row may not be an order.** Tables called `orders` are often really order *lines* (one row per item), or they include cancelled, test or duplicate rows. In that case you want something like:

```sql
SELECT customer_id, COUNT(DISTINCT order_id) AS order_count
FROM orders
WHERE status <> 'cancelled'
GROUP BY customer_id;
```

**The cheap check:** run `SELECT COUNT(*), COUNT(DISTINCT order_id) FROM orders;`. If the two numbers differ, the table isn't one row per order and the plain `COUNT(*)` is overcounting.

Two related tools worth knowing:

- If you want the count next to each order row instead of collapsing the rows, use a window function: `COUNT(*) OVER (PARTITION BY customer_id)`.
- On a big table, an index on `customer_id` lets most databases answer the `GROUP BY` from the index alone. A precomputed counter column or materialized view is only worth its upkeep if this query runs on a hot path, since it adds a way for the count to drift.
