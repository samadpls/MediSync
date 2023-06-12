from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard',dashboard,name="dashboard"),
    path('patient',patient,name='patiententry'),
    path('editpatient/<str:id_p>',editpatient,name='editpatient'),
    path('update-patient/<str:id_p>',update_patient,name='update-patient'),
    path('delete-patient/<str:id_p>',delete_patient,name='delete-patient'),
    path('doctor',doctor,name='doctorentry'),
    path('delete-doctor/<str:id_d>',delete_doctor,name='delete-doctor'),
    path('update_doctor/<str:id_d>',update_doctor,name='update_doctor'),
    path('editdoctor/<str:id_d>', editdoctor, name='editdoctor'),
    path('patientrecord', patientrecord, name='patientrecord'),
    path('save_patient',save_patient,name='save_patient'),
    path('save_doctor',save_doctor,name='save_doctor'),
    path('get_appointment',get_appointment,name='get_appointment'),
    path('getpatient/<str:patientId>/',getpatient,name='getpatient'),
    path('getrecord/<str:patientId>/',getrecord,name='getrecord')

]    