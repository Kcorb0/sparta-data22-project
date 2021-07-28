from app.extract.s3_client import *
from app.transform.clean_academy_csv import clean_academy_csv
from app.transform.clean_talent_json import clean_json_file
from app.transform.clean_spartaday_txt import clean_txt_file
from app.transform.clean_applicants_csv import clean_applicants_csv_file
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('cleaning.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def create_file_list(prefix):
    key_list = []

    if prefix == 'Talent/':
        jsons_list = []  # List of json names within Talent
        cnt = 10  # Count that resembles 1000 jsons
        while True:
            # Try accept that breaks if there is no contents to be found with the given prefix
            try:
                # List all keys within the talent folder and append to jsons_list
                talent_file = s3_client.list_objects(Bucket=bucket_name, Prefix=f'Talent/{str(cnt)}')['Contents']
                jsons_list.append([i['Key'] for i in talent_file])
            except:
                break
            cnt += 1
        [key_list.extend(i) for i in jsons_list]

    elif prefix == 'Talent/Applicants':
        months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        for month in months:
            files = s3_client.list_objects(Bucket=bucket_name, Prefix=f'Talent/{month}')['Contents']
            key_list.append(files[0]['Key'])
        print(key_list)

    else:
        files = s3_client.list_objects(Bucket=bucket_name, Prefix=f'{prefix}')['Contents']
        key_list = [i['Key'] for i in files]

    return key_list


def clean_academy():
    logger.info("Started to clean the academy files")
    for i in create_file_list('Academy/'):
        path = bucket_name + '/' + i

        clean_academy_csv(path)
        print(f'{i} cleaning successful')
    logger.info('Cleaning of academy files complete')


def clean_talent():
    logger.info('Started to clean the talent files')
    for i in create_file_list('Talent/'):
        path = bucket_name + '/' + i
        clean_json_file(path)
        print(f'{i} cleaning successful')
    logger.info('Cleaning of talent files complete')

def clean_spartaday():
    logger.info('Started to clean the sparta day files')
    for i in create_file_list('Talent/Sparta'):
        path = bucket_name + '/' + i
        clean_txt_file(path)
        print(f'{i} cleaning successful')
    logger.info('Cleaning of sparta day files complete')


def clean_applicants():
    logger.info('Started to clean the applicants files')
    for i in create_file_list('Talent/Applicants'):
        path = bucket_name + '/' + i
        clean_applicants_csv_file(path)
        print(f'{i} cleaning successful')
    logger.info('Cleaning of applicants files complete')


def clean_bucket():
    logger.info('The cleaning of the original files has started')
    clean_academy()
    clean_talent()
    clean_spartaday()
    clean_applicants()
    logger.info('All cleaning has been successfully completed')
