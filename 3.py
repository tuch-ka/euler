"""
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""


def is_simple(number):
    if number % 2 == 0:
        return number == 2

    d = 3
    while d**2 <= number and number % d != 0:
        d += 2

    return d**2 > number


num = 600851475143
square_root = round(num**0.5)

for x in range(square_root, 2, -1):
    if num % x == 0 and is_simple(x):
        print(x)
        break

