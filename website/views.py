from django.shortcuts import redirect, render, get_object_or_404
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
    random_pic=['../static/assets/img/team-2.jpg','../static/assets/img/team-1.jpg','../static/assets/img/team-3.jpg',
                '../static/assets/img/team-4.jpg','https://xsgames.co/randomusers/avatar.php?g=male',
                'https://xsgames.co/randomusers/avatar.php?g=female','https://xsgames.co/randomusers/avatar.php?g=pixel']
    doctor=Doctor.objects.all()
    patients = Patient.objects.values('id_p', 'name')
    return render(request,'dashboard.html',{'doctor':doctor,"random_pic":random_pic,'patients':patients})

def patient(request):
    patient=Patient.objects.all()
    return render(request,'patient.html',{'patient':patient})

@csrf_exempt
def get_appointment(request):
    if request.method == 'POST':
        # Get the selected patient ID and doctor ID from the AJAX request
        data = json.loads(request.body)
        patient_id = data['patientId']
        doctor_id = data['doctorId']

        
        # Retrieve the patient and doctor objects using their IDs
        patient = Patient.objects.get(id_p=patient_id)
        doctor = Doctor.objects.get(id_d=doctor_id)

        # Create a new Appointment object and save it to the database
        appointment = Appointment.objects.create(
            id_a="".join(random.choices(string.ascii_letters + string.digits, k=4)),
            patient=patient,
            doctor=doctor
        )
        
        return redirect('/dashboard')
    


def editpatient(request,id_p):
    patient1 = Patient.objects.filter(id_p=id_p).first()
    patient=Patient.objects.all()
    
    return render(request,'editpatient.html',{"patient": patient, "id": id_p,"patient1":patient1})

def update_patient(request,id_p):
    patient = Patient.objects.get(id_p=id_p)

    if request.method == 'POST':
        # Update the patient information based on the submitted form data
        patient.name = request.POST.get('name')
        patient.email = request.POST.get('email')
        patient.gender = request.POST.get('gender')
        patient.dob = request.POST.get('dob')
        patient.address = request.POST.get('address')
        patient.phone_number = request.POST.get('phone_number')
        patient.save()
        
    return redirect('/patient')
def delete_patient(request,id_p):
    patient = Patient.objects.get(id_p=id_p)
    patient.delete()
    return redirect('/patient')

def doctor(request):
    doctor=Doctor.objects.all()
    return render(request,'doctor.html',{'doctor':doctor})
    
def delete_doctor(request,id_d):
    doctor = Doctor.objects.get(id_d=id_d)
    doctor.delete()
    return redirect('/doctor')


def editdoctor(request,id_d):
    doctor1 = Doctor.objects.filter(id_d=id_d).first()
    doctor=Doctor.objects.all()
    return render(request,'editdoctor.html',{"doctor": doctor, "id": id_d,"doctor1":doctor1})

def update_doctor(request, id_d):
    doctor = Doctor.objects.get(id_d=id_d)
    print(doctor.day_of_week)
    print(doctor.time_range)
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        specialty = request.POST.get('specialty')
        start_time = request.POST.get('start_time')  
        end_time = request.POST.get('end_time')  
        start_day = request.POST.get('start_day') 
        end_day = request.POST.get('end_day') 
        day_of_week = f"{start_day}-{end_day}"
        time_range = f"{start_time}-{end_time}"

        doctor.name = full_name
        doctor.email = email
        doctor.specialty = specialty
        doctor.day_of_week = day_of_week
        doctor.time_range = time_range
        
        doctor.save()
        return redirect('/doctor')
    return redirect('/doctor')


    
def patientrecord(request):
    # If the request is not a POST request or the selected patient is not found, render the initial page
    return render(request, 'patientrecord.html', {'patients': Patient.objects.all()})
from django.http import JsonResponse

@csrf_exempt
def getrecord(request, patientId):
    appointments = Appointment.objects.filter(patient_id=patientId)

    appointment_data = [
        {
            'doctor_name': appointment.doctor.name,
            'specialty': appointment.doctor.specialty,
            'booking': appointment.date,
        }
        for appointment in appointments
    ]

    return JsonResponse({'appointments': appointment_data})


@csrf_exempt
def getpatient(request,patientId):
    patient = Patient.objects.get(id_p=patientId)
     # Create a dictionary with the patient record data
    print(patientId)
    patient_data = {
        'name': patient.name,
        'email': patient.email,
        'address': patient.address,
        'phone_number': patient.phone_number
    }
    
    print('here'*10)
      
        # Return the patient record data as a JSON response
    return JsonResponse(patient_data)

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
    return redirect('/patient')

def save_doctor(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        specialty = request.POST.get('specialty')
        start_time = request.POST.get('start_time')  
        end_time = request.POST.get('end_time')  
        start_day = request.POST.get('start_day') 
        end_day = request.POST.get('end_day') 
        day_of_week = f"{start_day}-{end_day}"
        time_range = f"{start_time}-{end_time}"
        doctor = Doctor.objects.create(
            id_d="".join(random.choices(string.ascii_letters + string.digits, k=4)),
            name=full_name,
            email=email,
            specialty=specialty,
            day_of_week=day_of_week, 
            time_range=time_range,  
        )
        doctor.save()

    return redirect('/doctor')

