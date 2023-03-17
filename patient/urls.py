from django.urls import path, include
from patient.views import home, create, login, appointment, scan

urlpatterns = [
    path('', home, name='patient_home'),
    path('register/', create, name='patient_create'),
    path('login/', login, name='patient_login'),
    path('appointment/', appointment, name='patient_appointment'),
    path('scan/', scan, name='patient_scan'),
]
