from main.create_academy_collection import *

# test to see if a collection has been created
def test_create_sparta_academy_collection():
    assert type(create_sparta_academy_collection()) == pymongo.collection.Collection
