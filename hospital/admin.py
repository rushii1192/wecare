from django.contrib import admin
<<<<<<< Updated upstream
from . models import DoctorModel

# Register your models here.

admin.site.register(DoctorModel)

=======
from .models import DoctorModel
# Register your models here.
admin.site.register(DoctorModel)
>>>>>>> Stashed changes
