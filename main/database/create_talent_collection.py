from create_database import *


# this function creates a sparta_day collection in the sparta_global database
def create_sparta_day_collection():
    sparta_day = db["sparta_day"]
    print('sparta_day collection has been created and added to sparta_db')
    return sparta_day