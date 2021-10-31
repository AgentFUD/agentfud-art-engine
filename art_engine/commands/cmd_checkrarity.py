from enum import _auto_null
import click
import json
import os
from rich import console

from rich.console import Console
from art_engine.engine import ArtEngine
import art_engine.appconfig as config
from rich.console import Console
from rich.table import Table


@click.command()
def cli():
    """
    Compares planned and actual rarities
    """
    engine = ArtEngine(config)
    engine.setup_engine()

    all_attributes = []
    trait_counts = {}
    # Get all the metadata json files
    metadata_files = os.listdir("./build/metadata")
    for fname in metadata_files:
        with open(os.path.join("./build/metadata", fname), "r") as jsonfile:
            metadata_json_content = json.load(jsonfile)
        all_attributes.append(metadata_json_content["attributes"])

    number_of_items_in_collection = len(all_attributes)

    for item_attributes in all_attributes:
        for attribute in item_attributes:
            if attribute["trait_type"] not in trait_counts:
                trait_counts[attribute["trait_type"]] = {}
            else:
                if attribute["value"] not in trait_counts[attribute["trait_type"]]:
                    trait_counts[attribute["trait_type"]][attribute["value"]] = 1
                else:
                    trait_counts[attribute["trait_type"]][attribute["value"]] += 1

    project = os.getcwd()
    table = Table()
    table.add_column(
        f"Trait type / Trait value ([yellow]Σ:{number_of_items_in_collection}[/yellow])", style="gold3"
    )
    table.add_column("Item count", style="dodger_blue1")
    table.add_column("Rarity", style="dodger_blue1")

    for k, v in trait_counts.items():
        for x, y in v.items():
            rarity = "{:.2f}".format(y / number_of_items_in_collection * 100)
            rarity = f"{rarity} %"
            table.add_row(f"{k} / {x}", str(y), rarity)
    console = Console()
    console.print(table)
