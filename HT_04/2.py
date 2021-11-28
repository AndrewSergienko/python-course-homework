"""
Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць строком на
< years > років під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
Функція повинна принтануть і вернуть суму, яка буде на рахунку.
"""


def bank(money, years, percent=10.0):
    for _ in range(years):
        money += money/100*percent
    print(money)
    return money


money = float(input("input money: "))
years = int(input("input years: "))
percent = input("input percent or enter: ")
if percent == "":
    bank(money, years)
else:
    bank(money, years, float(percent))

