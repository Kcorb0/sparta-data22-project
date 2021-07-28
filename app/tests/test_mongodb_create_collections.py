from app.load.mongodb_create_collections import *


# this tests to see whether an academy collection is created in MongoDB
def test_create_academy_collection():
    # success is indicated by the 'collection' type
    assert type(create_academy_collection()) is update_data_types_mongo.collection.Collection


# this tests to see whether a talent collection is created in MongoDB
def test_create_talent_collection():
    # success is indicated by the 'collection' type
    assert type(create_talent_collection()()) is update_data_types_mongo.collection.Collection


# this tests to see whether a sparta_day collection is created in MongoDB
def test_create_sparta_day_collection():
    # success is indicated by the 'collection' type
    assert type(create_sparta_day_collection()) is update_data_types_mongo.collection.Collection


# this tests to see whether a applicants collection is created in MongoDB
def test_create_applicants_collection():
    # success is indicated by the 'collection' type
    assert type(create_applicants_collection()) is update_data_types_mongo.collection.Collection
