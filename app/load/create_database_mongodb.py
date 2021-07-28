import pymongo
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('loading.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# CHANGE TO .env FILE INSTEAD.
username = input("What is your MongoDB username?")
password = input("What is your MongoDB password?")


# Function to create a database within MongoDB.
def create_database():
    client = pymongo.MongoClient(
        f'mongodb+srv://{username}:{password}@cluster0.wiayx.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE'
    )
    sparta_db = client["sparta_global"]
    logger.info('The sparta global database within MongoDB has been created.')
    return sparta_db


db = create_database()
