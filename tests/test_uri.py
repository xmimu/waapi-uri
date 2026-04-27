from waapi_uri import uri


def test_uris():
    assert uri is not None
    assert uri.ak_wwise_core_object_get == "ak.wwise.core.object.get"
