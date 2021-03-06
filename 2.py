"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2,
первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""

series = [1, 2]

while True:
    new_num = series[-1] + series[-2]
    if new_num < 4000000:
        series.append(new_num)
    else:
        break

series[:] = [
    x
    for x in series
    if x % 2 == 0
]

print(sum(series))
