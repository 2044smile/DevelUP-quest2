from django.shortcuts import render
from .forms import UserForm
from django.views.generic import CreateView


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'accounts/signup.html'
    success_url = "/"