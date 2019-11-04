from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser


class AccountManager(UserManager):
    pass


class LoveUser(AbstractUser):
    objects = AccountManager()