import click
from art_engine.engine import ArtEngine
import art_engine.appconfig as config
from rich.console import Console
from rich.table import Table


@click.command()
def cli():
    """
    Gathers and prints out information about your project
    """
    engine = ArtEngine(config)
    engine.setup_engine()
    console = Console()
    table = Table(show_header=True, header_style="bold yellow")
    table.add_column("Item")
    table.add_column("Value")

    table.add_row("Max possible combinations", str(engine.max_possible_combinations))
    table.add_row("Number of layers", str(len(engine.config.traits)))

    console.print(table)
