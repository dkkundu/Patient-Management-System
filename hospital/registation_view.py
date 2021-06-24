import logging
from django.shortcuts import render, redirect , HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, View
from hospital.models import Doctor
from hospital.forms import DoctorForm
from core.forms import CommonSignupForm
logger = logging.getLogger(__name__)


class RegistrationPages(View):
    template_name = 'hospital/registation.html'

    def get(self, request, *args, **kwargs):
        context = {
            "form": DoctorForm,
            "signup": CommonSignupForm,
            "form_patient": DoctorForm,
            "signup_patient": CommonSignupForm,

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = DoctorForm(request.POST, request.FILES or None)
        signup_form = CommonSignupForm(request.POST or None)
        if form.is_valid() and signup_form.is_valid():
            try:
                save_user = signup_form.save()
                obj = form.save(commit=False)
                obj.user = save_user
                obj.save()
                messages.success(self.request, "Account successfully created")
                logger.debug(self.request, "Account successfully created")
            except Exception as e:
                logger.error(f"Unable to create account: {e}")
                messages.warning(self.request, "Unable to create account")
                logger.debug(self.request, "Unable to create account")
        else:
            print("signup_form-----", signup_form.errors)
            print("form-----", form.errors)
            messages.warning(self.request, "Invalid data")
            logger.debug(self.request, "Unable to create account")

        context = {
            "form": form,
            "signup": signup_form

        }
        return render(request, self.template_name, context)



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



