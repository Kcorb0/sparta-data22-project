from app.load.convert_csv_to_dict import *
from app.extract.s3_client import *


# Function that extracts the files from the sparta day folder within the s3 bucket
def get_all_sparta_day_filepath():
    # Looks for the files whose filepath starts with 'Sparta-day/' - gets all files in talent folder and its contents
    sparta_day_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Talent/Sparta_day/')['Contents']
    # Lists the path, by referencing the 'Key', for each file in the applications folder
    all_sparta_day_filepath = [i['Key'] for i in sparta_day_file]
    return all_sparta_day_filepath


# Function which allows us to iterate through each file in the sparta day folder
def loop_through_sparta_day_filepath():
    list_all_sparta_day_content = []
    # Uses the list from get_all_sparta_day_filepath function
    for file in get_all_sparta_day_filepath():
        # Iterates through list to get the path for each file and use it for get_sparta_day_objects function
        file_to_use = get_csv_objects(file)
        # Iterates through list of dictionaries for each file and appends to list_all_sparta_day_content
        for each_dict in file_to_use:
            list_all_sparta_day_content.append(each_dict)
    return list_all_sparta_day_content
