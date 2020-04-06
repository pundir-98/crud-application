from pymongo import MongoClient as mongoDB
import os
class database:
    def __init__(self):
    
        self.client2 = mongoDB(os.environ['host-0f-mongo2'], 27017)
        
    def getClient2(self):
        return self.client2