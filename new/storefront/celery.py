import os
from celery import Celery
from celery import shared_task

#setting enviroment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

celery = Celery('storefront')
#specifying where celery can find configurahion variables
celery.config_from_object('django.conf:settings', namespace = 'CELERY')
#.
celery.autodiscover_tasks()