import click
from art_engine.engine_factory import ArtEngineFactory
import art_engine.appconfig as config
from rich.console import Console
from rich.table import Table


@click.option(
    "--collection-size",
    "-cs",
    required=True,
    type=int,
    help="How many I should try to generate",
)
@click.option(
    "--retries",
    "-r",
    type=int,
    default=0,
    help="How many additional generation steps should I try",
)
@click.command()
def cli(collection_size, retries):
    """
    Generates DNAs for your project in the cache folder
    """
    factory = ArtEngineFactory(config)
    engine = factory.getEngine()
    engine.setup_engine()
    engine.generate_dnas(collection_size, retries)
    engine.save_dnas()

    console = Console()
    table = Table(show_header=True, header_style="bold yellow")
    table.add_column("Info")
    table.add_column("Value")

    table.add_row("Attempted", str(collection_size))
    table.add_row("Generated", str(len(engine.dnas)))

    console.print(table)
