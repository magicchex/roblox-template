import subprocess
import sys
import time
import toml
import os
from rbxcloud_types import *
from helper import start_process


def update_universe(toml_: dict, api_key_: str) -> UniverseProcess:
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


def update_place(toml_: dict, api_key_: str) -> dict[str, PlaceProcess]:
    """Updates a place(s)' name, description, and server size

    Args:
        toml (dict): toml.load() -> dict
        api_key (str): roblox api key

    Returns:
        dict[str, PlaceProcess]: {placeName: {rbxcloudCMD, Subprocess}}
    """
    result = {}

    universe_id: dict = toml_.get("universe")
    if universe_id is None:
        return result
    universe_id: int = universe_id.get("id")
    if universe_id is None:
        return result
    universe_id = str(universe_id)

    place_data: dict = toml_.get("place")
    if place_data is None:
        return result
    for place_name, place_info in place_data.items():
        result[place_name] = {}
        if not isinstance(place_name, str):
            continue
        if not isinstance(place_info, dict):
            continue

        pid = place_info.get("id")
        if not isinstance(pid, int):
            continue
        pid = str(pid)
        pdesc = place_info.get("desc")
        server_size = place_info.get("server_size")
        if isinstance(server_size, int):
            server_size = str(server_size)

        result[place_name]["update_name"] = start_process(
            [
                "rbxcloud",
                "place",
                "update-name",
                "--pretty",
                "-u",
                universe_id,
                "-p",
                pid,
                "-n",
                place_name,
                "-a",
                api_key_,
            ]
        )
        if isinstance(pdesc, str):
            result[place_name]["update_description"] = start_process(
                [
                    "rbxcloud",
                    "place",
                    "update-description",
                    "--pretty",
                    "-u",
                    universe_id,
                    "-p",
                    pid,
                    "-d",
                    pdesc,
                    "-a",
                    api_key_,
                ]
            )
        if isinstance(server_size, str):
            result[place_name]["update_server_size"] = start_process(
                [
                    "rbxcloud",
                    "place",
                    "update-server-size",
                    "--pretty",
                    "-u",
                    universe_id,
                    "-p",
                    pid,
                    "-s",
                    server_size,
                    "-a",
                    api_key_,
                ]
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
    print(universe_results["update_name"][2])
    print(universe_results["update_description"][2])
    print(universe_results["restart"][2])

    place_results = update_place(CONFIG, API_KEY)
    for _, place_name_ in enumerate(place_results):
        print(place_results[place_name_]["update_name"][1])
        print(place_results[place_name_]["update_description"][1])
        print(place_results[place_name_]["update_server_size"][1])
