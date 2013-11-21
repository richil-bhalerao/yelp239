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
from restaurants import Restaurants
from RecoEngine import RecoEngine

#Ric End

#Ric Start
businessobj = None
restaurant = None
#Ric End

def setup(base,conf_fn):
    print '\n**** service initialization ****\n'
    global businessobj  
    businessobj = Business()
    global restaurant
    restaurant = Restaurants()

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


@route('/restaurants/:iD', method = 'GET')        
def getRestaurant(iD):        
    print "you are in getRestaurant()"

    try:
        entity = restaurant.get(iD)
    except:
        traceback.print_exc()
        abort(404, 'restaurants cannot be retrieved')

    if not entity:
        abort(404, 'restaurant not found')

    return MongoEncoder().encode(entity)


@route('/restaurants/zipcode/:zip', method = 'GET')
def getRestaurantsForZipcode(zipcode):
    print "getRestaurantsForZipcode()"
    try:
        entity = restaurant.getForZip(zipcode)
    except:
        traceback.print_exc()
        abort(404, 'restaurants cannot be retrieved')

    if not entity:
        abort(404, 'restaurants cannot be retrieved')

    return MongoEncoder().encode(entity)

@route('/recommendation/:params', method = 'GET')
def getRecommendation(params):
    print "getRecommendation()"
    try:
        print params
        response = {}
        reco = RecoEngine()
        response['decision'] = reco.isRecommended(params['zipcode'], params['preference'])
        if response['decision'] == -1:
            response['decision'] = 'NA'
        else:
            response['records'] = reco.findMostSimilarRestaurants(params['zipcode'], params['preference'])

        return response

    except:
        abort(404, 'recommendation failed')

input = ['Indian', 'Buffets', 'Paratha'] 
params = {'zipcode': '85048', 'preference': input}
#list = 
result = getRecommendation(params)
print "Decision: "+str(result['decision'])
print "Records: "
for l in result['records']:
    print l
#for i in list:
 #   print i

    