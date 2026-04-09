# fibonacci series

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
num = int(input("Enter how many terms: "))
print(f"Fibonacci series up to {num} terms: {fibonacci(num)}")
