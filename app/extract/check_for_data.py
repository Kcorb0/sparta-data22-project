from app.extract.s3_client import *


def list_bucket(prefix):
    # List objects in a bucket given a path, returns each key in a list

    objects = s3_client.list_objects(
        Bucket=bucket_name,
        Prefix=prefix
    )['Contents']

    return [i['Key'] for i in objects]


def list_talent(prefix):
    # Creates a list of the talent key names

    key_list = []
    cnt = 10

    # While the s3 lookup does not throw a KeyError loop through every 1000 files
    while True:
        try:
            dir_prefix = f'{prefix}{str(cnt)}'
            key_list.append(list_bucket(dir_prefix))
        except KeyError:
            break
        cnt += 1

    # Combining the list of every 1000 files
    combined_list = []
    [combined_list.extend(i) for i in key_list]

    return combined_list


def list_applicants():
    # Creates a list of applicants from s3 for each month

    key_list = []
    months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

    for month in months:
        files = s3_client.list_objects(Bucket=bucket_name, Prefix=f'Talent/{month}')['Contents']
        key_list.append(files[0]['Key'])

    return key_list


def files_difference(list1, list2):
    # Get the difference between the two provided lists
    return len(list1) - len(list2)


def check_new_data():
    # Check if new data has been added to the original s3 bucket
    # Get all lists for each collection of files from the
    # main bucket and the clean bucket

    # Get the difference for each collection of buckets
    applicant = files_difference(list_applicants(), list_bucket('Cleaned/Applicants/'))
    academy = files_difference(list_bucket('Academy/'), list_bucket('Cleaned/Academy/'))
    talent = files_difference(list_talent('Talent/'), list_talent('Cleaned/Json/'))
    spartaday = files_difference(list_bucket('Talent/Sparta'), list_bucket('Cleaned/Sparta_day/'))

    # Check if any of the collections have a difference greater than 0
    # If so then return false otherwise true
    if applicant > 0 or academy > 0 or talent > 0 or spartaday > 0:
        print('Adding newly added files.')
        return False
    else:
        print('Datastore is up to date.')
        return True
