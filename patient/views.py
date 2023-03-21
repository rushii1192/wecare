from django.shortcuts import render, HttpResponse
from .models import PatientModel, AppointmentModel
from faceDetection.detection import FaceRecognition

faceRecognition = FaceRecognition()

# Create your views here.
def home(request):
    # return HttpResponse("This is my home page")
    return render(request, 'HomepageExportReady.html')

def create(request):
    if request.method == 'POST':
        patient = PatientModel(
            email=request.POST.get('email'), 
            firstName=request.POST.get('firstName'),
            lastName=request.POST.get('lastName'),
            mobile=request.POST.get('mobile'),
            password=request.POST.get('password'),
            bloodGroup=request.POST.get('bloodGroup'),
        )
        patient.save()

        return HttpResponse("Successfully created")
    
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        patient = PatientModel.objects.filter(email=email, password=password)
        if patient:
            patient = patient[0]
            patient.is_active = True
            patient.save()
            print(patient)
            request.session['id'] = patient.mobile
            print(patient.email)
            return render(request, 'dashboard.html')
        else:
            return HttpResponse("Invalid credentials")
    
    return render(request, 'login.html')


def appointment(request):
    if request.method == 'POST':
        print(request.session['id'])
        patient = PatientModel.objects.get(mobile=request.session['id'])
        patient.is_active = False
        patient.save()
        print(patient.firstName)
        return HttpResponse("Succefully created")
    
    return HttpResponse("Not created")

def createAppointment(request):
    if request.method == 'POST':
        appointment = AppointmentModel(
            userId=request.session['id'], 
            startTime=request.POST.get('startTime'),
            endTime=request.POST.get('endTime'),
            status=request.POST.get('status'),
            symtopms=request.POST.get('symtopms'),
        )
        appointment.save()

        return HttpResponse("Successfully created")
    
    return render(request, 'appointment.html')

def scan(request):
    if request.method == 'POST':
        print(request.session['id'])
        # patient = PatientModel.objects.get(mobile=request.session['id'])
        # patient.is_active = True
        # patient.save()
        # print(patient.firstName)
        addFace(request.session['id'])
        return HttpResponse("Succefully added face")
    
    return HttpResponse("Not created")

def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()



