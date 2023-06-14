from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from database.models import *
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
import sqlite3,os
from django.core.files.storage import FileSystemStorage

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
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
    with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor()
            query = "SELECT * FROM Patient"  
            cursor.execute(query)

            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Prepare the data as a list of dictionaries
            patients = []
            for row in rows:
                patient = dict(zip(column_names, row))
                patients.append(patient)
            return render(request,'patient.html',{'patient':patients})

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
    with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor() 
            query_specific_patient = """
                SELECT * FROM Patient
                WHERE id_p = ?
            """
            cursor.execute(query_specific_patient, (id_p,))
            row_specific_patient = cursor.fetchone()
            # Get all patients
            query_all_patients = """
                SELECT * FROM Patient
            """
            cursor.execute(query_all_patients)
            rows_all_patients = cursor.fetchall()


    # Process the retrieved data as needed
    patient1 = dict(zip(['id_p', 'name', 'address', 'phone_number', 'email', 'dob', 'gender'], row_specific_patient)) if row_specific_patient else None
    print(patient1)
    patients = [dict(zip([description[0] for description in cursor.description], row)) for row in rows_all_patients]

    return render(request,'editpatient.html',{"patient": patients, "id": id_p,"patient1":patient1})

def update_patient(request,id_p):
    if request.method == 'POST':
       # Get the submitted form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor()
            # Update the patient information in the database
            query = """
                UPDATE Patient
                SET name = ?,
                    email = ?,
                    gender = ?,
                    dob = ?,
                    address = ?,
                    phone_number = ?
                WHERE id_p = ? 
            """
            values = (name, email, gender, dob, address, phone_number, id_p)
            cursor.execute(query, values)
        
        return redirect('/patient')
def delete_patient(request, id_p):
    with sqlite3.connect(BASE_DIR / 'data.db') as db:
        cursor = db.cursor()
        query = "DELETE FROM Patient WHERE id_p = ?"
        cursor.execute(query, (id_p,))
    return redirect('/patient')

def doctor(request):
    with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor()
            query = "SELECT * FROM Doctor"  
            cursor.execute(query)

            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Prepare the data as a list of dictionaries
            doctors = []
            for row in rows:
                doctor = dict(zip(column_names, row))
                doctors.append(doctor)
            print(doctors)
            return render(request,'doctor.html',{'doctor':doctors})
    
def delete_doctor(request,id_d):
    doctor = Doctor.objects.get(id_d=id_d)
    doctor.delete()
    return redirect('/doctor')


def editdoctor(request,id_d):
    with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor() 
            query_specific_doctor = """
                SELECT * FROM Doctor
                WHERE id_d= ?
            """
            cursor.execute(query_specific_doctor, (id_d,))
            row_specific_doctor = cursor.fetchone()
            # Get all doctors
            query_all_doctors = """
                SELECT * FROM Doctor
            """
            cursor.execute(query_all_doctors)
            rows_all_doctors = cursor.fetchall()


    # Process the retrieved data as needed
    doctor1 = dict(zip(['id_d', 'name',  'email', 'specialty', 'day_of_week','time_range'], row_specific_doctor)) if row_specific_doctor else None
    print(doctor1)
    doctors = [dict(zip([description[0] for description in cursor.description], row)) for row in rows_all_doctors]

    return render(request,'editdoctor.html',{"doctor": doctors, "id": id_d,"doctor1":doctor1})

def update_doctor(request, id_d):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        specialty = request.POST.get('specialty')
        day_of_week = request.POST.get('availability_day')
        time_range = request.POST.get('availability_time')
        with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor()
            # Update the Doctor information in the database
            query = """
                UPDATE Doctor
                SET name = ?,
                    email = ?,
                    specialty = ?,
                    day_of_week = ?,
                    time_range = ?
                WHERE id_d = ? 
            """
            values = (name, email, specialty, day_of_week, time_range,  id_d)
            cursor.execute(query, values)
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
        
         #connectig with sqlite3
        with sqlite3.connect(BASE_DIR/'data.db') as db:
            cursor=db.cursor()
            query = "INSERT INTO Patient (id_p, name, email, gender, dob, address, phone_number) VALUES (?, ?, ?, ?, ?, ?, ?)"
            values = ("".join(random.choices(string.ascii_letters + string.digits, k=4)),
                       name, email, gender, dob, address, phone)
            cursor.execute(query, values)
    return redirect('/patient')

def save_doctor(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        specialty = request.POST.get('specialty')
        day_of_week = request.POST.get('availability_day')
        time_range = request.POST.get('availability_time')
        doctor = Doctor.objects.create(id_d="".join(random.choices(string.ascii_letters + string.digits, k=4)),
            name=full_name, email=email, specialty=specialty,day_of_week=day_of_week, time_range=time_range)
        doctor.save()
    return redirect('/doctor')