import pymongo


# CHANGE TO CONFIG FILE
username = input("What is your MongoDB username?")
password = input("What is your MongoDB password?")


# Function to create a database within MongoDB.
def create_database():
    client = pymongo.MongoClient(f'mongodb+srv://{username}:{password}@cluster0.wiayx.mongodb.net/test')
    sparta_db = client["sparta_global"]
    return sparta_db


db = create_database()
