import click
from art_engine.engine import ArtEngine
import art_engine.appconfig as config


@click.command()
def cli():
    """
    Gathers and prints out information about your project
    """
    engine = ArtEngine(config)
    engine.setup_engine()
    click.echo("." * 60)
    click.echo(f"Max possible combinations: {engine.max_possible_combinations}")
    click.echo(f"Number of layers: {len(engine.config.traits)}")
    click.echo("." * 60)
