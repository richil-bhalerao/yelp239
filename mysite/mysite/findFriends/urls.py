##Nik Code Starts

from django.conf.urls.defaults import *

urlpatterns = patterns('',


url(r'^$','mooc.apps.findFriends.views.findFriendsConnections'),
url(r'^/search/([a-zA-Z0-9_]*)$','mooc.apps.findFriends.views.findFriendsConnections'),
url(r'^/AddFriendCourses/([a-zA-Z0-9_]*),([a-zA-Z0-9_.]*)$','mooc.apps.findFriends.views.AddFriendCourses', name="add_friend_course"),
url(r'^/findFriendServices/([a-zA-Z0-9_.]*)$','mooc.apps.findFriends.views.findFriendServices', name="find_friends_services"),
)

##Nik Code Ends
