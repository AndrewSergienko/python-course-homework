import requests


def get_item_ids(type, ids_in_db: set):
    if type not in ['ask', 'show', 'new', 'job']:
        return
    # Вертає тільки ті items, яких немає в базі
    item_ids = set(requests.get(f'https://hacker-news.firebaseio.com/v0/{type}stories.json').json())
    missing_ids = item_ids - ids_in_db
    return list(missing_ids)


def get_item_dict(item_id):
    item_info = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json').json()
    return item_info


def filling_attributes(item, unique_attrs):
    for attr in unique_attrs:
        if attr not in item:
            item[attr] = ''
