from django import forms
from patient_ms.models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = [
            "name",
            "age",
            "nid",
        ]

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = True
        self.fields["age"].required = True
        self.fields["nid"].required = True
