from subprocess import CompletedProcess
from typing import TypedDict


class UniverseProcess(TypedDict):
    update_name: tuple[
        CompletedProcess, str, str, bool
    ]  # _, CompletedProcess.stderr, CompletedProcess.stdout, CompletedProcess.returncode > 0
    update_description: tuple[CompletedProcess, str, str, bool]
    restart: tuple[CompletedProcess, str, str, bool]


class PlaceProcess(TypedDict):
    update_name: tuple[CompletedProcess, str, str, bool]
    update_description: tuple[CompletedProcess, str, str, bool]
    update_server_size: tuple[CompletedProcess, str, str, bool]
