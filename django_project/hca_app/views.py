from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
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
def register(request):
    return render(request, 'register.html', {'form': DoctorForm()})


# API

# HTTP Status Codes
HTTP_STATUS = {
    'SUCCESS': 200,
    'CREATED': 201,
    'UNAUTHORIZED': 403,
    'NOT_FOUND': 404,
    'INTERNAL': 500
}


# Register new doctor
@require_http_methods(["POST"])
def api_register(request):
    form = request.POST
    user = User.objects.create_user(username=form.get('username'),
                                    password=form.get('password'),
                                    email=form.get('email'),
                                    first_name=form.get('first_name'),
                                    last_name=form.get('last_name')
                                    )
    doc = Doctor(user=user,
                 document=form.get('document'),
                 cellphone=form.get('cellphone'),
                 userType=form.get('userType', 'std'))
    user.save()
    doc.save()
    return HttpResponse(200)


# Login
@require_http_methods(["POST"])
def api_login(request):
    form = request.POST
    user = authenticate(username=form.get('username'),
                        password=form.get('password')
                        )
    # TODO: also compare 'doctor's' document
    if user is not None:
        print('success: ' + str(HTTP_STATUS['SUCCESS']))
        return HttpResponse(request, HTTP_STATUS['SUCCESS'])
    else:
        print('unauthorized: ' + str(HTTP_STATUS['UNAUTHORIZED']))
        return HttpResponse(request, HTTP_STATUS['UNAUTHORIZED'])
