import pymongo
from App.clean_academy import *


def test_data_types():
    assert add_start_date_and_stream_to_academy('Business_20_2019-02-11.csv').dtypes[0] == 'stri'
    assert add_start_date_and_stream_to_academy('Business_20_2019-02-11.csv').dtypes[1] == 'object'
    for x in range(2, 50):
        assert add_start_date_and_stream_to_academy('Business_20_2019-02-11.csv').dtypes[x] == 'int64' or 'float64'
    assert add_start_date_and_stream_to_academy('Business_20_2019-02-11.csv').dtypes[50] == 'datetime64'
    assert add_start_date_and_stream_to_academy('Business_20_2019-02-11.csv').dtypes[51] == 'object'