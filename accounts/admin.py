from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import LoveUser
from .forms import LoverUserCreationForm, AccountChangeForm


class LoveUserAdmin(UserAdmin):
    model = LoveUser
    add_form = LoverUserCreationForm
    form = AccountChangeForm


admin.site.register(LoveUser, LoveUserAdmin)