from waapi_uri import uri
from waapi import WaapiClient


def test_uris():
    assert uri is not None
    assert uri.ak_wwise_core_object_get == "ak.wwise.core.object.get"
    with WaapiClient() as client:
        uris = client.call("ak.wwise.waapi.getFunctions")["functions"]  # type: ignore
        for uri_name in uris:
            assert hasattr(uri, uri_name.replace(".", "_"))
