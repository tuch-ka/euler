"""
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
a^2 + b^2 = c^2

Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""


def is_pifagor(a, b, c) -> bool:
    if a < b < c and a**2 + b**2 == c**2:
        return True
    return False


def is_thousand(a, b, c) -> bool:
    if a + b + c == 1000:
        return True
    return False


def search():
    for x in range(1000):
        for y in range(1000):
            for z in range(1000):
                if is_thousand(x, y, z):
                    if is_pifagor(x, y, z):
                        return x, y, z


res1, res2, res3 = search()
print(res1 * res2 * res3)
