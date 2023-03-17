from django.contrib import admin
from . models import PatientModel, AppointmentModel

# Register your models here.

admin.site.register(PatientModel)
admin.site.register(AppointmentModel)

