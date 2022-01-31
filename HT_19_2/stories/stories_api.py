import requests


class Item:
    def __init__(self, args):
        self.__dict__.update(args)


def get_items(type, ids_in_db: set):
    if type not in ['ask', 'show', 'new', 'job']:
        return
    # Вертає тільки ті items, яких немає в базі
    item_ids = set(requests.get(f'https://hacker-news.firebaseio.com/v0/{type}stories.json').json())
    missing_ids = item_ids - ids_in_db
    items_unique_attrs = set()
    items = []
    for item_id in missing_ids:
        item = get_item_obj(item_id)
        items.append(item)
        for field_name in item.__dict__.keys():
            items_unique_attrs.add(field_name)
    for item in items:
        filling_attributes(item, items_unique_attrs)
    return items


def get_item_obj(item_id):
    item_info = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json').json()
    item_obj = Item(item_info)
    return item_obj


def filling_attributes(item, unique_attrs):
    for attr in unique_attrs:
        if attr not in item.__dict__:
            item.__dict__[attr] = ''
