from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import LoveUser


class LoverUserCreationForm(UserCreationForm):
    class Meta:
        model = LoveUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(LoverUserCreationForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        if commit:
            user.save()
        return user


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = LoveUser
        fields = UserChangeForm.Meta.fields