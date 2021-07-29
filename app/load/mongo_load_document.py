from app.load.create_database_mongodb import db


def mongo_load_document(file):

    db.embedded_applicants_test.insert_one(file)
    
    #print('Collection does not exist.')
    #return 'Stopped'
