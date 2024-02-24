from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

handler404 = 'welcome.views.handler404'
handler500 = 'welcome.views.handler500'
handler403 = 'welcome.views.handler403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('i18n/', include('django.conf.urls.i18n')),  
    path('', RedirectView.as_view(url='doctors/')),
    path('', include('welcome.urls')),
    path('doctors/', include('doctors_appointment.urls')),
    path('users/', include('users.urls')),
    path('medicine/', include('medicine.urls')),
    path('__debug__/', include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)