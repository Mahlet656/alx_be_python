class Calculator:
    """A simple calculator class to demonstrate static and class methods."""
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """A static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """A class method to multiply two numbers, referencing a class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
