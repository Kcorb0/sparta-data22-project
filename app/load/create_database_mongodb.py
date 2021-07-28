import pymongo
from app.credentials.mongodb_env_variables import mongo_user, mongo_pass


# Function to create a database within MongoDB.
def create_database():
    client = pymongo.MongoClient(
        f'mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.wiayx.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE'
    )
    sparta_db = client["sparta_global"]
    return sparta_db


db = create_database()
