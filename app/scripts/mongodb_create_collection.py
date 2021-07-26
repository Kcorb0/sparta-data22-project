from app.mongodb_create_database import *


# this function creates a collection called 'sparta_day' in the 'sparta_global' database in MongoDB
def create_sparta_day_collection():
    sparta_day = db['sparta_day']
    return sparta_day



