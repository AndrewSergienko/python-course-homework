from django.db import models


class AStory(models.Model):
    story_id = models.IntegerField(default='-1')
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    time = models.TimeField(default='00:00:00')
    by = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, default='')

    class Meta:
        abstract = True


class Ask(AStory):
    descendants = models.IntegerField()
    score = models.IntegerField()


class Show(AStory):
    descendants = models.IntegerField()
    score = models.IntegerField()
    url = models.URLField()


class New(AStory):
    descendants = models.IntegerField()
    score = models.IntegerField()
    url = models.URLField()


class Job(AStory):
    url = models.URLField()
    score = models.IntegerField()


