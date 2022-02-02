from django.shortcuts import render, redirect, reverse

from . import stories_api
from .models import Ask, New, Job, Show

from datetime import datetime


def stories_index(request):
    context = {'saved_status': None}
    if 'saved_status' in request.GET:
        context['saved_status'] = request.GET['saved_status']
    return render(request, 'stories/index.html', context=context)


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
        story_blank = {
            'story_id': item.id,
            'title': item.title,
            'text': item.text,
            'time': datetime.fromtimestamp(item.time),
            'by': item.by,
            'type': item.type
        }
        if stories_class is Ask:
            story_obj = Ask(
                descendants=item.descendants,
                score=item.score
            )
        elif stories_class in [New, Show]:
            story_obj = stories_class(
                descendants=item.descendants,
                score=item.score,
                url=item.url
            )
        elif stories_class is Job:
            story_obj = Job(
                url=item.url,
                score=item.score
            )
        story_obj.__dict__.update(story_blank)
        return story_obj


def stories_save(request, type):
    stories = stories_api.get_items(type, get_stories_id(type))
    base_url = reverse('stories:stories_index')
    if stories is not None:
        for story in stories:
            story = create_stories_object(type, story)
            if story is not None:
                story.save()
        return redirect(f'{base_url}?saved_status=success')
    return redirect(f'{base_url}?saved_status=error')





