# Generated by Django 3.2.3 on 2021-07-03 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('patient_ms', '0007_auto_20210703_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorappointment',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointment_district', to='address.district'),
        ),
        migrations.AlterField(
            model_name='doctorappointment',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointment_division', to='address.division'),
        ),
        migrations.AlterField(
            model_name='doctorappointment',
            name='upazila',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointment_upazila', to='address.upazila'),
        ),
    ]
