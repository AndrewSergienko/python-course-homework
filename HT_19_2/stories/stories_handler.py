from datetime import datetime

from .models import Ask, New, Job, Show


def get_stories_class(type):
    types = {
        'ask': Ask,
        'new': New,
        'job': Job,
        'show': Show
    }
    if type in types.keys():
        return types[type]


def get_stories_id(type):
    stories_class = get_stories_class(type)
    if stories_class is not None:
        return set([story.id for story in stories_class.objects.all()])
    return set()


def create_stories_object(type, item):
    stories_class = get_stories_class(type)
    if stories_class is not None:
        item = filling_attrs(item,
                             ['id', 'title', 'text',
                              'time', 'by', 'type'])
        story_blank = {
            'story_id': item['id'],
            'title': item['title'],
            'text': item['text'],
            'time': datetime.fromtimestamp(item['time']),
            'by': item['by'],
            'type': item['type']
        }
        if stories_class is Ask:
            item = filling_attrs(item,
                                 ['descendants', 'score'])
            story_obj = Ask(
                descendants=item['descendants'],
                score=item['score']
            )
        elif stories_class in [New, Show]:
            item = filling_attrs(item,
                                 ['descendants', 'score', 'url'])
            story_obj = stories_class(
                descendants=item['descendants'],
                score=item['score'],
                url=item['url']
            )
        elif stories_class is Job:
            item = filling_attrs(item,
                                 ['url', 'score'])
            story_obj = Job(
                url=item['url'],
                score=item['score']
            )
        story_obj.__dict__.update(story_blank)
        return story_obj


def filling_attrs(item, attrs):
    for attr in attrs:
        if attr not in item.keys():
            item[attr] = ''
    return item
