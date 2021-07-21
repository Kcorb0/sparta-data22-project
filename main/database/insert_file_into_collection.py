from create_talent_collection import *


def insert_file_into_collection(file_list):
    create_sparta_day_collection()
    for i in file_list:
        name = i['name']
        print(f'{name} has been inserted.')
        db.sparta_day.insert_one(i)

insert_file_into_collection([{'name': 'Darb Noor', 
    'date': '04/04/2019', 
    'tech_self_score': {'Python': 1, 'JavaScript': 5}, 
    'strengths': ['Versatile', 'Determined', 'Composure'], 
    'weaknesses': ['Undisciplined'], 
    'self_development': 'Yes', 
    'geo_flex': 'Yes', 
    'financial_support_self': 'Yes', 
    'result': 'Pass', 
    'course_interest': 'Business'}]
)