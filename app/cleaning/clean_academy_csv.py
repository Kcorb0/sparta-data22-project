  
import boto3
import pandas as pd
from io import StringIO


def add_start_date_and_stream_to_academy(file_path):
    # Takes the file path and gets just the file name
    file_name = file_path.replace('data22-final-project/Academy/', '')
    # Gets the file from s3
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'
    key = 'Academy/'+file_name
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
    # Gets the required information from the file name and splits it into correct variables
    stream, number, date = file_name.split('_')
    # Reads the csv into a dataframe
    academy = pd.read_csv(s3_object['Body'])
    # Places the required data into the dataframe in a new column
    academy['start_date'] = date[0:10]
    academy['stream'] = stream
    # Uploads the file to s3
    csv_buffer = StringIO()
    academy.to_csv(csv_buffer, index=False)
    s3_resource = boto3.resource('s3')
    s3_resource.Object(bucket_name, 'Cleaned/Academy/Cleaned_'+file_name).put(Body=csv_buffer.getvalue())


add_start_date_and_stream_to_academy('data22-final-project/Academy/Business_20_2019-02-11.csv')