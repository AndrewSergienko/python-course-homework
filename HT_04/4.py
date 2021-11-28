"""
Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
і вертатиме список простих чисел всередині цього діапазона.
"""


def is_prime(num):
    if num > 0:
        if num <= 3:
            return num > 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    return False


def prime_list(start, end):
    result = set()
    if start <= 2 <= end:
        result.add(2)
    if start <= 3 <= end:
        result.add(3)
    for num in range(start, end, 6):
        if is_prime(num-1):
            result.add(num-1)
        if is_prime(num+1):
            result.add(num+1)
    return list(result)


bounds = list(map(int, input("input start end: ").split(" ")))
print(prime_list(bounds[0], bounds[1]))

