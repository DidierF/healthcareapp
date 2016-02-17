from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context


def login(request):
    return HttpResponse(get_template('login.html').render(Context()))


def index(request):
    return HttpResponse(get_template('index.html').render(Context()))
