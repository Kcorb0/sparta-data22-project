from app.cleaning.clean_json import *

# Logic Tree of this Cleaning Script:
#
# 1. Is it the right type/format?
#       True: Upload to new dict.
#       False: Go to step 2.
# 2. Is it convertible to the right type/format? True/False
#       True: Convert to new type and upload to new dict.
#       False: Set value to NULL and upload to new dict.
# 3. Convert new dict to json and upload to S3.

'''
User Story 48
As a developer, I need a defined output from the .json files when they are
read into pycharm, so that I can take a look at the output and determine the
next step in the pipeline.
'''

# Test: The initial json file has been made available in a dict format.

def test_json_raw_read():
    
    assert type(json_clean_file(file)) is dict


'''
User Story 50
As an analyst, imported .JSON file data needs to follow the YYYY/MM/DD date
format, so that I can transform the data uniformly.
'''

# We don't need to test the dict we import, because it has already passed
# previous tests.

# We want to test that the dates imported from the json files are all
# converted from strings to a date object in the format YYYY-MM-DD

# Test: The value returned by the json_clean_date function after being cleaned
#       is either null or a datetime object.

def test_json_clean_date():
    
    assert type(json_raw_dict['date']) is (None or datetime.date)
    
# Test: The value returned by the json_string_clean_date function is either a
#       string or a null.

def test_json_string_clean_date():                                         

    assert type(json_clean_dict['date']) is (None or str)
                                                
# Convert the 
    
'''
User Story 61
As an analyst, imported .JSON file data's numerical keys must be
integers/float/double where appropriate, so that analysis can be performed on
them.
'''
# We can assume that all techscores are integers?
# Check that the data type of the techscore values are integers

# Test: The value returned by the function json_clean_int is either a null or
#       an integer type.

def test_json_clean_int():
    for value in json_clean_dict['tech_self_score'].values():
        assert(type(value) is int)


'''
User Story 14
As an analyst, imported .JSON file data with yes/no keys must return True or
False instead, so that I can filter by boolean values.
'''

# Test: The values returned by the json_clean_bool function are either null or
#       booleans.

def test_json_clean_bool():
    assert type(json_clean_dict['self_development']) is bool
    assert type(json_clean_dict['geo_flex']) is bool
    assert type(json_clean_dict['financial_support_self']) is bool


'''
User Story 62
As a developer, imported .JSON file data must be returned as .JSON's after
cleaning, so that the pipeline code can run properly.
'''

# Check all transforms worked by checking that the changes have been written
# to the .json and it is in the correct format.
#
# We should check the following things:
# Date:               -     YYYY-mm-dd 1984-25-18
# Techscore Values:   -     Int type
# Yes/No:             -     Converted to Booleans

def test_json_clean_dict():
    assert type(json_clean_dict) is dict
