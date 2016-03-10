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
    officePhone = CharField(label='Office Phone', max_length=10)
    userType = ChoiceField(label='User Type', choices=models.USER_TYPES)


    helper = FormHelper()
    helper.form_methold = 'POST'
    helper.from_class = 'registerForm'
    helper.add_input(Submit('registerBtn', 'Register', css_class='btn btn-primary btn btn-lg btn-primary btn-bloc'))

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class PatientForm(ModelForm):
    class Meta:
        model = models.Patient
        fields = ['firstName', 'lastName', 'document', 'email', 'address', 'cellphone', 'officePhone']


class AppointmentForm(ModelForm):
    patient = ChoiceField(choices=[
        (pat.patientId, pat.firstName + ' ' + pat.lastName) for pat in models.Patient.objects.all()
        ])
    doctor = ChoiceField(choices=[
        (doc.doctorId, doc.user.first_name + ' ' + doc.user.last_name) for doc in models.Doctor.objects.all()
    ])

    class Meta:
        model = models.Appointment
        fields = ['patient', 'doctor', 'date']
        # widgets = {
        #     'patient': Select()
        # }
