from list_talent_json_filenames import get_talent_jsons
from read_json import read_json
from load_documents import *
from mongo_load_document import mongo_load_document
from list_academy_csv_filenames import get_academy_csvs


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

load_documents(get_talent_jsons(), 'json', 'talent')
load_documents(get_academy_csvs(), 'csv', 'academy')
