import sys
import pymongo

con = pymongo.MongoClient("mongodb://localhost")

db = con.test
users = db.users

doc = {'firstname': 'Andrew', 'lastname': 'Erlichson'}
print doc
print "about to insert the document"

try:
    users.insert_one(doc)
except Exception as e:
    print "insert failed", e

print doc
print "inserting again"

doc = {'firstname': 'Andrew', 'lastname': 'Erlichson'}
try:
    users.insert_one(doc)
except Exception as e:
    print "second insert failed", e
