"""Imports json to enable json manipulation."""
import json


class Inventory:
    """Manages the inventory json file and allows the user to add or remove items."""

    def __init__(self):
        self.filepath = "inventory_data.json"
        if not self.json_exists(self.filepath):
            self.create_json_file(self.filepath)

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

    def add_item(self, filepath: str, item: str, price: float):
        """Adds an item and its price to the json file."""
        new_item_data = {
            item: {
                "price": price
            }
        }
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        data.update(new_item_data)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def remove_item(self, filepath: str, item: str):
        """Removes an item from the json file."""
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        data.pop(item)
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


inv = Inventory()
inv.add_item(inv.filepath, "bread", 2.7)
