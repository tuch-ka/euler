"""
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
"""


def check_division(number) -> bool:
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True


x = 2520
while True:
    if check_division(x):
        print(x)
        break
    x += 20
