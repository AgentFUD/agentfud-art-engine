import os
import click


class ArtEngineCLI(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        commands_folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "commands")
        )
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace("cmd_", "").replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"art_engine.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ArtEngineCLI)
def cli():
    """Welcome to Agent FUD ArtEngine! An all-in-one cli tool for NFT artists!"""
    pass
