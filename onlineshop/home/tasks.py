from bucket import buckets


def all_bucket_object_task():
    result = buckets.get_object()
    return result