import pymongo

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.wiayx.mongodb.net/test")
sparta_db = client["sparta_global"]


# This function creates a Sparta Applicants collection in the Sparta Global Database.


def create_sparta_applicants_collection():
    sparta_applicants = sparta_db["Sparta_Applicants"]
    print('Sparta Applicants collection has been created and added to sparta_db')
    print(type(sparta_applicants))
    return sparta_applicants


create_sparta_applicants_collection()
