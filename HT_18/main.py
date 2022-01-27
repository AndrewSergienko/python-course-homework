import csv
import requests
from sys import argv

from Item import Item


def start():
    type = argv[1]
    print(type)
    if type == '':
        type = 'newstories'
    elif type not in ['askstories', 'showstories', 'newstories', 'jobstories']:
        print('Invalid type. Finish work.')
        return
    items = get_items(type)
    write_csv(type, items)


def get_items(type):
    items_id = requests.get(f'https://hacker-news.firebaseio.com/v0/{type}.json').json()
    items = []
    for item_id in items_id:
        items.append(get_item_obj(item_id))
    return items


def get_item_obj(item_id):
    item_info = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json').json()
    return Item(item_info)


def write_csv(type, items):
    with open(f'{type}.csv', 'w', encoding='utf-8') as file:
        field_names = ['id', 'deleted', 'type', 'by', 'time',
                         'text', 'dead', 'parent', 'poll', 'kids',
                         'url', 'score', 'title', 'parts', 'descendants']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for item in items:
            writer.writerow(item.__dict__)


start()





