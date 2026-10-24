The obvious answer:

```sql
SELECT customer_id, COUNT(*) AS n_orders
FROM orders
GROUP BY customer_id;
```

That query is correct. The non-obvious part is that it answers a slightly different question from the one you probably mean. Here's where it goes wrong.

**1. Customers with zero orders don't show up.**
`GROUP BY` can only make groups out of rows that exist. A customer who never ordered isn't missing a count of 0. They're just absent from the result. If you want "orders per customer" and not "customers who have orders, with their counts," start from the customers table:

```sql
SELECT c.customer_id, COUNT(o.order_id) AS n_orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id;
```

**2. In that LEFT JOIN, `COUNT(*)` is a bug.**
A customer with no orders still produces one joined row, with NULLs on the orders side. `COUNT(*)` counts that row, so the customer gets 1. `COUNT(o.order_id)` skips NULLs and correctly gives 0. Rule: `COUNT(*)` counts rows, `COUNT(col)` counts non-NULL values. After an outer join, those two numbers are different.

**3. `NULL` customer_id becomes its own group.**
Orders with no customer (guest checkout, bad data) collapse into a single `NULL` row in the first query. Decide on purpose whether to keep it or filter it out with `WHERE customer_id IS NOT NULL`.

**4. "Rows" may not mean "orders."**
If the table really holds one row per line item, `COUNT(*)` counts items. Use `COUNT(DISTINCT order_id)` to count orders. The same problem appears quietly whenever you join another one-to-many table (payments, shipments) before grouping. The join multiplies rows, and every count goes up with no error to warn you.

**5. If you need the count next to each row, use a window function:**

```sql
SELECT o.*, COUNT(*) OVER (PARTITION BY customer_id) AS customer_order_count
FROM orders o;
```

This keeps every order row and adds the per-customer total, with no self-join.

**6. Conditional counts in one pass:**

```sql
SELECT customer_id,
       COUNT(*) AS total,
       COUNT(*) FILTER (WHERE status = 'refunded') AS refunded
FROM orders
GROUP BY customer_id;
```

`FILTER` works in Postgres and SQLite. Elsewhere, use `SUM(CASE WHEN status = 'refunded' THEN 1 ELSE 0 END)`. To filter on the count itself, use `HAVING COUNT(*) > 5`. `WHERE` runs before grouping, so it can't see the count.

**7. Performance:** an index on `orders(customer_id)` lets most engines answer the basic query from the index alone, without reading the table. On a large table that's the difference between a full table scan and a cheap read of the index.

**Bottom line:** the counting is the easy part. What matters is which entity's rows you're counting (orders, line items, or customers) and what you start from: start from `customers` if zero-order customers should appear, and from `orders` if they shouldn't.
