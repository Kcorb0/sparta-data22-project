
import datetime


# Sets the date field to either a datetime object or to null.
def json_clean_date(file):
    try:
        file['date'] = (datetime.datetime.strptime(file['date'], '%d/%m/%Y').date())
    except:
        file['date'] = None

# If the date is a a datetime object, returns the str of the date.
def json_string_clean_date(file):
    if file['date'] == None:
        pass
    else:
        file['date'] = str(file['date'])

# Cleans the integers.
def json_clean_int(file):
    
    for key, value in file['tech_self_score'].items():
        
        try:
            file['tech_self_score'][key] = int(value)
        except:
            file['tech_self_score'][key] = None


# Cleans the booleans.
def json_clean_bool(file):
    
    bool_fields = ['self_development', 'geo_flex', 'financial_support_self']
    
    for field in bool_fields:

        if file[field] == "Yes":
            file[field] = True
        elif file[field] == "No":
            file[field] = False
        else:
            file[field] = None
