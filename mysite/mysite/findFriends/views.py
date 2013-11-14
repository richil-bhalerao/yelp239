######For Demo Start
#from django.http import HttpResponse
#
#def index(request):
#	return HttpResponse("Index Page")
######For Demo Start

##Nik Code Starts

from django.shortcuts import render_to_response
import urllib2
from mysite.users.models import ipaddress
import json
#import netifaces  ##Dynamically finds out the other moocs connected to My Mooc
	
# def findFriendsConnections(request):
# 	links=[]
# 	for friends in netifaces.interfaces():
# 		for node in netifaces.ifaddresses(friends)[netifaces.AF_INET]:
# 			print node['addr']
# 			links.append(node['addr'])
# 	ctx={"links" : links}
# 	
# 	return render_to_response('findFriends/findFriendsIndex.html',ctx)


def findFriendsConnections1(request):
	print " The Host is : ",request.get_host()
	return render_to_response('findFriends/findFriendsServices.html')


def AddFriendCourses(request):
#	print "Link:",link
	list= ipaddress.objects.values()
 	for val in list:
          ipadd = val
        
	ipadd = ipadd['ip']
           
 	print "current ipaddress is ", ipadd
        
 	url= "http://"+ipadd+"/course/list"
 	print "url is", url
	courseEntries = urllib2.urlopen(url)
	#userEntries = urllib2.urlopen('http://'+link+':8080/course/list')
#	print entries1
	jsondata= json.loads(courseEntries.read())
	#coursedata = jsondata
	
	coursedata=[]
	print "Course Data : ",coursedata
	for e in jsondata:
		courseId = e['_id']
		e['id'] = courseId
		coursedata.append(e)
	

	  

#for course in cjlist:
 #              courseId = course['_id']
  ##              course['id'] = courseId
  #              idlist.append(course)
   #             print courseId

	#request.session['userEmail']="nikhil@patil.com"
	#userEmail = request.session['userEmail']
	userEmail = request.session['uid']
	print jsondata
	ctx = {"entries" : coursedata , "userEmail" : userEmail, "CourseId" : courseId}
	return render_to_response('AddFriendCourses.html', ctx)

def findFriendServices(request):
	print "LINK :",link
	print " The Host is : ",request.get_host()
	
	ctx={"link" : link}
	return render_to_response('findFriendsServices.html')


##Nik Code Ends
