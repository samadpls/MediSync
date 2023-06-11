from django.db import models
import random,string
# Create your models here.
class Patient(models.Model):
    id_p = models.CharField(primary_key=True,default="".join(random.choices(string.ascii_letters + string.digits, k=4)), max_length=4)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)

class Availability(models.Model):
    day_of_week = models.CharField(max_length=20)
    time_range = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.day_of_week}: {self.time_range}"

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email= models.EmailField()
    specialty = models.CharField(max_length=100)
    availabilities = models.ManyToManyField(Availability)