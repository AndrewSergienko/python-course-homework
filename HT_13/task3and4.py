"""
3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white
і метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__
для завдання початкових розмірів об'єктів при їх створенні.
4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при
 створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
"""


class Figure:
    def __init__(self, color):
        self.color = 'white'

    def change_color(self, color):
        self.color = color


class Oval(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius


class Square(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side
