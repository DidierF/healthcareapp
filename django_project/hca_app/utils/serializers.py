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
        fields = ('user', 'doctorId', 'document', 'cellphone', 'officePhone', 'userType')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
