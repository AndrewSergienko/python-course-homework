"""
Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж):
периметр квадрата, площа квадрата та його діагональ.
"""
import math


def square(side_len):
    result = (side_len * 4, side_len ** 2, side_len * math.sqrt(2))
    return result


print(square(int(input("Input len side: "))))
