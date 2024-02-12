from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

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

    # def create(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # def delete(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    # def delete(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


""" 
Вместо того, чтобы писать несколько представлений, мы объединяем все общее поведение в классы под названием ViewSets.
При необходимости мы можем легко разбить их на отдельные представления, но использование наборов представлений позволяет сохранить логику представления хорошо организованной, а также очень лаконичной.
"""