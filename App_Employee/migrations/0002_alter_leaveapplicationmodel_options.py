# Generated by Django 4.1.3 on 2023-02-13 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leaveapplicationmodel',
            options={'ordering': ['employee', 'apply_date', 'nature_of_leave', 'number_of_days']},
        ),
    ]