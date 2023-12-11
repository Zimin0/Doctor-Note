# Generated by Django 4.2.3 on 2023-12-11 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_rename_name_medicine_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='today',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Принято сегодня'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='amount_per_day',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Кол-во раз в день'),
        ),
    ]
