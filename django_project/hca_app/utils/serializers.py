from .models import Doctor
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('user', 'doctorId', 'document', 'cellphone', 'officePhone', 'userType')
