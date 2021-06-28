from django.urls import path
from patient_ms.views import PatientInfoUpdate

app_name = 'patient_ms'
urlpatterns = [
    path('<int:pk>/update/', PatientInfoUpdate.as_view(), name='patient_info_update'),
]
