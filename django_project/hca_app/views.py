from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from .utils.forms import LoginForm


def index(request):
    return HttpResponse(get_template('index.html').render(Context()))


def login(request):
    return HttpResponse(get_template('login.html').render({'form': LoginForm()}))
    # return render(request, 'login.html')
