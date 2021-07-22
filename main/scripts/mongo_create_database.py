import pymongo


def create_database():
    # Create client for the mongo azure cluster
    client = pymongo.MongoClient('mongodb+srv://Josh:Z3lncxr8MkP8YKF4@cluster0.wiayx.mongodb.net/test')
    # Create sparta global database
    sparta_db = client["sparta_global"]
    
    return sparta_db

db = create_database()
