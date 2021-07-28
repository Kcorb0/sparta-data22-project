from app.extract.s3_client import *
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('extracting.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Function that creates a 2d array of json files by every 1000
def get_talent_jsons():
    logger.info('Started to put all talent files into a single list.')
    jsons_list = []  # List of json names within Talent
    cnt = 10  # Count that resembles 1000 jsons
    while True:
        # Try accept that breaks if there is no contents to be found with the given prefix
        try:
            # List all keys within the talent folder and append to jsons_list
            talent_file = s3_client.list_objects(Bucket=bucket_name, Prefix=f'Talent/{str(cnt)}')['Contents']
            jsons_list.append([i['Key'] for i in talent_file])
        except:
            logger.error('Error trying to append each talent file to a list.')
            break
        cnt += 1

    combined_list = []
    [combined_list.extend(i) for i in jsons_list]
    logger.info('All json files are in one location and ready to be uploaded to MongoDB.')
    return combined_list
