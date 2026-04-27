from pathlib import Path

from waapi import WaapiClient


def gen_topic():
    with WaapiClient() as client:
        topics = client.call("ak.wwise.waapi.getTopics")["topics"]  # type: ignore
        file = Path(__file__).parent.parent.joinpath("src", "waapi_uri", "topic.py")
        with open(file, "w") as f:
            for topic in topics:
                f.write(f'{topic.replace(".", "_")}: str = "{topic}"\n')


if __name__ == "__main__":
    gen_topic()
