import argparse
from configparser import ConfigParser
from pathlib import Path


def initialize_openses() -> None:
    """Preparing empty directory for OpenSES instance."""
    cwd = Path.cwd()

    if len(list(cwd.iterdir())) != 0:
        raise RuntimeError("OpenSES can't initialize in non-empty directory")

    openses_folder = cwd / ".openses"
    strategies_folder = cwd / "strategies"
    pipelines_folder = cwd / "pipelines"

    openses_folder.mkdir(exist_ok=True)
    strategies_folder.mkdir(exist_ok=True)
    pipelines_folder.mkdir(exist_ok=True)

    config_file = cwd / "config.ini"

    config = ConfigParser()
    config["OpenSES"] = {
        "NumWorkers": "1",
        "RenewalTime": "06:00 EST",
        "OpenTime": "06:05 EST",
        "CompletionTime": "06:10 EST",
        "InstanceName": "OpenSES Instance",
        "DefaultFundAmount": "10000",
        "StrategiesDirectory": "strategies",
        "PipelinesDirectory": "pipelines",
    }

    with config_file.open(mode="w") as f:
        config.write(f)


commands = {"init": initialize_openses}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="", choices=["init", "serve", "execute", "new"])
    args = parser.parse_args()

    if args.command in commands:
        commands[args.command]()
    else:
        raise NotImplementedError()


if __name__ == "__main__":
    main()
