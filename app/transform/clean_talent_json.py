from app.extract.s3_client import *
import json
import datetime


# Sets the date field to either a datetime object or to null.
def json_clean_date(file):
    try:
        file['date'] = (datetime.datetime.strptime(file['date'], '%d/%m/%Y').date())
    except:
        file['date'] = None


# If the date is a a datetime object, returns the str of the date.
def json_string_clean_date(file):
    if file['date'] == None:
        pass
    else:
        file['date'] = str(file['date'])


# Cleans the integers.
def json_clean_int(file):
    if 'tech_self_score' in file:
        for key, value in file['tech_self_score'].items():
            try:
                file['tech_self_score'][key] = int(value)
            except:
                file['tech_self_score'][key] = None


# Cleans the booleans.
def json_clean_bool(file):
    bool_fields = ['self_development', 'geo_flex', 'financial_support_self']

    for field in bool_fields:
        if file[field] == "Yes":
            file[field] = True
        elif file[field] == "No":
            file[field] = False
        else:
            file[field] = None


def clean_json_file(file_path):
    # Takes the file path and gets just the file name
    file_name = file_path.replace('data22-final-project/Talent/', '')
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
    s3_resource.Object(bucket_name, 'Cleaned/Json/'+file_name).put(
        Body=(bytes(json.dumps(json_file).encode('UTF-8')))
    )
