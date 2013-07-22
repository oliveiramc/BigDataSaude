# /Library/Python/2.7/site-packages/pymongo-2.5.1_-py2.7-macosx-10.7-intel.egg
#MONGOHQ_URL='mongodb://<user>:<password>@dharma.mongohq.com:10085/superheroes'



from pymongo import MongoClient
import datetime
import os
import pymongo

# Grab our connection information from the MONGOHQ_URL environment variable
# (mongodb://linus.mongohq.com:10045 -u username -pmy_password)
MONGO_URL = os.environ.get('MONGOHQ_URL')

##print os.environ.get('MONGOHQ_URL')

#connection = Connection(MONGO_URL)
#client = MongoClient(MONGO_URL)
 
client = MongoClient("mongodb://marcelo:marcelo@dharma.mongohq.com:10085/superheroes") 
 
# Specify the database
db = client.superheroes
# Print a list of collections
print db.collection_names()
 
# Specify the collection, in this case 'monsters'
collection = db.alterEgos
 
# Get a count of the documents in this collection
count = collection.count()
print "The number of documents you have in this collection is:", count
 
