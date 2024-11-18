import toml as tml
import os
import sys
from helper import start_process
import time


def check_for_rbxcloud():
    try:
        result = start_process(["rbxcloud", "-h"])
    except FileNotFoundError:
        print("User has not installed rbxcloud on their system.")
        return False

    if result.get("has_reach_error"):
        print("User has not installed rbxcloud on their system.")
        return False
    return True


def check_for_rojo():
    try:
        result = start_process(["rojo", "-h"])
    except FileNotFoundError:
        print("User has not installed Rojo on their system.")
        return False
    if result.get("has_reach_error"):
        print("User has not installed Rojo on their system.")
        return False
    return True


class RBXCloudPlace:
    def __init__(self, toml: dict | str) -> None:
        if not isinstance(toml, str):
            sys.exit("You must give the toml file path as string!")
        toml = tml.load(toml)
        self.__universe = toml.get("universe")
        if not isinstance(self.__universe, dict):
            sys.exit("Could not get universe!")
        self.__places = toml.get("place")
        if not isinstance(self.__places, dict):
            sys.exit("Could not get roblox places as an dictonary!")
        try:
            self.__api_key = sys.argv[1]
        except ValueError:
            sys.exit("No API key provided.")
        self.universe_id = self.__universe.get("id")
        if not isinstance(self.universe_id, int):
            sys.exit("Could not get universe id!")
        self.universe_id = str(self.universe_id)
        self.folder = self.__places.get("folderpath")
        self.current_place: None | dict = None
        self.current_place_name: None | str = None

    def get_places(self):
        result = {}
        for key, value in self.__places.items():
            if not isinstance(value, dict):
                continue
            result[key] = value
        return result

    def get_place(self, place_name: str):
        return self.__places.get(place_name)

    def set_current_place(self, place_name: str):
        isPlace = self.get_place(place_name)
        if not isinstance(isPlace, dict):
            return
        self.current_place = isPlace
        self.current_place_name = place_name
        return self.current_place

    def get_place_id(self):
        if self.current_place is None:
            return None
        place_id = self.current_place.get("id")
        if not isinstance(place_id, int):
            return None
        place_id = str(place_id)
        return place_id

    def __set_up_file_extension(self):
        if self.current_place is None:
            return None
        return (
            os.path.join(self.folder, f"{self.get_place_id()}.rbxl"),
            os.path.join(self.folder, f"{self.get_place_id()}.rbxlx"),
        )

    def get_place_file(self):
        if self.current_place is None:
            return None
        place_rbxl, place_rbxlx = self.__set_up_file_extension()
        if os.path.isfile(self.current_place.get("filepath")):
            return self.current_place.get("filepath")
        if os.path.isfile(place_rbxl):
            return place_rbxl
        if os.path.isfile(place_rbxlx):
            return place_rbxlx
        return None

    def get_version_type(self):
        if self.current_place is None:
            return None
        version_type = self.current_place.get("version_type", "saved")
        if "publish" in version_type:
            version_type = "published"
        else:
            version_type = "saved"
        return version_type

    def get_description(self):
        if self.current_place is None:
            return None
        description = self.current_place.get("desc", "")
        if not isinstance(description, str):
            return None
        return description

    def get_server_size(self):
        if self.current_place is None:
            return None
        server_size = self.current_place.get("server_size")
        if not isinstance(server_size, int):
            return None
        server_size = str(server_size)
        return server_size

    def rbxcloud_experience(self):
        if not check_for_rbxcloud():
            return None
        if self.current_place is None:
            return None
        place_file = self.get_place_file()
        place_id = self.get_place_id()
        if place_file is None:
            return None
        if place_id is None:
            return None

        return start_process(
            [
                "rbxcloud",
                "experience",
                "publish",
                "-f",
                place_file,
                "-p",
                place_id,
                "-u",
                self.universe_id,
                "-t",
                self.get_version_type(),
                "-a",
                self.__api_key,
            ]
        )

    def rbxcloud_update_name(self):
        if not check_for_rbxcloud():
            return None
        if self.current_place is None:
            return None
        place_id = self.get_place_id()
        return start_process(
            [
                "rbxcloud",
                "place",
                "update-name",
                "--pretty",
                "-u",
                self.universe_id,
                "-p",
                place_id,
                "-n",
                self.current_place_name,
                "-a",
                self.__api_key,
            ]
        )

    def rbxcloud_update_description(self):
        if not check_for_rbxcloud():
            return None
        if self.current_place is None:
            return None
        place_id = self.get_place_id()
        place_desc = self.get_description()
        if place_id is None:
            return None
        if place_desc is None:
            return None
        return start_process(
            [
                "rbxcloud",
                "place",
                "update-description",
                "--pretty",
                "-u",
                self.universe_id,
                "-p",
                place_id,
                "-d",
                place_desc,
                "-a",
                self.__api_key,
            ]
        )

    def rbxcloud_update_server_size(self):
        if not check_for_rbxcloud():
            return None
        if self.current_place is None:
            return None
        place_id = self.get_place_id()
        server_size = self.get_server_size()
        if place_id is None:
            return None
        if server_size is None:
            return None
        return start_process(
            [
                "rbxcloud",
                "place",
                "update-server-size",
                "--pretty",
                "-u",
                self.universe_id,
                "-p",
                place_id,
                "-s",
                server_size,
                "-a",
                self.__api_key,
            ]
        )

    def rojo_upload(self):
        if not check_for_rojo():
            return None
        if self.current_place is None:
            print("wow")
            return None
        place_id = self.get_place_id()
        place_file = self.get_place_file()
        if place_id is None:
            return None
        if place_file is None:
            return None
        return start_process(
            [
                "rojo",
                "upload",
                "--api_key",
                self.__api_key,
                "--universe_id",
                self.universe_id,
                "--asset_id",
                place_id,
                place_file,
            ]
        )

    def rojo_build(self):
        if not check_for_rojo():
            return None
        os.makedirs(self.folder, exist_ok=True)
        rbxl, rbxlx = self.__set_up_file_extension()
        rbxl_process = start_process(["rojo", "build", "--output", rbxl])
        rbxlx_process = start_process(["rojo", "build", "--output", rbxlx])
        return rbxl_process, rbxlx_process

    def __loop_through_every_place(self, func: callable):
        result = {}
        for place_name, place_property in self.__places.items():
            if not isinstance(place_property, dict):
                continue
            self.set_current_place(place_name)
            result[place_name] = func()
            time.sleep(1)
        return result

    def rojo_bulk_build(self):
        self.__loop_through_every_place(self.rojo_build)

    def rojo_bulk_upload(self):
        self.__loop_through_every_place(self.rojo_build)

    def rbxcloud_bulk_experience(self):
        self.__loop_through_every_place(self.rbxcloud_experience)

    def rbxcloud_bulk_update_name(self):
        self.__loop_through_every_place(self.rbxcloud_update_name)

    def rbxcloud_bulk_update_description(self):
        self.__loop_through_every_place(self.rbxcloud_update_description)

    def rbxcloud_bulk_update_server_size(self):
        self.__loop_through_every_place(self.rbxcloud_bulk_update_server_size)
