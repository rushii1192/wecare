from django.db import models
import datetime

# Create your models here.
class DoctorModel(models.Model):
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now=True)
    updated_on=models.DateTimeField(auto_now=True)


