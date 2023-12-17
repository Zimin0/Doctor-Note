from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView 

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]