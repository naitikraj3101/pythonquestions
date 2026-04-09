divisor = int(input("Enter divisor: "))
nums = [n for n in range(1, 101) if n % divisor == 0]
print(f"Numbers divisible by {divisor}:", nums)
