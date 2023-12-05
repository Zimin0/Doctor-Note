from django.urls import path
from welcome.views import welcome, page_in_progress

app_name = 'welcome'

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('in-progress/', page_in_progress, name='page_in_progress')
]
