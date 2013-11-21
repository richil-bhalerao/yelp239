"""
Storage interface
"""

import time
#Ric Start
import traceback
from pymongo import Connection
#Ric End

class Storage(object):
    
    #Initialize db object to none
    db = None 
    
    def __init__(self):
        # initialize our storage, data is a placeholder
        self.data = {}
        # for demo
        self.data['created'] = time.ctime()
       
        #Ric Start
        connection = Connection('localhost', 27017)
        #Create db object only if it is not created 
        if self.db is None:
            self.db = connection.yelpdb
        #Ric End
    
    
    #######################################Ric Start############################################
    def add(self, collection, data):
        print 'In Storage.add method'
        try:
            return self.db[collection].save(data)
            print 'data added in yelpdb'
        except:
            traceback.print_exc() 
            return "Error: Data cannot be added"
    
    def get(self, collection, fieldname, value):
        print 'In Storage.get method'
        try:
            return self.db[collection].find_one({fieldname:value}) #, {'_id':0})
        except:
            traceback.print_exc() 
            return "Error: Data cannot be retrieved"
        
    def update(self, collection, fieldname, value, data):
        print 'In Storage.update method'
        try:
            self.db[collection].update({fieldname:value}, data);
        except:
            traceback.print_exc() 
            return "Error: Data cannot be updated"    
    
    def remove(self, collection, fieldname, value):
        print 'In Storage.remove method'
        try:
            self.db[collection].remove({fieldname:value})
        except:
            traceback.print_exc() 
            return "Error: Data cannot be deleted"
    
    def getAll(self, collection):
        print 'In Storage.getAll method'
        try:
            return self.db[collection].find({}, {'_id':0})
        except:
            traceback.print_exc() 
            return "All data cannot be retrieved"


# for r in Storage().get('restaurants', 'business_id', 'jvvh4Q00Hq2XyIcfmAAT2A'):
#     print r
