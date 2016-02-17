from django.db import models

USER_TYPES = (
    ('admin', 'Administrator'),
    ('std', 'Standard'),
    ('lmtd', 'Limited')
)


# Users table
class Doctor(models.Model):
    doctorId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    document = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    cellphone = models.CharField(max_length=10)
    officePhone = models.CharField(max_length=10)
    userType = models.CharField(max_length=5, choices=USER_TYPES, default='std')
