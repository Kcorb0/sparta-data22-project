import boto3
from pprint import pprint


# this function extracts all the .txt files from the s3 bucket
def txt_list_all_file_names():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    txt_files = s3_client.list_objects(
        Bucket=bucket_name,
        # all of the .txt files begin with 'Sparta Day', which is used to extract them all
        Prefix='Talent/Sparta Day'
    )['Contents']
    # this adds all of the names of the files to the 'txt_files' list
    txt_list = [i['Key'] for i in txt_files]
    return txt_list




