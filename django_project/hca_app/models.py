from django.db import models


class Doctor(models.Model):
    doctorId = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

