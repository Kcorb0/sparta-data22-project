import json, boto3


def read_json(filename):

    # Create s3 client and define bucket
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    # Get file body from s3
    talent_file = s3_client.get_object(
        Bucket=bucket_name,
        Key = filename
    )['Body']

    # Decode bytes to string then load to json
    decoded_file = talent_file.read().decode('utf-8')
    convert_to_json = json.loads(decoded_file)

    return convert_to_json