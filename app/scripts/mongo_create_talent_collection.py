from mongo_create_database import db


# this function creates a sparta_day collection in the sparta_global database
def create_talent_collection():
    talent = db["talent"]
    return talent