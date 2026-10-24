The obvious fix is `cfg.get('timeout', 30)`, and it fixes the crash you're seeing. But YAML can produce at least three other inputs that it handles badly, and two of them fail silently. Here is each candidate fix, with the input that tells it apart from the one before it.

| Rung | Move | Claim | Input that tells them apart | Verdict |
|---|---|---|---|---|
| 1 | obvious | `t = cfg.get('timeout', 30)` | File with no `timeout` key gives 30 | **Works, but leaks.** Fixes the reported crash and nothing else |
| 2 | zoom in on what YAML actually emits | Missing isn't the only "absent". A line `timeout:` (or `timeout: ~`) means the key exists with value `None`, so `.get` returns `None` and the crash moves to wherever `t` gets used (`TypeError` inside `socket`/`requests`/`sleep`), far from the cause. An empty file makes `yaml.safe_load` return `None`, so `cfg.get` raises `AttributeError`. | Run with a file that contains only `timeout:`, then with an empty file. Rung 1 fails both | **Works.** One extra line, no downside |
| 3 | change the layer | Put defaults in one place at load time, and reject unknown keys. Rungs 1–2 both turn the typo `timout: 5` into a silent 30, and nobody notices until something hangs too long | File with `timout: 5`. Rungs 1–2 quietly run with 30; rung 3 errors | **Works if the config has more than ~3 keys or more than one place reads it.** Otherwise it's optional |
| 4 | dissolve / framework | Either "make timeout required and keep the crash", or pull in pydantic/Hydra and a schema | n/a | **Rejected.** The first ignores your requirement that the default is 30. The second adds a dependency to fix one key, and rung 3 already buys most of what it offers |

Rung 2 has one trap: don't write `cfg.get('timeout') or 30`. That turns `timeout: 0` into 30, and 0 often means "non-blocking" or "no timeout", so you'd be silently overriding a value the user actually set. Test for `None` explicitly.

**Minimum fix (rung 2):**

```python
cfg = yaml.safe_load(f) or {}          # empty file -> {}
t = cfg.get("timeout")
if t is None:                          # covers missing key AND `timeout:` with no value
    t = 30
```

**If the config is more than a couple of keys (rung 3):**

```python
DEFAULTS = {"timeout": 30}             # list every key here, one source of truth

def load_config(path):
    with open(path) as f:
        raw = yaml.safe_load(f) or {}
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: top level must be a mapping, got {type(raw).__name__}")
    unknown = raw.keys() - DEFAULTS.keys()
    if unknown:
        raise ValueError(f"{path}: unknown keys {sorted(unknown)}")   # catches `timout`
    cfg = {**DEFAULTS, **{k: v for k, v in raw.items() if v is not None}}
    t = cfg["timeout"]
    if isinstance(t, bool) or not isinstance(t, (int, float)) or t < 0:
        raise ValueError(f"{path}: timeout must be a non-negative number, got {t!r}")
    return cfg
```

The `bool` check is there on purpose. PyYAML reads YAML 1.1, so `timeout: yes` loads as `True`, and since `True == 1` in Python, a sloppy edit becomes a 1-second timeout. Quoted values like `timeout: "30"` load as strings and fail the same check.

**Verdict:** rung 2 is the floor; I'm about 80% sure that rung 3 is the right answer for you as soon as the config has a second key. The quickest way to decide between them: run `grep -c "cfg\[" yourscript.py`. If only `timeout` is read with bare `cfg[...]`, rung 2 is enough. If you get several hits, every one of them can raise the same `KeyError` and has the same silent-typo problem, so go with rung 3.
