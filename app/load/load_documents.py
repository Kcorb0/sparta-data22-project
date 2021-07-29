from app.load.list_talent_json_filenames import get_talent_jsons
from app.load.read_json import read_json
from app.load.mongo_load_document import mongo_load_document
from app.load.list_academy_csv_filenames import get_academy_csvs
from app.load.list_spartaday_csv_filenames import get_spartaday_csvs
from app.load.list_applicants_csv_filenames import get_applicants_csvs
from app.logging.load_logger import *


def load_documents(file_list, file_type, collection):
    # Loads the provided list of json documents to the MongoDB server

    if file_type == 'json':
        # If file
        for i in file_list:
            try:
                mongo_load_document(read_json(i), collection)
            except:
                logger.error('Error trying to load talent files into MongoDB. ')

    elif file_type == 'csv':
        for i in file_list:
            try:
                mongo_load_document(i, collection)
            except:
                logger.error('Error trying to load all files other than talent files to MongoDB.')
    else:
        print('Need valid file type.')

    print('Loading to datastore finished.')

    # for student in get_academy_csvs():


# Loop through applicants and embed the matching names from sparta day
# Loop through applicants and embed the matching names from talent
# Loop through applicants and embed the matching names from academy
def embed_all():
    get_applicants = get_applicants_csvs()
    get_academy = get_academy_csvs()
    get_spartaday = get_spartaday_csvs()
    get_talent = get_talent_jsons()

    def embed_academy():  # 397 matches
        logger.info('Academy files are being embedded into the applicants collection.')
        for student in get_applicants:  # For each student in the application list, do the block below
            for person in get_academy:  # For each person in academy list, do block below
                # for key, values in person.items():  # loops through each dictionary in academy list
                if person['name'] == student['name'] and person['Invited_date'] == student['date']:  # If the names match
                    # in both lists (A match on name)
                    academy_details = {'academy_details': person}  # Creates a variable containing a dictionary with the
                    # person's academy details
                    student.update(academy_details)  # Inserts the person's academy details as a dictionary into the
                    # applications doc under the matching name


    def embed_talent():  # Same as previous, 3107 matches
        logger.info('Talent files are being embedded into the applicants collection.')
        for student in get_applicants:
            for person in get_talent:
                if person['name'] == student['name']:
                    student.update({'talent_details': person})


    def embed_sparta_day():  # Same as previous, 4138 count
        logger.info('Sparta Day files are being embedded into the applicants collection.')
        for student in get_applicants:
            for person in get_spartaday:
                if person['Full_name'] == student['name']:
                    student.update({'sparta_day_details': person})

    return get_applicants


def load_to_mongodb():
    logger.info('Cleaned files are being loaded to MongoDB.')
    load_documents(embed_all(), 'csv', 'embedded_applicants')
    # load_documents(get_talent_jsons(), 'json', 'talent')
    # load_documents(get_academy_csvs(), 'csv', 'academy')
    # load_documents(get_spartaday_csvs(), 'csv', 'spartaday')
    # load_documents(get_applicants_csvs(), 'csv', 'applicants')


# def load_to_mongodb():
#     logger.info('Cleaned files are being loaded to MongoDB.')
#     load_documents(get_talent_jsons(), 'json', 'talent')
#     logger.info('Talent files have been successfully loaded.')
#     load_documents(get_academy_csvs(), 'csv', 'academy')
#     logger.info('Academy files have been successfully loaded.')
#     load_documents(get_spartaday_csvs(), 'csv', 'spartaday')
#     logger.info('Sparta day files have been successfully loaded.')
#     load_documents(get_applicants_csvs(), 'csv', 'applicants')
#     logger.info('Applicant files have been successfully loaded.')
