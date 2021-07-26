import boto3
from pprint import pprint
import json

s3_client = boto3.client('s3')

bucket_list = s3_client.list_buckets()
# pprint(bucket_list, sort_dicts=False)

bucket_name = 'data22-final-project'

# Want to actually access the data
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Talent/April2019Applicants.csv'
)
# pprint(s3_object, sort_dicts=False)


# Work our how to load Academy/Business_20_2019-02-11.csv into a usable form
import pandas as pd
pd.set_option('display.max_columns', None)

s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Talent/April2019Applicants.csv'
)

# print(s3_object['Body'])

testdata = pd.read_csv(s3_object['Body'])
print(testdata)
