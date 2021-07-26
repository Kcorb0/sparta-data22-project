import boto3
from pprint import pprint


# Function to count all csv files from s3 Talent folder.


def count_all_csv_files_talent():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    csv_files = s3_client.list_objects(
        Bucket=bucket_name,
        Prefix='Talent/ .csv'
    )
    talent_files_count = len(csv_files)
    talent_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Talent/ .csv')
    pprint(talent_files_count)
    pprint(talent_file)


count_all_csv_files_talent()
