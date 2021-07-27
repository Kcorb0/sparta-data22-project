import boto3
from app.config_manager import AWS_BUCKET_NAME


bucket_name = AWS_BUCKET_NAME
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
