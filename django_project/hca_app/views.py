from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.views.decorators.http import require_http_methods
from .models import Doctor
from .utils.forms import LoginForm, DoctorForm


# Pages

# Home page
def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))


# Login page
def login(request):
    return render_to_response('login.html',
                              context_instance=RequestContext(request),
                              dictionary={'form': LoginForm()})


# Doctor register page
def register(request):
    return render_to_response('register.html',
                              context_instance=RequestContext(request),
                              dictionary={'form': DoctorForm()})


# API

# Register new doctor
@require_http_methods(["POST"])
def api_register(request):
    form = request.POST
    doc = Doctor(username=form.get('username'),
                 password=form.get('password'),
                 email=form.get('email'),
                 document=form.get('document'),
                 cellphone=form.get('cellphone'),
                 userType=form.get('userType', 'standard'))
    doc.save()
    return HttpResponse(200)
