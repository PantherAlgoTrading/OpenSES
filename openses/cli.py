from argparse import ArgumentParser
from pathlib import Path

from flask import Flask

from openses.config import initialize_new_config_file
from openses.hub import add_views_to_app, initialize_db_tables


def initialize_openses() -> None:
    """Preparing empty directory for OpenSES instance."""
    cwd = Path.cwd()

    if len(list(cwd.iterdir())) != 0:
        raise RuntimeError("OpenSES can't initialize in non-empty directory")

    openses_folder = cwd / ".openses"
    strategies_folder = cwd / "strategies"
    pipelines_folder = cwd / "pipelines"

    openses_folder.mkdir()
    strategies_folder.mkdir()
    pipelines_folder.mkdir()

    initialize_new_config_file()

    initialize_db_tables()


def serve_openses_hub_instance() -> None:
    app = Flask("openses.hub")
    add_views_to_app(app)
    app.run()


commands = {"init": initialize_openses, "serve": serve_openses_hub_instance}


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("command", help="", choices=["init", "serve", "execute", "new"])
    args = parser.parse_args()

    # TODO: Remove if statement once all choices for command have been implemented
    if args.command in commands:
        commands[args.command]()
    else:
        raise NotImplementedError()
