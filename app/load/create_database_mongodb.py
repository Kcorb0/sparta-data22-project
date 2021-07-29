import pymongo
from app.credentials.mongodb_env_variables import mongo_user, mongo_pass
from app.logging.load_logger import *


# Function to create a database within MongoDB.
def create_database():
    client = pymongo.MongoClient(
        f'mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.wiayx.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE'
    )
    sparta_db = client["sparta_global"]
    logger.info('The sparta global database within MongoDB has been created.')
    return sparta_db


db = create_database()
