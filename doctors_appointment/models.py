from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.CharField(verbose_name="Врач", max_length=30, blank=False)
    date = models.CharField(verbose_name="Дата", max_length=10, help_text="Формат: XX.XX.XXXX", blank=False)
    time = models.CharField(verbose_name="Время", max_length=5, help_text="Формат: XX.XX", blank=False)
    address = models.CharField(verbose_name="Адрес", max_length=100, blank=False)
    office_number = models.CharField(verbose_name="Кабинет", max_length=6, blank=False)
    health_troubles = models.TextField(verbose_name="Жалобы", blank=True)

