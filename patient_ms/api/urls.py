from django.urls import path
from patient_ms.api.views import (
    DoctorAppointmentAPIView
)

app_name = 'patient_ms_api'
urlpatterns = [
    path(
        'doctor-appointment/',
        DoctorAppointmentAPIView.as_view(), name='doctor_appointment'
    ),
]
