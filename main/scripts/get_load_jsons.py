import json, boto3
from pprint import pprint
from collect_file_names import get_jsons
from read_jsons import read_json


def get_load_jsons():

    objects_list = []

    cnt = 1

    for i in get_jsons():
        content = objects_list.append(read_json(i))
        
        cnt += 1

    print('Done')

