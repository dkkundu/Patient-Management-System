import datetime
from django.shortcuts import render, redirect
from patient_ms.models import DoctorAppointment
from django.contrib import messages
from .models import Slider, Service, Doctor, Faq, Gallery
from django.views.generic import ListView, DetailView, TemplateView, View
from hospital.models import Contact
from patient_ms.models import DoctorAppointment
import logging
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
logger = logging.getLogger(__name__)


class VisitedAppointmentList(ListView):
    model = DoctorAppointment
    template_name = 'dashboard/appointment/vistied.html'

    def get_queryset(self):
        today = datetime.date.today()
        qs = self.model.objects.filter(
            doctor__user=self.request.user,
            appointment_day=today, is_visited=True
        )
        return qs


class UnVisitedAppointmentList(ListView):
    model = DoctorAppointment
    template_name = 'dashboard/appointment/not_vistied.html'

    def get_queryset(self):
        today = datetime.date.today()
        qs = self.model.objects.filter(
            doctor__user=self.request.user,
            appointment_day=today, is_visited=False
        )
        return qs


class AllPatientList(ListView):
    model = DoctorAppointment
    template_name = 'dashboard/patient/list.html'

