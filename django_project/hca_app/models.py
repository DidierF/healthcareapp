from django.contrib.auth.models import User
from django.db import models

USER_TYPES = (
    ('lmtd', 'Limited'),
    ('std', 'Standard'),
    ('admin', 'Administrator')
)

APPOINTMENT_STATUS = (
    ('active', 'Active'),
    ('cancel', 'Cancelled'),
    ('priority', 'Priority'),
    ('results', 'Results')
)


# Users table
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    document = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=250, null=True)
    cellphone = models.CharField(max_length=10)
    office_phone = models.CharField(max_length=10)
    user_type = models.CharField(max_length=5, choices=USER_TYPES, default='std')


# Patients
class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    email = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=250, null=True)
    cellphone = models.CharField(max_length=10)
    office_phone = models.CharField(max_length=10, null=True)
    insurance = models.CharField(max_length=50, null=True)
    depends = models.IntegerField(null=True)
    referred = models.CharField(max_length=50, null=True)
    allergies = models.CharField(max_length=200, null=True)
    surgery = models.CharField(max_length=200, null=True)
    family_history = models.CharField(max_length=200, null=True)
    other = models.CharField(max_length=200, null=True)


# TODO: Change name to 'CustomPatientField'
class CustomField(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default='active')
    note = models.CharField(max_length=500, null=True)


class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    treatment = models.CharField(max_length=100)
    dosage = models.CharField(max_length=250)


class BasicConsultationFormModel(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    notes = models.CharField(max_length=1000, null=True)


class OphthalmologyFormModel(BasicConsultationFormModel):
    glasses_right = models.CharField(max_length=20, null=True)
    glasses_left = models.CharField(max_length=20, null=True)
    pupils_right = models.CharField(max_length=20, null=True)
    pupils_left = models.CharField(max_length=20, null=True)
    refraction_right = models.CharField(max_length=20, null=True)
    refraction_left = models.CharField(max_length=20, null=True)
