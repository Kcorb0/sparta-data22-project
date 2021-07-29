from app.extract.s3_client import *
from app.transform.clean_academy_csv import clean_academy_csv
from app.transform.clean_talent_json import clean_json_file
from app.transform.clean_spartaday_txt import clean_txt_file
from app.transform.clean_applicants_csv import clean_applicants_csv_file
from app.logging.clean_logger import *
from tqdm import tqdm


def list_bucket(prefix):
    # List objects in a bucket given a path, returns each key in a list

    objects = s3_client.list_objects(
        Bucket=bucket_name,
        Prefix=prefix
    )['Contents']

    return [i['Key'] for i in objects]


def create_file_list(prefix):
    key_list = []

    if prefix == 'Talent/':
        jsons_list = []
        # Count that resembles 1000 jsons
        cnt = 10
        while True:
            # Try except that breaks if there is no contents to be found with the given prefix
            try:
                # List all keys within the talent folder and append to jsons_list
                dir_prefix = f'Talent/{str(cnt)}'
                jsons_list.append(list_bucket(dir_prefix))
            except:
                break
            cnt += 1
        [key_list.extend(i) for i in jsons_list]

    elif prefix == 'Talent/Applicants':
        months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        for month in months:
            files = s3_client.list_objects(Bucket=bucket_name, Prefix=f'Talent/{month}')['Contents']
            key_list.append(files[0]['Key'])
    else:
        key_list = list_bucket(prefix)

    return key_list


def clean_academy():
    logger.info("Started to clean the academy files.")
    print('Cleaning academy files.')
    for i in tqdm(create_file_list('Academy/')):
        path = bucket_name + '/' + i
        try:
            clean_academy_csv(path)
        except:
            logger.error('Error whilst trying to clean the academy csv files.')
            break
    print(f'Academy cleaning successful.')
    logger.info('Cleaning of academy files complete.')


def clean_talent():
    logger.info('Started to clean the talent files.')
    print('Cleaning talent files.')
    for i in tqdm(create_file_list('Talent/')):
        path = bucket_name + '/' + i
        try:
            clean_json_file(path)
        except:
            logger.error('Error trying to clean the talent json files.')
            break
    print(f'Talent cleaning successful.')
    logger.info('Cleaning of talent files complete.')


def clean_spartaday():
    logger.info('Started to clean the sparta day files.')
    print('Cleaning spartaday files.')
    for i in tqdm(create_file_list('Talent/Sparta')):
        path = bucket_name + '/' + i
        try:
            clean_txt_file(path)
        except:
            logger.error('Error trying to clean the sparta day csv files.')
            break
    print(f'Spartaday cleaning successful.')
    logger.info('Cleaning of sparta day files complete.')


def clean_applicants():
    logger.info('Started to clean the applicants files.')
    print('Cleaning applicants files.')
    for i in tqdm(create_file_list('Talent/Applicants')):
        path = bucket_name + '/' + i
        try:
            clean_applicants_csv_file(path)
        except:
            logger.error('Error trying to clean the applicants csv files.')
    print(f'Applicants cleaning successful.')
    logger.info('Cleaning of applicants files complete.')


def clean_bucket():
    logger.info('The cleaning of the original files has started.')
    print('cleaning_started')
    clean_academy()
    clean_talent()
    clean_spartaday()
    clean_applicants()
    logger.info('All cleaning has been successfully completed.')