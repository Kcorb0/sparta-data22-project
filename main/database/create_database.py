import pymongo


def create_database():
    client = pymongo.MongoClient()
    sparta_db = client["sparta_global"]
    return sparta_db

db = create_database()