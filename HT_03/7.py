"""
Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""


def calculator(expression: str):
    expression_elems = expression.split(" ")
    operation = expression_elems[1]
    operand1, operand2 = int(expression_elems[0]), int(expression_elems[2])
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "//": lambda x, y: x // y,
        "%": lambda x, y: x % y,
        "**": lambda x, y: x**y,
        "^": lambda x, y: x**y,
    }
    return operations[operation](operand1, operand2)


print(calculator(input("input expression: ")))
