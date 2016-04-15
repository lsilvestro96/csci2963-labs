from pymongo import MongoClient
from bson.objectid import ObjectId

#Set up client and database
client = MongoClient()
db = client.csci2963
collection = db.definitions

#Print all records in collection
print "All records: "
for x in collection.find():
	print x

#Print only one record in collection
print "\n"
print "One record: " 
print collection.find_one()

#Print entry for the word git
print "\n"
print "Entry for word git:"
print collection.find_one({"word": "git"})

#Print entry for object with id 56fe9e22bad6b23cde07b8ce
print "\n"
print "Entry for object ObjectId(\"56fe9e22bad6b23cde07b8ce\"):"
print collection.find_one({"_id": ObjectId('56fe9e22bad6b23cde07b8ce')})

#Insert new document into database and print the new entry
print "\n"
print "Insert new document into database"
post = {"word":"happy","definition":"adj. An emotion somebody experiences when they are elated"}
collection.insert_one(post) 
print collection.find_one({"word":"happy"})

collection.insert

