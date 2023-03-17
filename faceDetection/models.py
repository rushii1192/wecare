from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    face_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length = 100)
    job = models.CharField(max_length = 15)
    phone = models.CharField(max_length =  10)
    email = models.CharField(max_length = 20)
    bio = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.name
    
class PatientProfile(models.Model):
    email = models.CharField(max_length = 20)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    mobile = models.CharField(max_length =  10)
    bloodGroup = models.CharField(max_length= 20)

    def __str__(self) -> str:
        return self.firstName + self.lastName