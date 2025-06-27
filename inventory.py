import json


class Inventory:
    def __init__(self):
        try:
            with open(file="inventory.json", mode="r") as file:
                inventory_data = json.load(file)
        except FileNotFoundError:
            data = {
                "eggs": {
                    "price": 1.8,
                    "num_sales": 0,
                }
            }
            with open(file="inventory.json", mode="w") as file:
                json.dump(data, file, indent=4)
            with open(file="inventory.json", mode="r") as file:
                inventory_data = json.load(file)

        self.inventory_data = inventory_data
