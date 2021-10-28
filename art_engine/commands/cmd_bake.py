import click
from art_engine.engine import ArtEngine
import art_engine.appconfig as config


@click.group()
def cli():
    """
    Bakes images and metadata files
    """


@cli.command()
@click.argument("quantity", type=int)
def images(quantity):
    """Builds images based on configuration"""
    click.echo("Building images...")
    engine = ArtEngine(config)
    engine.setup_engine()
    engine.generate_dnas(quantity)
    engine.generate_sprite_configs()
    for index, sprite_config in enumerate(engine.sprite_configs):
        engine.build_image(index, sprite_config)


@cli.command()
@click.argument("quantity", type=int)
def metadata(quantity):
    """Builds metadata based on configuration"""
    click.echo("Building metadata...")
    engine = ArtEngine(config)
    engine.setup_engine()
    engine.generate_dnas(quantity)
    engine.generate_sprite_configs()
    for index, dna in enumerate(engine.dnas):
        engine.build_metadata(index, dna)


@cli.command()
@click.argument("quantity", type=int)
def all(quantity):
    """Builds images based on configuration"""
    click.echo("Building images and metadata...")
    engine = ArtEngine(config)
    engine.setup_engine()
    engine.generate_dnas(quantity)
    engine.generate_sprite_configs()
    for index, sprite_config in enumerate(engine.sprite_configs):
        engine.build_image(index, sprite_config)
    for index, dna in enumerate(engine.dnas):
        engine.build_metadata(index, dna)
