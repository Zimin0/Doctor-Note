from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='doctors/')),
    path('doctors/', include('doctors_appointment.urls')),
    path('users/', include('users.urls')),
]
    