from create_database_mongodb import *


# this function creates a collection called 'sparta_day' in the 'sparta_global' database in MongoDB
def create_talent_collection():
    talent = db['Talent']
    # this print statement shows when the collection has been created
    print('Talent collection has been added to sparta_db')
    # print(type(sparta_day))
    return talent


create_talent_collection()
