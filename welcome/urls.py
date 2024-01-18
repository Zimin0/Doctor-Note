from django.urls import path
from welcome.views import welcome, page_in_progress, redirect_page_with_reason, clear_session

app_name = 'welcome'

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('in-progress/', page_in_progress, name='page_in_progress'),
    path('redirect-to/to=<str:url_pattern_name>', redirect_page_with_reason, name='redirect_page_with_reason'),
    path('clear/session/cookies/', clear_session, name='clear_session')
]
