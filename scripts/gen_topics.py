import argparse
import json
from pathlib import Path


def gen_topic(schema_dir: Path) -> None:
    if not schema_dir.is_dir():
        raise ValueError(f"WAAPI schema directory does not exist: {schema_dir}")

    topics = set()
    for schema_file in schema_dir.glob("*.json"):
        schema = json.loads(schema_file.read_text())
        for topic in schema.get("topics", []):
            topics.add(topic["id"])

    if not topics:
        raise ValueError(f"No WAAPI topics found in: {schema_dir}")

    output = Path(__file__).parent.parent / "src" / "waapi_uri" / "topic.py"
    lines = ["# Generated from Wwise WAAPI schemas. Do not edit manually.", ""]
    variable_names = {}
    for topic in sorted(topics):
        variable_name = topic.replace(".", "_")
        conflicting_topic = variable_names.setdefault(variable_name, topic)
        if conflicting_topic != topic:
            raise ValueError(
                f"Topic variable name collision: {conflicting_topic} and {topic} "
                f"both map to {variable_name}"
            )
        lines.append(f'{variable_name}: str = "{topic}"')
    output.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate WAAPI subscription topic constants from Wwise schemas."
    )
    parser.add_argument(
        "schema_dir",
        type=Path,
        help="Path to Wwise Authoring/Data/Schemas/WAAPI",
    )
    gen_topic(parser.parse_args().schema_dir)
