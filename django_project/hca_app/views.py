from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models, forms, serializers


# Pages

# Home page
def index_view(request):
    return render(request, 'index.html')


# Login page
def login_view(request):
    return render(request, 'login.html', {'form': forms.LoginForm()})


# Dashboard
@login_required()
def dashboard_view(request):
    return render(request, 'dashboard.html', {'user': request.user})


# Doctors page
@login_required()
def doctors_view(request, doctor_id, new):
    if new:
        return render(request, 'doctors/register.html', {'form': forms.DoctorForm()})

    elif doctor_id:
        doctor = models.Doctor.objects.get(id=doctor_id)
        form = forms.DoctorForm(initial={
            'username': doctor.user.username,
            'email': doctor.user.email,
            'first_name': doctor.user.first_name,
            'last_name': doctor.user.last_name,
            'document': doctor.document,
            'cellphone': doctor.cellphone,
            'office_phone': doctor.office_phone,
            'userType': doctor.userType
        })
        return render(request, 'doctors/editDoctor.html', {'form': form, 'doctorId': doctor_id})

    else:
        return render(request, 'doctors/doctors.html', {'doctors': models.Doctor.objects.all()})


@login_required()
def patients_view(request, patient_id, new):
    if new:
        return render(request, 'patients/addPatient.html', {'form': forms.PatientForm()})

    elif patient_id:
        patient = models.Patient.objects.get(id=patient_id)
        form = forms.PatientForm(initial={
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'email': patient.email,
            # 'document': patient.document,
            'cellphone': patient.cellphone,
            'office_phone': patient.office_phone,
            'address': patient.address
        })
        return render(request, 'editPatient.html', {'form': form, 'patientId': patient_id})

    else:
        return render(request, 'patients/patients.html', {'patients': models.Patient.objects.all()})


@login_required()
def appointments_view(request, appointment_id, new):
    if new:
        return render(request, 'appointments/addAppointment.html', {'form': forms.AppointmentForm()})

    elif appointment_id:
        appointment = models.Appointment.objects.get(id=appointment_id)
        form = forms.AppointmentForm({
            'doctor': appointment.doctor.id,
            'patient': appointment.patient.id,
            'date': appointment.date
        })
        return render(request, 'appointments/editAppointment.html', {'form': form, 'appointment_id': appointment_id})

    else:
        return render(request, 'appointments/appointments.html', {'appointments': models.Appointment.objects.all()})


@login_required()
def medic_form_view(request, form_type):
    if form_type == 'ophthalmology':
        return render(request, 'medic_forms/ophthalmology.html', {'form': forms.OphthalmologyForm()})


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
        doc = models.Doctor(user=user,
                            document=form.get('document'),
                            cellphone=form.get('cellphone'),
                            office_phone=form.get('office_phone'),
                            userType=form.get('userType', 'std'))
        user.save()
        doc.save()

        if doc.id is None:
            user.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        # TODO: return user fields in doctor json
        if doctor_id:
            doctor = models.Doctor.objects.get(id=doctor_id)
            serializer = serializers.DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            doctors = models.Doctor.objects.all()
            for doctor in doctors:
                doctor.username = doctor.user.username
                # TODO: Add other fields

            serializer = serializers.DoctorSerializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        try:
            doctor = models.Doctor.objects.get(id=doctor_id)

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
                doctor.office_phone = form.get('office_phone')
                doctor.userType = form.get('userType')

                user.save()
                doctor.save()

                return Response(status=status.HTTP_200_OK)

            elif request.method == 'DELETE':

                user = doctor.user
                doctor.delete()
                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Doctor.DoesNotExist:
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
        patient = models.Patient(
            first_name=form.get('first_name'),
            last_name=form.get('last_name'),
            email=form.get('email'),
            address=form.get('address'),
            cellphone=form.get('cellphone'),
            office_phone=form.get('office_phone')
            # TODO: 'dependsOn' field
        )
        patient.save()
        if patient.id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'GET':

        if patient_id:
            patient = models.Patient.objects.get(id=patient_id)
            serializer = serializers.PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            patients = models.Patient.objects.all()
            serializer = serializers.PatientSerializer(patients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        try:
            patient = models.Patient.objects.get(id=patient_id)

            if request.method == 'PUT':
                form = request.data

                patient.first_name = form.get('first_name')
                patient.last_name = form.get('last_name')
                patient.email = form.get('email')
                patient.address = form.get('address')
                patient.cellphone = form.get('cellphone')
                patient.office_phone = form.get('office_phone')
                patient.save()

                return Response(status=status.HTTP_200_OK)

            elif request.method == 'DELETE':
                patient.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def api_appointment(request, appointment_id):
    if request.method == 'POST':
        form = request.data
        patient = models.Patient.objects.get(id=form.get('patient'))
        doctor = models.Doctor.objects.get(id=form.get('doctor'))

        appointment = models.Appointment(
            patient=patient,
            doctor=doctor,
            date=form.get('date')
        )
        appointment.save()
        if appointment.id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'GET':

        if appointment_id:
            appointment = models.Appointment.objects.get(id=appointment_id)
            serializer = serializers.AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            appointments = models.Appointment.objects.all()
            serializer = serializers.AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        try:
            appointment = models.Appointment.objects.get(id=appointment_id)

            if request.method == 'PUT':
                form = request.data

                appointment.doctor = form.get('doctor')
                appointment.patient = form.get('patient')
                appointment.date = form.get('date')
                appointment.save()

                return Response(status=status.HTTP_200_OK)

            elif request.method == 'DELETE':
                appointment.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Appointment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def api_prescription(request, prescription_id):
    if request.method == 'POST':
        form = request.data
        appointment = models.Appointment.objects.get(id=form.get('appointment'))

        prescription = models.Prescription(
            appointment=appointment,
            treatment=form.get('treatment'),
            dosage=form.get('dosage')
        )
        prescription.save()
        if prescription.id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'GET':

        if prescription_id:
            prescription = models.Prescription.objects.get(id=prescription_id)
            serializer = serializers.PrescriptionSerializer(prescription)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            prescription = models.Prescription.objects.all()
            serializer = serializers.PrescriptionSerializer(prescription, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        try:
            prescription = models.Prescription.objects.get(id=prescription_id)

            if request.method == 'PUT':
                form = request.data

                prescription.appointment = models.Appointment.objects.get(id=form.get('appointment'))
                prescription.treatment = form.get('treatment')
                prescription.dosage = form.get('dosage')
                prescription.save()

                return Response(status=status.HTTP_200_OK)

            elif request.method == 'DELETE':
                prescription.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Prescription.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
