import subprocess
import sys
import toml
import os
from rbxcloud_types import *
from rbxcloud_place import RBXCloudPlace
from helper import start_process


def update_universe(toml_: dict, api_key_: str) -> UniverseProcess | dict[None]:
    """Updates your game's title and description.

    Args:
        toml (dict): toml.load() -> dict
        api_key (str): roblox api key

    Returns:
        UniverseProcess: a dictionary with the completed processes.
    """
    result = {}
    universe_data: dict = toml_.get("universe")
    if universe_data is None:
        return result
    uid: int = universe_data.get("id")
    title: str = universe_data.get("title")
    desc: str = universe_data.get("desc")
    restart: bool = universe_data.get("restart")
    if uid is None:
        return result
    if title is None:
        return result
    if desc is None:
        return result
    if restart is None:
        return result

    uid = str(uid)
    result["update_name"] = start_process(
        [
            "rbxcloud",
            "universe",
            "update-name",
            "-p",
            "-a",
            api_key_,
            "-n",
            title,
            "-u",
            uid,
        ]
    )

    result["update_description"] = start_process(
        [
            "rbxcloud",
            "universe",
            "update-description",
            "-p",
            "-a",
            api_key_,
            "-d",
            desc,
            "-u",
            uid,
        ]
    )
    if not restart:
        return result
    result["restart"] = start_process(
        ["rbxcloud", "universe", "restart", "-a", api_key_, "-u", uid]
    )
    return result


if __name__ == "__main__":
    try:
        has_rbxcloud = subprocess.run(
            ["rbxcloud", "-h"], check=False, capture_output=True
        ).returncode
    except FileNotFoundError:
        sys.exit("User has not installed rbxcloud")
    if has_rbxcloud > 0:
        sys.exit("User has not installed rbxcloud.")
    API_KEY = sys.argv[1] if len(sys.argv) > 1 else sys.exit("No API key provided")
    # pylint: disable=unreachable
    TOML_PATH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else os.path.join(os.pardir, os.pardir, "rbxcloud.toml")
    )

    if not os.path.isfile(TOML_PATH):
        sys.exit("Could not find rbxcloud.toml")
    with open(TOML_PATH, "r", encoding="UTF-8") as f:
        CONFIG = toml.load(f)

    universe_results = update_universe(CONFIG, API_KEY)

    place = RBXCloudPlace(TOML_PATH)
    place.rojo_bulk_build()
