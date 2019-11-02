from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import LoveUser


class LoverUserCreationForm(UserCreationForm):
    class Meta:
        model = LoveUser
        fields = '__all__'


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = LoveUser
        fields = UserChangeForm.Meta.fields