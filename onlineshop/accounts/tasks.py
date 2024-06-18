from celery import shared_task
from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz


@shared_task
def delete_expire_otp_code():

    expire_time = datetime.now(tz=pytz.timezone("asia/tehran")) - timedelta(minutes=2)
    OtpCode.objects.filter(created__lt=expire_time).delete()
