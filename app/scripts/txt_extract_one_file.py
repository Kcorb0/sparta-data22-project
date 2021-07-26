import boto3


# this function extracts one .txt file from the s3 bucket
def txt_extract_one_file():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    status = s3_client.get_object(
        Bucket=bucket_name,
        Key='Talent/Sparta Day 1 August 2019.txt'
    )['ResponseMetadata']['HTTPStatusCode']
    # this returns whether or not the .txt file was successfully extracted
    return status



