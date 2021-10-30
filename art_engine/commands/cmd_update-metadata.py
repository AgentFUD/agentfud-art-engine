import click
import os
import json
from rich import print


@click.command()
@click.option("--new-url", "-u", required=True, help="New URL for images")
def cli(new_url):
    """
    Updates image url in generated metadata files
    """
    metadata_files = os.listdir("./build/metadata")
    for fname in metadata_files:
        with open(os.path.join("./build/metadata", fname), "r") as jsonfile:
            json_content = json.load(jsonfile)

        tmp = json_content["image"].rsplit("/", 1)
        new_img_url = "/".join([new_url, tmp[1]])
        json_content["image"] = new_img_url

        with open(os.path.join("./build/metadata", fname), "w") as jsonfile:
            json.dump(json_content, jsonfile, ensure_ascii=False, indent=4)

    print(
        f"[gold3]Processed[/gold3] [blue]{len(metadata_files)}[/blue] [gold3]metadata files[/gold3]"
    )
