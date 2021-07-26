from io import StringIO
import pandas as pd
import boto3


def change_dob():  # A function that modifies the dob column from DD/MM/YYYY to YYYY/MM/DD
    for index, row in df.iterrows():  # Loops over each row in pandas DataFrame
        if type(row['dob']) != float:  # Missing values or Nan's in pandas have data type "float", the if statement
            # filters these out
            df['dob'] = df['dob'].replace(row['dob'], row['dob'][-4:] + "-" + row['dob'][3:5] + "-" + row['dob'][0:2])


def change_degree():  # A function that ensures that degree's are in the format 1st, 2nd, 2:1 and 2:2
    for index, row in df.iterrows():
        if type(row['degree']) != float:
            df['degree'] = df['degree'].replace(0, "")


def make_name_uniform():
    for index, row in df.iterrows():
        if type(row['name']) != float:
            df['name'] = df['name'].replace(row['name'], row['name'].title())


# A dictionary containing the calendar values for each month, used in split_columns() function to replace word with
# number Eg. December to 12
months = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05",
          "june": "06", "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
          "december": "12"}


def split_month_column():  # Splitting the month column (Eg. "December 2019") into two new columns 1)year 2)month
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


def combine_split_columns():  # Combining the two columns created in split_columns() (year and month) with invited date
    # column so its format is YYY-MM-DD
    combined = []  # An empty list that will contain the rows for the new combined column
    for index, row in df.iterrows():
        if type(row['month']) != float:  # Concatenating year, month and invited_date
            # and appending as an element to "combined" list
            combined.append(row['year'] + "-" + row['month'] + "-" + str(int(row['invited_date'])))
        else:
            combined.append(None)  # For missing values "None" is used
    df['Invited_date'] = combined  # Assigning a new column the values in the combined list


def remove_old_columns():  # removes columns used to merge for the invite date
    df.drop(['month', 'invited_date', 'year'], axis=1, inplace=True)


def change_phone_number(replace_character):  # a function that removes the character given as an argument from the phone number's
    df['phone_number'] = df['phone_number'].str.replace(replace_character, '')
    return df


def change_phone_number_multiple():
    remove_characters = ['-', '(', ')', ' ']
    for character in remove_characters:
        change_phone_number(character)
    return df


def send_to_s3(file):  # Sends a df created by the functions in 'application cleaning' file to s3 bucket

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_client.put_object(
        Bucket='data22-final-project',
        Key='Cleaned/Talent/Applications/' + file,
        Body=csv_buffer.getvalue()
    )


# Loading data into S3
month = ["Jan", "Feb", "March", "April", "May",
         "June", "July", "Aug", "Sept", "Oct", "Nov",
         "Dec"]
year = ["2019"]

# month = ["Jan", "Feb", "March", "April", "May",
#          "June", "July", "Aug", "Sept", "Oct", "Nov",
#          "Dec"]
# year = ["2019", "2020", "2021"]

s3_client = boto3.client('s3')

bucket_name = 'data22-final-project'
for year in year:
    for month in month:
        s3_object = s3_client.get_object(
            Bucket=bucket_name,
            Key='Talent/' + month + year + 'Applicants.csv'
            )
        pd.set_option('display.max_rows', None)
        df = pd.read_csv(s3_object['Body'])
        change_phone_number_multiple()
        change_dob()
        change_degree()
        make_name_uniform()
        split_month_column()
        combine_split_columns()
        remove_old_columns()
        send_to_s3(month + year + 'Applications.csv')
