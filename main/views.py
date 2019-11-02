from django.shortcuts import render
from django.views.generic import ListView


def index(request):
    return render(request, 'main/index.html')


def list(request):
    return render(request, 'main/anniversary_list.html')


def writing(request):
    return render(request, 'main/anniversary_update.html')