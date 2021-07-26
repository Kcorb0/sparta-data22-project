from app.txt_read_one_file import txt_read_one_file


# this test determines whether the .txt file is successfully decoded and read
def test_txt_read_one_file():
    # the format of the decoded file should be a string
    assert type(txt_read_one_file()) is str
