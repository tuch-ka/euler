"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


def is_palindrome(number) -> bool:
    number = str(number)
    if number == number[::-1]:
        return True
    return False


def generate_multiply(maximum, minimum) -> list:
    results = []
    for x in range(maximum, minimum, -1):
        for y in range(maximum, minimum, -1):
            result = x * y
            if is_palindrome(result):
                results.append(result)
    return results


if __name__ == '__main__':
    print(max(generate_multiply(1000, 100)))
