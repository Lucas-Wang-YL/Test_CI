"""
Unit tests for Python CI/CD validation
"""
import pytest
from main import Calculator, greet, calculate_fibonacci


class TestCalculator:
    """Test cases for Calculator class"""
    
    def test_add(self):
        """Test addition"""
        assert Calculator.add(2, 3) == 5
        assert Calculator.add(-1, 1) == 0
        assert Calculator.add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction"""
        assert Calculator.subtract(5, 3) == 2
        assert Calculator.subtract(0, 5) == -5
        assert Calculator.subtract(10, 10) == 0
    
    def test_multiply(self):
        """Test multiplication"""
        assert Calculator.multiply(3, 4) == 12
        assert Calculator.multiply(-2, 3) == -6
        assert Calculator.multiply(0, 100) == 0
    
    def test_divide(self):
        """Test division"""
        assert Calculator.divide(10, 2) == 5
        assert Calculator.divide(1, 2) == 0.5
        assert Calculator.divide(-10, 2) == -5
    
    def test_divide_by_zero(self):
        """Test division by zero raises error"""
        with pytest.raises(ValueError):
            Calculator.divide(10, 0)


class TestGreet:
    """Test cases for greeting function"""
    
    def test_greet(self):
        """Test greeting message"""
        assert greet("Alice") == "Hello, Alice!"
        assert greet("Bob") == "Hello, Bob!"
    
    def test_greet_empty(self):
        """Test greeting with empty string"""
        assert greet("") == "Hello, !"


class TestFibonacci:
    """Test cases for fibonacci function"""
    
    def test_fibonacci_base_cases(self):
        """Test fibonacci base cases"""
        assert calculate_fibonacci(0) == 0
        assert calculate_fibonacci(1) == 1
        assert calculate_fibonacci(2) == 1
    
    def test_fibonacci_sequence(self):
        """Test fibonacci sequence"""
        assert calculate_fibonacci(5) == 5
        assert calculate_fibonacci(10) == 55
        assert calculate_fibonacci(15) == 610
    
    def test_fibonacci_negative(self):
        """Test fibonacci with negative input"""
        with pytest.raises(ValueError):
            calculate_fibonacci(-1)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
