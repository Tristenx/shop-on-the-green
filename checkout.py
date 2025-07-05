"""Checkout class."""


class Checkout:
    """Adds items to a cart and calculates the total price."""

    def __init__(self, inventory_data: dict):
        self.inventory_data = inventory_data
        self.cart = []

    def add_item_to_cart(self, item: str):
        """Takes an item as a string and adds it to the cart list."""
        if item in self.inventory_data:
            self.cart.append(item)

    def get_cart_total(self) -> float:
        """Calculates the total cost of everything in the cart."""
        total = 0
        for item in self.cart:
            total += self.inventory_data[item]["price"]
        return total
