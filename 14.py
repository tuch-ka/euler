"""
Следующая повторяющаяся последовательность определена для множества натуральных чисел:

n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается,
что все сгенерированные таким образом последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.
"""


def generate(number):
    def _generate_next(x):
        if x % 2 == 0:
            return x // 2
        return x * 3 + 1

    count = 0

    while number > 1:
        count += 1
        number = _generate_next(number)

    count += 1
    return count


maximum = 0
result = 0

for i in range(1000000):
    length = generate(i)
    if length > maximum:
        maximum = length
        result = i
        print(f'for now: length = {length}, result = {result}')

print(result)
