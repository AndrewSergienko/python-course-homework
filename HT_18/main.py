import csv
import requests
from sys import argv

from Item import Item


def start():
    if len(argv) == 1:
        type = ''
    else:
        type = argv[1]
    if type == '':
        type = 'newstories'
    elif type not in ['askstories', 'showstories', 'newstories', 'jobstories']:
        print('Invalid type. Finish work.')
        return
    items, items_unique_field_names = get_items(type)
    write_csv(type, items, items_unique_field_names)


def get_items(type):
    items_id = requests.get(f'https://hacker-news.firebaseio.com/v0/{type}.json').json()
    items = []
    items_unique_field_names = set()
    for item_id in items_id:
        item = get_item_obj(item_id)
        items.append(item)
        for field_name in item.__dict__.keys():
            items_unique_field_names.add(field_name)
    print(items_unique_field_names)
    return items, items_unique_field_names


def get_item_obj(item_id):
    item_info = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json').json()
    return Item(item_info)


def write_csv(type, items, field_names):
    with open(f'{type}.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for item in items:
            writer.writerow(item.__dict__)


start()





