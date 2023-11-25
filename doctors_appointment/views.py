from django.shortcuts import render

def display_doctors(request):
    return render(request, 'doctors_appointment/doctors.html', {})

def add_doctors_appointment(request):
    return render(request, 'doctors_appointment/add.html', {})
