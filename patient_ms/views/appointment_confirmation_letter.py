import logging
from django.views.generic import DetailView
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib import messages
from django.urls import reverse_lazy
from patient_ms.models import Patient
from patient_ms.forms import PatientUpdateForm
logger = logging.getLogger(__name__)


class AppointmentConfirmationLetterView(
    UserPassesTestMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView
):
    template_name = 'patient/update_patient.html'
    model = Patient
    permission_required = 'patient_ms.add_patient'

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get_success_url(self):
        messages.success(self.request, "Successfully Updated")
        logger.debug("Successfully Updated")
        return reverse_lazy("index")
