from django.shortcuts import render
from django.views.generic import View, TemplateView
from hospital.forms import DoctorForm
from core.forms import CommonSignupForm


class RegistrationPages(TemplateView):
    template_name = 'hospital/registation.html'


class DoctorRegistration(View):
    doctor_form = DoctorForm
    signup_form = CommonSignupForm
    template_name = 'hospital/doctor_registation.html'

    def get(self, request, *args, **kwargs):
        doctor_form = self.doctor_form
        signup_form = self.signup_form

        context = {
            "form": doctor_form,
            "signup": signup_form,

        }
        return render(request, self.template_name, context)
