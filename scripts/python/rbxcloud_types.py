from typing import TypedDict
from helper import StartProcessDict


class UniverseProcess(TypedDict):
    update_name: StartProcessDict
    update_description: StartProcessDict
    restart: StartProcessDict


class PlaceProcess(TypedDict):
    update_name: StartProcessDict
    update_description: StartProcessDict
    update_server_size: StartProcessDict
    experience: StartProcessDict
