"""
Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12),
 яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто або осiнь)
"""


def get_season(month_num):
    seasons = {
        "spring🌸": [3, 4, 5],
        "summer☀️": [6, 7, 8],
        "autumn🍁": [9, 10, 11],
        "winter❄️": [12, 1, 2]
    }
    for season, nums in seasons.items():
        if month_num in nums:
            return season
    return "Invalid month number"


num = int(input("input number of the month: "))
print(get_season(num))
