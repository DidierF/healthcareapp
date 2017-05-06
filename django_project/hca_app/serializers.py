from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = ('id', 'document', 'cellphone', 'office_phone', 'user_type')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient


class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomField


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prescription
