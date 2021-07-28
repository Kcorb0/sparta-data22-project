from app.extract.s3_client import *


# Function that creats a 2d array of json files by every 1000
def get_talent_jsons():

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

    combined_list = []
    [combined_list.extend(i) for i in jsons_list]
    
    return combined_list
