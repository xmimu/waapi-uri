from pathlib import Path

from waapi import WaapiClient


def gen_uri():
    with WaapiClient() as client:
        uris = client.call("ak.wwise.waapi.getFunctions")["functions"]  # type: ignore
        file = Path(__file__).parent.parent.joinpath("src", "waapi_uri", "uri.py")
        with open(file, "w") as f:
            for uri in uris:
                f.write(f'{uri.replace(".", "_")}: str = "{uri}"\n')


if __name__ == "__main__":
    gen_uri()
