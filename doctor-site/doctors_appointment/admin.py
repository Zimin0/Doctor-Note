from django.contrib import admin
from doctors_appointment.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'office_number', 'is_ended', 'archived', 'health_troubles')
    list_filter = ('patient', 'doctor', 'date', 'time', 'archived')
    search_fields = ('patient', 'doctor', 'date', 'time')

admin.site.register(Appointment, AppointmentAdmin)
