import sqlite3
from datetime import datetime

def open_connection():
    con = sqlite3.connect('database.sqlite')
    cur = con.cursor()
    return con, cur


def select_info_from_db(column, table, condition=None, values={}, all=False):
    con, cur = open_connection()
    if all:
        if condition:
            sql_request = f'SELECT {column} FROM {table} WHERE {condition}'
            result = cur.execute(sql_request, values).fetchall()
        else:
            sql_request = f'SELECT {column} FROM {table}'
            result = cur.execute(sql_request, values).fetchall()
    else:
        result = cur.execute(f'SELECT {column} FROM {table} WHERE {condition}', values).fetchone()
    con.commit()
    con.close()
    return result


def update_info_in_db(table, action, condition, values):
    con, cur = open_connection()
    cur.execute(f'UPDATE {table} SET {action} WHERE {condition}', values)
    con.commit()
    con.close()


def insert_info_in_db(table, table_values, values, values_dict):
    con, cur = open_connection()
    cur.execute(f'INSERT INTO {table} ({table_values}) VALUES {values}', values_dict)
    con.commit()
    con.close()


def log_transaction(*args):
    con, cur = open_connection()
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    request = """INSERT INTO transactions VALUES (NULL, :atm_id, :date, :time, :user, :operation, :num, :res_balance)"""
    values_dict = {"date": date,
                   "time": time,
                   "atm_id": args[0],
                   "user": args[1],
                   "operation": args[2],
                   "num": args[3],
                   "res_balance": args[4]}
    cur.execute(request, values_dict)
    con.commit()
    con.close()
    return True
