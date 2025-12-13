"""
Simple Python module for CI/CD testing
"""


class Calculator:
    """Simple calculator class for demonstration"""
    
    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Subtract two numbers"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"


def calculate_fibonacci(n):
    """Calculate fibonacci number at position n"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    # Test basic functionality
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(greet("World"))
    print(f"Fibonacci(10) = {calculate_fibonacci(10)}")
