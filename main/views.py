from django.shortcuts import render
from django.views.generic import ListView, CreateView
from main.models import AnniversaryPosts


def index(request):
    return render(request, 'main/index.html')


def list(request):
    return render(request, 'main/anniversary_list.html')


class AnniversaryCreate(CreateView):
    model = AnniversaryPosts
    fields = '__all__'
    template_name = 'main/anniversary_create.html'
    success_url = 'list'