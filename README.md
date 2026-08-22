# waapi-uri

Typed string constants for all [Wwise Authoring API (WAAPI)](https://www.audiokinetic.com/library/edge/?source=SDK&id=waapi.html) function URIs and subscription topics.

Eliminates hard-coded strings in your WAAPI automation scripts and enables IDE auto-completion and static type checking.

> **Wwise version:** Constants are generated from the **Wwise 2025.1.10.9233** WAAPI schemas.

## Installation

```bash
pip install waapi-uri
```

## Usage

### Function URIs

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

All WAAPI function URIs available through `WaapiClient` are module-level string constants on `waapi_uri.uri`, named by replacing `.` with `_`. Command-line-only schema functions are excluded.

| Constant | Value |
|---|---|
| `uri.ak_wwise_core_object_get` | `"ak.wwise.core.object.get"` |
| `uri.ak_wwise_core_object_set` | `"ak.wwise.core.object.set"` |
| `uri.ak_soundengine_postEvent` | `"ak.soundengine.postEvent"` |
| … | … |

### Subscription Topics

```python
from waapi_uri import topic
from waapi import WaapiClient

with WaapiClient() as client:
    # Subscribe to object name changes using a typed topic constant
    def on_name_changed(object, **kwargs):
        print(f"Renamed: {object['name']}")

    handler = client.subscribe(topic.ak_wwise_core_object_nameChanged, on_name_changed)
```

All WAAPI subscription topics are available as module-level string constants on `waapi_uri.topic`, using the same naming convention:

| Constant | Value |
|---|---|
| `topic.ak_wwise_core_object_nameChanged` | `"ak.wwise.core.object.nameChanged"` |
| `topic.ak_wwise_core_object_created` | `"ak.wwise.core.object.created"` |
| `topic.ak_wwise_core_project_saved` | `"ak.wwise.core.project.saved"` |
| … | … |

## Regenerating Constants

The constants are generated from the Wwise WAAPI schema files. To regenerate them against a different Wwise version, pass the installation's `Authoring/Data/Schemas/WAAPI` directory:

1. Locate the Wwise WAAPI schema directory.
2. Run the generation scripts:

```bash
python scripts/gen_uri.py "/Library/Application Support/Audiokinetic/Wwise 2025.1.10.9233/Authoring/Data/Schemas/WAAPI"
python scripts/gen_topics.py "/Library/Application Support/Audiokinetic/Wwise 2025.1.10.9233/Authoring/Data/Schemas/WAAPI"
```

These overwrite `src/waapi_uri/uri.py` and `src/waapi_uri/topic.py` with all functions callable through `WaapiClient` and all topics in the specified schema directory.

## Requirements

- Python >= 3.10

## License

[MIT](LICENSE)
