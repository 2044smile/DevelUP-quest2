from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('create/', views.AnniversaryCreate.as_view(), name='create'),
]