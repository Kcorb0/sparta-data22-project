from app.mongodb_insert_data import *


# this test is to see whether a file is successfully inserted into the collection in MongoDB
def test_insert_one_file():
    # the file type should be a cursor if it is in the collection
    assert type(db.sparta_day.find()) is pymongo.cursor.Cursor
