import org.junit.Test;
import org.junit.Before;
import static org.junit.Assert.*;

/**
 * Unit tests for Calculator class (JDK 21)
 */
public class CalculatorTest {
    
    private Calculator calculator;
    
    @Before
    public void setUp() {
        calculator = new Calculator();
    }
    
    // Addition tests
    @Test
    public void testAddPositive() {
        assertEquals(5, Calculator.add(2, 3));
    }
    
    @Test
    public void testAddNegative() {
        assertEquals(0, Calculator.add(-1, 1));
    }
    
    @Test
    public void testAddZero() {
        assertEquals(0, Calculator.add(0, 0));
    }
    
    // Subtraction tests
    @Test
    public void testSubtractPositive() {
        assertEquals(2, Calculator.subtract(5, 3));
    }
    
    @Test
    public void testSubtractNegative() {
        assertEquals(-5, Calculator.subtract(0, 5));
    }
    
    @Test
    public void testSubtractZero() {
        assertEquals(0, Calculator.subtract(10, 10));
    }
    
    // Multiplication tests
    @Test
    public void testMultiplyPositive() {
        assertEquals(12, Calculator.multiply(3, 4));
    }
    
    @Test
    public void testMultiplyNegative() {
        assertEquals(-6, Calculator.multiply(-2, 3));
    }
    
    @Test
    public void testMultiplyZero() {
        assertEquals(0, Calculator.multiply(0, 100));
    }
    
    // Division tests
    @Test
    public void testDividePositive() {
        assertEquals(5.0, Calculator.divide(10, 2), 0.0001);
    }
    
    @Test
    public void testDivideFraction() {
        assertEquals(0.5, Calculator.divide(1, 2), 0.0001);
    }
    
    @Test
    public void testDivideNegative() {
        assertEquals(-5.0, Calculator.divide(-10, 2), 0.0001);
    }
    
    @Test(expected = IllegalArgumentException.class)
    public void testDivideByZero() {
        Calculator.divide(10, 0);
    }
    
    // Greeting tests
    @Test
    public void testGreetWithName() {
        assertEquals("Hello, Alice!", Calculator.greet("Alice"));
    }
    
    @Test
    public void testGreetDifferentName() {
        assertEquals("Hello, Bob!", Calculator.greet("Bob"));
    }
    
    // Fibonacci tests
    @Test
    public void testFibonacciBaseZero() {
        assertEquals(0, Calculator.fibonacci(0));
    }
    
    @Test
    public void testFibonacciBaseOne() {
        assertEquals(1, Calculator.fibonacci(1));
    }
    
    @Test
    public void testFibonacciSmall() {
        assertEquals(1, Calculator.fibonacci(2));
        assertEquals(2, Calculator.fibonacci(3));
        assertEquals(3, Calculator.fibonacci(4));
        assertEquals(5, Calculator.fibonacci(5));
    }
    
    @Test
    public void testFibonacciLarger() {
        assertEquals(55, Calculator.fibonacci(10));
        assertEquals(610, Calculator.fibonacci(15));
    }
    
    @Test(expected = IllegalArgumentException.class)
    public void testFibonacciNegative() {
        Calculator.fibonacci(-1);
    }
}
