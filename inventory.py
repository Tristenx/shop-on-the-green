"""Imports json to enable json manipulation."""
import json


class Inventory:
    """Manages the inventory json file and allows the user to add or remove items."""

    def __init__(self):
        self.filepath = "inventory_data.json"
        if not self.json_exists():
            self.create_json_file()
        self.data = self.get_data()

    def json_exists(self) -> bool:
        """Checks if a file exists."""
        try:
            with open(self.filepath, "r", encoding="utf-8"):
                return True
        except FileNotFoundError:
            return False

    def create_json_file(self):
        """Creates a json file."""
        default_data = {
            "item": {
                "price": 0
            }
        }
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(default_data, file, indent=4)

    def add_item(self, item: str, price: float):
        """Adds an item and its price to the json file."""
        if isinstance(price, (float, int)):
            new_item_data = {
                item: {
                    "price": price
                }
            }
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
            data.update(new_item_data)
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            self.data = self.get_data()

    def remove_item(self, item: str):
        """Removes an item from the json file."""
        with open(self.filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        if item in data:
            data.pop(item)
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            self.data = self.get_data()

    def get_data(self) -> dict:
        """Reads the json file and returns the data dictionary."""
        with open(self.filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
