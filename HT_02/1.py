# Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
# Елементами списку повинні бути як рядки, так і числа.

input_list = [1, 2, '3', 'string', [1, 2, 3]]
print("".join(map(str, input_list)))
