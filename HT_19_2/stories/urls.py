from django.urls import path

from . import views


app_name = 'stories'
urlpatterns = [
    path('', views.stories_index, name='stories_index'),
    path('save/<str:type>', views.stories_save, name='stories_write')
]