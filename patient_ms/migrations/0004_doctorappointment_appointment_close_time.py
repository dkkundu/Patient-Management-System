# Generated by Django 3.2.3 on 2021-06-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_ms', '0003_doctorappointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorappointment',
            name='appointment_close_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Appointment Close Time'),
        ),
    ]