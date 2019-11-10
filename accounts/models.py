from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser


class AccountManager(UserManager):
    pass


class LoveUser(AbstractUser):
    objects = AccountManager()
    password2 = models.CharField(max_length=128, null=False)