from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^checkUname/$', views.checkUname, name='checkUname'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^login/$', views.login, name='login')
]