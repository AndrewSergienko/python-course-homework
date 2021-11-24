"""
Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат.
Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
"""


def func_1():
    return "func1 return"


def func_2():
    return "func2 return"


def func_3():
    return "func3 return"


def power_func(arg_func1, arg_func2, arg_func3):
    result = "power function return:\n"
    result += f"{arg_func1()}\n"
    result += f"{arg_func2()}\n"
    result += f"{arg_func3()}\n"
    return result


print(power_func(func_1, func_2, func_3))
