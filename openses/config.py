from datetime import time
from functools import cache
from pathlib import Path
from typing import Any, MutableMapping, NamedTuple

import toml

CONFIG_FILE_NAME: str = "config.toml"


class OpenSESConfig(NamedTuple):
    num_workers: int = 4
    renewal_time: time = time.fromisoformat("16:00:00")
    open_time: time = time.fromisoformat("16:05:00")
    completion_time: time = time.fromisoformat("16:10:00")
    instance_name: str = "Hub"
    default_fund_amount: int = 10000
    strategies_directory: str = "strategies"
    pipelines_directory: str = "pipelines"


class OpenSESHubConfig(NamedTuple):
    host: str = "0.0.0.0"
    port: int = 5000


def initialize_new_config_file(working_directory: Path = Path.cwd()) -> None:
    config_file = working_directory / CONFIG_FILE_NAME
    config = {"openses": OpenSESConfig()._asdict(), "hub": OpenSESHubConfig()._asdict()}

    # TODO: This always ignores timezones unless it's a datetime. Time is assumed to be EST
    with config_file.open(mode="w") as f:
        toml.dump(config, f)


@cache
def _read_config_file(working_directory: Path) -> MutableMapping[str, Any]:
    config_file = working_directory / CONFIG_FILE_NAME
    if not config_file.exists():
        raise RuntimeError("Can't find config.ini in working directory")

    config: MutableMapping[str, Any]
    with config_file.open() as f:
        config = toml.load(f)

    return config


def get_config(working_directory: Path = Path.cwd()) -> OpenSESConfig:
    config = _read_config_file(working_directory)
    return OpenSESConfig(**config["openses"])


def get_hub_config(working_directory: Path = Path.cwd()) -> OpenSESHubConfig:
    config = _read_config_file(working_directory)
    return OpenSESHubConfig(**config["hub"])
