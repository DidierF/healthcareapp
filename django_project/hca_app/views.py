from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .utils.serializers import DoctorSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.models import Doctor
from .utils.forms import LoginForm, DoctorForm


# Pages

# Home page
def index(request):
    return render(request, 'index.html')


# Login page
def login(request):
    return render(request, 'login.html', {'form': LoginForm()})


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
def edit_doctor(request, id):
    doctor = Doctor.objects.get(doctorId=id)
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
    return render(request, 'editDoctors.html', {'form': form})


# Dashboard
@login_required()
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


# API

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
@api_view(["POST"])
def api_register(request):
    form = request.POST
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


# Login
@api_view(["POST"])
def api_login(request):
    form = request.POST
    user = authenticate(username=form.get('username'),
                        password=form.get('password'))
    # TODO: also compare 'doctor's' document
    if user is not None:
        django_login(request, user)
        return Response(user.username, status.HTTP_200_OK)
    else:
        return Response(status.HTTP_401_UNAUTHORIZED)


# Logout
@csrf_exempt
@api_view(["GET"])
def api_logout(request):
    django_logout(request)
    return Response(status=status.HTTP_200_OK)
