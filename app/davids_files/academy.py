import boto3
from pprint import pprint
import json

s3_client = boto3.client('s3')

bucket_list = s3_client.list_buckets()
# pprint(bucket_list, sort_dicts=False)

bucket_name = 'data22-final-project'
bucket_contents = s3_client.list_objects_v2(
    Bucket=bucket_name,
    Prefix='Academy'
)
# pprint(bucket_contents)


s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(bucket_name)
# print(bucket)

objects = bucket.objects
# print(objects)

contents = objects.all()
# print(contents)

# Want to actually access the data
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Academy/Business_20_2019-02-11.csv'
)
# pprint(s3_object, sort_dicts=False)


# Work our how to load Academy/Business_20_2019-02-11.csv into a usable form
import pandas as pd
pd.set_option('display.max_columns', None)

s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Academy/Business_20_2019-02-11.csv'
)

# print(s3_object['Body'])

testdata = pd.read_csv(s3_object['Body'])
print(s3_object)

import pymongo
from pprint import pprint

client = pymongo.MongoClient("mongodb://18.185.56.206:27017")
db = client[""]
