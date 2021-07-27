from app.load.create_database_mongodb import *


# These functions create collections called in the 'sparta_global' database in MongoDB
def create_academy_collection():
    academy = db['academy']
    print('academy collection has been added to sparta_db')
    return academy


def create_talent_collection():
    talent = db['talent']
    print('talent collection has been added to sparta_db')
    return talent


def create_sparta_day_collection():
    sparta_day = db['sparta_day']
    print('sparta_day collection has been added to sparta_db')
    return sparta_day


def create_applicants_collection():
    applicants = db['applicants']
    print('applicants collection has been added to sparta_db')
    return applicants
