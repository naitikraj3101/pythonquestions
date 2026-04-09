def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

terms = int(input("Enter number of terms: "))
series = [fib(i) for i in range(terms)]
print("Fibonacci series:", series)
