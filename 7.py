"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?
"""


def is_simple(number):
    if number % 2 == 0:
        return number == 2

    d = 3
    while d**2 <= number and number % d != 0:
        d += 2

    return d**2 > number


i = 1
x = 1
while i <= 10001:
    x += 1
    if is_simple(x):
        i += 1

print(x)
