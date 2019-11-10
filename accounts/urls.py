from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    # path('login/', views.index, name='login'),
    # path('logout/', views.index, name='logout'),
]