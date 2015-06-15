from pymongo import MongoClient

# connect to database
connection = MongoClient('localhost', 27017)

db = connection.school

# handle to names collection
students = db.students1

cursor = students.find()

hws = {} # name : [{"_id": score}]
import sys
for s in cursor:
    score = sys.maxint 
    _id = s["_id"] 
    hw = s["scores"]
    for t in hw:
        if t["type"] == "homework" and score > t["score"]:
            score = t["score"]
    students.update({"_id":_id}, {"$pull":{"scores":{"type":"homework", "score":score}}})


