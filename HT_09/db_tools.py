import sqlite3
from datetime import datetime


def db_connection(func):
    def wrapper(*args):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        try:
            result = func(args, cur)
        except Exception as e:
            result = e
        con.commit()
        con.close()
        return result
    return wrapper


@db_connection
def get_user(args, cur: sqlite3.Cursor):
    request = """SELECT * FROM users WHERE login=:username"""
    user = cur.execute(request, {'username': args[0]}).fetchone()
    return user


@db_connection
def get_balance(args, cur: sqlite3.Cursor):
    request = """SELECT * FROM balances WHERE user=:username"""
    balance = cur.execute(request, {'username': args[0]}).fetchone()
    return balance[1]


@db_connection
def set_balance(args, cur: sqlite3.Cursor):
    request = """UPDATE balances SET balance=:balance WHERE user=:username"""
    cur.execute(request, {"balance": args[1], "username": args[0]})
    return True


@db_connection
def log_transaction(args, cur: sqlite3.Cursor):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    request = """INSERT INTO transactions VALUES (NULL, :date, :time, :user, :operation, :num, :res_balance)"""
    values_dict = {"date": date,
                   "time": time,
                   "user": args[0],
                   "operation": args[1],
                   "num": args[2],
                   "res_balance": args[3]}
    cur.execute(request, values_dict)
    return True


@db_connection
def get_all_banknotes(args, cur: sqlite3.Cursor):
    request = """SELECT * FROM banknotes"""
    banknotes = cur.execute(request).fetchall()
    banknotes = [list(banknote) for banknote in banknotes]
    banknotes = sorted(banknotes, key=lambda x: x[0], reverse=True)
    return banknotes


@db_connection
def set_all_banknotes(args, cur: sqlite3.Cursor):
    request = """UPDATE banknotes SET value=:value WHERE denomination=:denomination"""
    for banknote in args[0]:
        values_dict = {"denomination": banknote[0], "value": banknote[1]}
        cur.execute(request, values_dict)
    return True


@db_connection
def add_new_banknotes(args, cur: sqlite3.Cursor):
    request = """INSERT INTO banknotes VALUES (:denomination, :value)"""
    for banknote in args:
        values_dict = {"denomination": banknote[0], "value": banknote[1]}
        cur.execute(request, values_dict)
    return True


