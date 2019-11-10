from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import LoveUser


class LoverUserCreationForm(UserCreationForm):
    class Meta:
        model = LoveUser
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': '</br>150자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.',
            'email': '</br>Ex) example@example.com',
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


class LoginForm(forms.ModelForm):
    class Meta:
        model = LoveUser
        fields = ['username', 'password']
        labels = {
            'password': '비밀번호',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'username': '</br>150자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.'
        }