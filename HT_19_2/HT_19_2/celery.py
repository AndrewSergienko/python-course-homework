import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HT_19_2.settings')

app = Celery('HT_19_2')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
