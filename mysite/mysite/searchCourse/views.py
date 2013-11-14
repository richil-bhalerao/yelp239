######For Demo Start
#from django.http import HttpResponse
#
#def index(request):
#	return HttpResponse("Index Page")
######For Demo Start

##Nik Code Starts

from django.shortcuts import render_to_response
import urllib2, urllib

import json
import requests
from mysite.users.models import ipaddress
def searchCourse(request):
	
	print "Inside SearchCourse"
	listFlag = True
	searchFlag = False
	
	#print('http://localhost:8080/courses/'+query)
	#entries1 = urllib2.urlopen('http://localhost:8080/courses/'+query)
	
	
	if request.POST:
		print "http://localhost:8080/course/search/"+request.POST["search"]		
		#entries1 = urllib2.urlopen('http://localhost:8080/course/search/'+request.POST["search"])
		#jsondata= json.loads(entries1.read())
	else: 
		list= ipaddress.objects.values()
	for val in list:
         ipadd = val
       
	ipadd = ipadd['ip']
           
	print "current ipaddress is ", ipadd
        
	url= "http://"+ipadd+"/course/list"
         
		#entries1 = urllib2.urlopen('http://localhost:8080/course/list')
	entries1 = urllib2.urlopen(url)
	jsondata= json.loads(entries1.read())
	#code input
	#jsondata= json.parse(json.loads(entries1.read()))
	#jsondata= json.dumps(request.POST)
	print jsondata
	


	
	
	#print jsondata["courses"]
	#code ends
	#print ("The message returned from bottle: ", entries1.read())
	# "query" : query,
	ctx = {"listFlag" : listFlag, "searchFlag" : searchFlag, "entries" : jsondata}
	#info = {"info1" : "This is info1", "info2" : "This is info2"}
	#success=True
	#ctx = {"entries" : info, "success" : success}

	return render_to_response('searchCourse/searchCourseIndex.html',ctx)

def enrollCourse(request,email,id1):
	print "ID in enrollCourse : ",id1
	data = {"email" : email , "courseid" : id1}
	headers = {'content-type' : 'application/json'} 
#	data1 = urllib.urlencode(data)
	enrollData = json.dumps(data)
	#CourseEnrolled = urllib2.urlopen('http://'+request.get_host()+'/course/enroll',data)
	
#	hostIP=request.session['']
	list = ipaddress.objects.values()
    
	for val in list:
		ipadd = val
          
	ipadd = ipadd['ip']
              
	print "current ipaddress is ", ipadd
            
	url= "http://"+ipadd+"/course/enroll" 
	courseEnrolled = requests.put(url,data=enrollData,headers=headers)
	print courseEnrolled
	print 'http://'+request.get_host()+'/course/enroll'
	ctx = {"userEmail" : email, "courseId" : id1}
	return render_to_response('enrollCourse.html', ctx)










##Nik Code Ends
