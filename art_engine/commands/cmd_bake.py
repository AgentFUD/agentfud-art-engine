import click
import shutil
import os
from art_engine.engine import ArtEngine
import art_engine.appconfig as config


@click.command()
@click.argument('type', type=click.Choice(['images', 'metadata', 'both']))
@click.option('--quantity', '-q', type=int, required=True, help='How many I should generate')
@click.option('--regenerate', '-rg', type=bool)
def cli(type, quantity, regenerate):
    """
    Bakes images and metadata files
    """
    if regenerate:
        shutil.rmtree('./build', ignore_errors=True)
        for dir in config.project_template:
            os.makedirs(
                config.project_template[dir],
                exist_ok=True,
            )    

    engine = ArtEngine(config)
    engine.setup_engine()
    engine.generate_dnas(quantity)
    engine.generate_sprite_configs()
    if type in ['images', 'both']:
        for index, sprite_config in enumerate(engine.sprite_configs):
            engine.build_image(index, sprite_config)
    if type in ['metadata', 'both']:
        for index, dna in enumerate(engine.dnas):
            engine.build_metadata(index, dna)
