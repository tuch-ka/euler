"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.
"""


def is_simple(number):
    if number % 2 == 0:
        return number == 2

    d = 3
    while d**2 <= number and number % d != 0:
        d += 2

    return d**2 > number


def generate():
    for x in range(2, 2000000):
        if is_simple(x):
            yield x


simples = [simple for simple in generate()]
print(f'Простые числа: {simples}\nИх сумма: {sum(simples)}')
