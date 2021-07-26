import boto3
from pprint import pprint

# Test to get all CSV files within Talent.


def test_get_all_files():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    talent_file = s3_client.list_objects(Bucket=bucket_name, Prefix='Talent/')['Contents']

    pprint(talent_file)


test_get_all_files()
