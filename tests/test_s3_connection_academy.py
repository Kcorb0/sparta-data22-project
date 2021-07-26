import boto3

# Test to check the s3 connection within Academy.


def test_s3_connection():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    status = s3_client.get_object(
        Bucket=bucket_name,
        Key='Academy/Business_20_2019-02-11.csv'
    )['ResponseMetadata']['HTTPStatusCode']

    assert status == 200
