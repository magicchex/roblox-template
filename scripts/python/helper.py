import subprocess
from typing import TypedDict


class StartProcessDict(TypedDict):
    CompletedProcess: subprocess.CompletedProcess
    stderr: str
    stdout: str
    has_reach_error: bool


def start_process(command: list[str], print_on=False) -> StartProcessDict:
    """Start an subprocess with check=False and capture_output=True

    Args:
        command (list[str]): the program to run with optional args
        print_on (bool, optional): Whether to print std to terminal. Defaults to False.

    Returns:
        tuple[subprocess.CompletedProcess, str, str, bool]: subprocess, stderr, stdout, error?.
    """
    process = subprocess.run(command, check=False, capture_output=True)
    stderr = process.stderr.decode()
    stdout = process.stderr.decode()
    is_error = process.returncode > 0
    result = {
        "CompletedProcess": process,
        "stderr": stderr,
        "stdout": stdout,
        "has_reach_error": is_error,
    }
    if print_on is False:
        return result
    if len(stderr) > 0:
        print(f'Found errors while running "{command[0]}".\n{stderr}')
    if len(stdout) > 0:
        print(f'"{command[0]}" has outputted the following...\n{stdout}')
    if is_error:
        print(f"{command[0]} has returned a error code of {process.returncode}")
    return result
