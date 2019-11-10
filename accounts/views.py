from django.shortcuts import render
from .forms import LoverUserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    form_class = LoverUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('/')