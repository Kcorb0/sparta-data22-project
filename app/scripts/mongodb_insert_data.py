from app.mongodb_create_database import *


# this function inserts a single dummy file into the newly created collection
# The database and collection only become visible in MongoDB Compass once a file has been inserted
def insert_one_file():
    db.sparta_day.insert_one({
        'name': "Myles",
        'year': 2021,
        'score': 6.4,
        'course': "Data",
        'address': {
            'houseNumber': "Flat 1",
            'street': "3 High Street",
            'city': "Tywyn"
        }})

