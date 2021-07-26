import pymongo

# Test to check the MongoDB connection.


def test_mongodb_connection():
    # Make sure mongodb database is running on server and can be accessed using pymongo.
    client = pymongo.MongoClient()

    assert client.HOST == "localhost"
    assert client.PORT == 27017

    print(client.HOST)

# We are now using a cluster so we need to amend the test from local host to a server.
