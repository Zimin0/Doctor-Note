from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from api import views

router = DefaultRouter()
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'medicine', views.)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
