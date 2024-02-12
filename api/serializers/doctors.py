from doctors_appointment.models import Appointment

from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = Appointment
        fields = '__all__'
        