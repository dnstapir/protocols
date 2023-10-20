"""Split JSON schema in YAML into JSON files, one per subschema"""

import argparse
import json
from copy import deepcopy
from pathlib import Path

import yaml


def main():
    """Main function"""

    parser = argparse.ArgumentParser(description="Schema splitter")
    parser.add_argument("schema", metavar="filename")
    args = parser.parse_args()

    with open(args.schema) as fp:
        schema = yaml.safe_load(fp)

    subschemas = schema.get("anyOf", [])

    subschemas_names = []
    for subschema in subschemas:
        subschemas_names.append(subschema["$ref"].split("/")[-1])

    for subschema in subschemas:
        name = subschema["$ref"].split("/")[-1]

        schema2 = deepcopy(schema)

        schema2["properties"].update(schema["components"]["schemas"][name])

        del schema2["anyOf"]
        for n in subschemas_names:
            del schema2["components"]["schemas"][n]

        output = Path(args.schema).stem + f"-{name}.json"

        with open(output, "wt") as fp:
            json.dump(schema2, fp)


if __name__ == "__main__":
    main()
