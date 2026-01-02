/**
 * Simple Calculator class for CI/CD testing
 */
public class Calculator {

    /**
     * Add two numbers
     */
    public static int add(int a, int b) {
        return a + b;
    }

    /**
     * Subtract two numbers
     */
    public static int subtract(int a, int b) {
        return a - b;
    }

    /**
     * Multiply two numbers
     */
    public static int multiply(int a, int b) {
        return a * b;
    }

    /**
     * Divide two numbers
     */
    public static double divide(int a, int b) throws IllegalArgumentException {
        if (b == 0) {
            throw new IllegalArgumentException("Cannot divide by zero");
        }
        return (double) a / b;
    }

    /**
     * Calculate fibonacci number at position n
     */
    public static long fibonacci(int n) throws IllegalArgumentException {
        if (n < 0) {
            throw new IllegalArgumentException("n must be non-negative");
        }
        if (n == 0)
            return 0;
        if (n == 1)
            return 1;

        long a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            long temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }

    /**
     * Simple greeting function
     */
    public static String greet(String name) {
        return "Hello, " + name + "!";
    }

    /**
     * Main method for testing
     */
    public static void main(String[] args) {
        System.out.println("Calculator test running...");
        System.out.println("10 + 5 = " + add(10, 5));
        System.out.println("10 - 5 = " + subtract(10, 5));
        System.out.println("10 * 5 = " + multiply(10, 5));
        try {
            System.out.println("10 / 5 = " + divide(10, 5));
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
        System.out.println(greet("World"));
        try {
            System.out.println("Fibonacci(10) = " + fibonacci(10));
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
