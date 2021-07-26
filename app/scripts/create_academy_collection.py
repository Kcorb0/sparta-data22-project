from create_database_mongodb import *


# this function creates a collection called 'sparta_day' in the 'sparta_global' database in MongoDB
def create_academy_collection():
    academy = db['Academy']
    # this print statement shows when the collection has been created
    print('Academy collection has been added to sparta_db')
    # print(type(sparta_day))
    return academy


create_academy_collection()
