import data_tools as dt


def operation(operation, num1, num2):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y
    }
    if num1 < 0 or num2 < 0 or operation not in operations:
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
    if return_cash is None and oper == "-":
        message = f'"status": "ERROR", "operation": "{operations_message[oper]}", "balance": {balance}'
        print("В наявності немає купюр, щоб видати вам повну суму. Спробуйте зняти іншу суму.")
    else:
        if new_balance is None:
            status = "ERROR"
            print("Помилка транзакції. Невірні дані. Спробуйте ще раз.")
        else:
            status = "OK"
            balance = new_balance
            dt.update_balance(user, balance)
            print(f"Виконано. Баланс: {new_balance}.")
            if oper == "-":
                print("Готівка: \n" + format_cash(return_cash))
        message = f'"status": "{status}", "operation": "{operations_message[oper]}", "balance": {balance}'
    dt.log_transaction(user, message)


def get_banknotes_for_return(num, banknotes_dict, result_dict=None):
    if result_dict is None:
        result_dict = []
    if num == 0:
        return result_dict
    if len(banknotes_dict) == 1 and num % banknotes_dict[0][0] != 0:
        return
    if num // banknotes_dict[0][0] == 0:
        del banknotes_dict[0]
        return get_banknotes_for_return(num, banknotes_dict, result_dict)
    else:
        result_dict.append([banknotes_dict[0][0], num // banknotes_dict[0][0]])
        num %= banknotes_dict[0][0]
        return get_banknotes_for_return(num, banknotes_dict, result_dict)


def update_all_cash(banknotes: list, oper):
    flag = False
    banknotes_atm = dt.get_banknotes()
    for banknote in banknotes:
        flag = False
        for banknote_atm in banknotes_atm:
            if banknote[0] == banknote_atm[0]:
                flag = True
                banknote[1] = operation(oper, banknote_atm[1], banknote[1])
        if not flag and oper == "+":
            banknotes.append([banknote, operation(oper, 0, banknote[1])])
    dt.set_cash(banknotes_atm)


def format_cash(cash):
    result_str = ""
    for banknote in cash:
        result_str += f"{banknote[0]}: {banknote[1]}шт, "
    return result_str[:-2]


def menu(user, number_operation):
    if number_operation == "1":
        print("Ваш баланс:", dt.get_balance(user))
    elif number_operation == "2":
        num = int(input("Введіть кількість: "))
        transaction(user, "-", num)
    elif number_operation == "3":
        num = int(input("Введіть кількість: "))
        transaction(user, "+", num)
    elif number_operation == "4":
        cash_str = input("Введіть значення - <купюра: кількість>: ")
        cash = cash_str.split(': ')
        cash = list(map(int, cash))
        update_all_cash([cash], "+")
    else:
        return "Exit"


def login(username, password):
    users = dt.get_users()
    if [username, password] in users:
        return username
    return False


def start():
    user = False
    count = 2
    while count >= 0:
        username = input("Введіть логін: ")
        password = input("Введіть пароль: ")
        user = login(username, password)
        if user:
            print("Ви зайшли в систему")
            count = 0
        else:
            if count == 0:
                print("Завершую роботу")
                return
            print(f"Невірний логін або пароль. Осталось спроб: ", count)
        count -= 1

    while True:
        print("=================================\n"
              "1. Подивитись баланс\n"
              "2. Зняти кошти\n"
              "3. Поповнити кошти\n"
              "4. Повонити готівку\n"
              "інше. Вийти\n",)
        num_operation = input("Виберіть дію:")
        result = menu(user, num_operation)
        if result == "Exit":
            return


start()