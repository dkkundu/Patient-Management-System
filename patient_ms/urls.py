from django.urls import path
from patient_ms.views import (
    PatientInfoUpdate,
    DoctorAppointment,
    doctor_filter,
    DoctorPrescriptionView,
    ViewAllSavedRecord
)

app_name = 'patient_ms'
urlpatterns = [
    path(
        '<int:pk>/update/',
        PatientInfoUpdate.as_view(), name='patient_info_update'
    ),
    path(
        'calender/appointment/',
        DoctorAppointment.as_view(), name='appointment'
    ),
    path('appointment/filter/', doctor_filter, name='load_doctor'),
    path(
        'patient/<int:pk>/add/record/',
        DoctorPrescriptionView.as_view(), name='add_record'
    ),
    path(
        'patient/<int:pk>/record/view/',
        ViewAllSavedRecord.as_view(), name='view_record'
    ),

]
