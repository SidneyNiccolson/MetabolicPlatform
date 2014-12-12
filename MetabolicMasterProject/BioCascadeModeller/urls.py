from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
        url(r'^$', views.bcmHome, name='bcmHome'),
        url(r'^effluentmockup/$', views.test2, name='mockup'),
        url(r'^BCMabout/$', views.about2, name='about2'),
        url(r'^(?P<waste_id>\w+)/treatment_tech/(?P<treatment_id>\w+)_Modelling/results/$', views.calc_results_Struvite, name='treatmentTechModelling'),
        url(r'^(?P<waste_id>\w+)/treatment_tech/(?P<treatment_id>\w+)_Modelling/$', views.test, name='treatmentTechModelling'),

        url(r'^(?P<waste_id>\w+)/$', views.details, name='details'),
        url(r'^(?P<waste_id>\w+)/treatment_tech/$', views.treatmentTech, name='treatmentTech'),
        url(r'^(?P<waste_id>\w+)/treatment_tech/(?P<treat_id>\w+)/$', views.treatmentTech2, name='treatmentTech2'),


)