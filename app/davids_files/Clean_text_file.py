import pandas as pd
import boto3


def get_academy_location():  # obtains academy location as a string
    academy_location = txt_file.split('\n')[1].split(' ', 1)[0]
    return academy_location


def get_list_of_names():  # this function uses string manipulation to return a list of full names from the text file
    txt_list = txt_file.split('\n')  # returns a list with each element being a new line from the txt file
    txt_list.remove('')  # removes empty strings from the list
    name_list = [txt.split(' -  ', 1)[0] for txt in txt_list]  #
    name_list.remove('\r')
    name_list.remove(name_list[0])
    name_list.remove(name_list[0])
    return name_list


def get_list_of_first_names(name_list):  # obtains a list of first names from the list of full names
    first_names = [name.split(' ', 1)[0] for name in name_list]
    for name in range(len(first_names)):
        first_names[name] = first_names[name].capitalize()
    return first_names


def get_list_of_last_names(name_list):  # obtains a list of last names from the list of full names
    last_names = [name.split(' ', 1)[1] for name in name_list]
    for name in range(len(last_names)):
        last_names[name] = last_names[name].capitalize()
    return last_names


def get_list_of_psychometric_scores():  # obtains a list of pyschometric scores of the applicants
    txt_list = txt_file.split('\n')
    list_of_lines_split = [line.split(' -  ', 1) for line in txt_list]
    list_of_lines_split.remove(['\r'])
    list_of_lines_split.remove([''])
    list_of_lines_split.remove(list_of_lines_split[0])
    list_of_lines_split.remove(list_of_lines_split[0])
    list_of_performance = [list_of_lines_split[line][1] for line in range(0, len(list_of_lines_split))]
    pyschometrics_removed = [txt.split('Psychometrics: ', 1)[1] for txt in list_of_performance]
    list_of_pyschometric_scores = [txt.split('/', 1)[0] for txt in pyschometrics_removed]
    return list_of_pyschometric_scores


def get_list_of_presentation_scores():  # obtains a list of presentation scores of the applicants
    txt_list = txt_file.split('\n')
    list_of_lines_split = [line.split(' -  ', 1) for line in txt_list]
    list_of_lines_split.remove(['\r'])
    list_of_lines_split.remove([''])
    list_of_lines_split.remove(list_of_lines_split[0])
    list_of_lines_split.remove(list_of_lines_split[0])
    list_of_performance = [list_of_lines_split[line][1] for line in range(0, len(list_of_lines_split))]
    presentation_removed = [txt.split('Presentation: ', 1)[1] for txt in list_of_performance]
    list_of_presentation_scores = [txt.split('/', 1)[0] for txt in presentation_removed]
    return list_of_presentation_scores


def create_df(first_name_list, last_name_list, pyschometric_score_list, presentation_score_list, academy_location):
    df_scores = pd.DataFrame(
        {'First_name': first_name_list, 'Last_name': last_name_list, 'Pyschometric_score': pyschometric_score_list,
         'Presentation_score': presentation_score_list, 'Academy':academy_location})
    return df_scores


s3_client = boto3.client('s3')
bucket_list = s3_client.list_buckets()
bucket_name = 'data22-final-project'
bucket_contents = s3_client.list_objects_v2(
    Bucket=bucket_name,
    Prefix='Academy'
)

s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Talent/Sparta Day 1 October 2019.txt'
)
txt_file = s3_object['Body'].read().decode('utf-8')
