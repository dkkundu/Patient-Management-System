# PYTHON IMPORTS
import logging
# DJANGO IMPORTS
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from hospital.models import Doctor

# CORE IMPORTS

logger = logging.getLogger(__name__)


class DoctorAppointment(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    appointment_time = models.DateTimeField(
        _('Appointment Time'), null=True, blank=True
    )
    appointment_close_time = models.DateTimeField(
        _('Appointment Close Time'), null=True, blank=True
    )
    serial_number = models.PositiveIntegerField(
        _('Serial Number'), default=0
    )
    is_visited = models.BooleanField(
        _('Is Doctor Check'),default=False
    )

    def __str__(self):
        return f'{self.patient}- Dr:({self.doctor}), Time: {self.appointment_time}'


