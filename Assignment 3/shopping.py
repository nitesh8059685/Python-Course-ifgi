class ShoppingCart:
    """A simple shopping cart to store items and their quantities."""

    def __init__(self):
        """Set up an empty cart."""
        self.items = {}

    def add_item(self, item_name, quantity=1):
        """Add an item with the given quantity."""
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name):
        """Remove an item from the cart."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Item '{item_name}' not found in cart.")

    def total_quantity(self):
        """Get total number of items."""
        return sum(self.items.values())

    def display_items(self):
        """Show all items in the cart."""
        if not self.items:
            print("Shopping cart is empty.")
            return
        print("Current items in the cart:")
        for item, qty in self.items.items():
            print(f" - {item}: {qty}")
