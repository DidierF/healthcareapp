from django.conf.urls import url

from django.contrib import admin
from . import views

admin.autodiscover()

# Examples:
# url(r'^$', 'django_project.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
urlpatterns = [
                url(r'^$', views.index),
                url(r'^admin/', admin.site.urls),
                url(r'^login/$', views.login)
               ]
