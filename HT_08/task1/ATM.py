import data_tools as dt


def operation(operation, num1, num2):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y
    }
    if num1 < 0 or num2 < 0 or operation not in operations or num1 < num2:
        return
    return operations[operation](num1, num2)


def transaction(user, oper, num):
    operations_message = {
        "+": "Поповнення балансу",
        "-": "Зняття коштів"}
    balance = dt.get_balance(user)
    new_balance = operation(oper, balance, num)
    all_cash = dt.get_banknotes()
    return_cash = get_banknotes_for_return(num, all_cash)
    if return_cash is None and oper == "-" or not cash_validate_operation(return_cash):
        message = f'"status": "ERROR", "operation": "{operations_message[oper]}", "balance": {balance}'
        print("В наявності немає купюр, щоб видати вам повну суму. Спробуйте зняти іншу суму.")
    else:
        if new_balance is None:
            status = "ERROR"
            print("Помилка транзакції. Невірні дані. Спробуйте ще раз.")
        else:
            return_cash = [[key, return_cash[key]] for key in return_cash]
            status = "OK"
            balance = new_balance
            dt.update_balance(user, balance)
            print(f"Виконано. Баланс: {new_balance}.")
            if oper == "-":
                print("Готівка: \n" + format_cash(return_cash))
                update_all_cash(return_cash, "-")
        message = f'"status": "{status}", "operation": "{operations_message[oper]}", "balance": {balance}'
    dt.log_transaction(user, message)


def get_banknotes_for_return(num, cash):
    if num == 0:
        return dict()
    if len(cash) == 0:
        return
    current_banknote = cash[0][0]
    banknote_num = cash[0][1]
    banknotes_needed = num // current_banknote
    notes_num = min(banknote_num, banknotes_needed)

    for i in range(notes_num, -1, -1):
        result = get_banknotes_for_return(num - i * current_banknote, cash[1:])
        if result or result == {}:
            return {current_banknote: i} | result if i else result


def update_all_cash(banknotes: list, oper):
    flag = False
    banknotes_atm = dt.get_banknotes()
    for banknote in banknotes:
        flag = False
        for banknote_atm in banknotes_atm:
            if banknote[0] == banknote_atm[0]:
                flag = True
                banknote_atm[1] = operation(oper, banknote_atm[1], banknote[1])
        if not flag and oper == "+":
            banknotes_atm.append([banknote[0], operation(oper, banknote[1], 0)])
    dt.set_cash(banknotes_atm)


def format_cash(cash):
    result_str = ""
    for banknote in cash:
        result_str += f"{banknote[0]}: {banknote[1]}шт, "
    return result_str[:-2]


def user_menu(user, number_operation):
    if number_operation == "1":
        print("Ваш баланс:", dt.get_balance(user))
    elif number_operation == "2":
        num = int(input("Введіть кількість: "))
        transaction(user, "-", num)
    elif number_operation == "3":
        num = int(input("Введіть кількість: "))
        transaction(user, "+", num)
    else:
        return "Exit"


def collector_menu(user, number_operation):
    if number_operation == "1":
        print("Купюри:", format_cash(dt.get_banknotes()))
    elif number_operation == "2":
        num_str = input("Введіть дані наступним чином: <<banknote1: value1>, <banknoteN: valueN>>: ")
        num = num_str.split(", ")
        if is_valid_banknotes(num):
            num = [list(map(int, x.split(": "))) for x in num]
            update_all_cash(num, "+")
            print("Купюри внесено. Наявні купюри: ", format_cash(dt.get_banknotes()))
            message = f'"status": "OK", "operation": "Внесення купюр"'
            dt.log_transaction(user, message)
        else:
            print("Невірно введені данні. Спробуйте ще раз.")
    else:
        return "Exit"


def num_selection(message):
    print(message)
    return input("Виберіть дію: ")


def login(username, password):
    users = dt.get_users()
    if [username, password] in users:
        return username
    return False


def start():
    user_menu_message = "=================================\n" \
                        "1. Подивитись баланс\n" \
                        "2. Зняти кошти\n" \
                        "3. Поповнити кошти\n" \
                        "інше. Вийти\n"
    collector_menu_message = "=================================\n" \
                             "1. Подивитись список наявних купюр\n" \
                             "2. Заправити готівку\n" \
                             "інше. Вийти\n"
    user = False
    count = 2
    user_type = None
    while count >= 0:
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")
        user = login(username, password)
        if user:
            types = {
                'collector': 'Колектор',
                'user': 'Користувач'
            }
            user_type = dt.get_user_type(user)
            print("Ви зайшли в систему як", types[user_type])
            count = 0
        else:
            if count == 0:
                print("Завершую роботу")
                return
            print(f"Невірний логін або пароль. Осталось спроб: ", count)
        count -= 1

    if user_type == "collector":
        menu = collector_menu
        message = collector_menu_message
    else:
        menu = user_menu
        message = user_menu_message

    while True:
        num_operation = num_selection(message)
        result = menu(user, num_operation)
        if result == "Exit":
            return
        print()


def is_natural_number(num_str: str):
    return True if num_str.isdigit() and int(num_str) >= 0 else False


def is_valid_banknotes(b_list: list):
    for banknote in b_list:
        banknote = banknote.split(": ")
        if not is_natural_number(banknote[0]) or not is_natural_number(banknote[1]):
            return False
    return True


def cash_validate_operation(cash: list):
    banknotes_atm = dt.get_banknotes()
    cash = [[key, cash[key]] for key in cash]
    for banknote in cash:
        for banknote_atm in banknotes_atm:
            if banknote[0] == banknote_atm[0]:
                if banknote_atm[1] < banknote[1]:
                    return False
    return True


start()
