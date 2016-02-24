from django.contrib.auth.models import User
from .models import Doctor
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class DoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    # email = serializers.CharField(max_length=50)
    # first_name = serializers.CharField(max_length=50)
    # last_name = serializers.CharField(max_length=50)

    class Meta:
        model = Doctor
        fields = ('doctorId', 'username', 'document', 'cellphone', 'officePhone', 'userType')
