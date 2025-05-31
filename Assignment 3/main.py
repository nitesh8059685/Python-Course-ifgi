import calculator
import shopping

def calculator_tests():
    print("--- Calculator Tests ---")
    calc = calculator.Calculator()  # Create calculator instance
    print("7 + 5 =", calc.add(7, 5))
    print("34 - 21 =", calc.subtract(34, 21))
    print("54 * 2 =", calc.multiply(54, 2))
    print("144 / 2 =", calc.divide(144, 2))
    print("45 / 0 =", calc.divide(45, 0))  # Check zero division handling

def shopping_cart_tests():
    print("\n--- Shopping Cart Tests ---")
    cart = shopping.ShoppingCart()  # Create cart instance

    # Add a few items
    cart.add_item("USB Cable", 5)
    cart.add_item("Wireless Mouse", 2)
    cart.add_item("Headphones", 1)

    # Show items and quantity
    cart.display_items()
    print("Total quantity:", cart.total_quantity())

    # Remove one item and show updated cart
    cart.remove_item("Wireless Mouse")
    cart.display_items()
    print("Total quantity after removal:", cart.total_quantity())

if __name__ == "__main__":
    calculator_tests()
    shopping_cart_tests()
