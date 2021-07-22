from list_talent_json_filenames import get_jsons
from read_json import read_json
from insert_file_into_collection import *


def load_documents(file_list, file_type):
    # Loads the provided list of json documents to the MongoDB server

    if file_type == 'json':
        # If file 
        for i in file_list:
            insert_file_into_collection(read_json(i))
    elif file_type == 'csv':
        pass
    else:
        print('Need valid file type.')

    print('Loading to datastore finished.')

load_documents(get_jsons(), 'json')