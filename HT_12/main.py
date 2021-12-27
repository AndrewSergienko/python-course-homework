import csv

from bs4 import BeautifulSoup
import requests
import sqlite3
import csv_create


def parse_quotes(url=None):
    default_url = "http://quotes.toscrape.com/"
    if url is None:
        url = default_url
    else:
        url = default_url + url
    document = requests.get(url)
    soup = BeautifulSoup(document.text, 'html.parser')
    quotes = soup.select(".quote")
    for quote_div in quotes:
        quote = quote_div.select_one(".text").string
        author = quote_div.select_one(".author").string
        author_info = parse_author_info(default_url + quote_div.select_one("span a").get('href'))
        author_info['name'] = author
        write_db({'author': author, 'quote': quote}, author_info)
        write_csv({'author': author, 'quote': quote}, author_info)
    next_url = soup.select_one(".pager .next a")
    if next_url is not None:
        parse_quotes(next_url.get('href'))


def parse_author_info(url: str):
    document = requests.get(url)
    soup = BeautifulSoup(document.text, 'html.parser')
    author_info = soup.select_one(".container .author-details")
    author_born_date = author_info.select_one('.author-born-date').string
    author_born_place = author_info.select_one('.author-born-location').string
    return {'date': author_born_date, 'place': author_born_place}


def write_db(quote: dict, author: dict):
    con = sqlite3.connect('quotes.db')
    cur = con.cursor()
    request = "INSERT INTO quotes VALUES (:author, :quote)"
    if get_author_db(cur, quote['author']) is None:
        write_author_db(cur, author)
    cur.execute(request, quote)
    con.commit()
    con.close()


def write_author_db(cur: sqlite3.Cursor, data: dict):
    request = "INSERT INTO authors VALUES (:name, :date, :place)"
    cur.execute(request, data)


def get_author_db(cur: sqlite3.Cursor, author: str):
    request = "SELECT * FROM authors WHERE name=:name"
    author = cur.execute(request, {'name': author}).fetchone()
    return author


def get_author_csv(author):
    with open('authors.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if author in row:
                return author


def write_csv(quote: dict, author: dict):
    with open('quotes.csv', 'a', encoding='utf-8') as cf:
        writer = csv.writer(cf, delimiter=';')
        writer.writerow([quote['author'], quote['quote']])
    if get_author_csv(author) is None:
        with open('authors.csv', 'a', encoding='utf-8') as cf:
            writer = csv.writer(cf, delimiter=';')
            writer.writerow([author['name'], author['date'], author['place']])


parse_quotes()
