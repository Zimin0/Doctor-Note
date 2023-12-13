from django.db import models
from django.contrib.auth.models import User

class BaseEntityModel(models.Model):
    """ Базовая модель. От нее наследуются Appointment, Medicine. """
    patient = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, default=None)
    is_ended = models.BooleanField(verbose_name='Истек ли срок?', default=False)
    archived = models.BooleanField(verbose_name='Архивировано?', default=False)
