from django.urls import path, include
from patient.views import home

urlpatterns = [
    path('/', home, name='patient_home')
]
