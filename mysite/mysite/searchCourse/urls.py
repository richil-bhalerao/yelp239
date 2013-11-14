##Nik Code Starts

from django.conf.urls.defaults import *

urlpatterns = patterns('',


url(r'^$','mooc.apps.searchCourse.views.searchCourse', name="search_course"),
url(r'^/enrollCourse/([a-zA-Z0-9_@.]*),([a-zA-Z0-9_.]*)/$','mooc.apps.searchCourse.views.enrollCourse', name="enroll_course"),
url(r'^/findFriends$','mooc.apps.findFriends.views.findFriendsConnections', name="search_course"),

)

##Nik Code Ends
