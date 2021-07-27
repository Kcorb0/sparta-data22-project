from app.load.mongodb_create_collections import db


def mongo_load_document(file, collection):

    if collection == 'talent':
        # Insert file
        db.talent.insert_one(file)
        # Confirm file is loaded
        name = file['name']
        print(f'{name} has been inserted.')
    elif collection == 'academy':
        db.academy.insert_one(file)
    elif collection == 'spartaday':
        db.spartaday.insert_one(file)
    elif collection == 'applicants':
        db.applicants.insert_one(file)
    else:
        print('Collection does not exist.')
        return 'Stopped'
