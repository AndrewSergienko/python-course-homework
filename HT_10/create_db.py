import sqlite3


con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute("""CREATE TABLE users (
            login text NOT NULL PRIMARY KEY,
            password text NOT NULL,
            type text NOT NULL
            )""")

con.commit()

cur.execute("""CREATE TABLE balances (
            user text,
            balance integer,
            FOREIGN KEY (user) REFERENCES users(login)
            )""")

con.commit()

cur.execute("""CREATE TABLE transactions (
            id integer PRIMARY KEY,
            user text,
            operation text NOT NULL,
            number integer,
            result_balance integer,
            FOREIGN KEY (user) REFERENCES users(login)
            )""")

cur.execute("""CREATE TABLE banknotes (
            denomination integer PRIMARY KEY,
            value integer 
            )""")


con.commit()
con.close()