from app.mongodb_create_collection import *


# this tests to see whether a sparta_day collection is created in MongoDB
def test_create_sparta_day_collection():
    # success is indicated by the 'collection' type
    assert type(create_sparta_day_collection()) is pymongo.collection.Collection
