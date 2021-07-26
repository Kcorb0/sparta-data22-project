from main.create_database import *

# Test to see if a database has been created
def test_create_sparta_db():
    assert type(create_sparta_db()) == pymongo.database.Database
