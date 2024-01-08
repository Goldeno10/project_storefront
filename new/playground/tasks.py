from celery import shared_task
from time import sleep
#from storefront.celery import celery


#@celery.task
@shared_task
def notify_customers(message):
    print('sending 10k emails...')
    print(message)
    sleep(10)
    print('Emails were succesfully sent!')