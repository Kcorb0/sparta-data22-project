from app.txt_extract_all_files import txt_extract_all_files


# this test is to see if all of the .txt files were successfully extracted from s3
def test_txt_extract_all_files():
    # there are 152 .txt files in the s3 bucket. If all are successfully extracted, the count will equal 152
    assert txt_extract_all_files() == 152
