from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser


class AccountManager(UserManager):
    pass


class LoveUser(AbstractUser):
    objects = AccountManager()


# TODO main 에서 작성한 LoveUser Model을 accounts 앱으로 옮겼고, error 발생 해결 필요