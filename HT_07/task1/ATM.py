from datetime import datetime
from data_functions import get_data, set_data


def get_user_data_path(user, file):
    if file == 'balance':
        return f"data/{user}_data/{user}_balance.data"
    elif file == 'transactions':
        return f"data/{user}_data/{user}_transactions.data"


def get_balance(user):
    return int(get_data(get_user_data_path(user, 'balance')))


def update_balance(user, balance, operation, num):
    if num < 0:
        return
    if operation == "replenishment":
        balance += num
    elif operation == "withdrawal":
        if num > balance:
            return
        balance -= num
    set_data(get_user_data_path(user, 'balance'), 'w', str(balance))
    return balance


def transaction(user, operation, num):
    balance = get_balance(user)
    balance_after = update_balance(user, balance, operation, int(num))
    if balance_after is None:
        log_message = f'operation: "{operation}", amount: {num}, balance: {balance}'
        log_action(user, log_message, status='Error')
        if num < 0:
            return f"Помилка. Спроба здійснити операцію з від'ємним числом"
        return f"Помилка. На вашому рахнуку недостатьно котштів. Баланс: {balance}"
    balance = balance_after
    log_message = f'operation: "{operation}", amount: {num}, balance: {balance}'
    log_action(user, log_message)
    return f"Виконано. Баланс: {balance}"


def log_action(user, message, status='OK'):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    log_message = '{' + f'date: "{date}", time: "{time}", status: "{status}", {message}' + '}\n'
    set_data(get_user_data_path(user, 'transactions'), 'a', log_message)


def login(user, password):
    users = get_data('data/users.data').split('\n')
    users = [user.split(', ') for user in users]
    if [user, password] in users:
        log_message = f'operation: Log-in'
        log_action(user, log_message)
        return True
    return False


def main_interface(user):
    menu = "Виберіть дію:\n" \
           "1. Подивитись баланс\n" \
           "2. Поповнити баланс\n" \
           "3. Зняти кошти\n" \
           "4. Вихід\n"
    num_action = input(f"{menu}Ваша дія: ")
    if num_action == "1":
        print(f"Ваш баланс: {get_balance(user)}")
    elif num_action == "2":
        num = int(input("Введіть кількість: "))
        print(transaction(user, 'replenishment', num))
    elif num_action == "3":
        num = int(input("Введіть кількість: "))
        print(transaction(user, 'withdrawal', num))
    elif num_action == "4":
        print("Завершую роботу")
        return "Exit"
    else:
        print("Незрозуміла команда. Спробуйте знову.")


def start():
    user = None
    is_login = False
    for i in range(3):
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")
        if login(username, password):
            is_login = True
            user = username
            break
        print("Невірний логін або пароль. Осталось спроб: ", 2 - i)
    if is_login:
        while True:
            result = main_interface(user)
            print()
            if result == "Exit":
                return
    else:
        print("Всі спроби вичерпані. Завершую роботу")


start()
