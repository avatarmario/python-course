def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
factorial_5 = factorial(5)
print(f"Factorial of 5: {factorial_5}")

#fibonacci sequence
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci_5 = fibonacci(5)
print(f"Fibonacci of 5: {fibonacci_5}")