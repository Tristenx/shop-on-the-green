"""Imports json to enable json manipulation."""
import json


class Inventory:
    """Manages the inventory json file and allows the user to add or remove items."""

    def __init__(self):
        if not self.json_exists("inventory_data.json"):
            self.create_json_file("inventory_data.json")
        else:
            print("yes")

    def json_exists(self, filepath: str) -> bool:
        """Checks if a file exists."""
        try:
            with open(filepath, "r", encoding="utf-8"):
                return True
        except FileNotFoundError:
            return False

    def create_json_file(self, filepath: str):
        """Creates a json file."""
        default_data = {
            "item": {
                "price": 0
            }
        }
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(default_data, file, indent=4)


inv = Inventory()
