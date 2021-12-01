"""
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
"""


def custom_range(start, end=None, step=1):
    if step == 0:
        raise ValueError("custom_range() arg 3 must not be zero")
    if end is None:
        end = start
        start = 0
    if step < 0 and start < end:
        return
    count = start
    while start <= count < end or end < count <= start:
        yield count
        count += step
    return


print(list(custom_range(10, 0, -1)))

