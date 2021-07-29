import boto3

# CHANGE TO CONFIG FILE.
s3_client = boto3.client('s3')
bucket_name = 'data22-final-project'

s3_resource = boto3.resource('s3')
