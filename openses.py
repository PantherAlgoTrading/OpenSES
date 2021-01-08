#!/usr/bin/env python

import sys
from configparser import ConfigParser
from pathlib import Path


def initialize_openses():
    cwd = Path()
    openses_folder = cwd / ".openses"
    strategies_folder = cwd / "strategies"
    pipelines_folder = cwd / "pipelines"

    openses_folder.mkdir(exist_ok=True)
    strategies_folder.mkdir(exist_ok=True)
    pipelines_folder.mkdir(exist_ok=True)

    config_file = cwd / "config.ini"

    with config_file.open(mode="w") as f:
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
        config.write(f)


commands = {"init": initialize_openses}

if __name__ == "__main__":
    command = sys.argv[1]

    if command in commands:
        commands[command]()
