from app.load.mongo_load_document import mongo_load_document
from app.load.read_json import read_json
from app.load.list_talent_json_filenames import get_talent_jsons
from app.load.list_academy_csv_filenames import get_academy_csvs
from app.load.list_spartaday_csv_filenames import get_spartaday_csvs
from app.load.list_applicants_csv_filenames import get_applicants_csvs
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('loading.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


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
    logger.info('Cleaned files are being loaded to MongoDB')
    load_documents(get_talent_jsons(), 'json', 'talent')
    logger.info('Talent files have been successfully loaded.')
    load_documents(get_academy_csvs(), 'csv', 'academy')
    logger.info('Academy files have been successfully loaded.')
    load_documents(get_spartaday_csvs(), 'csv', 'spartaday')
    logger.info('Sparta day files have been successfully loaded.')
    load_documents(get_applicants_csvs(), 'csv', 'applicants')
    logger.info('Applicant files have been successfully loaded.')
