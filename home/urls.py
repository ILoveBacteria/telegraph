from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login/code/', views.login_code, name='login_code'),
    path('login/password/', views.login_password, name='login_password'),
]
