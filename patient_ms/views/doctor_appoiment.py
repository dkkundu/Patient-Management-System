import logging

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
)
from django.contrib import messages
from patient_ms.models import DoctorAppointment
from patient_ms.forms import DoctorAppointmentForm

logger = logging.getLogger(__name__)


class DoctorAppointment(
    UserPassesTestMixin,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    model = DoctorAppointment
    form_class = DoctorAppointmentForm
    template_name = 'appointment/index.html'
    permission_required = 'patient_ms.add_patient'

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get_success_url(self):
        messages.success(self.request, "Successfully Updated")
        logger.debug("Successfully Updated")
        return reverse_lazy("index")

