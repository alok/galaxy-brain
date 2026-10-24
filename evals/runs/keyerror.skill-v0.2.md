The obvious fix, `cfg.get('timeout', 30)`, is mostly right. It misses two ways YAML gives you nothing, though, and once the default is silent, typos get through too.

```python
cfg = yaml.safe_load(f) or {}        # an empty or all-comments file loads as None, not {}
t = cfg.get('timeout')
if t is None:                        # covers a missing key AND `timeout:` / `timeout: null`
    t = 30
```

Why each line is there:

- **`or {}`**: `yaml.safe_load` returns `None` for an empty file. Your `KeyError` then turns into `AttributeError: 'NoneType' object has no attribute 'get'`.
- **`is None` rather than `.get(key, 30)`**: if the file has `timeout:` with no value, the key exists and maps to `None`. So `.get('timeout', 30)` returns `None`, and the crash shows up later in whatever uses `t`.
- **`is None` rather than `.get('timeout') or 30`**: the `or` version quietly turns `timeout: 0` into 30. That matters if 0 means "no wait" or "disabled" anywhere downstream.

**The step past that (about 60% worth doing, depending on how many keys you read):** a silent default means a typo like `timout: 60` loads fine and runs at 30, and you never find out. If the script reads more than two or three config keys, keep all the defaults in one place and reject keys you don't recognize:

```python
from dataclasses import dataclass, fields

@dataclass
class Config:
    timeout: float = 30
    # ...other keys and their defaults

raw = yaml.safe_load(f) or {}
unknown = raw.keys() - {fl.name for fl in fields(Config)}
if unknown:
    raise ValueError(f"unknown config keys: {sorted(unknown)}")
cfg = Config(**{k: v for k, v in raw.items() if v is not None})
```

(Pydantic with `extra="forbid"` does the same thing and also checks types. That catches `timeout: "30s"` as well, which neither version above handles.)

**How to decide:** grep for `cfg[` and `cfg.get(` in the script. If `timeout` is the only key, use the three-line fix and stop. If there are several, use the dataclass. Every one of those accesses can fail the same way, and fixing them one at a time scatters defaults all over the code.

**What I'd skip:** making `timeout` required so the crash counts as correct. You said the default is 30, so that answers a different question. Writing a full JSON Schema for the YAML is also too much for one script.
