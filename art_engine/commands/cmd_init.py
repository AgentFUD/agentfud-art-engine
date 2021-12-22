import click
import os
import shutil
from art_engine import appconfig
import pathlib


@click.command()
@click.argument("target_directory", type=str)
@click.option(
    "--project-type",
    type=click.Choice(["simple", "complex"], case_sensitive=False),
    required=True,
)
def cli(target_directory, project_type):
    """
    Initializes a new Art Engine project
    """
    click.echo("Init started ...")
    if project_type == "simple":
        config_file_name = "config_files/simple_instance_config.py"
        project_template = appconfig.simple_project_template
    elif project_type == "complex":
        config_file_name = "config_files/complex_instance_config.py"
        project_template = appconfig.complex_project_template

    parent_dir = pathlib.Path(__file__).parent.resolve().parent.resolve()
    instance_config_full_path = os.path.join(parent_dir, config_file_name)

    for dir in project_template:
        os.makedirs(
            os.path.join(target_directory, project_template[dir]),
            exist_ok=True,
        )
    shutil.copy(
        instance_config_full_path, os.path.join(target_directory, "instance_config.py")
    )
    click.echo("Done ...")
