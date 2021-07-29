import pymongo
from app.credentials.mongodb_env_variables import *
from app.logging.load_logger import *

# Function to create a database within MongoDB.
def create_database():
    grab_credentials()
    mongo_user = os.getenv('MONGODB_USER')
    mongo_pass = os.getenv('MONGODB_PASS')
    client = pymongo.MongoClient(
        f'mongodb+srv://{mongo_user}:{mongo_pass}@cluster0.wiayx.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE'
    )
    sparta_db = client["sparta_global"]
    logger.info('The sparta global database within MongoDB has been created.')
    return sparta_db

db = create_database()