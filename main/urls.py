from django.urls import path, include
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.AnniversaryList.as_view(), name='list'),
    path('create/', views.AnniversaryCreate.as_view(), name='create'),
]