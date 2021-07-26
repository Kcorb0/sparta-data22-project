import pymongo


# Function to create a database within MongoDB.


def create_database():
    client = pymongo.MongoClient(mongodb+srv://<username>:<password>@cluster0.wiayx.mongodb.net/test)
    sparta_db = client["sparta_global"]
    return sparta_db


db = create_database()
print(db)
