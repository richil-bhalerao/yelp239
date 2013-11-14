from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#from mysite.userModel import Document

import urllib2
import json

success = False




def courseList(request):
    # Handle Category List
 
    
    if request.method == 'GET':
            global success
            global userId
            global cjlist
            
            uname=request.session['uid']
            print uname
            #Send the get category request  
            userurl="http://localhost:8080/user/"+uname
            status = urllib2.urlopen(userurl)
            
            data = json.loads(status.read())
            print data 
            
            cjlist=[]
            idlist=[]
            course=data['enrolled']
            for c in course:
                 url="http://localhost:8080/course/"+c
                 print url
                 cget=urllib2.urlopen(url)
                  
                 cdetail=json.loads(cget.read())
               #  print cdetail
                 cjlist.append(cdetail)
                 
            success=True
            
            for course in cjlist:
                courseId = course['_id']
                course['id'] = courseId
                idlist.append(course)
                print courseId             
           
            return render_to_response('courselist.html', {'userId': uname, 'success': success, 'cjlist': idlist}) 
            
def courseDetail(request,id):
    #print id
    uname=request.session['uid']
    return render_to_response('coursedetail.html', {'userId': uname})

