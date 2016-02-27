from django.contrib.auth.models import User
from . import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class DoctorSerializer(serializers.ModelSerializer):
    # TODO: fix remaining fields
    username = serializers.CharField(max_length=50)
    # email = serializers.CharField(max_length=50)
    # first_name = serializers.CharField(max_length=50)
    # last_name = serializers.CharField(max_length=50)

    class Meta:
        model = models.Doctor
        fields = ('doctorId', 'username', 'document', 'cellphone', 'officePhone', 'userType')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
