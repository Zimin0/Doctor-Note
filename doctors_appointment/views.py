from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from doctors_appointment.models import Appointment

@login_required
def display_doctors(request):
    context = {}
    appointments = Appointment.objects.filter(patient=request.user, archived=False) 
    context['appointments'] = appointments
    return render(request, 'doctors_appointment/doctors.html', context)

@login_required
def add_doctors_appointment(request):
    if request.method == "POST":
        ...
    return render(request, 'doctors_appointment/add.html', {})

@login_required
def detail_appointment(request, appt_id):
    context = {}
    appointment = get_object_or_404(Appointment, id=appt_id)
    context['appointment'] = appointment
    return render(request, 'doctors_appointment/detail.html', context)

@login_required
def edit_appointment(request, appt_id):
    context = {}
    if request.method == "GET":
        # заполняем форму добавления данными из базы данных
        appointment =  get_object_or_404(Appointment, id=appt_id)
        context['appointment'] = appointment
        return render(request, 'doctors_appointment/edit.html', context)
    if request.method == "POST":
        ...
