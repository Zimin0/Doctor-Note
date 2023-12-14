from django.apps import AppConfig


class DoctorsAppointmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'doctors_appointment'
    verbose_name = 'Записи к врачу'
