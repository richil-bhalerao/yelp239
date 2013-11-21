"""

@author: Richil Bhalerao

"""

import json
from pymongo import Connection
from data.storage import Storage
from restaurants import Restaurants
from operator import itemgetter, attrgetter

class RecoEngine(object):

   
     #Initialize db object to none
    db = None
    
    def __init__(self):
         
        self.db = Storage().db
        #Ric End


    def computeJaccardIndex(self, set1, set2):
        n = len(set1.intersection(set2))
        #return float(n / float(len(set2)))
        return float(n / float(len(set1)+len(set2)-n))
        
    #----------------------------------------------------------------
    def sampleSimilarity(self):
        
        user = set(['indian', 'traditional', 'dosa'])
        
        sample1 = set(['indian', 'chaat', 'samosa'])
        sample2 = set(['indian', 'traditional', 'rice'])
        sample3 = set(['indian', 'traditional', 'dosa'])
        sample4 = set(['american', 'fastfood', 'buffalo chicken'])
        sample5 = set(['american', 'samosa'])
        
        samples = [sample1, sample2, sample3, sample4, sample5]
        for xet in samples:
            print self.computeJaccardIndex(user, xet)
    #----------------------------------------------------------------
        
    def findMostSimilarRestaurants(self, zipcode, preference):
        
        rest = Restaurants()
        longlat = rest.getLatLongFromZipCode(zipcode)
        
        #This means that no restaurant exists in the vicinity of that zipcode
        if longlat == None:
            return None
        
        #distance is miles/3959 = radians
        vicinityList = rest.getRestaurantsInVicinity(longlat, 0.03)
        print "Number of records retrieved in the vicinity are: ", len(vicinityList)
        
        similarityList = []
        
        for l in vicinityList:
            categories = l['categories']
            simIndex = self.computeJaccardIndex(set(categories), set(preference))
            record = (l, simIndex)
            if simIndex > 0:
                similarityList.append(tuple(record))
            
        #Sort the list in decreasing order of similarity
        similarityList = sorted(similarityList, key=itemgetter(1), reverse=True)
        
        print "Number of similar restaurants found: ", len(similarityList)
        return similarityList
    
    
    def isRecommended(self, zipcode, preference):
        similarityList = self.findMostSimilarRestaurants(zipcode, preference)
        
        if similarityList == None:
            print "No restaurants exist in the vicinity"
            return True
        
        if len(similarityList)==0:
            print "No restaurants found that were similar to one that you propose"
            return True
            
        for l in similarityList:
            rating = l[0]['stars']
            simIndex = l[1]
            if  (rating >= 3.5) and (simIndex>=0.5):
                print "We found a high rated restaurant which is very similar to to your preference..."
                print "User Preference: ", preference
                print "Categories: ", json.dumps(l[0]['categories'])
                print "Similarity: ", simIndex*100, "%"
                print "Rating: ", rating, " stars"
                return False
        
        print "No similar restaurant found which had a rating in that region"    
        return True
            
        


# list = RecoEngine().findMostSimilarRestaurants('85057', set(['Fast Food', 'Sandwiches']))
# for i in range(0, 4):
#      print list[i]


# print RecoEngine().isRecommended('85054', ['Sandwiches', 'Fast Food', 'Amercian'])
# print "------------------------------------"
# print RecoEngine().isRecommended('85048', ['Indian', 'Buffets', 'Paratha'])
    
            
    
