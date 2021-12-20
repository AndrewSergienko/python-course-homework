import time
import requests
import re
from datetime import datetime
from datetime import timedelta


def request_json(url, params=None):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return


def get_current_exchange_rate():
    body = request_json("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    if body:
        return [f"{currency['ccy']} - купівля: {currency['buy']}, продаж: {currency['sale']}" for currency in body]
    else:
        return "Помилка звязку з сервером. Не вдалося завантажити дані."


def get_archive_exchange_rate(currency, date: str):
    currs = ['UAH', 'RUR', 'EUR', 'USD', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK',
             'DKK', 'GBP', 'GEL', 'HUF', 'ILS', 'JPY', 'KZT', 'MDL', 'NOK',
             'PLN', 'SEK', 'UZS', 'SGD', 'TMT', 'TRY']
    valid_date = re.search(r'(\d{2}\.){2}\d{4}', date).group(0)
    if valid_date is not None and currency in currs:
        valid_date_parts = list(map(int, valid_date.split('.')))
        target_date = datetime(valid_date_parts[2], valid_date_parts[1], valid_date_parts[0])
        prev_rate = None
        while target_date <= datetime.now():
            result, prev_rate = get_exchange_rate_by_day(currency, target_date, prev_rate)
            yield result
            target_date = get_next_date(target_date)
            time.sleep(1)
    else:
        return ['Невірно введена дата. Спробуйте ввести іншу']


def get_exchange_rate_by_day(currency, date: datetime, prev_rate):
    params = {"json": "", "date": f"{date.day}.{date.month}.{date.year}"}
    body = request_json("https://api.privatbank.ua/p24api/exchange_rates", params=params)
    for currency_response in body["exchangeRate"]:
        try:
            if currency_response['currency'] == currency:
                rate = currency_response['saleRateNB']
                return f"Дата: {body['date']}     НБУ: {rate}" \
                       f"    {'-----' if prev_rate is None else '{:.3f}'.format(rate - prev_rate)}", rate
        except KeyError:
            pass


def get_next_date(date: datetime):
    try:
        new_date = datetime(date.year, date.month, date.day + 1)
    except ValueError:
        day = 1
        if date.month == 12:
            month = 1
            year = date.year + 1
        else:
            month = date.month + 1
            year = date.year
        new_date = datetime(year, month, day)
    return new_date


def convert_currency(curr1, curr2, value: int):
    currs = ['UAH', 'RUR', 'EUR', 'USD', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK',
             'DKK', 'GBP', 'GEL', 'HUF', 'ILS', 'JPY', 'KZT', 'MDL', 'NOK',
             'PLN', 'SEK', 'UZS', 'SGD', 'TMT', 'TRY']
    if curr1 in currs and curr2 in currs and value >= 0:
        date = datetime.now()
        params = {'json': "", 'date': f"{date.day}.{date.month}.{date.year}"}
        body = request_json("https://api.privatbank.ua/p24api/exchange_rates", params)
        if not body["exchangeRate"]:
            date = datetime.now() - timedelta(1)
            params = {'json': "", 'date': f"{date.day}.{date.month}.{date.year}"}
            body = request_json("https://api.privatbank.ua/p24api/exchange_rates", params)
        currs_rate = {curr['currency']: curr["purchaseRateNB"] for curr in body["exchangeRate"][1:]}
        if curr1 == curr2:
            return value
        elif curr1 == "UAH":
            return value / float(currs_rate[curr2])
        elif curr2 == "UAH":
            return value * float(currs_rate[curr1])
        else:
            uah = value * float(currs_rate[curr1])
            return uah / float(currs_rate[curr2])
    return "Неправильні данні або помилка відповіді від серверу. Спробуйте ввести інші дані або српобуйте пізніше"
