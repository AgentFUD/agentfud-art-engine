import click
import shutil
import os
from art_engine.engine_factory import ArtEngineFactory
import art_engine.appconfig as config
from rich.progress import track


@click.command()
@click.argument("type", type=click.Choice(["images", "metadata", "both"]))
@click.option("--clean-up/--no-clean-up", "-cl/-ncl", default=False)
def cli(type, clean_up):
    """
    Bakes images and metadata files
    """
    factory = ArtEngineFactory(config)
    engine = factory.getEngine()
    project_template = None

    if engine.config.engine_type == "simple":
        project_template = config.simple_project_template
    elif engine.config.engine_type == "complex":
        project_template = config.complex_project_template

    if clean_up:
        shutil.rmtree("./build", ignore_errors=True)
        for dir in project_template:
            os.makedirs(
                project_template[dir],
                exist_ok=True,
            )

    engine.setup_engine()
    try:
        engine.load_dnas()
    except FileNotFoundError:
        print("DNA database has not been found, please run artengine dna command first")
        return

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
