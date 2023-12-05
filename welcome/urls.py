from django.urls import path
from welcome.views import welcome

app_name = 'welcome'

urlpatterns = [
    path('', welcome, name='welcome'),
]
