"""
Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def validation(username: str, password: str):
    if not 3 <= len(username) <= 50:
        raise ValidationError("Invalid name length. The length should be in the range from 3 to 50.")
    if len(password) < 8:
        raise ValidationError("Invalid password length. Length must be 8 characters or more.")
    if not isdigit_in_string(password) or password.isdigit():
        raise ValidationError("Invalid password. Password must contain letters and numbers")
    if not isupper_and_islower_in_string(password):
        raise ValidationError("Invalid password. Password must be uppercase and lowercase.")
    return True


def isdigit_in_string(string: str):
    for char in string:
        if char.isdigit():
            return True
    return False


def isupper_and_islower_in_string(string: str):
    upper = lower = False
    for char in string:
        if upper and lower:
            return True
        if not upper and char.isupper():
            upper = True
        else:
            lower = True


if __name__ == "__main__":
    username, password = input("Input username and password: ").split(' ')
    print(validation(username, password))
