from django.db import models
from django.utils import timezone
import datetime

class ActiveMedicineManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_ended=False).order_by('-end_date')

class Medicine(models.Model):
    class Meta:
        verbose_name = "Лекарство"
        verbose_name_plural = "Лекарства"

    name = models.CharField(verbose_name='Название', max_length=15)
    end_date = models.DateField(verbose_name='Последний день приема')
    amount_per_day = models.CharField(verbose_name='Кол-во раз в день', max_length=40, help_text='Может содержать как число, так и описание: 2 таблетки в 3 дня' )
    dosage = models.CharField(verbose_name='Дозировка за один прием', max_length=30, help_text='Например: 3 капсулы')
    comments = models.TextField(verbose_name='Комментарии')
    is_ended = models.BooleanField(verbose_name='Прием лекарства закончился?', default=False)

    objects = models.Manager()
    active_medicine_sorted = ActiveMedicineManager()

    def __str__(self) -> str:
        return f'{self.name}: до {self.end_date}'

    def save(self, *args, **kwargs):
        self.is_ended = self.is_medicine_over()
        super(Medicine, self).save(*args, **kwargs)

    def is_medicine_over(self) -> bool:
        """ Проверяет, закончился ли прием лекарства. """
        current_timezone = timezone.get_current_timezone()
        current_date = timezone.now()
        medicine_date = self.end_date
        medicine_datetime = datetime.datetime.combine(medicine_date, datetime.time(0, 0), tzinfo=current_timezone)
        return medicine_datetime < current_date
