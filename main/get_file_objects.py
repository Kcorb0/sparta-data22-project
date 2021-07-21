import json, boto3
from pprint import pprint
from collect_file_names import get_jsons
from read_jsons import read_json


def get_file_objects():

    objects_list = []

    for i in get_jsons():
        objects_list.append(read_json(i))
        print(i)

    return objects_list

get_file_objects()