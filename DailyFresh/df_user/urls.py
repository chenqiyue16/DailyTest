from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^checkUname/$', views.checkUname, name='checkUname'),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^login/$', views.login, name='login'),
    url(r'^checkPwd/$', views.checkPwd, name='checkPwd'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^user_center_info/$', views.user_center_info, name='user_center_info'),
    url(r'^user_center_order/$', views.user_center_order, name='user_center_order'),
    url(r'^user_center_site/$', views.user_center_site, name='user_center_site'),
    url(r'^user_center_site_handle/$', views.user_center_site_handle, name='user_center_site_handle')
]