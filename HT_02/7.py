"""
Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
Приклад словника (можете використовувати свій):
dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
Вихідний результат:
MIN: 10
MAX: 60
"""

dict_1 = {1: 70, 2: 20, 3: 30, 4: 40, 5: 50, 6: 10}

print(f"MIN: {dict_1[min(dict_1.keys(), key=lambda x: dict_1[x])]}\n"
      f"MAX: {dict_1[max(dict_1.keys(), key=lambda x: dict_1[x])]}")