from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import LoginForm, DoctorForm, PatientForm
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer


# Pages

# Home page
def index_view(request):
    return render(request, 'index.html')


# Login page
def login_view(request):
    return render(request, 'login.html', {'form': LoginForm()})


# Dashboard
@login_required()
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})


# Doctors page
@login_required()
def doctors_view(request, doctor_id, new):

    if new:
        return render(request, 'doctors/register.html', {'form': DoctorForm()})

    elif doctor_id:
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
        return render(request, 'doctors/editDoctor.html', {'form': form, 'doctorId': doctor_id})

    else:
        return render(request, 'doctors/doctors.html', {'doctors': Doctor.objects.all()})


@login_required()
def patients_view(request, patient_id, new):
    if new:
        return render(request, 'patients/addPatient.html', {'form': PatientForm()})

    elif patient_id:
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
        return render(request, 'patients/editPatient.html', {'form': form, 'patientId': patient_id})

    else:
        return render(request, 'patients/patients.html', {'patients': Patient.objects.all()})


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
        return Response(user.username, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# Logout
@api_view(['POST'])
def api_logout(request):
    django_logout(request)
    return Response(status=status.HTTP_200_OK)


# Get all registered doctors
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def api_doctors(request, doctor_id):
    if request.method == 'POST':
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

    elif request.method == 'GET':
        # TODO: return user fields in doctor json
        if doctor_id:
            doctor = Doctor.objects.get(doctorId=doctor_id)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            doctors = Doctor.objects.all()
            for doctor in doctors:
                doctor.username = doctor.user.username
                # TODO: Add other fields

            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        try:
            doctor = Doctor.objects.get(doctorId=doctor_id)

            if request.method == 'PUT':
                form = request.data

                user = doctor.user
                user.username = form.get('username')
                if form.get('password'):
                    user.set_password(form.get('password'))
                user.first_name = form.get('first_name')
                user.last_name = form.get('last_name')
                user.email = form.get('email')

                doctor.document = form.get('document')
                doctor.cellphone = form.get('cellphone')
                doctor.officePhone = form.get('officePhone')
                doctor.userType = form.get('userType')

                user.save()
                doctor.save()

                return Response(status=status.HTTP_200_OK)

            elif request.method == 'DELETE':

                user = doctor.user
                doctor.delete()
                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# Patients CRUD
#
# Methods:
# POST: Create a new patient with given params
# GET: Gets given patient if patient_id is given or all if not
# PUT: Modifies patient with given patient_id, sets data from sent form
# DELETE: Deletes patient with given patient_id
#
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
            # TODO: 'dependsOn' field
        )
        patient.save()
        if patient.patientId is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'GET':

        if patient_id:
            patient = Patient.objects.get(patientId=patient_id)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        try:
            patient = Patient.objects.get(patientId=patient_id)

            if request.method == 'PUT':
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

        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
