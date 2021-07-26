# -*- coding: utf-8 -*-

import boto3
import json
from clean_json import (json_clean_date,json_string_clean_date,
json_clean_int, json_clean_bool)



# Takes the 
def clean_json_file(file_path):
    # Takes the file path and gets just the file name
    file_name = file_path.replace('data22-final-project/Talent/', '')
    # Gets the file from s3
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'
    key = 'Talent/' + file_name
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
    # Reads the txt_file
    json_file = json.loads(s3_object['Body'].read())


    # Performs cleaning
    json_clean_date(json_file)
    json_string_clean_date(json_file)
    json_clean_int(json_file)
    json_clean_bool(json_file)
   
    
    # Uploads the file to s3
    s3_resource = boto3.resource('s3')
    
    s3_resource.Object(bucket_name, 'Cleaned/Talent/Json/'+file_name).put(
    Body=(bytes(json.dumps(json_file).encode('UTF-8')))
    )

clean_json_file("data22-final-project/Talent/10384.json")
