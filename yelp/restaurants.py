"""

@author: Richil Bhalerao

"""

import time

import traceback
from pymongo import Connection
from data.storage import Storage


class Restaurants(object):
    
    #Initialize db object to none
    db = None
    
    def __init__(self):
         
        self.db = Storage().db
        print "restaurants created"   
    # get all restaurant records in a radius of specified distance to a provided latitude and longitude     
    def getRestaurantsInVicinity(self, longlat, distance):

        query = { "loc" : { "$maxDistance" : distance, "$near" : longlat} }

        cursor = self.db['restaurants'].find(query, {"_id":0})

        recordList =  [c for c in cursor]

        print "No. of records retrieved in the vicinity are: ", len(recordList)
        return recordList
    
    #get latitude and longitude for a corresponding zip code
    def getLatLongFromZipCode(self, zipcode):

        query = {"full_address": { "$regex": "\w*%s$" %(zipcode)}}
        data = self.db['restaurants'].find_one(query)
        if (data==None):
            return None
        return data['loc']

    #get a restaurants using it's ID
    def get(self, value):
        print 'In restaurant.get() method'
        try:
            query = {"business_id": value}
            return self.db['restaurants'].find(query)
        except:
            traceback.print_exc()
            return 'failed'

    #get all restaurants in the selected zipcode
    def getForZip(self,zipcode):
        print 'getForZip()'
        try:
            query = {"full_address": { "$regex": "\w*%s$" %(zipcode)}}
            return self.db['restaurants'].find(query)
        except:
            return 'failed'
        
        
# for r in Restaurants().getRestaurantsInVicinity(Restaurants().getLatLongFromZipCode('85053'), 0.030):
#       print r
# for r in Restaurants().getForZip('85053'):
#     print r 