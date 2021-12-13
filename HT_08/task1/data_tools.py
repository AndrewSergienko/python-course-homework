from datetime import datetime


def get_path(file, user=None):
    if user is not None:
        return f"data/{user}_data/{user}_{file}.data"
    return f"data/{file}.data"


def read_full_data(path):
    with open(path) as file:
        return file.read()


def write_data(path, mode, message):
    with open(path, mode) as file:
        file.write(str(message))


def get_balance(user):
    return int(read_full_data(get_path('balance', user)))


def update_balance(user, balance):
    write_data(get_path('balance', user), 'w', balance)


def log_transaction(user, message):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    log_message = '{' + f'"date": "{date}", "time": "{time}", {message}' + '}\n'
    write_data(get_path('transactions', user), 'w', log_message)


def get_banknotes():
    banknotes_str = read_full_data(get_path("amount_cash"))
    banknotes = banknotes_str.split("\n")
    return [[int(x.split(': ')[0]), int(x.split(': ')[1])] for x in banknotes]


def get_users():
    users = read_full_data("data/users.data").split('\n')
    users = [[user.split(', ')[0], user.split(', ')[1]] for user in users]
    return users


def set_cash(cash: list):
    cash_str = ""
    for banknote in cash:
        cash_str += f"{banknote[0]}: {banknote[1]}\n"
    write_data("data/amount_cash.data", 'w', cash_str)