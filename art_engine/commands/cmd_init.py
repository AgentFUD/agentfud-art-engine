import click
import os
import shutil
from art_engine import appconfig
import pathlib


@click.command()
@click.argument("target_directory", type=str)
@click.option(
    "--yes",
    is_flag=True,
    expose_value=False,
    prompt="Are you sure you want to generate a new project?",
)
def cli(target_directory):
    """
    Initializes a new Art Engine project
    """
    click.echo("Init started ...")

    parent_dir = pathlib.Path(__file__).parent.resolve().parent.resolve()
    instance_config_full_path = os.path.join(parent_dir, "instance_config.py")

    for dir in appconfig.project_template:
        os.makedirs(
            os.path.join(target_directory, appconfig.project_template[dir]),
            exist_ok=True,
        )
    shutil.copy(instance_config_full_path, target_directory)
    click.echo("Done ...")
