import click
import pkg_resources  # part of setuptools
from rich.console import Console
from rich.table import Table


@click.command()
def cli():
    """
    AgentFUD Art Engine version and project info
    """
    version = pkg_resources.require("agentfud-art-engine")[0].version
    table = Table(show_header=False)
    table.add_row("artengine version", version)
    table.add_row("Python package", "https://pypi.org/project/agentfud-art-engine/")
    table.add_row("Repository", "https://github.com/AgentFUD/agentfud-art-engine")
    table.add_row("Issues", "https://github.com/AgentFUD/agentfud-art-engine/issues")
    table.add_row("News & Contact", "https://twitter.com/AgentFud")
    console = Console()
    console.print(table)
