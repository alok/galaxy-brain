```python
n = len(items) if items is not None else 0
```

This doesn't need a ladder of reframes. It's a narrow question and the obvious answer is basically right. There are only two non-obvious points worth knowing.

**1. Prefer `is not None` over `len(items or [])`.** For a real list the two give the same answer, because an empty list is falsy and `len` is 0 either way. But `or` calls `bool(items)`, and some sequence types refuse that:

```python
import numpy as np
items = np.array([1, 2])
len(items or [])   # ValueError: truth value of an array ... is ambiguous
```

pandas objects do the same. The `is not None` version only checks for the case you meant to check.

**2. Make sure None should really count as 0.** If `None` means "nothing here", returning 0 is fine. If it means "not loaded yet" or "the call failed", the 0 hides a bug: it flows into later code and looks like a real empty result. In that case, deal with it where the value is created, not where it's used:

```python
def process(items: list[str] | None = None) -> None:
    items = [] if items is None else items   # the usual fix for a mutable default argument
    ...
```

From then on, `items` is always a list and plain `len(items)` works. Add the `list[str] | None` type hint and mypy or pyright will flag any other unguarded `len` call before it runs.

To decide: check whether any caller handles `None` differently from `[]`. If none do, normalize at the entry point and drop the guard. If some do, keep `None` and leave the 0 out of it, so each caller handles the None case itself.
