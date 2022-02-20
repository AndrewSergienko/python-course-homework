from django.shortcuts import render, redirect, reverse

from . import tasks
from . import stories_handler
from . import stories_api
from celery import group


def stories_index(request):
    context = {'saved_status': None}
    if 'saved_status' in request.GET:
        context['saved_status'] = request.GET['saved_status']
    return render(request, 'stories/index.html', context=context)


def stories_save(request, type):
    base_url = reverse('stories:stories_index')
    stories = stories_api.get_item_ids(type, stories_handler.get_stories_id(type))
    save_list = []
    if stories is not None:
        for story_id in stories:
            save_list.append(tasks.save_story.s(type, story_id))
        result_group = group(save_list)
        result_group.apply_async()
        return redirect(f'{base_url}?saved_status=success')
    return redirect(f'{base_url}?saved_status=error')





