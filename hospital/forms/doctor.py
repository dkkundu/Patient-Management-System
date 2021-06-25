from django import forms
from hospital.models import Doctor
from crispy_forms.helper import FormHelper
class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
            "name",
            "picture",
            'speciality'

        ]
        widgets = {
            'speciality': forms.Textarea(attrs={
                'id': 'speciality',
                'rows': 2
            }),

        }

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # # self.helper.form_show_labels = False
        self.fields["name"].required = True
        self.fields["picture"].required = True



