from HT_19_2.celery import app

from . import stories_handler
from . import stories_api


@app.task
def save_story(type, story_id):
    story = stories_api.get_item_dict(story_id)
    story_obj = stories_handler.create_stories_object(type, story)
    if story_obj is not None:
        story_obj.save()


