import json
import datetime
from bson import ObjectId
import pymongo
import os

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
if __name__ == '__main__':
    client = pymongo.MongoClient("localhost", 27017, maxPoolSize=50)
    d = dict((db, [collection for collection in client[db].list_collection_names()])
             for db in client.list_database_names())
    print (json.dumps(d))
    for item in ['subject-areas','product-management']:
        os.mkdir(item)
        for colection in d[item]:
            print (">>>>>>>",colection)
            database = client['product-management']
            col = getattr(database,colection) #Here colection is my collection
            print(col)
            array = list(col.find())
            # make db folder
            print(json.dumps(array, default=str))
            dbName =str(item)
            with open('% s/% s.json' % (dbName,colection), 'w') as f:
                f.write(json.dumps(array, default=str))
                print('DONE!!!!!!!!!!')
