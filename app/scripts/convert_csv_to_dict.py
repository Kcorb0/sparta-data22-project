import boto3
import pandas as pd
import json


# Function to put all the contents of a single csv file into a dictionary
def get_csv_objects(file_name):
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'
    # Gets each file as an actual object - can see its contents
    single_csv_file = s3_client.get_object(
        Bucket=bucket_name,
        Key=file_name
    )['Body']
    # Puts the contents of the file into a csv format using pandas
    reading_file = pd.read_csv(single_csv_file)
    # Converts into a dictionary
    csv_json_file = reading_file.to_json(orient='records')
    csv_list = json.loads(csv_json_file)
    return csv_list