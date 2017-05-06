from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button
from django.contrib.auth.models import User
from django.forms import Form, CharField, ModelForm, ChoiceField, PasswordInput
from . import models


class LoginForm(Form):
    username = CharField(label='Username', required=True, max_length=50)
    document = CharField(label='Document', required=True, max_length=20)
    password = CharField(label='Password', required=True, max_length=50, widget=PasswordInput)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.from_class = 'loginForm'
    helper.add_input(Button('loginBtn', 'Login', css_class='btn btn-primary btn-lg btn-bloc pull-right'))


class DoctorForm(ModelForm):
    document = CharField(label='Document', max_length=20)
    cellphone = CharField(label='Cellphone', max_length=10)
    office_phone = CharField(label='Office Phone', max_length=10)
    user_type = ChoiceField(label='User Type', choices=models.USER_TYPES)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.from_class = 'doctorForm'
    helper.add_input(Button('saveBtn', 'Save', css_class='btn btn-primary btn-lg btn-bloc pull-right'))

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class PatientForm(ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.from_class = 'patientForm'
    helper.add_input(Button('saveBtn', 'Save', css_class='btn btn-primary btn-lg btn-bloc pull-right'))

    class Meta:
        model = models.Patient
        fields = '__all__'  # ['first_name', 'last_name', 'email', 'address', 'cellphone', 'office_phone']


class AppointmentForm(ModelForm):
    patient = ChoiceField(choices=[
        (pat.id, pat.first_name + ' ' + pat.last_name) for pat in models.Patient.objects.all()
        ])
    doctor = ChoiceField(choices=[
        (doc.id, doc.user.first_name + ' ' + doc.user.last_name) for doc in models.Doctor.objects.all()
    ])

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.from_class = 'appointmentForm'
    helper.add_input(Button('saveBtn', 'Save', css_class='btn btn-primary btn-lg btn-bloc pull-right'))

    class Meta:
        model = models.Appointment
        fields = '__all__'


class PrescriptionForm(ModelForm):
    appointment = ChoiceField(
        choices=[(appt.id, str(appt.date) + ' (' + appt.patient.first_name + ' ' + appt.patient.last_name + ')')
                 for appt in models.Appointment.objects.all()])

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.from_class = 'prescriptionForm'
    helper.add_input(Button('saveBtn', 'Save',
                            css_class='btn btn-lg btn-primary btn-bloc pull-right'))

    class Meta:
        model = models.Prescription
        fields = '__all__'


class OphthalmologyForm(ModelForm):
    patient = ChoiceField(choices=[
        (pat.id, pat.first_name + ' ' + pat.last_name) for pat in models.Patient.objects.all()
        ])
    doctor = ChoiceField(choices=[
        (doc.id, doc.user.first_name + ' ' + doc.user.last_name) for doc in models.Doctor.objects.all()
    ])

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.from_class = 'ophthalmologyForm'
    helper.add_input(Button('saveBtn', 'Save',
                            css_class='btn btn-lg btn-primary btn-bloc pull-right'))

    class Meta:
        model = models.OphthalmologyFormModel
        fields = '__all__'
