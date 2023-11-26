from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from doctors_appointment.models import Appointment

@login_required
def display_doctors(request):
    """ Главная страница с записями к врачу. """
    context = {}
    appointments = Appointment.objects.filter(patient=request.user, archived=False) 
    context['appointments'] = appointments
    return render(request, 'doctors_appointment/doctors.html', context)

@login_required
def add_doctors_appointment(request):
    """ Добавление записи к врачу. """
    if request.method == "POST":
        ...
    return render(request, 'doctors_appointment/add.html', {})

@login_required
def detail_appointment(request, appt_id):
    """ Детальная информация о записи у врача. """
    context = {}
    appointment = get_object_or_404(Appointment, id=appt_id)
    context['appointment'] = appointment
    return render(request, 'doctors_appointment/detail.html', context)

@login_required
def edit_appointment(request, appt_id):
    """ Изменение записи ко врачу """
    context = {}
    if request.method == 'GET':
        # заполняем форму добавления данными из базы данных
        appointment =  get_object_or_404(Appointment, id=appt_id)
        context['appointment'] = appointment
        return render(request, 'doctors_appointment/edit.html', context)
    if request.method == "POST":
        ...

@login_required
def add_report(request, appt_id):
    """ Добавление отчета после посещения врача """
    context = {}
    appointment = get_object_or_404(Appointment, id=appt_id) 
    if request.method == 'GET':
        context['doctor_and_datatime'] = f'{appointment.doctor} - {appointment.date} в {appointment.time}'
        return render(request, 'doctors_appointment/report.html', context)
    if request.method == 'POST':
        report = request.POST.get('report', None)
        appointment.report = report
        appointment.save()
        return redirect('doctors:display_doctors')