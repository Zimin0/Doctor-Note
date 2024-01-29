# Generated by Django 4.2.3 on 2024-01-03 23:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors_appointment', '0002_appointment_additional_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='additional_file',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'png', 'jpeg'])], verbose_name='Дополнительный файл'),
        ),
    ]
