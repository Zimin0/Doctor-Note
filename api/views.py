from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions
from rest_framework.authtoken.models import Token


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from doctors_appointment.models import Appointment
from medicine.models import Medicine
from api.serializers.doctors import AppointmentSerializer
from api.serializers.medicine import MedicineSerializer
from api.serializers.users import UserSerializer, GroupSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    http_method_names = ['get', 'post', 'head']


class UserViewSet(viewsets.ModelViewSet):
    """ Вывод всех пользователей. """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(APIView):
    """ Вход пользователя. """
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

@method_decorator(csrf_exempt, name='dispatch')
class UserRegistrationView(generics.CreateAPIView):
    """ Регистрация пользователя. """
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

""" 
Вместо того, чтобы писать несколько представлений, мы объединяем все общее поведение в классы под названием ViewSets.
При необходимости мы можем легко разбить их на отдельные представления, но использование наборов представлений позволяет сохранить логику представления хорошо организованной, а также очень лаконичной.
"""

"""
Почему мы переопределяем маршрут login, а не используем базовый из path('api-auth/', include('rest_framework.urls'))????
Потому что он по дефолту требует csrf токена, который не нужен в аутентификации на основе кастомоного токена rest_framework!
Мы пишем свое представление и выключаем csrf защиту: @csrf_exempt ... class UserLoginView(APIView):
"""