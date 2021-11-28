"""
Вводиться число.
Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""


def num_operation(num):
    if num > 0:
        return num**2
    elif num < 0:
        return num+100
    return num


print(num_operation(int(input("Input num: "))))