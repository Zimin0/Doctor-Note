from django.contrib import admin
from django.urls import path
from doctors_appointment.views import display_doctors, add_doctors_appointment, detail_appointment, add_report

app_name = 'doctors'

urlpatterns = [
    path('', display_doctors, name='display_doctors'),
    path('add/', add_doctors_appointment, name='add_doctors_appointment'),
    path('appointment/<int:appt_id>/', detail_appointment, name='detail_appointment'),
    path('add-report/<int:appt_id>', add_report, name='add_report'),
]
