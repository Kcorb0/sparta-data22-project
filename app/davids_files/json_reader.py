import json
import datetime


def json_clean_file(file):
    # Loads the json file into a dict format
    def json_raw_read(file_path):
        with open(file_path) as raw_file:
            return (json.load(raw_file))

    # Sets the date field to either a datetime object or to null.
    def json_clean_date(json_raw_date):
        try:
            print("Converting date to datetime object...")
            return (datetime.datetime.strptime(json_raw_date, '%d/%m/%Y').date())
        except:
            print("Cannot convert date to datetime object, setting to Null...")
            return (None)

    # If the date is a a datetime object, returns the str of the date.
    def json_string_clean_date(json_clean_date):
        if json_raw_dict['date'] == None:
            return None
        else:
            return str(json_raw_dict['date'])

    # Cleans the integers.
    def json_clean_int(json_raw_int):
        try:
            print("Converted score to integer...")
            return int(json_raw_int)
        except:
            print("Cannot convert score to integer; setting to Null...")
            return None

    # Cleans the booleans.
    def json_clean_bool(field):

        if json_raw_dict[field] == "Yes":
            print("Yes converted to True...")
            return True
        if json_raw_dict[field] == "No":
            print("No converted to False...")
            return False
        else:
            print("Could not convert, setting to Null...")
            return None

    # Writes the cleaned dict over the original raw dict in the JSON file.
    def json_write_clean_dict(file_path, clean_dict):

        raw_file = open(file_path, "w")
        print("File opened successfully...")
        json.dump(clean_dict, raw_file)
        print("Cleaned Data offloaded to json file successfully.")
        raw_file.close()
        print("File closed successfully...")

    # Executes all the above functions in the correct order to clean the file.
    json_raw_dict = json_raw_read(file)
    json_clean_dict = json_raw_dict

    json_raw_dict['date'] = json_clean_date(json_raw_dict['date'])

    json_clean_dict['date'] = json_string_clean_date(json_raw_dict['date'])

    for key, value in json_raw_dict['tech_self_score'].items():
        json_clean_dict['tech_self_score'][key] = json_clean_int(value)

    bool_fields = ['self_development', 'geo_flex', 'financial_support_self']

    for field in bool_fields:
        json_clean_dict[field] = json_clean_bool(field)

    json_write_clean_dict(file, json_clean_dict)
