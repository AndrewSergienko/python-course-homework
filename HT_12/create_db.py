import sqlite3


def create():
    con = sqlite3.connect('quotes.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE authors (
                name text NOT NULL PRIMARY KEY,
                date_birth text NOT NULL,
                place_birth text NOT NULL
                )""")
    con.commit()
    cur.execute("""CREATE TABLE quotes (
                author text,
                quote text,
                FOREIGN KEY (author) REFERENCES authors(name)
                )""")
    con.commit()
    con.close()