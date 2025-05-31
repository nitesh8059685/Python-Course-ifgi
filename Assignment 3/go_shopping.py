from easy_shopping import Calculator, ShoppingCart

def main():
    print("--- Using easy_shopping package ---")
    
    calc = Calculator()  # Create calculator
    print("12 + 8 =", calc.add(12, 8))
    print("100 / 0 =", calc.divide(100, 0))  # Division by zero check

    cart = ShoppingCart()  # Create shopping cart
    cart.add_item("Bananas", 5)
    cart.add_item("Eggs", 12)
    cart.display_items()
    print("Total quantity:", cart.total_quantity())

if __name__ == "__main__":
    main()
