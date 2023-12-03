from django import forms
from doctors_appointment.models import Appointment

class AppointmentForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'])
    time = forms.TimeField(input_formats=['%H:%M'])

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'address', 'office_number', 'health_troubles']
