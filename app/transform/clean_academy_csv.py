from app.extract.s3_client import *
import pandas as pd
from io import StringIO


def clean_academy_csv(file_path):
    # Takes the file path and gets just the file name
    file_name = file_path.replace('data22-final-project/Academy/', '')
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
    s3_resource.Object(bucket_name, 'Cleaned/Academy/Cleaned_'+file_name).put(Body=csv_buffer.getvalue())
