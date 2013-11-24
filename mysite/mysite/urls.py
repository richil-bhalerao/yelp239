from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    
    (r'^index/$','mysite.yelpUI.views.index'),
    (r'^recommender/$','mysite.yelpUI.views.recommender'),
    
    #Ric Start
    url(r'^getbusinessdata/$', 'mysite.yelpUI.views.getJson'),
    url(r'^postpeferencejson/$', 'mysite.yelpUI.views.postPreferenceJson'),
    #Ric End
    
   
   
   
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)
