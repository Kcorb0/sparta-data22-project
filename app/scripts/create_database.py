import pymongo


# this creates a database called sparta_global in MongoDB
def create_sparta_db():
    client = pymongo.MongoClient("localhost:27017")
    sparta_db = client['sparta_global']
    return sparta_db
