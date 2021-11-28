"""
Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
"""


def count_identical_elements(data_list):
    result_count = {}
    for i, target in enumerate(data_list):
        if target not in result_count:
            elem_count = 0
            for elem in data_list[i:]:
                if target == elem:
                    elem_count += 1
            result_count[target] = elem_count
    return result_count


data_list = input("Input list (<x1> <x2> ... <xn>): ").split(" ")
print(count_identical_elements(data_list))
