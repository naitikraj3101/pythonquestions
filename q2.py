#Q python program to solve quadratic equation

import math

def solve_quadratic(a, b, c):
    # Calculate discriminant
    D = b**2 - 4*a*c
    
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        return f"Two distinct real roots: {root1}, {root2}"
    elif D == 0:
        root = -b / (2*a)
        return f"One real root (double root): {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*a)
        return f"Complex roots: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i"


print(solve_quadratic(1, -3, -4))  # Equation: x^2 - 3x - 4 = 0
