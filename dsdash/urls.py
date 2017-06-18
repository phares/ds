from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dsdash, name='dsdash'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^member/$', views.member, name='members'),
    url(r'^volunteer/$', views.volunteer, name='volunteers'),

]