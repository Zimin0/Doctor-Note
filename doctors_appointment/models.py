from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.CharField(verbose_name="Врач", max_length=20, blank=False)
    date = models.DateField(verbose_name="Дата", max_length=10, help_text="Формат: XX.XX.XXXX", blank=False)
    time = models.TimeField(verbose_name="Время", max_length=5, help_text="Формат: XX:XX", blank=False)
    address = models.CharField(verbose_name="Адрес", max_length=100, blank=False)
    office_number = models.CharField(verbose_name="Кабинет", max_length=6, blank=False)
    health_troubles = models.TextField(verbose_name="Жалобы", blank=True, null=True)
    archived = models.BooleanField(verbose_name="Архивировано?", default=False)
    report = models.TextField(verbose_name="Отчет после приема", blank=True, null=True)
    is_ended = models.BooleanField(verbose_name="Закончился ли прием?", default=False)
    
    def convert_date(self, date_str:str) -> dict:
        """ Converts data from "21.03.1980" to datetime.date object """
        result = {'date':None, 'status':'OK'}
        try:    
            day, month, year = list(map(int, date_str.split('.'))) 
            result['date'] = datetime.date(year, month, day)
        except:
            result['status'] = 'ERROR: invalid format of data.'
        return result  
    
    def convert_time(self, time_str:str) -> dict:
        """ Converts time from "12:45" to datetime.time object """
        result = {'time':None, 'status':'OK'}
        try:    
            hour, minutes = list(map(int, time_str.split(':'))) 
            result['time'] = datetime.time(hour, minutes, 00)
        except:
            result['status'] = 'ERROR: invalid format of time.'
        return result  
    
    def is_appointment_over(self) -> bool:
        """ Проверяет, прошла ли встреча у доктора исходя из назначенного времени."""
        current_timezone = timezone.get_current_timezone()
        current_datetime = timezone.now()
        appointment_datetime = datetime.datetime.combine(self.date, self.time)
        appointment_datetime = appointment_datetime.replace(tzinfo=current_timezone)
        return appointment_datetime < current_datetime