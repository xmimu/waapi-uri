import argparse
import json
from pathlib import Path


def gen_uri(schema_dir: Path) -> None:
    if not schema_dir.is_dir():
        raise ValueError(f"WAAPI schema directory does not exist: {schema_dir}")

    functions = set()
    for schema_file in schema_dir.glob("*.json"):
        schema = json.loads(schema_file.read_text())
        for function in schema.get("functions", []):
            if set(function.get("restrict", [])) == {"commandLine"}:
                continue
            functions.add(function["id"])

    if not functions:
        raise ValueError(f"No WAAPI functions found in: {schema_dir}")

    output = Path(__file__).parent.parent / "src" / "waapi_uri" / "uri.py"
    lines = ["# Generated from Wwise WAAPI schemas. Do not edit manually.", ""]
    variable_names = {}
    for uri in sorted(functions):
        variable_name = uri.replace(".", "_")
        conflicting_uri = variable_names.setdefault(variable_name, uri)
        if conflicting_uri != uri:
            raise ValueError(
                f"URI variable name collision: {conflicting_uri} and {uri} "
                f"both map to {variable_name}"
            )
        lines.append(f'{variable_name}: str = "{uri}"')
    output.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate WAAPI function URI constants from Wwise schemas."
    )
    parser.add_argument(
        "schema_dir",
        type=Path,
        help="Path to Wwise Authoring/Data/Schemas/WAAPI",
    )
    gen_uri(parser.parse_args().schema_dir)
