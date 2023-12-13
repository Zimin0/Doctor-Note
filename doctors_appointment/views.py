from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from doctors_appointment.models import Appointment
from doctors_appointment.forms import AppointmentForm

from welcome.decorators import page_in_progress

@login_required
def display_doctors(request):
    """ Главная страница с записями к врачу. """
    context = {}
    # appointments = Appointment.active_appointments_sorted.filter(patient=request.user) 
    appointments = request.user.appointments.all()

    for appt in appointments: # смотрим, какие записи уже истекли
        if not appt.is_ended:
            if appt.is_appointment_over():
                appt.is_ended = True
                appt.save()
    context['appointments'] = appointments
    return render(request, 'doctors_appointment/doctors.html', context)

@login_required
def add_doctors_appointment(request):
    """ Добавление записи к врачу. """
    if request.method == "POST":
        print(request.POST)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Создаем новую запись в базе данных
            new_appt = form.save(commit=False)
            new_appt.patient = request.user
            new_appt.save()
            return redirect('doctors:display_doctors')
        else:
            print("Форма невалидна!")
            print(form.errors)
            return render(request, 'doctors_appointment/addDoctor.html', {'form': form, 'errors': form.errors})
    else:
        form = AppointmentForm()
        return render(request, 'doctors_appointment/addDoctor.html', {'form':form})

@login_required
def edit_appointment(request, appt_id):
    """ Изменение записи ко врачу """
    appointment = get_object_or_404(Appointment, id=appt_id)
    print(f"Сейчас в объявлении {appointment.date}")
    print(f"Сейчас в объявлении {appointment.time}")
    if request.method == 'POST':
        print(request.POST)
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            print("Форма сохранена!")
            return redirect('doctors:display_doctors')
        else:
            print("Форма невалидна!")
            print(form.errors)

    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'doctors_appointment/editDoctor.html', {'form': form})

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

@login_required
@require_POST
def delete_appointment(request, appt_id):
    obj = get_object_or_404(Appointment, id=appt_id)
    obj.delete()
    return JsonResponse({'status':'success'})