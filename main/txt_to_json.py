import json, boto3
from pprint import pprint

# Creating an s3 client
s3_client = boto3.client('s3')
# Defining the bucket name
bucket_name = 'data22-final-project'


def txt_reading():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'
    text_file = s3_client.get_object(
        Bucket=bucket_name,
        Key='Talent/Sparta Day 1 August 2019.txt'
    )['Body']
    decoded_text_file = text_file.read().decode('utf-8')
    return decoded_text_file