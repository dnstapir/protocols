"""Split JSON schema in YAML into JSON files, one per subschema"""

import argparse
import json
import logging
from copy import deepcopy
from pathlib import Path

import yaml


def main():
    """Main function"""

    parser = argparse.ArgumentParser(description="Schema splitter")
    parser.add_argument("schema", metavar="filename")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    with open(args.schema) as fp:
        schema = yaml.safe_load(fp)
        logging.info("Read %s", args.schema)

    subschemas = schema.get("anyOf", [])

    subschemas_names = []
    for subschema in subschemas:
        subschemas_names.append(subschema["$ref"].split("/")[-1])

    for subschema in subschemas:
        subschema_name = subschema["$ref"].split("/")[-1]

        logging.info("Processing %s", subschema_name)

        schema2 = deepcopy(schema)

        schema2["properties"].update(
            schema["components"]["schemas"][subschema_name]["properties"]
        )
        schema2["required"] = list(
            set(schema2["required"])
            | set(schema["components"]["schemas"][subschema_name]["required"])
        )

        del schema2["anyOf"]
        for n in subschemas_names:
            del schema2["components"]["schemas"][n]

        output = Path(args.schema).stem + f"-{subschema_name}.json"
        with open(output, "wt") as fp:
            json.dump(schema2, fp)
            logging.info("Wrote %s", output)

        output = Path(args.schema).stem + f"-{subschema_name}.yaml"
        with open(output, "wt") as fp:
            yaml.dump(schema2, fp)
            logging.info("Wrote %s", output)


if __name__ == "__main__":
    main()
