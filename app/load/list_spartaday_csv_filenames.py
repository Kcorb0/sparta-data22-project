from convert_csv_to_dict import *


# Function that extracts the files from the spartaday folder within the s3 bucket
def get_all_spartaday_filepath():
    # Looks for all the files whose filepath starts with 'spartaday/', gets content of all files in spartaday folder.
    spartaday_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Sparta_day/')['Contents']
    # Lists the path, by referencing the 'Key', for each file in the spartaday folder
    all_spartaday_filepath = [i['Key'] for i in spartaday_file]
    return all_spartaday_filepath


# Function which allows us to iterate through each file in the spartaday folder
def get_spartaday_csvs():
    list_all_spartaday_content = []
    # Uses the list from get_all_spartaday_filepath function
    for file in get_all_spartaday_filepath():
        # Iterates through list to get the path for each file and use it for get_academies_objects function
        file_to_use = get_csv_objects(file)
        # Iterates through list of dictionaries for each file and appends to list_all_spartaday_content
        for each_dict in file_to_use:
            list_all_spartaday_content.append(each_dict)
    return list_all_spartaday_content
