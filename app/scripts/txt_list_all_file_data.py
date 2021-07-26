from app.txt_list_all_file_names import *


# this function creates a list of all of the data within the .txt files
def txt_list_all_file_data(file_name):
    s3_client = boto3.client('s3')
    bucket_name = 'data22-final-project'

    txt_files = s3_client.get_object(
        Bucket=bucket_name,
        Key=file_name
    )['Body']
    # create an empty list
    txt_list = []
    for i in txt_files:
        # convert the body of the files from binary
        x = i.decode('utf-8')
        # append the decoded .txt file to the list
        txt_list.append(x)
    return txt_list


# this uses the list of all the file names (which represent the file paths) created in 'txt_list_all_file_names'
def loop_through_txt_list_all_file_names():
    list_all_txt_content = []
    for i in txt_list_all_file_names():
        # this inserts all the names of the files into the 'txt_list_all_file_data' function
        list_all_txt_content.append(txt_list_all_file_data(i))
    return list_all_txt_content

