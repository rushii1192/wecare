from django.shortcuts import render, redirect, HttpResponse
from faceDetection.detection import FaceRecognition
from patient.models import PatientModel, AppointmentModel
from .models import DoctorModel

# Create your views here.
faceRecognition = FaceRecognition()

def patientLogin(request):
    face_id = faceRecognition.recognizeFace()
    patient = PatientModel.objects.get(mobile=face_id)

    appointments = AppointmentModel.objects.filter(userId=face_id)

    doctors = DoctorModel.objects.filter(status="Free")

    currentAppointment = appointments[0]
    currentDoctor = doctors[0]

    currentAppointment.status = "Reached"
    currentAppointment.docterId = doctors[0].email

    currentAppointment.save()

    currentDoctor.status = "Occupied"
    currentDoctor.occupiedBy = face_id
    currentDoctor.save()

    print("succefully updated")

    return HttpResponse(f"Hello {patient.firstName} {patient.lastName}")


def patientLogout(request):
    face_id = faceRecognition.recognizeFace()
    patient = PatientModel.objects.get(mobile=face_id)

    appointments = AppointmentModel.objects.filter(userId=face_id)

    doctors = DoctorModel.objects.filter(occupiedBy=face_id)

    currentAppointment = appointments[0]
    currentDoctor = doctors[0]

    currentAppointment.status = "Reached"
    currentAppointment.save()

    currentDoctor.status = "Free"
    currentDoctor.occupiedBy = ""
    currentDoctor.save()

    print("succefully updated")

    return HttpResponse(f"Bye {patient.firstName} {patient.lastName}")

    

def createDoctor(request):
    if request.method == "POST":
        doctor = DoctorModel()
        doctor.name = request.POST.get("name")
        doctor.email = request.POST.get("email")
        doctor.save()
        return HttpResponse("Created The Doctor")
    
    return render(request, "hospital/Doctor.html")
