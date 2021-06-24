import logging
from django.shortcuts import render, redirect , HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from hospital.models import Doctor
from hospital.forms import DoctorForm
from core.forms import CommonSignupForm
logger = logging.getLogger(__name__)


class RegistrationPages(TemplateView):
    template_name = 'hospital/registation.html'


class DoctorRegistration(CreateView):
    form_class = DoctorForm
    model = Doctor
    signup_form = CommonSignupForm
    template_name = 'hospital/doctor_registation.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            DoctorRegistration, self
        ).get_context_data(*args, **kwargs)
        context["signup"] = self.signup_form
        return context

    def form_valid(self, form):
        signup_form = self.signup_form(
            self.request.POST
        )
        if signup_form.is_valid():
            save_user = signup_form.save()
            print("save_user------", save_user)
            save_doctor = form.save(commit=False)
            save_doctor.user = save_user
            save_doctor.save()
            print("save_doctor------", save_doctor)
        else:
            print("signup_form-----", signup_form.errors)
            print("form-----", form.errors)
            return redirect(self.error_url())

        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Account successfully created")
        logger.debug(self.request, "Account successfully created")
        return reverse_lazy("index")

    def error_url(self):
        messages.warning(self.request, "Account successfully created")
        logger.debug(self.request, "Request Error")
        return reverse_lazy("index")



