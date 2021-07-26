import pymongo


# this function creates a database called 'sparta_db' within MongoDB
def create_sparta_db():
    client = pymongo.MongoClient('localhost:27017')
    sparta_db = client['sparta_global']
    return sparta_db


# storing this function as a variable allows it to be easily called in other functions
db = create_sparta_db()
