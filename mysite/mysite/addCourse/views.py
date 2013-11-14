from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from mysite.users.models import ipaddress

#from mysite.userModel import Document
from mysite.addCourse.courseform import CourseForm
import urllib2
import requests,json

def addCourse(request):
   if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            global success
            global userId
            
            print "came here"
            category = request.POST.get('category')
            title = request.POST.get('title')
            section = request.POST.get('section')
            dept=request.POST.get('dept')
            term=request.POST.get('term')
            year=request.POST.get('year')
            instructorname=request.POST.get('instructorname')
            instructoremail=request.POST.get('instructoremail')
            days=request.POST.get('days')
            hours=request.POST.get('hours')
            description=request.POST.get('description')
            attachment=request.POST.get('attachment')
            version=request.POST.get('version')
            
            
            
            
            
            
            category = form.cleaned_data['category']
            title = form.cleaned_data['title']
            section= form.cleaned_data['section']
            dept=form.cleaned_data['dept']
            term=form.cleaned_data['term']
            year=form.cleaned_data['year']
            instructorname=form.cleaned_data['instructorname']
            instructoremail=form.cleaned_data['instructoremail']
            days=form.cleaned_data['days']
            hours=form.cleaned_data['hours']
            description=form.cleaned_data['description']
            attachment=form.cleaned_data['attachment']
            version=form.cleaned_data['version']
            
            
            
            
            print category
            print title
            print section
            userId=request.session['uid']
            success = True
            
            headers = {'content-type': 'application/json'}
            payload = {
            "category": str(category),
#            "id":"test1",
            "title": str(title),
            "section": str(section),
            "dept": str(dept),
            "term": str(term),
            "year": str(year),
            "instructor": [
            {
            "name": instructorname,
            "email": instructoremail
            }
            ],
            "days": [
            "Monday",
            "Wednesday",
            "Friday"
            ],
            "hours": [
            "8:00AM",
            "9:15:AM"
            ],
            "Description": description,
            "attachment": "",
            "version": version
            }
            
            jsonData=json.dumps(payload)
#             formData = {'category': category, 'title': title, 'section': section, 'dept':dept, 'term':term, 'year':year,'instructor:[{/'name/''}    
#             formDataInJson = json.dumps(formData)
            #print 'formDataInJson : ' , formDataInJson
            
            #Send the Add User Request and get the status 
            list= ipaddress.objects.values()
            for val in list:
                ipadd = val
           
            ipadd = ipadd['ip']
               
            print "current ipaddress is ", ipadd
            
            url= "http://"+ipadd+"/course" 
            #url="http://localhost:8080/course"
            print "URL : ",url
#           
           # status = urllib2.urlopen(url)
            course=requests.post(url,data=json.dumps(payload),headers=headers)
            print course
           # status = json.loads('{"success": true}')
            #print 'Status Json : ' , status  
            #status['success'] = False   
#             url= "http://localhost:8080/user/course"
#             cid=course['id']
#             
#             print "cid=",cid
#             payload={"email":userId, "courseid":cid}
#             requests.put(url,data=json.dumps(payload),headers=headers)
#         
#                return render_to_response('userAdd.html', {'userId': userId, 'form': form, 'success': success}) 
            return render_to_response('AddSuccess.html',{ 'userId': userId},context_instance=RequestContext(request))
            
   else:
           
            userId=request.session['uid']
            success = False
            form = CourseForm()
            return render_to_response('courseAdd.html', {'userId': userId, 'form': form},context_instance=RequestContext(request))
        
        
def courseDetail(request):
    cid=request.get['va']
    return render_to_response('coursedetail.html', {'userId': uname})