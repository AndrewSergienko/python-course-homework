"""
6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
"""


class ObjectCounter:
    counter = 0

    def __init__(self):
        ObjectCounter.counter += 1


ObjectCounter()
ObjectCounter()
ObjectCounter()

print(ObjectCounter.counter)
