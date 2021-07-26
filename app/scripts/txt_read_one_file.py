import boto3


# this function pulls a .txt file from s3, converts it from binary, and reads it
def txt_read_one_file():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    text_file = s3_client.get_object(
        Bucket=bucket_name,
        Key='Talent/Sparta Day 1 August 2019.txt'
    )['Body']
    # this decodes the .txt file from binary and reads it
    decoded_text_file = text_file.read().decode('utf-8')
    return decoded_text_file



