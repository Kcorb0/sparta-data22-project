from io import StringIO
import pandas as pd
from app.extract.s3_client import *


def change_dob(df):  # A function that modifies the dob column from DD/MM/YYYY to YYYY/MM/DD
    for index, row in df.iterrows():  # Loops over each row in pandas DataFrame
        if type(row['dob']) != float:  # Missing values or Nan's in pandas have data type "float", the if statement
            # filters these out
            df['dob'] = df['dob'].replace(row['dob'], row['dob'][-4:] + "-" + row['dob'][3:5] + "-" + row['dob'][0:2])


def change_degree(df):  # A function that ensures that degree's are in the format 1st, 2nd, 2:1 and 2:2
    for index, row in df.iterrows():
        if type(row['degree']) != float:
            df['degree'] = df['degree'].replace(0, "")


def make_name_uniform(df):
    for index, row in df.iterrows():
        if type(row['name']) != float:
            df['name'] = df['name'].replace(row['name'], row['name'].title())


# A dictionary containing the calendar values for each month, used in split_columns() function to replace word with
# number Eg. December to 12
months = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05",
          "june": "06", "july": "07", "august": "08", "sept": "09", "october": "10", "november": "11",
          "december": "12"}


def split_month_column(df):  # Splitting the month column (Eg. "December 2019") into two new columns 1)year 2)month
    # Loop one adds the year column and loop two adds the month column
    # Loop three modifies the month values
    for index, row in df.iterrows():
        if type(row['month']) != float:
            df['year'] = df.month.str[-4:]
    for index, row in df.iterrows():
        if type(row['month']) != float:
            df['month'] = df['month'].replace(row['month'], row['month'][:-5].lower())  # Some months are capitalised so
            # .lower() is used
    for index, row in df.iterrows():
        if type(row['month']) != float:
            df['month'] = df['month'].replace(row['month'], months[row['month']])  # Replace the month name (Eg.
            # "April") with it's calendar number (Eg. "04") from the months dictionary


#  Combining the two columns created in split_columns() (year and month) with invited date
def combine_split_columns(df):
    # column so its format is YYY-MM-DD
    combined = []  # An empty list that will contain the rows for the new combined column
    for index, row in df.iterrows():
        if type(row['month']) != float:  # Concatenating year, month and invited_date
            # and appending as an element to "combined" list
            combined.append(row['year'] + "-" + row['month'] + "-" + str(int(row['invited_date'])))
        else:
            combined.append(None)  # For missing values "None" is used
    df['Invited_date'] = combined  # Assigning a new column the values in the combined list


def remove_old_columns(df):  # removes columns used to merge for the invite date
    df.drop(['month', 'invited_date', 'year'], axis=1, inplace=True)


#  A function that removes the character given as an argument from the phone number's
def change_phone_number(df, replace_character):
    df['phone_number'] = df['phone_number'].str.replace(replace_character, '')


def change_phone_number_multiple(df):
    remove_characters = ['-', '(', ')', ' ']
    for character in remove_characters:
        change_phone_number(df, character)
    df['phone_number'] = ('\"' + df['phone_number'] + '\"')


def clean_applicants_csv_file(file_path):
    # Takes the file path and gets just the file name
    file_name = file_path.replace('data22-final-project/Talent/', '')
    key = 'Talent/'+file_name
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
    # Reads the txt_file
    df = pd.read_csv(s3_object['Body'])
    # Performs cleaning
    change_phone_number_multiple(df)
    change_dob(df)
    change_degree(df)
    make_name_uniform(df)
    split_month_column(df)
    combine_split_columns(df)
    remove_old_columns(df)
    # Uploads the file to s3
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource.Object(bucket_name, 'Cleaned/Applicants/'+file_name).put(Body=csv_buffer.getvalue())
