"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
 які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def show_age(self):
        return self.age

    def print_name(self):
        print(self.name)

    def show_all_information(self):
        return f"Name: {self.name}\nAge: {self.age}\nProfession: {self.profession}"


p1 = Person("Adam Adamson", 26, "Soldier")
p2 = Person("Jack Davidson", 23, "Backend developer")

print(p1.show_all_information(), '\n', p2.show_all_information())
