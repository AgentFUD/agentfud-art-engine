import click
import os
import shutil
from art_engine import appconfig


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
    for dir in appconfig.project_template:
        os.makedirs(
            os.path.join(target_directory, appconfig.project_template[dir]),
            exist_ok=True,
        )
    shutil.copy("art_engine/instance_config_template.py", target_directory)
    shutil.move(
        target_directory + "/instance_config_template.py",
        target_directory + "/instance_config.py",
    )
    click.echo("Done ...")
