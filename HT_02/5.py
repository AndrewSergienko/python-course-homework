"""Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити).
Словник для роботи захардкодити свій.
Приклад словника (не використовувати):
{'a': 1, 'b': 3, 'c': 1, 'd': 5}
Очікуваний результат:
{'a': 1, 'b': 3, 'd': 5}"""

data_dict = {
    'key1': 1,
    'key2': 'value1',
    'key3': '1',
    1: 1,
    2: 'value1'}

temp_values = []
res_dict = {}
for key, value in data_dict.items():
    if value not in temp_values:
        temp_values.append(value)
        res_dict[key] = value

print(res_dict)