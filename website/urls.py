from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard',dashboard,name="dashboard"),
    path('patient',patient,name='patiententry'),
    path('editpatient',editpatient,name='editpatient'),
    path('doctor',doctor,name='doctorentry'),
    path('editdoctor',editdoctor,name='editdoctor'),


]    