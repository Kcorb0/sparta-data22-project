from app.load.create_database_mongodb import db


def mongo_load_document(file):
    db.applicants.insert_one(file)
