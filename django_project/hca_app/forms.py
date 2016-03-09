from django.contrib.auth.models import User
# from django.forms import Form, CharField, ModelForm, ChoiceField
from django import forms
from django.forms import Form, CharField, ModelForm, ChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . import models


class LoginForm(Form):
    username = CharField(label='Username', required=True, max_length=50)
    document = CharField(label='Document', required=True, max_length=20)
    password = CharField(label='Password', required=True, max_length=50, widget=forms.PasswordInput)

    helper = FormHelper()
    helper.form_methold = 'POST'
    helper.from_class = 'loginForm'
    helper.add_input(Submit('loginBtn', 'Login', css_class='btn btn-primary btn btn-lg btn-primary btn-bloc'))

class DoctorForm(ModelForm):
    document = CharField(label='Document', max_length=20)
    cellphone = CharField(label='Cellphone', max_length=10)
    office_phone = CharField(label='Office Phone', max_length=10)
    user_type = ChoiceField(label='User Type', choices=models.USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class PatientForm(ModelForm):
    class Meta:
        model = models.Patient
        fields = ['first_name', 'last_name', 'email', 'address', 'cellphone', 'office_phone']


class AppointmentForm(ModelForm):
    patient = ChoiceField(choices=[
        (pat.id, pat.first_name + ' ' + pat.last_name) for pat in models.Patient.objects.all()
        ])
    doctor = ChoiceField(choices=[
        (doc.id, doc.user.first_name + ' ' + doc.user.last_name) for doc in models.Doctor.objects.all()
    ])

    class Meta:
        model = models.Appointment
        fields = '__all__'


class PrescriptionForm(ModelForm):
    class Meta:
        model = models.Prescription
        fields = '__all__'

