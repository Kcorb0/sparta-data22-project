from app.load.convert_csv_to_dict import *
from app.logging.extract_logger import *


# Function that extracts the files from the applicants folder within the s3 bucket
def get_all_applicants_filepath():
    logger.info('Extracting applicants files from s3 bucket.')
    # Looks for all the files whose filepath starts with 'applicants/', gets content of all files in applicants folder
    applicants_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Applicants/')['Contents']
    # Lists the path, by referencing the 'Key', for each file in the applicants folder
    all_applicants_filepath = [i['Key'] for i in applicants_file]
    return all_applicants_filepath


# Function which allows us to iterate through each file in the applicants folder
def get_applicants_csvs():
    list_all_applicants_content = []
    # Uses the list from get_all_applicants_filepath function
    for file in get_all_applicants_filepath():
        # Iterates through list to get the path for each file and use it for get_academies_objects function
        try:
            file_to_use = get_csv_objects(file)
        except:
            logger.error('Error whilst trying to convert applicants csv to a dict.')
            break
        # Iterates through list of dictionaries for each file and appends to list_all_applicants_content
        for each_dict in file_to_use:
            try:
                list_all_applicants_content.append(each_dict)
            except:
                logger.error('Error whilst trying to add each element of each applicants dict to a list.')
    logger.info('Academy csv files converted to json and ready to load into MongoDB.')
    return list_all_applicants_content
