from django import forms
from doctors_appointment.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'address', 'office_number', 'health_troubles']
