from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from doctors_appointment.models import Appointment

@login_required
def display_doctors(request):
    user = request.user
    appointments = Appointment.objects.filter() 
    return render(request, 'doctors_appointment/doctors.html', {})

@login_required
def add_doctors_appointment(request):
    return render(request, 'doctors_appointment/add.html', {})
