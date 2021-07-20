import json, boto3
from pprint import pprint
from main.main import get_jsons

def test_get_all_files():
    assert sum([len(i) for i in get_jsons()]) == 3105

test_get_all_files()