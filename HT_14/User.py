import db_tools as db


class User:
    def __init__(self, login, type):
        self.login = login
        self.type = type
        self.balance = db.select_info_from_db("balance", "balances", "user=:login", {'login': self.login})

    def update_balance(self, new_balance):
        self.balance = new_balance
        db.update_info_in_db("balances", f"balance=:new_balance", f"user=:login",
                             {'new_balance': new_balance, 'login': self.login})
