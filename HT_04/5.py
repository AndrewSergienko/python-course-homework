"""
Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""


def fibonacci(num):
    f1 = 0
    f2 = 1
    print(f1)
    while f2 < num:
        print(f2)
        f1, f2 = f2, f1 + f2


fibonacci(int(input("Input num: ")))