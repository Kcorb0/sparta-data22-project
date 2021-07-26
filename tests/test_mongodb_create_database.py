from app.mongodb_create_database import *


# this tests to see whether a database is created in MongoDB
def test_create_sparta_db():
    # success is indicated by a 'database' type
    assert type(create_sparta_db()) is pymongo.database.Database
