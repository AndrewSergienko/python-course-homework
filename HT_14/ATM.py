import db_tools as dt
from User import User
import request_tools as rt


class ATM:
    def __init__(self, id):
        self.id = id
        self.banknotes = self.get_banknotes()
        self.current_user = None

    def auth(self, login, password):
        user_info = dt.select_info_from_db('*', 'users', 'login=:login AND password=:password',
                                           {'login': login, 'password': password})
        if user_info:
            self.current_user = User(login, user_info[2])
            return True
        return False

    def get_balance(self):
        if type(self.current_user.balance) == tuple:
            return self.current_user.balance[0]
        return self.current_user.balance

    def get_banknotes(self):
        banknotes = dt.select_info_from_db('denomination, value', 'banknotes', 'atm_id=:atm_id', {'atm_id': self.id}, all=True)
        if type(banknotes[0]) == int:
            banknotes = [banknotes]
        return banknotes

    def _operation(self, oper, num1, num2):
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y
        }
        if num1 < 0 or num2 < 0 or oper not in operations or num1 < num2:
            return
        return operations[oper](num1, num2)

    def _transaction(self, oper, num):
        operations_message = {
            "+": "Поповнення балансу",
            "-": "Зняття коштів"}
        balance = self.get_balance()
        new_balance = self._operation(oper, balance, num)
        all_cash = self.banknotes
        return_cash = self.get_banknotes_for_return(num, all_cash)
        if return_cash is None and oper == "-" or not self.availability_banknotes(return_cash):
            print("Невірно введені данні, або в наявності немає купюр, щоб видати вам повну суму. Спробуйте зняти іншу суму.")
        else:
            if new_balance is None:
                print("Помилка транзакції. Невірні дані. Спробуйте ще раз.")
            else:
                return_cash = [[key, return_cash[key]] for key in return_cash]
                balance = new_balance
                self.current_user.update_balance(balance)
                print(f"Виконано. Баланс: {new_balance}.")
                if oper == "-":
                    print("Готівка: \n" + self.format_cash(return_cash))
                    self.update_all_cash(return_cash, "-")
        dt.log_transaction(self.id, self.current_user.login, operations_message[oper], num, balance)

    def get_banknotes_for_return(self, num, cash):
        if num == 0:
            return dict()
        if len(cash) == 0:
            return
        current_banknote = cash[0][0]
        banknote_num = cash[0][1]
        banknotes_needed = num // current_banknote
        notes_num = min(banknote_num, banknotes_needed)

        for i in range(notes_num, -1, -1):
            result = self.get_banknotes_for_return(num - i * current_banknote, cash[1:])
            if result or result == {}:
                return {current_banknote: i} | result if i else result

    def update_all_cash(self, banknotes: list, oper):
        new_banknotes = []
        for banknote in banknotes:
            flag = False
            if self.banknotes is not None:
                for i, banknote_atm in enumerate(self.banknotes):
                    banknote_atm = list(banknote_atm)
                    if banknote[0] == banknote_atm[0]:
                        flag = True
                        banknote_atm[1] = self._operation(oper, banknote_atm[1], banknote[1])
                        self.banknotes[i] = banknote_atm

            if not flag and oper == "+":
                new_banknotes.append([banknote[0], banknote[1]])
        self.update_all_banknotes_value()
        if new_banknotes:
            self.add_new_banknotes(new_banknotes)
        self.banknotes = self.get_banknotes()


    def update_all_banknotes_value(self):
        if self.banknotes is not None:
            for banknote in self.banknotes:
                values_dict = {'id': self.id, "denomination": banknote[0], "value": banknote[1]}
                dt.update_info_in_db('banknotes', 'value=:value', 'atm_id=:id AND denomination=:denomination', values_dict)
        return True

    def add_new_banknotes(self, banknotes):
        for banknote in banknotes:
            values_dict = (self.id ,banknote[0], banknote[1])
            dt.insert_info_in_db('banknotes', 'atm_id, denomination, value', '(?, ?, ?)', values_dict)
        return True

    def format_cash(self, cash):
        result_str = ""
        if cash is None:
            return
        for banknote in cash:
            result_str += f"{banknote[0]}: {banknote[1]}шт, "
        return result_str[:-2]

    def availability_banknotes(self, cash):
        banknotes_atm = self.banknotes
        cash = [[key, cash[key]] for key in cash]
        for banknote in cash:
            for banknote_atm in banknotes_atm:
                if banknote[0] == banknote_atm[0]:
                    if banknote_atm[1] < banknote[1]:
                        return False
        return True

    def start(self):
        user_menu_message = "=================================\n" \
                            "1. Подивитись баланс\n" \
                            "2. Зняти кошти\n" \
                            "3. Поповнити кошти\n" \
                            "4. Курс валют на сьогодні\n" \
                            "5. Курс валюти за певний час\n" \
                            "6. Конвертувати валюту\n" \
                            "інше. Вийти\n"
        collector_menu_message = "=================================\n" \
                                 "1. Подивитись список наявних купюр\n" \
                                 "2. Заправити готівку\n" \
                                 "інше. Вийти\n"
        for i in range(3, 0, -1):
            data = input(f"Введіть логін і пароль через пробіл. Залишилось спроб: {i} - ").split(' ')
            if len(data) == 2:
                login, password = data
            else:
                login = password = None
            auth_result = self.auth(login, password)
            if auth_result:
                print(f"Вітаю. Ви зайшли в систему як {self.current_user.type}")
                menu_dict = {'client': [self.user_menu, user_menu_message],
                             'collector': [self.collector_menu, collector_menu_message]}
                menu, message = menu_dict[self.current_user.type]
                menu_result = None
                while True:
                    print(message)
                    oper_num = input('Введіть номер операції: ')
                    menu_result = menu(oper_num)
                    if menu_result == 'Exit':
                        print('Завершую роботу.')
                        return
            else:
                if i == 1:
                    print('Завершую роботу.')


    def user_menu(self, number_operation):
        currs = {'UAH': "Гривня", 'RUR': "Російський рубль", 'EUR': "Євро", 'USD': "Американський долар",
                 'BYN': "Білоруський рубель", "CAD": "Канадський долар", "CHF": "Швейцарський франк",
                 "CNY": "Юань Женьміньбі", "CZK": "Чеська крона", "DKK": "Данська крона", "GBP": "Фунт стерлінгів",
                 "GEL": "Грузинський ларі", "HUF": "Угорський форинт", "ILS": "Новий ізраїлсьський шекель",
                 "JPY": "Японська єна", "KZT": "Казахстанський теньге", "MDL": "Молдовський лей",
                 "NOK": "Норвезька крона", "PLN": "Злотий", "SEK": "Шведська крона", "UZS": "Узбецький сум",
                 "SGD": "Сінгапурський долар", "TMT": "Туркменський манат", "TRY": "Турецька ліра"}
        if number_operation == "1":
            print("Ваш баланс:", self.get_balance())
        elif number_operation == "2":
            num = int(input("Введіть кількість: "))
            self._transaction("-", num)
        elif number_operation == "3":
            num = int(input("Введіть кількість: "))
            self._transaction("+", num)
        elif number_operation == "4":
            result = rt.get_current_exchange_rate()
            for line in result:
                print(line)
        elif number_operation == "5":
            print("Ініціал    Валюта")
            for curr in currs.keys():
                print(f"{curr} --- {currs[curr]}")
            curr = input("Введіть ініціалі валюти: ")
            date = input("Введіть дату у форматі <dd.mm.yyyy>: ")
            for rate in rt.get_archive_exchange_rate(curr, date):
                print(rate)
        elif number_operation == "6":
            print("Ініціал    Валюта")
            for curr in currs.keys():
                print(f"{curr} --- {currs[curr]}")
            convert_operation = input("Ввеідть данні в наступному форматі <валюта1 валюта2 кількість>: ")
            convert_operation = convert_operation.split(" ")
            print(rt.convert_currency(convert_operation[0], convert_operation[1], int(convert_operation[2])))
        else:
            return "Exit"

    def collector_menu(self, number_operation):
        if number_operation == "1":
            print("Купюри:", self.format_cash(self.banknotes))
        elif number_operation == "2":
            num_str = input("Введіть дані наступним чином: <<banknote1: value1>, <banknoteN: valueN>>: ")
            num = num_str.split(", ")
            if self.is_valid_banknotes(num):
                num = [list(map(int, x.split(": "))) for x in num]
                self.update_all_cash(num, "+")
                print("Купюри внесено. Наявні купюри: ", self.format_cash(self.banknotes))
                dt.log_transaction(self.id, self.current_user.login, "Внесення купюр", 0, 0)
            else:
                print("Невірно введені данні. Спробуйте ще раз.")
        else:
            return "Exit"

    def is_valid_banknotes(self, b_list: list):
        for banknote in b_list:
            banknote = banknote.split(": ")
            if not self.is_natural_number(banknote[0]) or not self.is_natural_number(banknote[1]):
                return False
        return True

    def is_natural_number(self, num_str: str):
        return True if num_str.isdigit() and int(num_str) >= 0 else False

    def exit(self):
        self.current_user = None
        print('Завершую роботу.')
