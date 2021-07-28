import json
import ujson
from app.extract.s3_client import *


def read_json(filename):
    # Get file body from s3
    talent_file = s3_client.get_object(
        Bucket=bucket_name,
        Key=filename
    )['Body'].read().decode('utf-8')

    # Decode bytes to string then load to json
    # Using ultra json to speed up the process a little
    reading_file = ujson.loads(talent_file)
    print('converted to json')

    return reading_file