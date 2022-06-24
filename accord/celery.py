import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accord.settings')

app = Celery('accord') 
app.config_from_object('django.config:settings', namespace='CELERY')
app.autodiscover_tasks()