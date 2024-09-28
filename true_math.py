# В true_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
# Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)

from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second


if __name__ == '__main__':
    result1 = divide(2, 0)
    result2 = divide(43, 2)
    print(result1)
    print(result2)