import click
import shutil
import os
from art_engine.engine import ArtEngine
import art_engine.appconfig as config
from rich.progress import track


@click.command()
@click.argument("type", type=click.Choice(["images", "metadata", "both"]))
@click.option(
    "--quantity", "-q", type=int, required=True, help="How many I should generate"
)
@click.option("--regenerate", "-rg", type=bool)
def cli(type, quantity, regenerate):
    """
    Bakes images and metadata files
    """
    if regenerate:
        shutil.rmtree("./build", ignore_errors=True)
        for dir in config.project_template:
            os.makedirs(
                config.project_template[dir],
                exist_ok=True,
            )

    engine = ArtEngine(config)
    engine.setup_engine()
    engine.generate_dnas(quantity)
    engine.generate_sprite_configs()
    if type in ["metadata", "both"]:
        for index, dna in track(
            enumerate(engine.dnas),
            total=len(engine.dnas),
            description="Baking metadata:",
        ):
            engine.build_metadata(index, dna)
    if type in ["images", "both"]:
        for index, sprite_config in track(
            enumerate(engine.sprite_configs),
            total=len(engine.sprite_configs),
            description="Baking images:",
        ):
            engine.build_image(index, sprite_config)
