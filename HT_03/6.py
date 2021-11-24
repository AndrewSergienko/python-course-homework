"""
Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""


# для filter()
def is_not_digit(c: str):
    return not c.isdigit()


def analyze_string(string):
    digits = filter(str.isdigit, string)
    digits = list(map(int, digits))
    letters = list(filter(is_not_digit, string))
    if 30 <= len(string) <= 50:
        string_length = len(string)
        number_digits = len(digits)
        print(f"string length: {string_length}\n"
              f"number digits: {number_digits}\n"
              f"number letters: {string_length - number_digits}")
    elif len(string) < 30:
        print(f"sum digits: {sum(digits)}\n"
              f"letters: {''.join(letters)}")
    else:
        print(f"reverse string: {string[::-1]}")


string = input("input string: ")
analyze_string(string)