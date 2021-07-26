import boto3


# this function extracts all the .txt files from the s3 bucket
def txt_extract_all_files():
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'
    txt_files = s3_client.list_objects(
        Bucket=bucket_name,
        # all of the .txt files begin with 'Sparta Day', which is used to extract them all
        Prefix='Talent/Sparta Day'
    )
    # this returns the amount of .txt files extracted from the s3 bucket
    txt_files_count = len(txt_files['Contents'])
    return txt_files_count



