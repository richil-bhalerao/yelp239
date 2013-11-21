'''
Created on November 01, 2013

@author: richil
'''

from data.storage import Storage
import traceback
from bson.objectid import ObjectId

class Business(object):
    
    def __init__(self):
        print 'business created'
        # create storage
        self.__store = Storage()
        
        
    def get(self, value):
        print 'In business.get method'
        try:
            return self.__store.get('business', 'business_id', value)
        except:
            traceback.print_exc()
            return 'failed'    
        
    def remove(self, value):
        print 'In business.remove method'
        try:
            return self.__store.remove('business', 'business_id', value)
        except:
            traceback.print_exc()
            return 'failed'
    
    def getAll(self):
        print 'In business.getAll method'
        try:
            return self.__store.getAll('business')
        except:
            traceback.print_exc()
            return 'failed'

#print 'hello'
    