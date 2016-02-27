from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .utils.serializers import DoctorSerializer, PatientSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.models import Doctor, Patient
from .utils.forms import LoginForm, DoctorForm, PatientForm


# Pages

# Home page
def index(request):
    return render(request, 'index.html')


# Login page
def login(request):
    return render(request, 'login.html', {'form': LoginForm()})


# Dashboard
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


# Doctor register page
@login_required()
def register(request):
    return render(request, 'register.html', {'form': DoctorForm()})


# Doctors page
@login_required()
def doctors(request):
    return render(request, 'doctors.html', {'doctors': Doctor.objects.all()})


# Doctor edition page
@login_required()
def edit_doctor(request, doctor_id):
    doctor = Doctor.objects.get(doctorId=doctor_id)
    form = DoctorForm(initial={
        'username': doctor.user.username,
        'email': doctor.user.email,
        'first_name': doctor.user.first_name,
        'last_name': doctor.user.last_name,
        'document': doctor.document,
        'cellphone': doctor.cellphone,
        'officePhone': doctor.officePhone,
        'userType': doctor.userType
    })
    return render(request, 'editDoctor.html', {'form': form})


@login_required()
def patients(request):
    return render(request, 'patients.html', {'patients': Patient.objects.all()})


@login_required()
def new_patient(request):
    return render(request, 'addPatient.html', {'form': PatientForm()})


@login_required()
def edit_patient(request, patient_id):
    patient = Patient.objects.get(patientId=patient_id)
    form = PatientForm(initial={
        'firstName': patient.firstName,
        'lastName': patient.lastName,
        'email': patient.email,
        'document': patient.document,
        'cellphone': patient.cellphone,
        'officePhone': patient.officePhone,
        'address': patient.address
    })
    return render(request, 'editPatient.html', {'form': form, 'patientId': patient_id})


# API

# Login
@api_view(['POST'])
def api_login(request):
    form = request.data
    user = authenticate(username=form.get('username'),
                        password=form.get('password'))
    # TODO: also compare 'doctor's' document
    if user is not None:
        django_login(request, user)
        return Response(user.username, status.HTTP_200_OK)
    else:
        return Response(status.HTTP_401_UNAUTHORIZED)


# Logout
# TODO: change to post method
@csrf_exempt
@api_view(['GET'])
def api_logout(request):
    django_logout(request)
    return Response(status=status.HTTP_200_OK)


# Get all registered doctors
@api_view(['GET'])
def api_doctors(request):
    try:
        all_doctors = Doctor.objects.all()
        for doctor in all_doctors:
            doctor.username = doctor.user.username
            # TODO: Add other fields

    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(all_doctors, many=True)
        return Response(serializer.data)


# Register new doctor
@api_view(['POST'])
def api_register(request):
    form = request.data
    user = User.objects.create_user(username=form.get('username'),
                                    password=form.get('password'),
                                    email=form.get('email'),
                                    first_name=form.get('first_name'),
                                    last_name=form.get('last_name'))
    doc = Doctor(user=user,
                 document=form.get('document'),
                 cellphone=form.get('cellphone'),
                 officePhone=form.get('officePhone'),
                 userType=form.get('userType', 'std'))
    user.save()
    doc.save()

    if doc.doctorId is None:
        user.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def api_patient(request, patient_id):

    if request.method == 'POST':
        form = request.data
        patient = Patient(
            firstName=form.get('firstName'),
            lastName=form.get('lastName'),
            document=form.get('document'),
            email=form.get('email'),
            address=form.get('address'),
            cellphone=form.get('cellphone'),
            officePhone=form.get('officePhone')
            # TODO: depends on field
        )
        patient.save()
        if patient.patientId is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    else:
        try:
            patient = Patient.objects.get(patientId=patient_id)

            if request.method == 'GET':
                serializer = PatientSerializer(patient)
                return Response(serializer.data, status=status.HTTP_200_OK)

            elif request.method == 'PUT':
                form = request.data

                patient.firstName = form.get('firstName')
                patient.lastName = form.get('lastName')
                patient.email = form.get('email')
                patient.address = form.get('address')
                patient.cellphone = form.get('cellphone')
                patient.officePhone = form.get('officePhone')
                patient.save()

                return Response(status=status.HTTP_200_OK)

            elif request.method == 'DELETE':
                patient.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        except Patient.doesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
