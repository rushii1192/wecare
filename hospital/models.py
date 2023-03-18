from django.db import models

# Create your models here.
class DoctorModel(models.Model):
    email=models.CharField(max_length=200)
    name=models.CharField(max_length=50)
    created_on=models.DateTimeField(auto_now=True)
    updated_on=models.DateTimeField(auto_now=True)
    roomNumber=models.IntegerField(default=0)
    status = models.CharField(max_length=30, default="Free")
    occupiedBy = models.CharField(max_length=100, default=None)


