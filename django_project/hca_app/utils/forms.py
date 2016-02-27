from django.contrib.auth.models import User
from django.forms import Form, CharField, ModelForm, ChoiceField
from . import models


class LoginForm(Form):
    username = CharField(label='Username', max_length=50)
    document = CharField(label='Document', max_length=20)
    password = CharField(label='Password', max_length=50)


class DoctorForm(ModelForm):
    document = CharField(label='Document', max_length=20)
    cellphone = CharField(label='Cellphone', max_length=10)
    officePhone = CharField(label='Office Phone', max_length=10)
    userType = ChoiceField(label='User Type', choices=models.USER_TYPES)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class PatientForm(ModelForm):
    class Meta:
        model = models.Patient
        fields = ['firstName', 'lastName', 'document', 'email', 'address', 'cellphone', 'officePhone']
