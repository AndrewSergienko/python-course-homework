"""
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції
з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
"""


class Calc:
    """
    Це клас, який має методи додавання, віднімання, ділення та множення.
    Не потребує аргументів при створенні екземпляру.

    ---- Атрибути ----
    last_result - результат попередньої операції

    ---- Методи ----
    .plus(num1, num2) -> поверне результат додавання чисел
    .minus(num1, num2) -> поверне результат віднімання чисел
    .multiple(num1, num2) -> поверне результат множення чисел
    .division(num1, num2) -> поверне результат ділення чисел
    """
    def __init__(self):
        self.last_result = None

    def plus(self, num1, num2):
        res = num1 + num2
        self.last_result = res
        return res

    def minus(self, num1, num2):
        res = num1 - num2
        self.last_result = res
        return res

    def multiple(self, num1, num2):
        res = num1 * num2
        self.last_result = res
        return res

    def division(self, num1, num2):
        if num2 == 0:
            return
        res = num1 / num2
        self.last_result = res
        return res


a = Calc()
print(
    a.plus(1, 2), '\n',
    'last_result: ', a.last_result, '\n',
    a.minus(1, 2), '\n',
    'last_result: ', a.last_result, '\n',
    a.multiple(5, 2), '\n',
    'last_result: ', a.last_result, '\n',
    a.division(9, 3), '\n',
    'last_result: ', a.last_result, '\n',
    a.__doc__
)