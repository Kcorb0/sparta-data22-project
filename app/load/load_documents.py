from app.load.list_talent_json_filenames import get_talent_jsons
from app.load.mongo_load_document import mongo_load_document
from app.load.list_academy_csv_filenames import get_academy_csvs
from app.load.list_spartaday_csv_filenames import get_spartaday_csvs
from app.load.list_applicants_csv_filenames import get_applicants_csvs
from app.logging.load_logger import *
from tqdm import tqdm


def load_documents(file_list):
    # Loads the provided list of json documents to the MongoDB server
    print('Loading documents to datastore.')

    for file in tqdm(file_list):
        mongo_load_document(file)

    print('Loading to datastore finished.')


def embed_all():
    # Embed data from spartaday, academy and talent in the applicants document

    get_applicants = get_applicants_csvs()
    get_academy = get_academy_csvs()
    get_spartaday = get_spartaday_csvs()
    get_talent = get_talent_jsons()

    print('Applicants, Spartaday, Academy and Talent document list creation complete.')

    logger.info('Sparta Day files are being embedded into the applicants collection.')
    for student in get_applicants:
        for person in get_spartaday:
            if person['Full_name'] == student['name']:
                student.update({'sparta_day_details': person})

    logger.info('Talent files are being embedded into the applicants collection.')
    for student in get_applicants:
        for person in get_talent:
            if person['name'] == student['name']:
                student.update({'talent_details': person})

    logger.info('Academy files are being embedded into the applicants collection.')
    for student in get_applicants:
        for person in get_academy:
            if person['name'] == student['name']:
                # in both lists (A match on name)
                student.update({'academy_details': person})

    print('All embedding to the applicants documents completed.')

    return get_applicants


def load_to_mongodb():
    logger.info('Cleaned files are being loaded to MongoDB.')
    load_documents(embed_all())
