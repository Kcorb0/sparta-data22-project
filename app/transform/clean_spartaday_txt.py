import pandas as pd
from app.extract.s3_client import *
import calendar
from io import StringIO


# Obtains date as a string in the correct format YYYY/MM/DD
def get_date(txt_file):
    date = txt_file.split('\n')[0].split(' ', 1)[1]
    list_of_date_elements = date.split(' ')
    list_of_date_elements[2] = list_of_date_elements[2][:4]
    if len(list_of_date_elements[0]) != 2:
        list_of_date_elements[0] = '0' + list_of_date_elements[0]
    dict_of_months = {month: index for index, month in enumerate(calendar.month_name) if month}
    list_of_date_elements = [dict_of_months.get(item, item) for item in list_of_date_elements]
    correct_date_format = str(list_of_date_elements[2]) + '-' + str(list_of_date_elements[1]) + '-' + str(
        list_of_date_elements[0])
    return correct_date_format


# Obtains academy location as a string
def get_academy_location(txt_file):
    academy_location = txt_file.split('\n')[1].split(' ', 1)[0]
    return academy_location


# This function uses string manipulation to return a list of full names from the text file
def get_list_of_names(txt_file):
    txt_list = txt_file.split('\n')  # returns a list with each element being a new line from the txt file
    txt_list.remove('')  # removes empty strings from the list
    name_list = [txt.split(' -  ', 1)[0] for txt in txt_list]
    name_list.remove('\r')
    name_list.remove(name_list[0])
    name_list.remove(name_list[0])
    return name_list


# Obtains a list of first names from the list of full names
def get_list_of_first_names(name_list):
    first_names = [name.split(' ', 1)[0] for name in name_list]
    for name in range(len(first_names)):
        first_names[name] = first_names[name].capitalize()
    return first_names


# Obtains a list of last names from the list of full names
def get_list_of_last_names(name_list):
    last_names = [name.split(' ', 1)[1] for name in name_list]
    for name in range(len(last_names)):
        last_names[name] = last_names[name].capitalize()
    return last_names


# Obtains a list of pyschometric scores of the applicants
def get_list_of_psychometric_scores(txt_file):
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


# Obtains a list of presentation scores of the applicants
def get_list_of_presentation_scores(txt_file):
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


def create_df(first_name_list, last_name_list, pyschometric_score_list, presentation_score_list, academy_location,
              correct_date):
    df_scores = pd.DataFrame(
        {'First_name': first_name_list, 'Last_name': last_name_list, 'Pyschometric_score': pyschometric_score_list,
         'Presentation_score': presentation_score_list, 'Academy': academy_location, 'Date': correct_date})
    return df_scores


def clean_txt_file(file_path):
    # Takes the file path and gets just the file name
    file_name = file_path.replace('data22-final-project/Talent/', '')
    key = 'Talent/'+file_name
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
    # Reads the csv into a dataframe
    txt_file = s3_object['Body'].read().decode('utf-8')
    # Places the required data into the dataframe in a new column
    academy = get_academy_location(txt_file)
    name_list = get_list_of_names(txt_file)
    first_names = get_list_of_first_names(name_list)
    last_names = get_list_of_last_names(name_list)
    pyschometric_scores = get_list_of_psychometric_scores(txt_file)
    presentation_scores = get_list_of_presentation_scores(txt_file)
    correct_date = get_date(txt_file)
    txt_file = create_df(first_names, last_names, pyschometric_scores, presentation_scores, academy, correct_date)
    # Uploads the file to s3
    csv_buffer = StringIO()
    txt_file.to_csv(csv_buffer, index=False)
    s3_resource.Object(bucket_name, 'Cleaned/Talent/Sparta_day/'+file_name.replace('txt', 'csv'))\
        .put(Body=csv_buffer.getvalue())
