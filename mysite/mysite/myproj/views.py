# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from mysite.myproj.forms import CategoryForm
import urllib2
import json

success = False
userId = 'Spandana'

def index(request):
    return render_to_response('Home.html', {'userId': 'Spandana'})

def categoryAdd(request):
    # Handle User Add
    global success
    global userId
    success = False
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            global success
            global userId
            print 'Inside Valid Form', success
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            creationDate = form.cleaned_data['creationDate']
            status = form.cleaned_data['status']
           
            formData = {'email': email, 'description': description, 'creationDate': creationDate, 'status': status}    
            formDataInJson = json.dumps(formData) 
            #print 'formDataInJson : ' , formDataInJson
            
            #Send the Add User Request and get the status  
            ret = urllib2.urlopen('http://198.162.100.40:8080/category', formDataInJson)
            
            categoryObj = json.loads(ret.read())
            if (categoryObj.getcode() == 200):
               success = True
            #success = True 
               
            if (success):
                success = True
                return render_to_response('status.html', {'userId': userId, 'message': 'Category Added Successfully', 'title': 'Add Category Status', 'forwardToUrl': 'categoryAdd', 'forwardToText': '<<< Back To Add Category>>>'}) 
            else:
                success = False
                return render_to_response('status.html', {'userId': userId, 'message': 'Category Add Failed', 'title': 'Add Category Status',  'forwardToUrl': 'categoryAdd', 'forwardToText': '<<< Back To Add Category>>>'}) 
        else:
            global success
            global userId
            success = False
            form = CategoryForm()
            return render_to_response('status.html', {'userId': userId, 'message': 'Category Add Failed', 'title': 'Add Category Status',  'forwardToUrl': 'categoryAdd', 'forwardToText': '<<< Back To Add Category>>>'}) 

    else:
            global success
            global userId
            success = False
            form = CategoryForm()
            return render_to_response('categoryAdd.html', {'userId': userId, 'form': form}) 
            

def categoryList(request):
    # Handle Category List
    global success
    global userId
    success = False
    
    if request.method == 'GET':
            global success
            global userId
            #Send the get category request  
            status = urllib2.urlopen('http://198.162.100.40:8080/category/list')
            #status = open('data/Category.json')
            
            if (status.getcode() == 200):
               success = True
            #success = True 
               
            if (success):
                #get category list from response body
                #categoryList = json.load(status)
                categoryList = json.loads(status.read())
                print 'Category List : ', categoryList
                success = True
                return render_to_response('categoryList.html', {'userId': userId, 'success': success, 'categoryList': categoryList}) 
            else:
                success = False
                return render_to_response('status.html', {'userId': userId, 'message': 'Category List Fetch Failed', 'title': 'Category List Status',  'forwardToUrl': 'categoryManager', 'forwardToText': '<<< Back To Category Manager >>>'}) 
    else:
            global success
            global userId
            success = False
            return render_to_response('categoryManager.html', {'userId': userId}) 
 
            
def categoryManager(request):
    global userId
    return render_to_response('categoryManager.html', {'userId': userId})
    #return HttpResponseRedirect('next_view')

def courseManager(request):
    global userId
    return render_to_response('courseManager.html', {'userId': userId})

def courseList(request):
   # Handle Course List
    global success
    global userId
    success = False
    
    if request.method == 'GET':
            uname=request.session['uid']
            print uname
            #Send the get category request  
            userurl="http://198.162.100.40:8080/user/"+uname
            status = urllib2.urlopen(userurl)
            
            data = json.loads(status.read())
            print data 
            
            cjlist=[]
            idlist=[]
            course=data['own']
              
            for c in course:
                 url="http://198.162.100.40:8080/course/"+c
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
            #Send the get course request  
#             status = urllib2.urlopen(rse'http://198.162.100.40:8080/course/list')
#             #status = open('data/Courses.json')
#             
#             if (status.getcode() == 200):
#                success = True
            #success = True 
               
            if (success):
                #get course list from response body tat will display is already done
                #courseList = json.load(status)
                
                print 'Course List : ', cjlist
                success = True
                return render_to_response('courseList.html', {'userId': userId, 'success': success, 'cjlist': idlist})
              
              
                
def courseDetail(request, course_id):
    
   # Handle Course List
    global success
    global userId
    success = False
    print "COURSE ID : ",course_id
    if request.method == 'GET':
            global success
            global userId
            
            #Send the get course request  
            status = urllib2.urlopen('http://198.162.100.40:8080/course/id')
            #status = open('data/Course.json')
            
            if (status.getcode() == 200):
               success = True
            #success = True 
               
            if (success):
                #get course list from response body
                course = json.loads(status.read())
                #course = json.load(status)
                print 'Course  : ', course
                success = True
                return render_to_response('courseDetail.html', {'userId': userId, 'success': success, 'course': course})

def courseEnroll(request):
    global userId
    return render_to_response('categoryManager.html', {'userId': userId})
   
def quiz(request):
    return render_to_response('Quiz.html', {'userId': 'Spandana'})
    
def announcement(request):
    return render_to_response('Announcement.html', {'userId': 'Spandana'})
    
def discussion(request):
    return render_to_response('Discussion.html', {'userId': 'Spandana'})
   

                
	
