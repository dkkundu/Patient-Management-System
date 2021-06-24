from django import forms
from hospital.models import Doctor
from crispy_forms.helper import FormHelper


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
            "name",
            "picture",
            "experience",
            "speciality",
            "division",
            "district",
            "upazila",
            "post_code",
            "address"
        ]
        widgets = {
            'division': forms.Select(attrs={
                'id': 'division'
            }),
            'district': forms.Select(attrs={
                'id': 'district'
            }),
            'upazila': forms.Select(attrs={
                'id': 'upazila'
            }),
            'post_code': forms.NumberInput(attrs={
                'id': 'post_code',
                "oninput": "javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);",
                # noqa
                'maxLength': 4
            }),
            'address': forms.Textarea(attrs={
                'id': 'present_address',
                'rows': 2
            }),
            'experience': forms.Textarea(attrs={
                'id': 'experience',
                'rows': 2
            }),

        }

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False



