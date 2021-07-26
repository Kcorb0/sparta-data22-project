from app.txt_list_all_file_names import txt_list_all_file_names


# this tests to see whether the function successfully creates a list of all the file names
def test_txt_list_all_file_names():
    # if the function produces a list, and the length of the list equals 152, the function is successful
    assert type(txt_list_all_file_names()) is list
    assert len(txt_list_all_file_names()) == 152
