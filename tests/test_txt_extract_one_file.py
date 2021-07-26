from app.txt_extract_one_file import *


# this test determines whether the .txt file was successfully extracted from the s3 bucket
def test_txt_extract_one_file():
    # a status code of 200 indicates success, 400 indicates failure
    assert txt_extract_one_file() == 200
