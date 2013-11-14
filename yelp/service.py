"""
Created on November 01, 2013

@author: richil
"""

import time
import sys


# bottle framework
from bottle import request, response, route, run, template, abort

#Ric Start
import traceback
import json
from inspect import trace
from bson.objectid import ObjectId
from json import JSONEncoder

from business import Business
#Ric End


#Ric Start
businessobj = None
#Ric End

def setup(base,conf_fn):
   print '\n**** service initialization ****\n'
   global businessobj  
   businessobj = Business()

#################################Ric Start#######################################################

@route('/business/:id', method='GET')
def get_business(id):
    print 'You are in get business service'
    
    try:
        entity = businessobj.get(id)
    except:
        traceback.print_exc()
        abort(404, 'business cannot be retrieved')    
        
    if not entity:
        abort(404, 'No business with id %s' % id)       
        
    return MongoEncoder().encode(entity)

@route('/business/list', method='GET')
def getAll_business():
    print 'you are in getAll_business'
    try:
        cursor = businessobj.getAll()
        entity = [d for d in cursor]
        print entity
    except:
        traceback.print_exc()
        abort(404, 'businesss cannot be retrieved')    
        
    if not entity:
        abort(404, 'No business found')       
        
    return  MongoEncoder().encode(entity)
        
        


class MongoEncoder(JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return JSONEncoder.default(obj, **kwargs)     
     







#################################### Ric - End ##############################################

