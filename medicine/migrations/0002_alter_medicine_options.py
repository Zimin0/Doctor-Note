# Generated by Django 4.2.3 on 2023-12-11 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'Лекарство', 'verbose_name_plural': 'Лекарства'},
        ),
    ]
