import boto3
import pandas as pd


# this function reads the cleaned .txt file from s3, which has been converted to a .csv
def txt_to_csv_cleaned_df():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    text_file = s3_client.get_object(
        Bucket=bucket_name,
        # this is the file path for the newly cleaned .txt file (which is now a .csv file)
        Key='Cleaned/Talent/Sparta_day/Sparta Day 1 October 2019.csv'
    )['Body']
    # this converts the csv to a dataframe for easy visualisation
    df = pd.read_csv(text_file)
    return df


