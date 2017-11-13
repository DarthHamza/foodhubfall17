from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.restaurant_list, name='restaurant_list'),
    url(r'^detail/(?P<restaurant_id>\d+)/$', views.restaurant_detail, name='restaurant_detail'),

    url(r'^create/$', views.restaurant_create, name='restaurant_create'),
    url(r'^update/(?P<restaurant_id>\d+)/$', views.restaurant_update, name='restaurant_update'),
    url(r'^delete/(?P<restaurant_id>\d+)/$', views.restaurant_delete, name='restaurant_delete'),
]
