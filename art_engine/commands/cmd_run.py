import click
import importlib


@click.command()
@click.argument("filename")
def cli(filename):
    """
    Runs any python script
    """
    click.echo(f"Executing {filename}")
    sName = filename.replace("/", ".")[:-3]
    out = importlib.import_module(sName)
