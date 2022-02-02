from django.contrib import admin

from .models import Ask, New, Job, Show


@admin.register(Ask)
class AskAdmin(admin.ModelAdmin):
    list_display = ['story_id', 'title', 'time', 'by']


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ['story_id', 'title', 'time', 'by']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['story_id', 'title', 'time', 'by']


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['story_id', 'title', 'time', 'by']