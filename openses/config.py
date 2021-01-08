from configparser import ConfigParser
from pathlib import Path


def initialize_new_config_file(path: Path) -> None:
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
