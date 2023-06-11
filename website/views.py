from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from database.models import *
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
import uuid
import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def dashboard(request):
    return render(request,'dashboard.html')

def patient(request):
    patient=Patient.objects.all()
    return render(request,'patient.html',{'patient':patient})

def editpatient(request):
    patient=Patient.objects.all()
    return render(request,'editpatient.html',{'patient':patient})

def doctor(request):
    return render(request,'doctor.html')

def editdoctor(request):
    return render(request,'editdoctor.html')

def patientrecord(request):
    return render(request,'patientrecord.html')

def save_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        # Create a new patient record
        patient = Patient(id_p="".join(random.choices(string.ascii_letters + string.digits, k=4)),name=name, email=email, gender=gender, dob=dob, address=address, phone_number=phone)
        patient.save()
         
    return render(request, 'patient.html')

