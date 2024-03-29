from django.db import models
from hospital.models import DoctorModel
from django.contrib.auth.hashers import make_password
# Create your models here.

class PatientModel(models.Model):   
    email = models.CharField(max_length=100)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    password = models.CharField(max_length=70)
    bloodGroup = models.CharField(max_length=25)
    createDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super(PatientModel, self).save(*args, **kwargs)


class AppointmentModel(models.Model):
    # userId = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    userId = models.CharField(max_length=100)
    docterId = models.CharField(max_length=100)
    startTime = models.DateTimeField(auto_now=True)
    endTime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100)
    symtopms = models.CharField(max_length=200)
    # doctorId = models.ForeignKey(DoctorModel, on_delete=models.CASCADE, blank=True)


