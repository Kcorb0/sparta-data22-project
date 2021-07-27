from app.load.mongo_load_document import mongo_load_document
from app.load.read_json import read_json
from app.load.list_talent_json_filenames import get_talent_jsons
from app.load.list_academy_csv_filenames import get_academy_csvs
from app.load.list_spartaday_csv_filenames import get_spartaday_csvs
from app.load.list_applicants_csv_filenames import get_applicants_csvs


def load_documents(file_list, file_type, collection):
    # Loads the provided list of json documents to the MongoDB server

    if file_type == 'json':
        # If file
        for i in file_list:
            mongo_load_document(read_json(i), collection)

    elif file_type == 'csv':
        for i in file_list:
            mongo_load_document(i, collection)
    else:
        print('Need valid file type.')

    print('Loading to datastore finished.')


def load_to_mongodb():
    load_documents(get_talent_jsons(), 'json', 'talent')
    load_documents(get_academy_csvs(), 'csv', 'academy')
    load_documents(get_spartaday_csvs(), 'csv', 'spartaday')
    load_documents(get_applicants_csvs(), 'csv', 'applicants')
