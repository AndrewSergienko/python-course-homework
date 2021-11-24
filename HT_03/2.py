"""
Користувачем вводиться початковий і кінцевий рік.
Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).
"""

start_year, end_year = list(map(int, input("Input years (<start_year> <end_year>): ").split(" ")))

for year in range(start_year, end_year+1):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year)
