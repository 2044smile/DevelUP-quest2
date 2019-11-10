from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import LoveUser


class LoverUserCreationForm(UserCreationForm):
    class Meta:
        model = LoveUser
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': '</br>150 자 이하 문자, 숫자 및 @ /. / + /-/ _ 만 사용가능',
            'email': '</br>Ex) example@example.com',
            'password': 'password1',
            '_password': 'password1',
            'password1': 'password1',
            'password2': 'password1',
            'check_password': 'password2',
        }

    def save(self, commit=True):
        user = super(LoverUserCreationForm, self).save(commit=True) # 본인의 부모를 호출해서 저장하겠다.
        if commit:
            user.save()
        return user


class AccountChangeForm(UserChangeForm):
    class Meta:
        model = LoveUser
        fields = UserChangeForm.Meta.fields