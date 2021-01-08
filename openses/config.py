from configparser import ConfigParser
from datetime import time, tzinfo
from pathlib import Path
from typing import NamedTuple


class OpenSESConfig(NamedTuple):
    num_workers: int = 4
    renewal_time: str = "16:00:00-05:00"
    open_time: str = "16:05:00-05:00"
    completion_time: str = "16:10:00-05:00"
    instance_name: str = "Hub"
    default_fund_amount: int = 10000
    strategies_directory: str = "strategies"
    pipelines_directory: str = "pipelines"


class OpenSESHubConfig(NamedTuple):
    host: str = "0.0.0.0"
    port: int = 5000


def initialize_new_config_file(working_directory: Path = Path.cwd()) -> None:
    config_file = working_directory / "config.ini"
    config = ConfigParser()
    config["OpenSES"] = OpenSESConfig()._asdict()
    config["OpenSES.Hub"] = OpenSESHubConfig()._asdict()

    with config_file.open(mode="w") as f:
        config.write(f)


def get_config(working_directory: Path = Path.cwd()) -> OpenSESConfig:
    config_file = working_directory / "config.ini"

    if not config_file.exists():
        raise RuntimeError("Can't find config.ini in working directory")

    config = ConfigParser()
    config.read(config_file)

    return OpenSESConfig(**config._sections["OpenSES"])


if __name__ == "__main__":
    initialize_new_config_file()
    print(get_config())
