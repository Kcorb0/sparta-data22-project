from App.Applicants import *


# To test that all fields have the correct data types for the csv
def test_data_types():
    assert testdata.dtypes[0] == 'int64'
    assert testdata.dtypes[1] == 'object'
    assert testdata.dtypes[2] == 'object'
    # need to change to date time
    assert testdata.dtypes[3] == 'datetime64'
    assert testdata.dtypes[4] == 'object'
    assert testdata.dtypes[5] == 'object'
    assert testdata.dtypes[6] == 'object'
    assert testdata.dtypes[7] == 'object'
    assert testdata.dtypes[8] == 'object'
    assert testdata.dtypes[9] == 'object'
    assert testdata.dtypes[10] == 'object'
    assert testdata.dtypes[11] == 'float64'
    assert testdata.dtypes[12] == 'object'
    assert testdata.dtypes[13] == 'object'


