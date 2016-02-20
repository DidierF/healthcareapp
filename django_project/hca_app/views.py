from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.template.loader import get_template
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
    # form = request.POST
    return HttpResponse(200);
