import boto3

# Creating an s3 client.
s3_client = boto3.client('s3')
# Defining the bucket name.
bucket_name = 'data22-final-project'


def get_csvs():
    # Function that creates a 2d array of if csv files in increments of 1000.

    csvs_list = []  # List of csv names within Talent
    count = 10  # Count that resembles 1000 csvs

    while True:
        # Try accept that breaks if there is no contents to be found with the given prefix.
        try:
            # List all keys within the talent folder and append to csvs_list
            talent_file = s3_client.list_objects(Bucket=bucket_name, Prefix=f'Talent/{str(count)}')['Contents']
            csvs_list.append([i['Key'] for i in talent_file])
        except:
            break
        count += 1

    combined_list = []
    [combined_list.extend(i) for i in csvs_list]

    return combined_list


get_csvs()
