import json, boto3


def test_read_json():

    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    talent_file = s3_client.get_object(
        Bucket=bucket_name,
        Key = 'Talent/10383.json'
    )['Body']

    decoded_file = talent_file.read().decode('utf-8')

    convert_to_json = json.loads(decoded_file)

    assert type(convert_to_json) is dict