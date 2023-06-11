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
    return render(request,'patient.html')

def editpatient(request):
    return render(request,'editpatient.html')

def doctor(request):
    return render(request,'doctor.html')

def editdoctor(request):
    return render(request,'editdoctor.html')