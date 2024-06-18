from bucket import buckets
from celery import shared_task

def all_bucket_object_task():
    result = buckets.get_object()
    return result


@shared_task
def delete_object_task(key):
    buckets.delete_object(key)


@shared_task
def download_object_bucket_task(key):
    buckets.download_object_bucket(key)