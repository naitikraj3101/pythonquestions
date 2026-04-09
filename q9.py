def is_armstrong(num):
    order = len(str(num))
    total = sum(int(digit) ** order for digit in str(num))
    return total == num

start = int(input("Enter start: "))
end = int(input("Enter end: "))

print(f"Armstrong numbers between {start} and {end}:")
for n in range(start, end+1):
    if is_armstrong(n):
        print(n)
