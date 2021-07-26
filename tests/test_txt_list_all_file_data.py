from app.txt_list_all_file_data import *


# this tests to see whether the function successfully creates a list of all the data from all the .txt files
def test_txt_list_all_file_data():
    # if the function produces a list, and the length of the list equals 152, the function is successful
    assert type(loop_through_txt_list_all_file_names()) is list
    assert len(loop_through_txt_list_all_file_names()) == 152
