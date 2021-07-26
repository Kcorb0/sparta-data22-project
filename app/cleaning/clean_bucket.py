import boto3
from clean_academy_csv import clean_academy_csv

# Creating an s3 client
s3_client = boto3.client('s3')
# Defining the bucket name
bucket_name = 'data22-final-project'


def create_file_list(prefix):
    
    talent_file = s3_client.list_objects(Bucket=bucket_name, Prefix=f'{prefix}')['Contents']
    key_list = [i['Key'] for i in talent_file]
    
    return key_list

def clean_academy():
    for i in create_file_list('Academy/'):
        path = bucket_name+'/'+i
        clean_academy_csv(path)


clean_academy()