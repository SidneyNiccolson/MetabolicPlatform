from django.conf.urls import patterns, include, url
from BioCascadeModeller import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from MetabolicMasterProject import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MetabolicMasterProject.views.home', name='home'),
    # url(r'^MetabolicMasterProject/', include('MetabolicMasterProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.homePage, name='homePage'),
    url(r'^BioCascadeModeller/', include('BioCascadeModeller.urls'),

))
