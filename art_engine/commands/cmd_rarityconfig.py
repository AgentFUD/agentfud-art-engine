import click
from art_engine.engine import ArtEngine
import art_engine.appconfig as config


@click.command()
def cli():
    """
    Generates rarity config json file
    """
    engine = ArtEngine(config)
    engine.setup_engine()
    engine.generate_rarity_config()
    print("Generates rarity config json file.")
