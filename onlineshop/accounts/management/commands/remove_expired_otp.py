from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
    help = "remove all expire otp  codes"

    def handle(self, *args, **aptions):
        expire_time = datetime.now(tz=pytz.timezone("asia/tehran")) - timedelta(
            minutes=2
        )
        OtpCode.objects.filter(created__lt=expire_time).delete()
        self.stdout.write("all otp expir deleted")
