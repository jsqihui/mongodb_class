import bottle
import pymongo

# this is the handler for the default path of the web server 

@bottle.route('/')
def index():

    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.test
    name = db.names
    item = name.find_one()

    return '<b>Hello %s!<b>' % item['name']

bottle.run(host='localhost', port=8082)
