class Calculator:
    """Performs basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b. Handle division by zero."""
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"
