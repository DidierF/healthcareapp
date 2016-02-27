from django.conf.urls import url

from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    # Pages
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^dashboard/$', views.dashboard),
    url(r'^doctor/$', views.doctors),
    url(r'^doctor/([0-9]+)/$', views.edit_doctor),
    url(r'^patients/$', views.patients),
    url(r'^patients/([0-9]*/$)|(new/$)', views.edit_patient),
    url(r'^patients/new/$', views.new_patient),

    # API
    url(r'^api/v1/login$', views.api_login),
    url(r'^api/v1/logout$', views.api_logout),
    url(r'^api/v1/doctors$', views.api_doctors),
    url(r'^api/v1/register$', views.api_register),
    url(r'^api/v1/patients/([0-9]*)$', views.api_patient),
]
