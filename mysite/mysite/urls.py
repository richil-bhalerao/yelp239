from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    (r'^login/$','mysite.users.views.login_view'),
    (r'^index/$','mysite.users.views.index'),
    (r'^logout/$','mysite.users.views.logout'),
    (r'^courseAdd/$','mysite.addCourse.views.addCourse'),
    url(r'^viewCourse/([a-zA-Z0-9_]*)$', 'mysite.enCourses.views.courseDetail', name='courseView'),
    url(r'^cl/$', 'mysite.enCourses.views.courseList', name='cl'),
    url(r'^qz/$', 'mysite.enCourses.views.quiz', name='qz'),
    url(r'^an/$', 'mysite.enCourses.views.announcement', name='an'),
    url(r'^ds/$', 'mysite.enCourses.views.discussion', name='ds'),
    
    url(r'^categoryManager$', 'mysite.myproj.views.categoryManager', name='categoryManager'),
    url(r'^categoryAdd$', 'mysite.myproj.views.categoryAdd', name='categoryAdd'),
    url(r'^categoryList$', 'mysite.myproj.views.categoryList', name='categoryList'),
    url(r'^courseManager$', 'mysite.myproj.views.courseManager', name='courseManager'),
    url(r'^courseList$', 'mysite.myproj.views.courseList', name='courseList'),
    url(r'^courseDetail/([a-zA-Z0-9_]*)$', 'mysite.myproj.views.courseDetail', name='courseDetail'),
    url(r'^quiz$', 'mysite.myproj.views.quiz', name='quiz'),
    url(r'^announcement$', 'mysite.myproj.views.announcement', name='announcement'),
    url(r'^discussion$', 'mysite.myproj.views.discussion', name='discussion'),
    
    
    url(r'^courselist$', 'mysite.enCourses.views.courseList', name='courselist'),
    url(r'^moocList$', 'mysite.users.views.mooclist', name='moocList'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
    url(r'^findFriends/enrollCourse/([a-zA-Z0-9_@.]*),([a-zA-Z0-9_.]*)/$','mysite.searchCourse.views.enrollCourse', name="enroll_course"),
    url(r'^/findFriendServices/$','mysite.findFriends.views.findFriendServices'),
    url(r'^findFriends/AddFriendCourses/$','mysite.findFriends.views.AddFriendCourses', name="add_friend_course"),
    url(r'^exthome/([a-zA-Z0-9_:./]*)$', 'mysite.users.views.exthome', name='exthome'),
)
