from django.conf.urls import patterns, url
from BioCascadeModeller import views

urlpatterns = patterns('',
        url(r'^$', views.bcmHome, name='bcmHome'))