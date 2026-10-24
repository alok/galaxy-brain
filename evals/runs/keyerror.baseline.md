The quick fix is `t = cfg.get('timeout', 30)`. It handles the case you hit, but it misses three others and hides a fourth.

**Where `.get('timeout', 30)` still breaks**

```yaml
# 1. key present, value null
timeout:
```
`cfg.get('timeout', 30)` returns `None`, not 30. The default only applies when the key is absent, and `timeout:` or `timeout: ~` counts as present. Your crash then shows up later, inside whatever function receives `None`.

```yaml
# 2. empty file (or only comments)
```
`yaml.safe_load` returns `None`, so `cfg.get` raises `AttributeError: 'NoneType' object has no attribute 'get'`. Same bug, different exception.

```yaml
# 3. wrong type
timeout: "30"     # or: timeout: 30s
```
You get the string `"30"` back. Nothing checks it until it gets compared or added to something.

**The one `.get` makes worse**

```yaml
timout: 120
```
Before the fix, this typo crashed with `KeyError`, which was a good thing because it told you something was wrong. After the fix it quietly runs with 30, and the user's 120 is ignored. A per-call default turns "config is wrong" into "config is silently ignored". That's the real cost of sprinkling `.get(key, default)` through the code.

**What to do instead**

Validate the config once, at load time, against one schema. Close off unknown keys, and coerce types there:

```python
from dataclasses import dataclass, fields
import yaml

@dataclass(frozen=True)
class Config:
    timeout: float = 30.0

def load_config(path) -> Config:
    raw = yaml.safe_load(open(path)) or {}          # empty file -> {}
    if not isinstance(raw, dict):
        raise ValueError(f"{path}: top level must be a mapping")
    known = {f.name for f in fields(Config)}
    unknown = raw.keys() - known
    if unknown:
        raise ValueError(f"{path}: unknown keys {sorted(unknown)}")  # catches 'timout'
    raw = {k: v for k, v in raw.items() if v is not None}            # null -> default
    cfg = Config(**raw)
    if not isinstance(cfg.timeout, (int, float)) or cfg.timeout <= 0:
        raise ValueError(f"{path}: timeout must be a positive number, got {cfg.timeout!r}")
    return cfg

t = load_config("config.yaml").timeout
```

If you already depend on pydantic, `class Config(BaseModel, extra="forbid"): timeout: PositiveFloat = 30` does the same job in one line. It also gives you string-to-number coercion and decent error messages.

**Design notes**

- Keep the default in one place, the schema, not repeated at every access site. Otherwise the CLI, the tests and the code drift to three different defaults.
- Decide whether `timeout: null` should mean "use the default" (as above) or "no timeout". Many libraries treat `None` as "wait forever", so passing `None` through by accident is a real hazard, not just a style issue. Make that choice on purpose.
- Don't use `cfg.get('timeout') or 30`. It turns `0` into 30. That might be fine here, but it's the same silent-override pattern.

So: `.get` stops the crash. Rejecting unknown keys at load time is what keeps the default from masking a typo.
