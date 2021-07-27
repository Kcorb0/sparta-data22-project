import pymongo


# CHANGE TO .env FILE INSTEAD.
username = input("What is your MongoDB username?")
password = input("What is your MongoDB password?")


# Function to create a database within MongoDB.
def create_database():
    client = pymongo.MongoClient(
        f'mongodb+srv://{username}:{password}@cluster0.wiayx.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE'
    )
    sparta_db = client["sparta_global"]
    return sparta_db


db = create_database()
