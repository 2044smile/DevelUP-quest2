from django.shortcuts import render, redirect
from .forms import LoverUserCreationForm, LoginForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login as dj_login, authenticate


class UserCreateView(CreateView): # 회원가입
    form_class = LoverUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


def login(request): # 로그인
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {
                'error': '로그인 실패'
            })
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {
            'form': form
        })
    return render(request, 'accounts/login.html')