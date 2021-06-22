from django import forms
from hospital.models import Doctor
from crispy_forms.helper import FormHelper


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        exclude = [
            "user",
            "expertize",
            "twitter",
            "facebook",
            "instagram"
        ]

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False



