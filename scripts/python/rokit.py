# pylint: disable=missing-module-docstring
import sys
import os
from helper import start_process


def install_rokit():
    # pylint: disable=missing-function-docstring
    print("Installing rokit via cargo")
    _, cargo_stderr, __, ___ = start_process(["cargo", "install", "rokit", "--locked"])
    if "already installed" in cargo_stderr:
        print("Rokit has already been installed. Now updating rokit.")
        start_process(["rokit", "self-update"], print_on=True)
    else:
        start_process(["rokit", "self-install"], print_on=True)


def get_rokit_tools(filepath: str) -> dict[str, str]:
    """Retrieves tools from rokit.toml
    Args:
        filepath (str): path to rokit.toml
    Returns:
        dict[str, str]: [tool alias]=tool ref
    """
    result = {}
    with open(filepath, "r", encoding="UTF-8") as file:
        lines = file.read().splitlines()
        if "[tools]" in lines:
            extract_rokit_tools = lines[lines.index("[tools]") + 1 :]
        else:
            sys.exit("Could not find tools header in rokit.toml")
    for _, tool in enumerate(extract_rokit_tools):
        alias = tool.split(" = ")[0]
        ref = tool.split(" = ")[-1].replace('"', "")
        ref = ref[: ref.index("@")]
        result[alias] = ref
    if len(result) < 1:
        sys.exit("There were no tools specified in rokit.toml")
    return result


def install_rokit_tools(tools: dict[str, str]):
    """Installs rokit tools

    Args:
        tools (dict[str,str]): from get_rokit_tools()
    """
    for _, dict_key in enumerate(tools):
        print(f"Trusting {tools[dict_key]}")
        start_process(["rokit", "trust", f"{tools[dict_key]}"])
    print("Installing rokit tools")
    start_process(["rokit", "install", "--no-trust-check"], print_on=True)


if __name__ == "__main__":
    ROKIT_TOML = os.curdir + os.sep + "rokit.toml"
    if not os.path.isfile(ROKIT_TOML):
        sys.exit("Could not find rokit.toml")
    rokit_tools = get_rokit_tools(ROKIT_TOML)
    install_rokit()
    install_rokit_tools(rokit_tools)
