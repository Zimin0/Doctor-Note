from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='doctors/')),
    path('', include('welcome.urls')),
    path('doctors/', include('doctors_appointment.urls')),
    path('users/', include('users.urls')),
    path('medicine/', include('medicine.urls')),
    path('__debug__/', include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)