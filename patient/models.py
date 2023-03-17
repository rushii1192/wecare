from django.db import models

# Create your models here.

class PatientModel(models.Model):   
    email = models.CharField(max_length=100)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    password = models.CharField(max_length=70)
    createDate = models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)


class AppointmentModel(models.Model):
    userId = models.ForeignKey(PatientModel)
    startTime = models.DateTimeField()


