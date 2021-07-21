import json, boto3


def test_s3_connection():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    status = s3_client.get_object(
        Bucket=bucket_name,
        Key = 'Talent/10383.json'
    )['ResponseMetadata']['HTTPStatusCode']
    
    assert status == 200
