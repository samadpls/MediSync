# Create your models here.
from django.db import models
import random,string
# Create your models here.
class Patient(models.Model):
    id_p = models.CharField(primary_key=True,max_length=4)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)

class Doctor(models.Model):
    id_d = models.CharField(primary_key=True,max_length=4)
    name = models.CharField(max_length=255)
    email= models.EmailField()
    specialty = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=20)
    time_range = models.CharField(max_length=50)

class Appointment(models.Model):
    id_a = models.CharField(primary_key=True, max_length=4)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)