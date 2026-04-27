# waapi-uri

Typed string constants for all [Wwise Authoring API (WAAPI)](https://www.audiokinetic.com/library/edge/?source=SDK&id=waapi.html) function URIs.

Eliminates hard-coded URI strings in your WAAPI automation scripts and enables IDE auto-completion and static type checking.

> **Wwise version:** URI constants are generated from **Wwise 2025.1.7**.

## Installation

```bash
pip install waapi-uri
```

## Usage

```python
from waapi_uri import uri
from waapi import WaapiClient

with WaapiClient() as client:
    # Use typed constants instead of raw strings
    result = client.call(uri.ak_wwise_core_object_get, {
        "from": {"path": ["\\Actor-Mixer Hierarchy"]},
        "options": {"return": ["name", "type"]},
    })
```

All WAAPI function URIs are available as module-level string constants on `waapi_uri.uri`, named by replacing `.` with `_`:

| Constant | Value |
|---|---|
| `uri.ak_wwise_core_object_get` | `"ak.wwise.core.object.get"` |
| `uri.ak_wwise_core_object_set` | `"ak.wwise.core.object.set"` |
| `uri.ak_soundengine_postEvent` | `"ak.soundengine.postEvent"` |
| … | … |

## Regenerating URIs

The URI constants are auto-generated from a running Wwise instance. To regenerate them against a different Wwise version:

1. Open Wwise with WAAPI enabled.
2. Run the generation script:

```bash
python scripts/gen_uri.py
```

This will overwrite `src/waapi_uri/uri.py` with all function URIs reported by the connected Wwise instance.

## Requirements

- Python >= 3.10

## License

[MIT](LICENSE)
