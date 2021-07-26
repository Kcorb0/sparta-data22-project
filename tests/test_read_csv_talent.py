import boto3
import pandas as pd

# Test to read all CSV files within Talent.


def test_read_csv():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    talent_file = s3_client.get_object(
        Bucket=bucket_name,
        Key='Talent/April2019Applicants.csv'
    )['Body']

    convert_to_csv = pd.read_csv(talent_file)

    print(type(convert_to_csv))
