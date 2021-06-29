from django import forms
from patient_ms.models import DoctorAppointment


class DoctorAppointmentForm(forms.ModelForm):
    class Meta:
        model = DoctorAppointment
        exclude = [
            'patient',
            "serial_number",
            "is_visited",
        ]

    def __init__(self, *args, **kwargs):
        super(DoctorAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].required = True
        self.fields['appointment_time'].required = True
        self.fields['appointment_close_time'].required = True
        self.fields['appointment_time'].widget.attrs['placeholder'] = 'Start Date (YY-MM-DD H:M)'
        self.fields['appointment_close_time'].widget.attrs['placeholder'] = 'Start Date (YY-MM-DD H:M)'


