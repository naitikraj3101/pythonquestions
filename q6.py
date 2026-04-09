# Q program to check prime number
import math

def is_prime(x:int) -> bool:
    if x <= 1:
        return False
    elif x == 2:
        return True

    for i in range(3,int(math.sqrt(x))+ 1, 2):
        if x % i == 0:
            return False
        return True

for i in range(1,20):
    status = is_prime(i)
    print(f'{i} is a prime number' if status else f'{i} is not a prime number')