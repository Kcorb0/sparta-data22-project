import pandas as pd
import json
from app.extract.s3_client import *


def get_all_academy_filepath():
    # Function that extracts the files from the academy folder within the s3 bucket
    
    # Looks for all the files whose filepath starts with 'Academy/' - gets all files in academy folder and its contents
    academy_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Cleaned/Academy/')['Contents']

    # Lists the path, by referencing the 'Key', for each file in the academy folder
    all_academy_filepath = [i['Key'] for i in academy_file]

    return all_academy_filepath


def get_academies_objects(file_name):
    # Function to put all the contents of a single csv file into a dictionary

    # Gets each file as an actual object - can see its contents
    single_academy_file = s3_client.get_object(
        Bucket=bucket_name,
        Key=file_name
    )['Body']
    # Puts the contents of the file into a csv format using pandas
    reading_file = pd.read_csv(single_academy_file)
    # Converts into a json file, formatted using replace and split
    academy_json_file = reading_file.to_json(orient='records')[1:-1].replace('},{', '}-{').split('-')
    academy_list = []
    # For each row in the academy file, it uploads it into the above list as a KVP
    for i in academy_json_file:
        academy_list.append(json.loads(i))
    return academy_list


def get_academy_csvs():
    # Function which allows us to iterate through each file in the academy folder

    list_all_academy_content = []
    # Uses the list from get_all_academy_filepath function
    for i in get_all_academy_filepath():
        # Iterates through said list to get the path for each file and use it for get_academies_objects function
        list_all_academy_content.append(get_academies_objects(i))
    
    combined_list = []
    [combined_list.extend(i) for i in list_all_academy_content]

    return combined_list
