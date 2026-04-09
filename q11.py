terms = int(input("Enter number of terms: "))
result = list(map(lambda x: 2 ** x, range(terms)))
print("Powers of 2:", result)
