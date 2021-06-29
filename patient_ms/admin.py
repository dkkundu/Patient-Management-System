from django.contrib import admin
from patient_ms.models import (
    Patient,
    DoctorAppointment
)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'age', 'nid', 'division', 'district',
        'upazila'
    ]


@admin.register(DoctorAppointment)
class DoctorAppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'patient', 'doctor', 'appointment_time', 'serial_number', 'is_visited',
    ]
