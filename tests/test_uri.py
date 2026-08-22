import json
from pathlib import Path

from waapi_uri import uri


def test_uris():
    manifest = json.loads(
        (Path(__file__).parent / "fixtures" / "wwise_2025.1.10.9233.json").read_text()
    )
    assert uri is not None
    assert uri.ak_wwise_core_object_get == "ak.wwise.core.object.get"
    assert uri.ak_wwise_core_object_getPropertyNames == (
        "ak.wwise.core.object.getPropertyNames"
    )
    assert uri.ak_wwise_core_plugin_getList == "ak.wwise.core.plugin.getList"
    assert uri.ak_wwise_core_profiler_captureLog_save == (
        "ak.wwise.core.profiler.captureLog.save"
    )

    lines = Path(uri.__file__).read_text().splitlines()
    constants = {
        line.split(":")[0]: line.split('"')[1]
        for line in lines
        if ": str = " in line
    }
    assert constants == {
        function.replace(".", "_"): function for function in manifest["functions"]
    }
