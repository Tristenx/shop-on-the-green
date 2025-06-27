import json


class Inventory:
    def __init__(self):
        try:
            with open("inventory.json", "r") as file:
                inventory_data = json.load(file)
        except FileNotFoundError:
            data = {
                "eggs": {
                    "price": 1.8,
                    "num_sales": 0,
                }
            }
            with open("inventory.json", "w") as file:
                json.dump(data, file, indent=4)
            with open("inventory.json", "r") as file:
                inventory_data = json.load(file)

        self.inventory_data = inventory_data

    def add_inventory(self, item_name, price):
        new_item = {
            item_name: {
                "price": price,
                "num_sales": 0,
            }
        }
        with open("inventory.json", "r") as file:
            inventory_data = json.load(file)
            inventory_data.update(new_item)
        with open("inventory.json", "w") as file:
            json.dump(inventory_data, file, indent=4)
        with open("inventory.json", "r") as file:
            inventory_data = json.load(file)

        self.inventory_data = inventory_data
