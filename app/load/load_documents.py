from list_talent_json_filenames import get_talent_jsons
from read_json import read_json
from mongo_load_document import mongo_load_document
from list_academy_csv_filenames import get_academy_csvs
from list_spartaday_csv_filenames import get_spartaday_csvs
from list_applicants_csv_filenames import get_applicants_csvs



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

    # for student in get_academy_csvs():


# Loop through applicants and embed the matching names from sparta day
# Loop through applicants and embed the matching names from talent
# Loop through applicants and embed the matching names from academy
get_applicants = get_applicants_csvs()
get_academy = get_academy_csvs()
get_spartaday = get_spartaday_csvs()
get_talent = get_talent_jsons()


def embed_academy():  # 397 matches

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
    for student in get_applicants:
        for person in get_talent:
            if person['name'] == student['name']:
                student.update({'talent_details': person})


def embed_sparta_day():  # Same as previous, 4138 count
    for student in get_applicants:
        for person in get_spartaday:
            if person['Full_name'] == student['name']:
                student.update({'sparta_day_details': person})


def load_to_mongodb():
    load_documents(get_applicants, 'csv', 'embedded_applicants')
    # load_documents(get_talent_jsons(), 'json', 'talent')
    # load_documents(get_academy_csvs(), 'csv', 'academy')
    # load_documents(get_spartaday_csvs(), 'csv', 'spartaday')
    # load_documents(get_applicants_csvs(), 'csv', 'applicants')


embed_talent()
embed_academy()
embed_sparta_day()

load_to_mongodb()
