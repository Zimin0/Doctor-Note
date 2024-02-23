from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from api import views
from api.views import UserLoginView, UserRegistrationView, UserChangePasswordView

router = DefaultRouter()
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'medicine', views.MedicineViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('change-password/', UserChangePasswordView.as_view(), name='change_password'),
    # path('api-auth/', include('rest_framework.urls')),
]

#print(router.urls) # - Все маршруты, сгенерированные роутером