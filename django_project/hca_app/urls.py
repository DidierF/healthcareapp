from django.conf.urls import url

from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    # Pages
    url(r'^$', views.login_view),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login_view),
    url(r'^dashboard/$', views.dashboard_view),
    url(r'^doctors/([0-9]*?|(new?))/?$', views.doctors_view),
    url(r'^patients/([0-9]*?|(new?))/?$', views.patients_view),
    url(r'^patients/edit/([0-9]*)/$', views.patients_edit_view),
    url(r'^appointments/([0-9]*?|(new?))/?$', views.appointments_view),
    url(r'^prescriptions/([0-9]*?|(new?))/?$', views.prescriptions_view),
    url(r'^medic_forms/([a-zA-Z]*?)/?$', views.medic_form_view),
    url(r'^ophthalmology/([0-9]*?|(new?))/?$', views.ophthalmology_view),

    # API
    url(r'^api/v1/login$', views.api_login),
    url(r'^api/v1/logout$', views.api_logout),
    url(r'^api/v1/doctors/([0-9]*)$', views.api_doctors),
    url(r'^api/v1/patients/([0-9]*)$', views.api_patient),
    url(r'^api/v1/appointments/([0-9]*)$', views.api_appointment),
    url(r'^api/v1/prescriptions/([0-9]*)$', views.api_prescription),
    url(r'^api/v1/ophthalmology/([0-9]*)$', views.api_ophthalmology),
    url(r'^api/v1/mail/prescriptions$', views.api_prescription_mail),
    url(r'^api/v1/mail/appointments$', views.api_appointment_mail),
    url(r'^api/v1/pdf/appointments/([0-9]*)$', views.api_appointment_pdf),

]
