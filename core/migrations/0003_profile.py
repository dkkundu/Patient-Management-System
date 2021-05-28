# Generated by Django 3.0.8 on 2020-07-06 07:18

import core.models.profile
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200702_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.profile.media_upload_path, verbose_name='Profile Picture')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('spouse_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of Spouse')),
                ('father_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of Father')),
                ('mother_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name of Mother')),
                ('nid', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator('^(\\d{10}|\\d{13}|\\d{17})$', message='Numeric 10/13/17 digits (ex: 1234567890)')], verbose_name='National ID')),
                ('passport', models.CharField(blank=True, max_length=9, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]{2}\\d{7}$', message='Alphanumeric 9 characters (ex: PA3456789)')], verbose_name='Passport')),
                ('is_active', models.BooleanField(default=True, null=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Updated')),
            ],
        ),
    ]
