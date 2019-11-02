from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import LoverUserCreationForm, AccountChangeForm
from .models import *


class LoveUserAdmin(UserAdmin):
    model = LoveUser
    add_form = LoverUserCreationForm
    form = AccountChangeForm


admin.site.register(LoveUser, LoveUserAdmin)