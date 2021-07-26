import boto3
from pprint import pprint


# Function to count all csv files from s3 Academy folder.


def count_all_csv_files_academy():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    txt_files = s3_client.list_objects(
        Bucket=bucket_name,
        Prefix='Academy/'
    )
    academy_files_count = len(txt_files['Contents'])
    pprint(academy_files_count)


count_all_csv_files_academy()
