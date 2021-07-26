import boto3
import pandas as pd

# Test to read all CSV files within Academy.


def test_read_csv():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    academy_file = s3_client.get_object(
        Bucket=bucket_name,
        Key='Academy/Business_20_2019-02-11.csv'
    )['Body']

    convert_to_csv = pd.read_csv(academy_file)

    print(type(convert_to_csv))
