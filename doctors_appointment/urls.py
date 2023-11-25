from django.contrib import admin
from django.urls import path
from doctors_appointment.views import display_doctors

urlpatterns = [
    path('doctors/', display_doctors),
]
