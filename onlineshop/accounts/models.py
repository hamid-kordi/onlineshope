from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, AbstractUser

# Create your models here.
from .managers import UserMnagers


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserMnagers()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email", "full_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number} - {self.code} - {self.created}"
