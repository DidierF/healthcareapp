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

    # API
    url(r'^api/v1/doctors$', views.api_doctors),
    url(r'^api/v1/register$', views.api_register),
    url(r'^api/v1/login$', views.api_login),
]
