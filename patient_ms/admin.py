from django.contrib import admin
from patient_ms.models import (
    Patient
)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'age', 'nid', 'division', 'district',
        'upazila'
    ]
