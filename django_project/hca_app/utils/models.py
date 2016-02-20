from django.contrib.auth.models import User
from django.db import models

USER_TYPES = (
    ('lmtd', 'Limited'),
    ('std', 'Standard'),
    ('admin', 'Administrator')
)


# Users table
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctorId = models.AutoField(primary_key=True)
    document = models.CharField(max_length=20, unique=True)
    cellphone = models.CharField(max_length=10)
    officePhone = models.CharField(max_length=10)
    userType = models.CharField(max_length=5, choices=USER_TYPES, default='std')
