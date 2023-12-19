
from celery import shared_task
n = 0

@shared_task
def check():
    global n
    n += 1
    return n

