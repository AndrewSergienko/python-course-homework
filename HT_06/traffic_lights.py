"""
Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
"""
import time


def colors_gen():
    colors = ["Green", "Red"]
    reverse_step = 1
    while True:
        yield colors[::reverse_step]
        reverse_step *= -1


def print_colors(print_time, color1, color2):
    for _ in range(print_time):
        print(f"{color1}{' '*(14-len(color1))}{color2}")
        time.sleep(1)


def traffic_lights(color_time=3, change_color_time=1):
    get_colors = colors_gen()
    while True:
        color_for_cars, color_for_pedestrians = get_colors.__next__()
        print_colors(color_time, color_for_cars, color_for_pedestrians)
        color_for_cars = "Yellow"
        print_colors(change_color_time, color_for_cars, color_for_pedestrians)


traffic_lights()
