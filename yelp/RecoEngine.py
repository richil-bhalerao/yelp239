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

        #distance is miles/3959 = radians
        vicinityList = rest.getRestaurantsInVicinity(longlat, 0.03)

        similarityList = []

        for l in vicinityList:

            categories = set(l['categories'])
            simIndex = self.computeJaccardIndex(categories, preference)
            record = (l, simIndex)
            similarityList.append(tuple(record))

        #Sort the list in decreasing order of similarity
        similarityList = sorted(similarityList, key=itemgetter(1), reverse=True)

        return similarityList


list = RecoEngine().findMostSimilarRestaurants('85053', set(['wafaigaou', 'wafaigaou']))
for i in range(0, 4):
    print list[i]