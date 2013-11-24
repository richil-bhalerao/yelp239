from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


#from mysite.userModel import Document

import urllib2
import requests,json
from urllib2 import urlopen
from django.http.response import HttpResponse

import json

def index(request):
    return render_to_response('index.html')

def recommender(request):
    return render_to_response('recommender.html')


def getJson(request):
    url = "http://localhost:8080/business/gA5CuBxF-0CnOpGnryWJdQ"
    data = urlopen(url).read()
    # do whatever you want
    return HttpResponse(data, mimetype="application/json")


@csrf_exempt
def postPreferenceJson(request):
    url = "http://localhost:8080/recommendation"
    headers = {'content-type': 'application/json'}
    payload = request.body
    
    print "payload before jsondumps is: ", payload
    
    result = requests.post(url, data=payload, headers=headers)
    return HttpResponse(result, mimetype="application/json")
    

   