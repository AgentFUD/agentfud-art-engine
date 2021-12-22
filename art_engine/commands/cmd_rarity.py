import click, json
from rich.console import Console
from rich.table import Table
from art_engine.engine_factory import ArtEngineFactory
import art_engine.appconfig as config


@click.group()
def cli():
    """
    Generates and checks planned rarities
    """
    pass


@click.command()
def generate():
    """
    Generate rarity configuration file
    """
    factory = ArtEngineFactory(config)
    engine = factory.getEngine()
    engine.setup_engine()
    engine.generate_rarity_config()


@click.command()
def check():
    """
    Compares and outputs real rarities based on DNA database
    """
    factory = ArtEngineFactory(config)
    engine = factory.getEngine()
    engine.setup_engine()

    dnas = []
    trait_counts = {}
    planned_rarities = []
    project_template = None

    if engine.config.engine_type == "simple":
        project_template = config.simple_project_template
    elif engine.config.engine_type == "complex":
        project_template = config.complex_project_template

    try:
        with open(project_template["cache"] + "/metadata.json", "r") as f:
            dnas = json.load(f)
    except FileNotFoundError:
        print("DNA database not found")
        return
    try:
        with open(config.RARITY_JSON_NAME, "r") as file:
            planned_rarities = json.load(file)
    except FileNotFoundError:
        print("Rarity config file not found")
        return

    number_of_items_in_collection = len(dnas)

    for dna in dnas:
        for trait in dna:
            if trait not in trait_counts:
                trait_counts[trait] = {}
            if dna[trait] not in trait_counts[trait]:
                trait_counts[trait][dna[trait]] = 1
            else:
                trait_counts[trait][dna[trait]] += 1

    table = Table()
    table.add_column(
        f"Trait type / Trait value ([yellow]Σ:{number_of_items_in_collection}[/yellow])",
        style="gold3",
    )
    table.add_column("Item count", style="dodger_blue1")
    table.add_column("Planed Weight", style="dodger_blue1")
    table.add_column("Rarity", style="dodger_blue1")

    for k, v in trait_counts.items():
        for x, y in v.items():
            rarity = "{:.2f}".format(y / number_of_items_in_collection * 100)
            rarity = f"{rarity} %"
            planned_rarity = planned_rarities[k][x]
            table.add_row(f"{k} / {x}", str(y), str(planned_rarity), rarity)
    console = Console()
    console.print(table)


cli.add_command(generate)
cli.add_command(check)
