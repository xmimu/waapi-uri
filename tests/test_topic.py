from waapi_uri import topic
from waapi import WaapiClient


def test_topics():
    assert topic is not None
    assert topic.ak_wwise_ui_selectionChanged == "ak.wwise.ui.selectionChanged"
    with WaapiClient() as client:
        topics = client.call("ak.wwise.waapi.getTopics")["topics"]  # type: ignore
        for topic_name in topics:
            assert hasattr(topic, topic_name.replace(".", "_"))
