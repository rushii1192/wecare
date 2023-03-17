from django.shortcuts import render, HttpResponse
from .models import PatientModel

# Create your views here.
def home(request):
    return HttpResponse("This is my home page")


def create(request):
    if request.method == 'POST':
        patient = PatientModel(
            email=request.POST.get('email'), 
            firstName=request.POST.get('firstName'),
            lastName=request.POST.get('lastName'),
            mobile=request.POST.get('mobile'),
            password=request.POST.get('password'),
        )
        patient.save()

        return HttpResponse("Successfully created")
    
    return HttpResponse("This is my Register page")



