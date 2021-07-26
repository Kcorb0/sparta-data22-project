from App.academy import *


# To test that all fields have the correct data types for the csv
def test_academy():
    # Might be erroring on Null value
    assert testdata.dtypes[0] == 'stri'
    assert testdata.dtypes[1] == 'object'
    for x in range(2, 50):
        assert testdata.dtypes[x] == 'int64' or 'float64'
