from django import forms
from doctors_appointment.models import Appointment
from django.forms.widgets import DateInput

class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        # widget=DateInput(attrs={'type': 'date', 'format': '%d/%m/%Y'}),
        input_formats=['%d/%m/%Y', '%d.%m.%Y', '%d-%m-%Y', '%Y-%m-%d']
    )
    time = forms.TimeField(input_formats=['%H:%M'])

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'address', 'office_number', 'health_troubles', 'report', 'archived', 'is_ended']
