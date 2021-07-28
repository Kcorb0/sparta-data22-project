from app.load.convert_csv_to_dict import *
from app.extract.s3_client import *


# Function that extracts the files from the academy folder within the s3 bucket
def get_all_academy_filepath():
    # Looks for all the files whose filepath starts with 'Academy/' - gets all files in academy folder and its contents
    academy_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Academy/')['Contents']
    # Lists the path, by referencing the 'Key', for each file in the academy folder
    all_academy_filepath = [i['Key'] for i in academy_file]
    return all_academy_filepath


# Function which allows us to iterate through each file in the academy folder
def loop_through_academy_filepath():
    list_all_academy_content = []
    # Uses the list from get_all_academy_filepath function
    for file in get_all_academy_filepath():
        # Iterates through list to get the path for each file and use it for get_academies_objects function
        file_to_use = get_csv_objects(file)
        # Iterates through list of dictionaries for each file and appends to list_all_academy_content
        for each_dict in file_to_use:
            list_all_academy_content.append(each_dict)
    return list_all_academy_content
