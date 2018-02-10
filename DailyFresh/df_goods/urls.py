from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^type(\d+)_(\d+)_(\d+)/$', views.type_list, name='type_list'),
    url(r'type(\d+)/(\d+)/$', views.detail, name='detail')
]