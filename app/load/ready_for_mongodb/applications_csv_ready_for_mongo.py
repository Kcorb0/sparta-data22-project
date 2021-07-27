from app.load.convert_csv_to_dict import *
from app.extract.s3_client import *


# Function that extracts the files from the applications folder within the s3 bucket
def get_all_applications_filepath():
    # Looks for the files whose filepath starts with 'Applications/' - gets all files in applications folder
    # and its contents
    applications_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Talent/Applications/')['Contents']
    # Lists the path, by referencing the 'Key', for each file in the applications folder
    all_applications_filepath = [i['Key'] for i in applications_file]
    return all_applications_filepath


# Function which allows us to iterate through each file in the applications folder
def loop_through_applications_filepath():
    list_all_applications_content = []
    # Uses the list from get_all_applications_filepath function
    for file in get_all_applications_filepath():
        # Iterates through list to get the path for each file and use it for get_applications_objects function
        file_to_use = get_csv_objects(file)
        # Iterates through list of dictionaries for each file and appends to list_all_applications_content
        for each_dict in file_to_use:
            list_all_applications_content.append(each_dict)
    return list_all_applications_content
