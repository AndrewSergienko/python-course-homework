"""
Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
"""


class LoginException(Exception):
    def __str__(self):
        return "Invalid username or password"


def authorization(username, password, silent=False):
    users = [
        ['username1', 'password1'],
        ['user1234', 'qwertyuiop'],
        ['nagibator2008', 'xXtraktorXx'],
        ['Killer_Jack', '13092006sobaka'],
        ['Renamed_User12345', '1q2w3e4r5t']
    ]
    for user in users:
        if username == user[0] and password == user[1]:
            return True
    if silent:
        return False
    else:
        raise LoginException()


login, password = input("Input login and password: ").split(" ")
silent = True if input("on silent? (1 - True, 0 - False): ") == "1" else False
print(authorization(login, password, silent))
