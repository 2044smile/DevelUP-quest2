from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import LoveUser


class LoverUserCreationForm(UserCreationForm):
    class Meta:
        model = LoveUser
        fields = '__all__'


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = LoveUser
        fields = UserChangeForm.Meta.fields


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']