from app.extract.s3_client import *
import pandas as pd


# Creating a function to read a CSV file.
def read_csv(filename):
    talent_file = s3_client.get_object(
        Bucket=bucket_name,
        Key=filename
    )['Body']

    decoded_file = talent_file.read().decode('utf-8')

    convert_to_json = pd.read_csv(decoded_file)

    print(type(convert_to_json))
