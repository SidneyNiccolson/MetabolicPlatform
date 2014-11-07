from django.conf.urls import patterns, url
from BioCascadeModeller import views

urlpatterns = patterns('',
        url(r'^$', views.bcmHome, name='bcmHome'),
        url(r'^category/(?P<waste_id>\w+)/$', views.details, name='details'),
        url(r'^category/(?P<waste_id>\w+)/treatment_tech/$', views.treatmentTech, name='treatmentTech'),
)