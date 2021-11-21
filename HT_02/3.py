# Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
# Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

sample_data = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
result_data = []
for elem in sample_data:
    if len(elem) != 0:
        result_data.append(elem)

print(result_data)