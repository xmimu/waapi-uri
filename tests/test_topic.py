import json
from pathlib import Path

from waapi_uri import topic


def test_topics():
    manifest = json.loads(
        (Path(__file__).parent / "fixtures" / "wwise_2025.1.10.9233.json").read_text()
    )
    assert topic is not None
    assert topic.ak_wwise_ui_selectionChanged == "ak.wwise.ui.selectionChanged"

    lines = Path(topic.__file__).read_text().splitlines()
    constants = {
        line.split(":")[0]: line.split('"')[1]
        for line in lines
        if ": str = " in line
    }
    assert constants == {
        subscribed_topic.replace(".", "_"): subscribed_topic
        for subscribed_topic in manifest["topics"]
    }
