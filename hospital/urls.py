from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', patientLogin, name='patientLogin'),
    path('createDoctor/', createDoctor, name="createDoctor"),
    path('logout/', patientLogout, name='patientLogout'),
]
