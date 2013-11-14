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
           
    # get all restaurant records in a radius of specified distance to a provided latitude and longitude     
    def getRestaurantsInVicinity(self, longlat, distance):
        
        query = { "loc" : { "$maxDistance" : distance, "$near" : longlat} }
        
        cursor = self.db['restaurants'].find(query)
        
        recordList =  [c for c in cursor]
        
        print "No of records retrieved in the vicinity are: ", len(recordList)
        return recordList
    
    #get latitude and longitude for a corresponding zip code
    def getLatLongFromZipCode(self, zipcode):
        
        query = {"full_address": { "$regex": "\w*%s$" %(zipcode)}}
        data = self.db['restaurants'].find_one(query)
        return data['loc']

    

    

# for r in Restaurants().getRestaurantsInVicinity(Restaurants().getLatLongFromZipCode('85053'), 0.030):
#     print r


#print Restaurants().getLatLongFromZipCode('85053') 