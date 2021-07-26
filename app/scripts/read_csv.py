import boto3
import pandas as pd

# Creating an s3 client.
s3_client = boto3.client('s3')
# Defining the bucket name.
bucket_name = 'data22-final-project'

# Creating a function to read a CSV file.


def read_csv(filename):
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    talent_file = s3_client.get_object(
        Bucket=bucket_name,
        Key=filename
    )['Body']

    decoded_file = talent_file.read().decode('utf-8')

    convert_to_json = pd.read_csv(decoded_file)

    print(type(convert_to_json))
