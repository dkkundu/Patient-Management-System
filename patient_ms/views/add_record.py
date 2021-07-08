import logging

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.contrib import messages
from patient_ms.models import (
    DoctorPrescription,
    Patient
)
from patient_ms.forms import (
    DoctorPrescriptionForm,
    record_file_formset
)

logger = logging.getLogger(__name__)


class DoctorPrescriptionView(
    UserPassesTestMixin,
    LoginRequiredMixin,
    View
):
    model = DoctorPrescription
    form_class = DoctorPrescriptionForm
    file_form = record_file_formset
    template_name = 'dashboard/record/add_record.html'

    def test_func(self):
        """Tests if the user is active"""
        return self.request.user.is_active  # any active user

    def get(self, request, pk):
        patient_object = Patient.objects.get(
            pk=pk
        )
        print("----", patient_object)
        context = {
            'form': self.form_class,
            'file': self.file_form,
            'patient_object': patient_object
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = self.form_class(request.POST)
        file_form = self.file_form(request.POST, request.FILES)

        try:
            patient_object = Patient.objects.get(
                pk=pk
            )
            if patient_object and form.is_valid():
                save_object = form.save(commit=False)
                save_object.doctor = self.request.user
                save_object.patient = patient_object
                save_object.save()
                print("Text saved")
                for file_form_object in file_form:
                    if file_form_object.is_valid():
                        file = file_form_object.save(commit=False)
                        file.record = save_object
                        file.save()
                        print("Text Document")
        except Exception as e:
            messages.warning(request, "Unable to save record")
            logging.debug(request, f"Unable to save record {e}")
        context = {
            'form': self.form_class,
            'file': self.file_form
        }
        return render(request, self.template_name, context)

    def get_success_url(self):
        messages.success(self.request, "Successfully Updated")
        logger.debug("Successfully Updated")
        return reverse_lazy("index")

    def get_error_url(self):
        messages.warning(self.request, "Unable to get Appointment")
        logger.debug("Unable to get Appointment")
        return reverse_lazy("dashboard")