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
                }
            }
            with open("inventory.json", "w") as file:
                json.dump(data, file, indent=4)
            with open("inventory.json", "r") as file:
                inventory_data = json.load(file)

        self.inventory_data = inventory_data

    def add_item(self, item_name, price):
        new_item = {
            item_name: {
                "price": price,
            }
        }
        with open("inventory.json", "r") as file:
            inventory_data = json.load(file)
            inventory_data.update(new_item)
        with open("inventory.json", "w") as file:
            json.dump(inventory_data, file, indent=4)

        self.inventory_data = inventory_data

    def remove_item(self, item_name):
        with open("inventory.json", "r") as file:
            inventory_data = json.load(file)
            if item_name in inventory_data:
                del inventory_data[item_name]
        with open("inventory.json", "w") as file:
            json.dump(inventory_data, file, indent=4)

        self.inventory_data = inventory_data


x = Inventory()
print(x.inventory_data)
x.add_item("eggs", 1.8)
print(x.inventory_data)
